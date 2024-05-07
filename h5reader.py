import enum
import os
from sys import api_version
import time
import numpy as np
from numpy.core.defchararray import array
from numpy.core.function_base import _logspace_dispatcher
from numpy.lib.function_base import append
from scipy.optimize import curve_fit
import pandas as pd
import h5py
import matplotlib.colors as mcolors
import matplotlib._color_data as mcd

from matplotlib import pyplot as plt
import sys
sys.path.insert(0, '../python')
from SNS_function import get_factor

# fileName = 'shot_noise(noPBS).h5'
# fileName = 'intensity_noise(noPBS).h5'
result_path = '../test_MTY/'

# fileName = 'SN_ellipticity_333K_b2.h5'
fileName = 'test2_MTY.h5'
f = h5py.File(result_path + fileName, 'r')

# # demonstration
# f_shot = h5py.File(result_path + 'shot_noise(noPBS).h5', 'r')
# f_intensity = h5py.File(result_path + 'intensity_noise(noPBS).h5', 'r')
f_electronic = h5py.File(result_path + 'electronic_noise.h5', 'r') #电子噪声部分，暂时保留以保证程序正常运行


# is there a more rerasonable way of extracting the parameters that are shared by all datasets?
seg_len = f_electronic['electronic noise mode=101_0PSD'].attrs['segment length']
sr = f_electronic['electronic noise mode=101_0PSD'].attrs['sample rate(MHz)']*1e6 #sample rate unit of Hz
df = sr/seg_len


