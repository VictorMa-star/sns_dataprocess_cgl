import enum
import os
from sys import api_version
import time
import numpy as np
from numpy.core.defchararray import array
from numpy.lib.function_base import append
from scipy.optimize import curve_fit
import pandas as pd
import h5py
import BG_noise
import matplotlib.colors as mcolors
import matplotlib._color_data as mcd

from matplotlib import pyplot as plt


# fileName = 'shot_noise(noPBS).h5'
# fileName = 'intensity_noise(noPBS).h5'
result_path = '../result/'

# fileName = 'SN_ellipticity_333K_b2.h5'
fileName = 'SN_ellipticity_333K_site6_1_b.h5'
f = h5py.File(result_path + fileName, 'r')

# demonstration
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


def power_law(f, m, a, f0):
    return a/(f + f0)**m

def inverse_power_law(f, m, a, f0):
    return a*(f + f0)**m

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
    ### calculate integrated noise directly from data
    # P.append(np.sum(datum['PSD'][int(cutoff_low/df):int(cutoff_high/df)])*df)
    # # print(np.sum(data[i]['PSD'][int(1.5/df):int(2.5/df)]), np.std(data[i]['PSD'][int(1.5/df):int(2.5/df)]))
    
    ### Lorentzian fitting
    ROI = (freq>cutoff_low) & (freq<cutoff_high)
    param_temp = curve_fit(lorentzian_0, freq[ROI], datum['PSD'][:,0][ROI], maxfev=10000, p0=p0)[0] # maxfev ???
    # param_temp[1] = np.abs(param_temp[1])
    # P_fit.append(param_temp[0]*param_temp[1]*np.pi/4)
    
    param.append(param_temp)

# param = np.array(param)
# print(param[:5])

'''visualziation'''
text_prop = {'fontsize': 16}
title_prop = {'fontsize': 18}

# fig = plt.figure()
# ax = plt.axes()
# freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6


# for datum in rotation_noise:
#     # plt.semilogy(freq, (datum['PSD'] - electronic_noise[1]['PSD'])/datum['factor']**2, label=datum['label'])
#     plt.plot(freq, datum['PSD'][:,0]/datum['factor']**2, label=datum['label'])


# plt.xlim(0, 0.5)
# plt.ylim(0, 1.4e-14)


# # plt.title('comp offset', title_prop)
# plt.tick_params(axis='both', which='both', labelsize=14)
# ax.yaxis.get_offset_text().set_fontsize(14)
# plt.xlabel('frequency (MHz)', text_prop)
# # plt.ylabel(r'PSD ($V^2/Hz$)', text_prop)
# plt.ylabel(r'RIN ($1/Hz$)', text_prop)

# plt.legend()
# plt.tight_layout()


# fig_P = plt.figure()
# ax = plt.axes()

# plt.plot(B_list, P_list, 'bo')
# plt.title(fileName, title_prop)
# plt.tick_params(axis='both', which='both', labelsize=14)
# ax.yaxis.get_offset_text().set_fontsize(14)
# plt.xlabel('B (Gs)', text_prop)
# plt.ylabel(r'integrated relative noise', text_prop)

# # plt.legend()
# plt.tight_layout()


color_list = mcd.CSS4_COLORS # mcd.XKCD_COLORS,
solid_style_list = [name[1] for name in list(enumerate(color_list))[30:]]
dashed_style_list = [name[1] for name in list(enumerate(color_list))[30:]]

fig_lw = plt.figure()
ax = plt.axes()
# plt.plot(B_list, param[:,1], 'bo')

# for i in np.array(range(len(B_list)))[(np.array(B_list) > -2) & (np.array(B_list) < 1.7)]:
#     plt.plot(freq, rotation_noise[i]['PSD'][:,0], label=f'{str(round(B_list[i], 1))}(Gs)')
#     plt.plot(freq, lorentzian_0(freq, *param[i]), '--')

powerlaw_fit = []
exponent = []
ROI = (freq < 0.125) & (freq > 0.003)
# for i in np.array(range(len(B_list)))[(np.array(B_list) > -1.5) & (np.array(B_list) < -0.5)]:
for i in np.array(range(len(B_list)))[(np.array(B_list) > -1.5) & (np.array(B_list) < 0)]:
    # plt.loglog(freq, rotation_noise[i]['PSD'][:,0], label=f'{str(round(B_list[i], 1))}(Gs)')#, color=solid_style_list[i])
    # plt.loglog(freq, rotation_noise[i]['PSD'][:,0], label=f'{str(round(B_list[i], 1))}(Gs)')#, color=solid_style_list[i])
    plt.plot(freq, rotation_noise[i]['PSD'][:,0], label=f'{str(round(B_list[i], 1))}(Gs)')#, color=solid_style_list[i])
    try:
        param_temp = np.polyfit(np.log(freq[ROI]), np.log(rotation_noise[i]['PSD'][:,0][ROI]), deg=1)
        powerlaw_fit.append(param_temp)
        exponent.append(param_temp[0])
        plt.plot(freq, np.exp(param_temp[1])*freq**param_temp[0], '--')#, color=dashed_style_list[i])
        
    except:
        print(B_list[i], ' fails')
    # plt.loglog(freq, lorentzian_0(freq, *param[i]), '--')
print(powerlaw_fit)


# ROI = (freq < 0.125) & (freq > 0.03)
# p0 = [2, 4.5e13, 0.0]
# exponent = []
# for i in np.array(range(len(B_list)))[(np.array(B_list) > -1.4) & (np.array(B_list) < 1.4)]:
#     # plt.plot(freq, rotation_noise[i]['PSD'][:,0], label=f'{str(round(B_list[i], 1))}(Gs)', color=solid_style_list[i])
#     plt.plot(freq, 1/rotation_noise[i]['PSD'][:,0], label=f'{str(round(B_list[i], 1))}(Gs)', color=solid_style_list[i])
#     # breakpoint()
#     param_temp = curve_fit(inverse_power_law, freq[ROI], 1/rotation_noise[i]['PSD'][:,0][ROI], p0)
#     powerlaw_fit.append(param_temp)
#     exponent.append(param_temp[0][0])
#     # print(*param_temp[0])
#     plt.plot(freq, inverse_power_law(freq, *param_temp[0]), '--', color=dashed_style_list[i])
#     # plt.loglog(freq, lorentzian_0(freq, *param[i]), '--')


# yee = np.linspace(0, 0.5, 100)
# plt.plot(yee, inverse_power_law(yee, ))

plt.xlim(0.01, 0.2)
plt.ylim(0, 1e-9)

# param = np.array(param)
# plt.plot(B_list, param[:,1], 'bo')

# plt.title('comp offset', title_prop)
plt.tick_params(axis='both', which='both', labelsize=14)
ax.yaxis.get_offset_text().set_fontsize(14)
plt.xlabel('freq (MHz)', text_prop)
plt.ylabel(r'linewidth (Hz)', text_prop)


plt.legend()
plt.tight_layout()


# plt.figure()
# # breakpoint()
# plt.plot(np.array(B_list)[(np.array(B_list) > -1) & (np.array(B_list) < -0.3)] , exponent, 'bo')

plt.show()

