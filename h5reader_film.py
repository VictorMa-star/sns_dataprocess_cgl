from cProfile import label
import enum
import os
from sys import api_version
import time
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
from scipy.sparse import data
import h5py
import matplotlib.colors as mcolors
import matplotlib._color_data as mcd

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# fileName = 'shot_noise(noPBS).h5'
# fileName = 'intensity_noise(noPBS).h5'
result_path = '../result/'
figure_path = '../figure/'

# fileName = 'SN_ellipticity_333K_b2.h5'
fileName = 'SN_ellipticity_330K.h5'
f = h5py.File(result_path + fileName, 'r')

# # demonstration
# f_shot = h5py.File(result_path + 'shot_noise(noPBS).h5', 'r')
# f_intensity = h5py.File(result_path + 'intensity_noise(noPBS).h5', 'r')
f_electronic = h5py.File(result_path + 'electronic_noise.h5', 'r')


# is there a more rerasonable way of extracting the parameters that are shared by all datasets?
seg_len = f_electronic['electronic noise mode=101_0PSD'].attrs['segment length']
sr = f_electronic['electronic noise mode=101_0PSD'].attrs['sample rate(MHz)']*1e6
df = sr/seg_len


# dtype = [('PSD', np.float32, (seg_len//2)), ('factor', np.float64)]
dtype_withname = [('PSD', np.float32, (seg_len//2)), ('factor', np.float64), ('label', 'U100')]
dtype_field = [('PSD', np.float32, (seg_len//2, 3)), ('factor', np.float64), ('field', np.float32, 2),('label', 'U100')]


def get_factor(f, name):    
    # 200 Newport 1807 (80MHz)\
    if f[name].attrs['mode'] == '200':
        correction = (2)*2

    # 100 = Thorlabs PD210A (1MHz) monitor + no real-time DC (I noise, no 2)
    # 102 Thorlabs PD210A (1MHz) monitor + no real-time DC +  Dual\
    elif f[name].attrs['mode'] == '100':
        correction = (1/10*1.5)
    elif f[name].attrs['mode'] == '102':
        correction = (1/10*1.5)*2
    
    # 101 Thorlabs PD210A (1MHz) RF output + no real-time DC\
    # 103 Thorlabs PD210A (1MHz) RF(monitor- blocked) + no real-time DC\
    elif f[name].attrs['mode'] == '101':
        correction = (30*(1/300*100))*2
    elif f[name].attrs['mode'] == '103':
        correction = 30*(1/300*100)

    else:
        # print(f"{f[name].attrs['mode']} not considered in get_factor(f, name) yet")
        if f[name].attrs['mode'] == '111':
            correction = (30*(1/300*100))*2
            return correction
        else:
            print(f"{f[name].attrs['mode']} not considered in get_factor(f, name) yet")

    return f[name].attrs['V0/2 in scope (mV)']/1e3*correction

### note: if the value in oscilloscope is divided directly in Labview, then only "correction" need to be considered!


electronic_noise = np.array(
    list(zip(
        [f_electronic[name][:,2] for name in f_electronic.keys()], 
        [0 for name in f_electronic.keys()],
        [name for name in f_electronic.keys()],
    )),
    dtype=dtype_withname
)
f_electronic.close()


rotation_noise = np.array(
    list(zip(
        [f[name] for name in f.keys()], 
        [get_factor(f, name) for name in f.keys()],
        [f[name].attrs['field(Gs)'] for name in f.keys()],
        [name for name in f.keys()],
    )),
    dtype=dtype_field
)

rotation_noise = np.array([rotation_noise[i] for i in 
    np.argsort([f[name].attrs['V0/2 in scope (mV)'] for name in f.keys()])
])
rotationNoise_V = np.sort([f[name].attrs['V0/2 in scope (mV)'] for name in f.keys()])

f.close()


'''calculation'''
P_list = []
B_list = []
for datum in rotation_noise:
    P_list.append(np.sum(datum['PSD'][:,0][3:seg_len//5]/datum['factor']**2))
    B_list.append(datum['field'][0])

### fitting
def lorentzian_0(x, a, FWHM):
    return a*FWHM**2 / (FWHM**2 + 4*(x)**2 )
    # return a*FWHM**2 / (FWHM**2 + 4*(x)**2 )

def power_law(f, m, f0, a):
    return a*(f + f0)**m

def inverse_power_law(f, m, f0, a):
    return a/(f + f0)**m

# def power_low(x, a, FWHM):
#     return 


p0 = [1e-12, 0.1]
P = []
P_fit = []
param = []
cutoff_low = 0.0020 # in MHz
cutoff_high = 0.25
freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6

for datum in rotation_noise:    
    ROI = (freq>cutoff_low) & (freq<cutoff_high)
    param_temp = curve_fit(lorentzian_0, freq[ROI], datum['PSD'][:,0][ROI], maxfev=10000, p0=p0)[0] # maxfev ???
    param.append(param_temp)

order = np.argsort(B_list)
B_list = np.array(B_list)[order]
P_list = np.array(P_list)[order]
rotation_noise = rotation_noise[order]

'''visualziation'''
text_prop = {'fontsize': 16}
title_prop = {'fontsize': 18}

### animation
fig, ax = plt.subplots()
xdata, ydata = [], []
dot, = plt.plot([], [], 'bo')
line1, = plt.plot([], [], 'r-', lw=1, label='low B')
line2, = plt.plot([], [], 'g-', lw=1, label='high B')
# ln, = plt.plot([], [], 'b-')
title = ax.text(1, 0.9, fileName, horizontalalignment='right', transform=ax.transAxes, **text_prop)
text = ax.text(0.9, 0.75, '', horizontalalignment='right', transform=ax.transAxes, **text_prop)
ROI = (freq < 0.5)

def init():
    ax.set_xlim(np.min(freq[ROI]), np.max(freq[ROI]))
    lim = 3e-11
    ax.set_ylim(-0.05*lim, lim)
    return dot, line1, line2, text

def update(frame):
    # print(frame) # for debugging
    xdata = freq[ROI]
    ydata = rotation_noise[frame]['PSD'][:,0][ROI]
    dot.set_data(xdata, ydata)
    
    line1.set_data(xdata, rotation_noise[frame]['PSD'][:,1][ROI])
    line2.set_data(xdata, rotation_noise[frame]['PSD'][:,2][ROI])

    text.set_text(f'B = {str(np.round(B_list[frame], 1))} Gs')
    return dot, line1, line2, text

ani = FuncAnimation(fig, update, frames=list(range(len(rotation_noise))), init_func=init, blit=True, interval=500, repeat=True)

ani.save(filename=figure_path + fileName + '.gif')
plt.show()