# dtype = [('PSD', np.float32, (seg_len//2)), ('factor', np.float64)]
dtype_withname = [('PSD', np.float32, (seg_len//2)), ('factor', np.float64), ('label', 'U100')] 

# datatype of the list of RAW PSD data
dtype_field = [('PSD', np.float32, (seg_len//2, 3)), ('factor', np.float64), ('field', np.float32, 2),('label', 'U100')]
# By default data type str takes length of 1.So, you will only get one character. we can set max data length by \
# using np.dtype('U100'). Un where U is unicode and n is number of characters in it



electronic_noise = np.array(
    list(zip(
        [f_electronic[name][:,2] for name in f_electronic.keys()], 
        [0 for name in f_electronic.keys()],
        [name for name in f_electronic.keys()],
    )),
    dtype=dtype_withname
)
f_electronic.close()

# kerr rotation noise
rotation_noise_raw = np.array(
    list(zip(
        [f[name] for name in f.keys()], 
        [get_factor(f, name) for name in f.keys()],
        [f[name].attrs['field(Gs)'] for name in f.keys()],
        [name for name in f.keys()],
    )),
    dtype=dtype_field
)

rotation_noise = np.array([rotation_noise_raw[i] for i in 
    np.argsort([f[name].attrs['V0/2 in scope (mV)'] for name in f.keys()])
])
rotationNoise_V = np.sort([f[name].attrs['V0/2 in scope (mV)'] for name in f.keys()])
f.close()


'''calculation'''
P_list = []
B_list = []
for datum in rotation_noise:
    # calculate the intergrated P:
    P_list.append(np.sum(datum['PSD'][:,0][3:seg_len//5]/datum['factor']**2)) #PP's thought: the raw data has been divided by V0(no factor added), so the factor should be considered in the process.
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
# Nyquist limit?--MTY
freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6 # in MHz

for datum in rotation_noise: 
    # cut off   
    ROI = (freq>cutoff_low) & (freq<cutoff_high)
    param_temp = curve_fit(lorentzian_0, freq[ROI], datum['PSD'][:,0][ROI], maxfev=10000, p0=p0)[0] # maxfev ???
    param.append(param_temp)
# print('Here' + str(param))
order = np.argsort(B_list)
B_list = np.array(B_list)[order]
P_list = np.array(P_list)[order]
rotation_noise = rotation_noise[order]

'''visualziation'''
text_prop = {'fontsize': 16}
title_prop = {'fontsize': 18}

fig = plt.figure(figsize=(6,5))
ax = plt.axes()
freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6

data_plot = rotation_noise[15:35][::2]
colors = plt.cm.brg(np.linspace(0,1,len(data_plot)))
for j in range(len(data_plot)):
    # plt.semilogy(freq, (datum['PSD'] - electronic_noise[1]['PSD'])/datum['factor']**2, label=datum['label'])

    datum = data_plot[j]
    plt.plot(freq, datum['PSD'][:,0]/datum['factor']**2, color=colors[j], label=f"{str(datum['label'][datum['label'].find('['):datum['label'].find(']')]) + ']'}(Gs)")


plt.xlim(0, 0.5)
plt.ylim(0, 10e-14)


plt.title(fileName, title_prop)
plt.tick_params(axis='both', which='both', labelsize=14)
ax.yaxis.get_offset_text().set_fontsize(14)
plt.xlabel('frequency (MHz)', text_prop)
plt.ylabel(r'relative noise ($1/Hz$)', text_prop)

plt.legend()
plt.tight_layout()


fig_P = plt.figure()
ax = plt.axes()

plt.plot(B_list, P_list, 'bo')
plt.title(fileName, title_prop)
plt.tick_params(axis='both', which='both', labelsize=14)
ax.yaxis.get_offset_text().set_fontsize(14)
plt.xlabel('B (Gs)', text_prop)
plt.ylabel(r'integrated relative noise', text_prop)

# plt.legend()
plt.tight_layout()


color_list = mcd.CSS4_COLORS # mcd.XKCD_COLORS,
solid_style_list = [name[1] for name in list(enumerate(color_list))[35:]]
dashed_style_list = [name[1] for name in list(enumerate(color_list))[35:]]


fig_lw = plt.figure(figsize=(6,5))
ax = plt.axes()

powerlaw_fit = []
lorentz_fit = []
log_fit = []
exponent = []
ROI = (freq < 0.3) & (freq > 0.01)
# for i in np.array(range(len(B_list)))[(np.array(B_list) > -1.5) & (np.array(B_list) < -0.5)]:

# B_list_sub = np.array(range(len(B_list)))[(np.array(B_list) > -1.7) & (np.array(B_list) < -0)][::2]
B_list_sub = np.array(range(len(B_list)))[(np.array(B_list) > -1) & (np.array(B_list) < 1)]
colors = plt.cm.brg(np.linspace(0,1,len(B_list_sub)))
for j in range(len(B_list_sub)):
    i = B_list_sub[j]
    datum = rotation_noise[i]
    # plt.loglog(freq, rotation_noise[i]['PSD'][:,0], label=f'{str(round(B_list[i], 1))}(Gs)', color=colors[j])
    
    param_temp = np.polyfit(np.log(freq[ROI]), np.log(datum['PSD'][:,0][ROI]/datum['factor']**2), deg=1)
    log_fit.append(param_temp)
    exponent.append(param_temp[0])
    print(param_temp[0])
    # plt.plot(freq, np.exp(param_temp[1])*freq**param_temp[0], '--', color=colors[j])
    # plt.loglog(freq, np.exp(param_temp[1])*freq**param_temp[0], '--', color=colors[j])

    
    try:
        # 335K
        # ROI_powerlaw = (freq < 0.12) & (freq > 0.001)
        # 345K
        ROI_powerlaw = (freq < 0.5) & (freq > 0.001)
        ROI_lorentz = (freq < 0.5) & (freq > 0.001)

        powerlaw_fit.append(curve_fit(power_law, freq[ROI_powerlaw], 1/(datum['PSD'][:,0][ROI_powerlaw]/datum['factor']**2), p0 = [np.abs(exponent[-1]), 0.001, 1e16]))
        lorentz_fit.append(curve_fit(lorentzian_0, freq[ROI_powerlaw], (datum['PSD'][:,0][ROI_powerlaw]/datum['factor']**2), p0 = [1e-12, 0.1]))

        # plt.plot(freq[ROI_powerlaw], 1/rotation_noise[i]['PSD'][:,0][ROI_powerlaw], '--', color=colors[j])
        # plt.plot(freq[ROI_powerlaw], power_law(freq[ROI_powerlaw], *powerlaw_fit[-1][0][0:2], powerlaw_fit[-1][0][2]), 'k--', label=r'$\nu$ =' + f'{powerlaw_fit[-1][0][0]}')

        ### normal color
        # breakpoint()
        # plt.plot(freq, datum['PSD'][:,0]/datum['factor']**2, color=colors[j])
        # plt.plot(freq[ROI_powerlaw], inverse_power_law(freq[ROI_powerlaw], *powerlaw_fit[-1][0][0:2], 1/powerlaw_fit[-1][0][2]), '--',  color=colors[j], label=f'{str(datum["field"])}, ' + r'$\nu$ =' + f'{round(powerlaw_fit[-1][0][0],1)}')
        # plt.plot(freq[ROI_lorentz], lorentzian_0(freq[ROI_lorentz], *lorentz_fit[-1][0]), '--',  color=colors[j], label=r'FWHM=' + f'{round(lorentz_fit[-1][0][1], 2)}')
        # breakpoint()
        # plt.loglog(freq, datum['PSD'][:,0]/datum['factor']**2, color=colors[j])
        # plt.loglog(freq[ROI_powerlaw], inverse_power_law(freq[ROI_powerlaw], *powerlaw_fit[-1][0][0:2], 1/powerlaw_fit[-1][0][2]), '--',  color=colors[j], label=r'$\nu$ =' + f'{powerlaw_fit[-1][0][0]}')
        # plt.loglog(freq[ROI_lorentz], lorentzian_0(freq[ROI_lorentz], *lorentz_fit[-1][0]), '--',  color=colors[j], label=r'FWHM=' + f'{lorentz_fit[-1][0][1]}')
        

        ### color for comparison
        plt.plot(freq, datum['PSD'][:,0]/datum['factor']**2, color=colors[j])
        plt.plot(freq[ROI_powerlaw], inverse_power_law(freq[ROI_powerlaw], *powerlaw_fit[-1][0][0:2], 1/powerlaw_fit[-1][0][2]), 'c--', label=r'$\nu$ =' + f'{powerlaw_fit[-1][0][0]}')
        plt.plot(freq[ROI_lorentz], lorentzian_0(freq[ROI_lorentz], *lorentz_fit[-1][0]), 'r--', label=r'FWHM=' + f'{lorentz_fit[-1][0][1]}')

        # plt.loglog(freq, datum['PSD'][:,0]/datum['factor']**2, color=colors[j], label=f'{str(datum["field"])}')
        # plt.loglog(freq[ROI_powerlaw], inverse_power_law(freq[ROI_powerlaw], *powerlaw_fit[-1][0][0:2], 1/powerlaw_fit[-1][0][2]), 'c--')
        # plt.loglog(freq[ROI_lorentz], lorentzian_0(freq[ROI_lorentz], *lorentz_fit[-1][0]), 'r--')

        print('power low fit exponent = ', powerlaw_fit[-1][0][0:2])
        
    except:
        print(f'{B_list[i]} fitting fails')
        pass

print(powerlaw_fit)

# plt.xlim(0, 0.5)
# plt.ylim(0, .5e-12)

# loglog plot
plt.xlim(1e-3, 0.5)
plt.ylim(1e-14, .5e-12)

plt.title(fileName, title_prop)
plt.tick_params(axis='both', which='both', labelsize=14)
ax.yaxis.get_offset_text().set_fontsize(14)
plt.xlabel('freq (MHz)', text_prop)
plt.ylabel(r'relative noise (1/Hz)', text_prop)


plt.legend()
plt.tight_layout()


# plt.figure()
# # breakpoint()
# plt.plot(np.array(B_list)[(np.array(B_list) > -1) & (np.array(B_list) < -0.3)] , exponent, 'bo')

plt.show()

