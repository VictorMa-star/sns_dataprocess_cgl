from bdb import Breakpoint
import time
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
import h5py
import matplotlib.colors as mcolors
import matplotlib._color_data as mcd

from matplotlib import pyplot as plt
import sys

sys.path.insert(0, '../python')
from SNS_function import SNS_data, get_property


# fileName = 'shot_noise(noPBS).h5'
# fileName = 'intensity_noise(noPBS).h5'
result_path = '../result/'

# # fileName = 'SN_ellipticity_333K_b2.h5'
# fileName = 'SNS_R_IP_295K_site6_12.h5'
# f = h5py.File(result_path + fileName, 'r')

# # # demonstration
# # f_shot = h5py.File(result_path + 'shot_noise(noPBS).h5', 'r')
# # f_intensity = h5py.File(result_path + 'intensity_noise(noPBS).h5', 'r')
# f_electronic = h5py.File(result_path + 'electronic_noise.h5', 'r')


# # # is there a more rerasonable way of extracting the parameters that are shared by all datasets?
# # seg_len = f_electronic['electronic noise mode=101_0PSD'].attrs['segment length']
# # sr = f_electronic['electronic noise mode=101_0PSD'].attrs['sample rate(MHz)']*1e6
# # df = sr/seg_len


# electronic_noise = []
# for name in f_electronic.keys():
#     electronic_noise.append(SNS_data(f_electronic, name))
# f_electronic.close()


# data = []
# # import SNS_dataset
# for name in f.keys():
#     # if '..\\20220\\' + name in SNS_dataset.SNS_R_IP_320K:
#         data.append(SNS_data(f, name))
# f.close()

# '''processing'''
# data_processed = []
# sort_by = []
# for datum in data:
#     sort_by.append(datum.field[0])
#     # sort_by.append(datum.sig_V0)

# # sort by wl, power, etc...
# sort_index = np.argsort(sort_by)

# for i in sort_index:
#     data_processed.append(data[i])

# f.close()

data_real = np.loadtxt('../20220305/3rd_test_real.txt')
data_imag = np.loadtxt('../20220305/3rd_test_imag.txt')
data = np.array([data_real, data_imag])

# freq = np.linspace(0, 488.281*4096/2, 4096//2)/1e6
df = 12.2
# X, Y = np.mgrid[0:4096//2//5,0:4096//2//5]*df/1e6
X, Y = np.mgrid[0:410,0:410]*df/1e6
freq = Y[0]
# breakpoint()
fig = plt.figure()
ax = plt.axes(projection ='3d')

# data[0][data[0] > 1e-5] = 1e-5
# data[0][data[0] < -1e-5] = -1e-5
# surf = ax.plot_surface(X, Y, data[0], cmap ='viridis')#, edgecolor ='green')
# ax.set_zlim(-1e-5, 1e-5)

