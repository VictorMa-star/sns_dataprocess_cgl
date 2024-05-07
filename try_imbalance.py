import os
import time
import numpy as np
from numpy.core.fromnumeric import shape
from numpy.core.numeric import ones
import pandas as pd
import h5py
import BG_noise

from matplotlib import pyplot as plt


# fileName = 'shot_noise(noPBS).h5'
# fileName = 'intensity_noise(noPBS).h5'
result_path = '../result/'

fileName = 'imbalance.h5'
f = h5py.File(result_path + fileName, 'r')

# demonstration
f_electronic = h5py.File(result_path + 'electronic_noise.h5', 'r')


# is there a more rerasonable way of extracting the parameters that are shared by all datasets?
seg_len = f_electronic['electronic noise mode=101_0PSD'].attrs['segment length']
sr = f_electronic['electronic noise mode=101_0PSD'].attrs['sample rate(MHz)']*1e6
df = sr/seg_len


# dtype = [('PSD', np.float32, (seg_len//2)), ('factor', np.float64)]
# dtype_withname = [('PSD', np.float32, (seg_len//2)), ('factor', np.float64), ('label', 'U100')]
dtype = [('PSD', np.float32, (seg_len//2, 3)), ('factor', np.float64), ('label', 'U100')]


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
        print(f"{f[name].attrs['mode']} not considered in get_factor(f, name) yet")

    return f[name].attrs['V0/2 in scope (mV)']/1e3*correction


imbalance = np.array(
    list(zip(
        [f[name] for name in f.keys()], 
        [get_factor(f, name) for name in f.keys()],
        [name for name in f.keys()],
    )),
    dtype=dtype
)
imbalance = np.array([imbalance[i] for i in 
    np.argsort([f[name].attrs['V0/2 in scope (mV)'] for name in f.keys()])
])
PSD_V = np.sort([f[name].attrs['V0/2 in scope (mV)'] for name in f.keys()])
wavelength = f[list(f.keys())[0]].attrs['wavelength(nm)']

f.close()



'''visualziation'''
text_prop = {'fontsize': 16}
title_prop = {'fontsize': 18}

fig = plt.figure()
ax = plt.axes()
freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6


for datum in imbalance:
    # plt.semilogy(freq, (datum['PSD'] - electronic_noise[1]['PSD'])/datum['factor']**2, label=datum['label'])
    plt.plot(freq, datum['PSD'][:,0]/datum['factor']**2, label=datum['label'])

plt.plot(freq, (imbalance[0]['PSD'][:,0] + imbalance[1]['PSD'][:,0])/datum['factor']**2, label=datum['label'])

plt.plot(freq, np.zeros(shape=np.shape(freq)), 'k--', label=datum['label'])

plt.xlim(0, 2.5)
plt.ylim(-1.4e-14, 1.4e-14)




# plt.title('comp offset', title_prop)
plt.tick_params(axis='both', which='both', labelsize=14)
ax.yaxis.get_offset_text().set_fontsize(14)
plt.xlabel('frequency (MHz)', text_prop)
# plt.ylabel(r'PSD ($V^2/Hz$)', text_prop)
plt.ylabel(r'RIN ($1/Hz$)', text_prop)

plt.legend()
plt.tight_layout()


# fig_shot_scale = plt.figure()
# ax = plt.axes()

# VtomW = 0.12
# for i in range(len(shot_noise)):
#     plt.plot(freq, (shot_noise[i]['PSD'] - electronic_noise[1]['PSD'])/shot_noise[i]['factor']**2*(ShotNoise_V[i]*2/1e3*VtomW)*1e-3, label=shot_noise[i]['label'])

# plt.plot(freq, np.ones(len(freq))*2*1240/wavelength*1.6e-19, 'k--', label=r'shot noise limit, 2$h\nu$')

# plt.ylim(0, 1e-18)
# plt.xlim(0, 5)
# plt.tick_params(axis='both', which='both', labelsize=14)
# ax.yaxis.get_offset_text().set_fontsize(14)
# plt.xlabel('frequency (MHz)', text_prop)
# plt.ylabel(r'RIN$\cdot \langle P \rangle$ ($W\cdot rad^2/Hz$)', text_prop)

# plt.legend()
# plt.tight_layout()


plt.show()

