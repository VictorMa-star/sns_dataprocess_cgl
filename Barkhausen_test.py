import os
import time
import numpy as np
from matplotlib import pyplot as plt

# data = np.loadtxt('../20220208/yee')
# plt.figure()
# plt.hist(data, bins=200)

# is this Gaussian noise?

data = np.loadtxt('../20220211/test2', skiprows=1)
BG = np.loadtxt('../20220211/BG', skiprows=1)
freq = data[:,0]
ROI = (freq>0.003) & (freq<0.015)


# PSD_u = data[:,3] - data[:,1]
# for PSD in (PSD_u,):
#     param = np.polyfit(np.log(freq[ROI]), np.log(PSD[ROI]), deg=1)
#     print(param)
#     # plt.loglog(freq, PSD, label='PSD')
#     plt.loglog(freq, freq**param[0]*np.exp(param[1]))

PSD_d = data[:,4] - BG
PSD_d2 = data[:,5] - BG
for PSD in (PSD_d, PSD_d2):
    param = np.polyfit(np.log(freq[ROI]), np.log(PSD[ROI]), deg=1)
    print(param)
    # plt.loglog(freq, PSD, label='PSD')
    plt.loglog(freq, freq**param[0]*np.exp(param[1]))

plt.loglog(freq, data[:,1], label='BG up')
plt.loglog(freq, data[:,2], label='BG down')
plt.loglog(freq, BG, label='BG down, after slope')

# plt.loglog(freq, PSD_u, label='BG down')
plt.loglog(freq, PSD_d, label='PSD_d')
plt.loglog(freq, PSD_d2, label='PSD_d2')

# plt.loglog(freq, data[:,3], label='PSD up')
# plt.loglog(freq, data[:,4], label='PSD down')
# plt.loglog(freq, data[:,5], label='PSD down 2')
plt.ylim(-1,1)

plt.legend()
plt.show()