# breakpoint()
ROI_f = slice(2, len(freq)//10)
data[0][data[0] > 1e-4] = 1e-4
data[0][data[0] < -1e-4] = -1e-4
data[1][data[1] > 1e-4] = 1e-4
data[1][data[1] < -1e-4] = -1e-4
# breakpoint()
surf = ax.plot_surface(X[ROI_f,ROI_f], Y[ROI_f,ROI_f], data[0][ROI_f,ROI_f], cmap ='viridis')#, edgecolor ='green')
# ax.set_zlim(-10e-5, 10e-5)
ax.set_zlim(-1e-6, 1e-6)

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.tight_layout()
plt.show()


# '''calculation'''
# # P_list = []
# # B_list = []
# # for datum in rotation_noise:
# #     P_list.append(np.sum(datum['PSD'][:,0][3:seg_len//5]/datum['factor']**2))
# #     B_list.append(datum['field'][0])

# seg_len = np.shape(data[0].PSD)[0]*2 # Nyquist
# sr = data[0].sr
# df = sr/seg_len
# freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6

# for datum in data:
#     datum.P = np.sum(datum.PSD[:,0][(freq>0.003) & (freq<0.03)]/datum.factor**2)


# ### fitting
# def lorentzian_0(x, a, FWHM):
#     return a*FWHM**2 / (FWHM**2 + 4*(x)**2 )
#     # return a*FWHM**2 / (FWHM**2 + 4*(x)**2 )

# def power_law(f, m, f0, a):
#     return a*(f + f0)**m

# def inverse_power_law(f, m, f0, a):
#     return a/(f + f0)**m

# # def power_low(x, a, FWHM):
# #     return 


# p0 = [1e-12, 0.1]
# P = []
# P_fit = []
# param = []
# cutoff_low = 0.0020 # in MHz
# cutoff_high = 0.25

# for datum in data_processed:    
#     ROI = (freq>cutoff_low) & (freq<cutoff_high)
#     param_temp = curve_fit(lorentzian_0, freq[ROI], datum.PSD[:,0][ROI], maxfev=10000, p0=p0)[0] # maxfev ???
#     param.append(param_temp)

# # order = np.argsort(B_list)
# # B_list = np.array(B_list)[order]
# # P_list = np.array(P_list)[order]
# # rotation_noise = rotation_noise[order]


# '''visualziation'''
# text_prop = {'fontsize': 16}
# title_prop = {'fontsize': 18}

# fig = plt.figure(figsize=(6,5))
# ax = plt.axes()
# freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6

# # enough to mask all except for 800Gs
# # f_ex = 4.5e-2
# # Df = 0.2e-2

# # include 800Gs
# f_ex = 4.53e-2
# Df = 0.3e-2

# exclusion = [False]*len(freq)
# exclusion_list = []
# for n in range(1,20):
#     exclusion = exclusion | ((freq > n*f_ex - Df) & (freq < n*f_ex + Df))
#     exclusion_list.append((freq > n*f_ex - Df) & (freq < n*f_ex + Df))

# # data_plot = rotation_noise[15:35][::2]
# data_plot = data_processed[::2]

# colors = plt.cm.brg(np.linspace(0,1,len(data_plot)))
# for j in range(len(data_plot)):
#     # plt.semilogy(freq, (datum['PSD'] - electronic_noise[1]['PSD'])/datum['factor']**2, label=datum['label'])

#     datum = data_plot[j]
#     plt.plot(freq, datum.PSD[:,0]/datum.factor**2, color=colors[j], label=f"{str(datum.field[0])} (Gs)")
#     for exclusion_range in exclusion_list:
#         plt.plot(freq[exclusion_range], datum.PSD[:,0][exclusion_range]/datum.factor**2, 'w')


# plt.xlim(0, 0.2)
# plt.ylim(0, 5e-12)


# plt.title(fileName, title_prop)
# plt.tick_params(axis='both', which='both', labelsize=14)
# ax.yaxis.get_offset_text().set_fontsize(14)
# plt.xlabel('frequency (MHz)', text_prop)
# plt.ylabel(r'relative noise ($1/Hz$)', text_prop)

# plt.legend()
# plt.tight_layout()


# # fig_P = plt.figure()
# # ax = plt.axes()

# # for datum in data:
# #     plt.plot(datum.field[0], datum.P, 'bo')
# # plt.title(fileName, title_prop)
# # plt.tick_params(axis='both', which='both', labelsize=14)
# # ax.yaxis.get_offset_text().set_fontsize(14)
# # plt.xlabel('B (Gs)', text_prop)
# # plt.ylabel(r'integrated relative noise', text_prop)

# # # plt.legend()
# # plt.tight_layout()


# # color_list = mcd.CSS4_COLORS # mcd.XKCD_COLORS,
# # solid_style_list = [name[1] for name in list(enumerate(color_list))[35:]]
# # dashed_style_list = [name[1] for name in list(enumerate(color_list))[35:]]


# fig_lw = plt.figure(figsize=(6,5))
# ax = plt.axes()

# powerlaw_fit = []
# lorentz_fit = []
# log_fit = []
# exponent = []

# ROI = (freq[~exclusion] < 0.2) & (freq[~exclusion] > 0.003)

# B_list = get_property(data_processed, 'field')[:,0]
# ROI_B = (B_list > -0.1) & (B_list < 0.7)
# colors = plt.cm.brg(np.linspace(0,1,len(ROI_B.nonzero()[0])))

# # ### 0 field
# # param_0field = np.polyfit(np.log(freq[~exclusion][ROI]), np.log(-data_processed[-1].PSD[:,0][~exclusion][ROI]/datum.factor**2), deg=1)
# # print(param_0field)
# # BG_0field = freq**param_0field[0]*np.exp(param_0field[1])
# # plt.loglog(freq[~exclusion][ROI], -data_processed[-1].PSD[:,0][~exclusion][ROI]/datum.factor**2)
# # plt.loglog(freq, BG_0field, 'k--')

# # plt.figure()
# # plt.plot(freq, BG_0field, 'k', label='BG')
# # for j, datum in enumerate(np.array(data_processed)[0:-3][::2]):
# #     # old
# #     # index j is for color
# #     # plt.loglog(freq, datum.PSD[:,0]/datum.factor**2, label=f'{datum.field[0]} (Gs)', color=colors[j])
# #     # plt.loglog(freq[~exclusion], -datum.PSD[:,0][~exclusion]/datum.factor**2, label=f'{datum.wl} (nm)')#, color=colors[j])
    
# #     ### linear fit in loglog plot
# #     PSD_temp = (BG_0field + datum.PSD[:,0]/datum.factor**2)
# #     plt.plot(freq[~exclusion], PSD_temp[~exclusion], label=f'{datum.field[0]} (Gs)')#, color=colors[j])
# #     plt.plot(freq[~exclusion][ROI], PSD_temp[~exclusion][ROI], label=f'{datum.field[0]} (nm)')#, color=colors[j])
# #     param = np.polyfit(np.log(freq[~exclusion][ROI]), np.log(PSD_temp[~exclusion][ROI]), deg=1)
# #     print(param)
# #     powerlaw_fit.append(param)
# #     plt.plot(freq, freq**param[0]*np.exp(param[1]), 'k--')
    
# #     # ### powerlaw fit a/(f + f0)^m
# #     # ROI = (freq[~exclusion] < 0.5) & (freq[~exclusion] > 0.003)
# #     # PSD_temp = (BG_0field + datum.PSD[:,0]/datum.factor**2)
# #     # plt.loglog(freq[~exclusion], PSD_temp[~exclusion], label=f'{datum.field[0]} (Gs)')#, color=colors[j])
    
# #     # # plt.loglog(freq[~exclusion][ROI], PSD_temp[~exclusion][ROI], label=f'{datum.field[0]} (nm)')#, color=colors[j])

# #     # param = curve_fit(inverse_power_law, freq[~exclusion][ROI], PSD_temp[~exclusion][ROI], p0 = [1.5, 0.001, 1e-16])
# #     # print(param[0][0])
# #     # powerlaw_fit.append(param[0])
# #     # plt.plot(freq[~exclusion][ROI], inverse_power_law(freq[~exclusion][ROI], *param[0]), '--')#,  color=colors[j], label=f'{str(datum["field"])}, ' + r'$\nu$ =' + f'{round(powerlaw_fit[-1][0][0],1)}')


# # print(np.array(powerlaw_fit)[:,0])

# # # # linear plot
# # # plt.xlim(0, 0.5)
# # # plt.ylim(0, .5e-12)

# # # # loglog plot
# # plt.xlim(1e-3, 0.5)
# # # plt.ylim(1e-14, .5e-12)
# # plt.ylim(0.2e-14, 1e-12)

# # plt.title(fileName, title_prop)
# # plt.tick_params(axis='both', which='both', labelsize=14)
# # ax.yaxis.get_offset_text().set_fontsize(14)
# # plt.xlabel('freq (MHz)', text_prop)
# # plt.ylabel(r'relative noise (1/Hz)', text_prop)

# # plt.legend()
# # plt.tight_layout()

# # plt.figure()
# # powerlaw_fit = np.array(powerlaw_fit)
# # plt.plot(get_property(data_processed, 'field')[0:-3,0][::2], powerlaw_fit[:,0], label='exponent')
# # # plt.plot(get_property(data_processed, 'field')[:,0], powerlaw_fit[:,0]/np.max(np.abs(powerlaw_fit[:,0])), label='exponent')
# # # plt.plot(get_property(data_processed, 'field')[:,0], powerlaw_fit[:,1]/np.max(np.abs(powerlaw_fit[:,1])), label='shift')
# # # plt.plot(get_property(data_processed, 'field')[:,0], powerlaw_fit[:,2]/np.max(np.abs(powerlaw_fit[:,2])), label='amp')

# # plt.legend()

# # # plt.figure()
# # # # plt.plot(get_property(data_processed, 'wl'), np.array(log_fit)[:,1], 'bo')
# # # plt.plot(get_property(data_processed, 'wl'), get_property(data_processed, 'sig_V0'), 'bo')


# # # plt.figure()
# # # # breakpoint()
# # # plt.plot(np.array(B_list)[(np.array(B_list) > -1) & (np.array(B_list) < -0.3)] , exponent, 'bo')

# plt.show()
