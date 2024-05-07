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

from SNS_function import SNS_data

# fileName = 'shot_noise(noPBS).h5'
# fileName = 'intensity_noise(noPBS).h5'
result_path = '../result/'
figure_path = '../figure/'

# fileName = 'SN_ellipticity_333K_b2.h5'
# fileName = 'SN_ellipticity_330K.h5'
fileName = 'SNS_E_IP_320K_site8_633nm.h5'
# fileName = 'SNS_R_IP_295K_site6_12.h5'
f = h5py.File(result_path + fileName, 'r')

data = []
for name in f.keys():
    # if '..\\20220\\' + name in SNS_dataset.SNS_R_IP_320K:
        data.append(SNS_data(f, name))
f.close()


sort_by = []
for datum in data:
    sort_by.append(datum.field[0])
    # sort_by.append(datum.sig_V0)

# sort by wl, power, etc...
sort_index = np.argsort(sort_by)
# sort_index = np.argsort(sort_by)[::-1] # in descending order

data_processed = []
for i in sort_index:
    data_processed.append(data[i])

# for high T, IP field
BG = data_processed[-1]
for datum in data_processed:
    datum.PSD[:,0] -= BG.PSD[:,0]
    # pass
    # datum.PSD[:,1] -= BG.PSD[:,1]



seg_len = np.shape(data[0].PSD)[0]*2 # Nyquist
sr = data[0].sr
df = sr/seg_len
freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6

# # demonstration
# f_shot = h5py.File(result_path + 'shot_noise(noPBS).h5', 'r')
# f_intensity = h5py.File(result_path + 'intensity_noise(noPBS).h5', 'r')
f_electronic = h5py.File(result_path + 'electronic_noise.h5', 'r')

f.close()

'''visualziation'''
text_prop = {'fontsize': 16}
title_prop = {'fontsize': 18}

### animation
fig, ax = plt.subplots()
xdata, ydata = [], []
dot, = plt.plot([], [], 'bo')
line1, = plt.plot([], [], 'r-', lw=1, label='low B')
line2, = plt.plot([], [], 'g-', lw=1, label='high B')
# dot, = plt.loglog([], [], 'bo')
# line1, = plt.loglog([], [], 'r-', lw=1, label='low B')
# line2, = plt.loglog([], [], 'g-', lw=1, label='high B')

# plt.title(fileName, title_prop)
plt.tick_params(axis='both', which='both', labelsize=14)
ax.yaxis.get_offset_text().set_fontsize(14)
plt.xlabel('frequency (MHz)', text_prop)
plt.ylabel(r'relative noise ($1/Hz$)', text_prop)

# ln, = plt.plot([], [], 'b-')
title = ax.text(1, 0.9, fileName, horizontalalignment='right', transform=ax.transAxes, **text_prop)
text = ax.text(0.9, 0.75, '', horizontalalignment='right', transform=ax.transAxes, **text_prop)
ROI = (freq < 0.2)

def init():
    ax.set_xlim(np.min(freq[ROI][1:]), np.max(freq[ROI]))
    lim = .5e-11
    # ax.set_ylim(-0.05*lim, lim)
    ax.set_ylim(1e-5*lim, lim)
    # raw
    # ax.set_ylim(-0.4*lim, 0.2*lim)
    
    return dot, line1, line2, text

def update(frame):
    # print(frame) # for debugging
    xdata = freq[ROI]
    ydata = data_processed[frame].PSD[:,0][ROI]/data_processed[frame].factor**2
    dot.set_data(xdata, ydata)
    
    line1.set_data(xdata, data_processed[frame].PSD[:,1][ROI]/data[frame].factor**2)
    line2.set_data(xdata, data_processed[frame].PSD[:,2][ROI]/data[frame].factor**2)

    text.set_text(f'B = {str(np.round(data_processed[frame].field[0], 1))} Gs')
    return dot, line1, line2, text

ani = FuncAnimation(fig, update, frames=list(range(len(data_processed))), init_func=init, blit=True, interval=500, repeat=True)

# plt.legend()
plt.tight_layout()
ani.save(filename=figure_path + fileName + '.gif')
# ani.save(filename=figure_path + fileName + '_raw' + '.gif')

plt.show()

