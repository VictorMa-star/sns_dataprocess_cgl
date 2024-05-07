import time
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
import h5py
import matplotlib.colors as mcolors
import matplotlib._color_data as mcd
import math

from matplotlib import pyplot as plt
import sys
import os

# for integrated noise
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter


sys.path.insert(0, '../python')
from SNS_function import SNS_data, get_property, inverse_power_law, inverse_power_law_P, lorentzian_0
from importlib import import_module
from SNS_calculate_error import process_directory
'''
This script is to write all useful info into the .processed.h5 files.
You may have to make minor changes to the interval for integration or the fitting parameter, 
and store them into the .processed.h5 files as well. 
After doing so, you should be able to reproduce all results with only the .processed.h5 files.
'''
result_path = '../test_MTY/'
fileName = '310K_1.h5'
int_error_factor = 620418
f = h5py.File(result_path + fileName, 'r')
int_folder_path = ''
# result_fig_path = r'D:\SNS\test_result_processed\\'
'''
电子噪声部分暂时不予考虑
# f_electronic = h5py.File(result_path + 'electronic_noise.h5', 'r')

# electronic_noise = []
# for name in f_electronic.keys():
#     electronic_noise.append(SNS_data(f_electronic, name))
# f_electronic.close()

'''
processed_path = '../test_MTY/'
# fileName_processed = 'SNS_R_IP_800nm_T_dependence.processed.h5'
fileName_processed = 'test_processed_MTY.h5'

# fileName[:-3] + '.processed' + fileName[-3:]
# f_processed = h5py.File(processed_path + fileName_processed, 'w')
f_processed = h5py.File(processed_path + fileName_processed, 'a') # should be default, unless one wants to overwrite the file

# fileName_processed = 'SNS_R_IP_site8_T_dependence_P.h5'

data = []
name_list = []
for name in f.keys():
    # if '..\\20211203\\' + name in getattr(SNS_dataset, fileName[:-3]):
        data.append(SNS_data(f, name))
        name_list.append(name)
        # # # extract Z position
        # data[-1].Z = float(name.split('_')[0][name.find('Z=')+2:])

'''processing'''
# sort the data by field
data_processed = []
sort_by = []
for datum in data:
    sort_by.append(datum.field[0])
    # sort_by.append(datum.sig_V0)
    # sort_by.append(datum.Z)


# sort by wl, power, etc...
sort_index = np.argsort(sort_by)

for i in sort_index:
    data_processed.append(data[i])


'''freq'''
seg_len = np.shape(data[0].PSD)[0]*2 # Nyquist
sr = data[0].sr
df = sr/seg_len
freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6

'''exclusion'''
# include 800Gs
# f_ex = 0.0276
# Df = 0.001
f_ex = 0
Df = 0.0003

# enough to mask all except for 800Gs
# f_ex = 4.5e-2
# Df = 0.2e-2
exclusion = np.array([False]*len(freq))
exclusion_list = []

# for n in range(1,2):
#     exclusion = exclusion | ((freq > n*f_ex - Df) & (freq < n*f_ex + Df))
#     exclusion_list.append((freq > n*f_ex - Df) & (freq < n*f_ex + Df))

# f_ex = 0.07705
# Df = 0.0005
# for n in range(1,2):
#     exclusion = exclusion | ((freq > n*f_ex - Df) & (freq < n*f_ex + Df))
#     exclusion_list.append((freq > n*f_ex - Df) & (freq < n*f_ex + Df))

'''integrated noise'''
#在此设置积分范围
P_cutoff = [0.001, 0.05]
ROI_P = (freq>P_cutoff[0]) & (freq<P_cutoff[1])

smo_inspection = []
for datum in data:
    ### raw
    datum.P = np.sum(datum.PSD[:,0][ROI_P])/datum.factor**2*df

    ### smoothened
    PSD_smo = savgol_filter(datum.PSD[:,0][~exclusion], 5, 3)
    PSD_spline = interp1d(freq[~exclusion], PSD_smo, kind='linear')(freq)
    # got to plot this out and see how much change does this make
    datum.P_smo = np.sum(PSD_spline[ROI_P])/datum.factor**2*df
    # smo_inspection.append(plt.plot(freq[ROI_P], PSD_spline[ROI_P]))


'''write intermediate results to '.process.h5' files'''
if fileName[:-3] in f_processed:
    pass
else:
    f.copy(f['/'], f_processed['/'], fileName[:-3])

f_processed[f'{fileName[:-3]}'].attrs['name_list'] = np.array(name_list, dtype='S62')
f_processed[f'{fileName[:-3]}'].attrs['exclusion'] = exclusion
f_processed[f'{fileName[:-3]}'].attrs['P_cutoff'] = P_cutoff

# Process the first folder
if int_folder_path:
    int_data = np.array(process_directory(int_folder_path)).astype(float)
    int_data[:,2]*=int_error_factor
    int_data[:,1]*=int_error_factor
    f_processed[f'{fileName[:-3]}'].attrs['P_int'] =int_data
Zhi_data_int = np.array([get_property(data_processed, 'field')[:,0], \
                                                    get_property(data_processed, 'P')]).T

# print((np.array([int_data[:,0], \
#         int_data[:,1]]).T / np.array([get_property(data_processed, 'field')[:,0], \
#                                                     get_property(data_processed, 'P')]).T)[:,1])
# print(np.average((np.array([int_data[:,0], \
#         int_data[:,1]]).T / np.array([get_property(data_processed, 'field')[:,0], \
#                                                     get_property(data_processed, 'P')]).T)[:,1]))
# int_field = process_directory(folder_path_1)
# int_values_1 = np.array(output_data_1)[:, 1].astype(float)
# error_values_1 = np.array(output_data_1)[:, 2].astype(float) * int_error_factor

f_processed[f'{fileName[:-3]}'].attrs['P'] = Zhi_data_int

# print(get_property(data_processed, 'P') / int_values_1)
f_processed[f'{fileName[:-3]}'].attrs['P_smoothened'] = np.array([get_property(data_processed, 'field')[:,0], \
                                                    get_property(data_processed, 'P_smo')]).T
f_processed[f'{fileName[:-3]}'].attrs['Temperature (K)'] = f[list(f.keys())[0]].attrs['Temperature (K)']
f_processed[f'{fileName[:-3]}'].attrs['segment length'] = f[list(f.keys())[0]].attrs['segment length']
f_processed[f'{fileName[:-3]}'].attrs['sample rate(MHz)'] = f[list(f.keys())[0]].attrs['sample rate(MHz)']
# should also include fitting results, if any
f.close()
f_processed.close()

# '''BG'''
# ROI = (freq[~exclusion] < 0.05) & (freq[~exclusion] > 0.005)

# ### 0 field
# param_0field = np.polyfit(np.log(freq[~exclusion][ROI]), np.log(-data_processed[-1].PSD[:,0][~exclusion][ROI]/datum.factor**2), deg=1)
# print(param_0field)
# # BG_0field = freq**param_0field[0]*np.exp(param_0field[1])
# param = curve_fit(inverse_power_law, freq[ROI], -data_processed[-1].PSD[:,0][ROI]/data_processed[-1].factor**2, p0 = [1.5, 0.001, .2e-14])
# print(param)
# # BG_0field = inverse_power_law(freq, *param[0])
# BG_0field = data_processed[-1].PSD[:,0]/data_processed[-1].factor**2
# # fig_BG = plt.figure(figsize=(6,5))
# # ax = plt.axes()
# # plt.loglog(freq[~exclusion][ROI], -data_processed[-1].PSD[:,0][~exclusion][ROI]/datum.factor**2)
# # plt.loglog(freq, BG_0field, 'k--')


# '''visualziation'''
# text_prop = {'fontsize': 16}
# title_prop = {'fontsize': 18}
# ### P
# plt.figure()
# ax = plt.axes()
# plt.errorbar(output_data_1[:,0], output_data_1[:,1], yerr=output_data_1[:,2], fmt='o', linestyle='-', capsize=3,label='centering')
# max_field = 1.05*np.max(np.abs(get_property(data_processed, 'field')[:,0]))
# plt.xlim(-max_field, max_field)
# # plt.xlim(np.min(get_property(data_processed, 'Z')), np.max(get_property(data_processed, 'Z')))

# plt.title(fileName, title_prop)
# plt.tick_params(axis='both', which='both', labelsize=14)
# ax.yaxis.get_offset_text().set_fontsize(14)
# plt.xlabel('in-plane B (Gs)', text_prop)
# plt.ylabel('integrated noise', text_prop)

# plt.tight_layout()

# ### plot raw - BG
# fig = plt.figure(figsize=(6,5))
# ax = plt.axes()
# freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6
# data_plot = data_processed

# colors = plt.cm.brg(np.linspace(0,1,len(data_plot)))
# for j in range(len(data_plot)):
#     # plt.semilogy(freq, (datum['PSD'] - electronic_noise[1]['PSD'])/datum['factor']**2, label=datum['label'])
#     datum = data_plot[j]
#     # plt.plot(freq, -BG_0field + datum.PSD[:,0]/datum.factor**2, color=colors[j], label=f"{str(datum.field[0])} (Gs)")
    
#     # raw
#     plt.plot(freq, datum.PSD[:,0]/datum.factor**2, color=colors[j], label=f"{str(datum.field[0])} (Gs)")
#     # plt.plot(freq[~exclusion], datum.PSD[:,0][~exclusion]/datum.factor**2, color=colors[j], label=f"{str(datum.field[0])} (Gs)")

#     # fill the gaps with spline interpolation
#     PSD_smo = savgol_filter(datum.PSD[:,0][~exclusion], 5, 3)
#     PSD_spline = interp1d(freq[~exclusion], PSD_smo, kind='linear')(freq)/datum.factor**2
#     plt.plot(freq, PSD_spline, color=colors[j], label=f"{str(datum.field[0])} (Gs)")
    
#     # mask the spikes
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


# # # color_list = mcd.CSS4_COLORS # mcd.XKCD_COLORS,
# # # solid_style_list = [name[1] for name in list(enumerate(color_list))[35:]]
# # # dashed_style_list = [name[1] for name in list(enumerate(color_list))[35:]]

# # ### plot "raw - BG" and "fit"
# # plt.figure()
# # ax = plt.axes()
# # powerlaw_fit = []
# # inverse_fit = []
# # lorentz_fit = []
# # log_fit = []
# # exponent = []
# # plt.plot(freq, BG_0field, 'k', label='BG')
# # ROI_B = slice(2,-2)
# # for j, datum in enumerate(np.array(data_processed)[ROI_B]):
# #     ### linear fit in loglog plot
# #     PSD_temp = (-BG_0field + datum.PSD[:,0]/datum.factor**2)
# #     # plt.plot(freq[~exclusion], PSD_temp[~exclusion], label=f'{datum.field[0]} (Gs)')#, color=colors[j])
# #     # plt.plot(freq[~exclusion][ROI], PSD_temp[~exclusion][ROI], label=f'{datum.field[0]} (nm)')#, color=colors[j])

# #     plt.loglog(freq[~exclusion], PSD_temp[~exclusion], label=f'{datum.field[0]} (Gs)')#, color=colors[j])
# #     plt.loglog(freq[~exclusion][ROI], PSD_temp[~exclusion][ROI], label=f'{datum.field[0]} (nm)')#, color=colors[j])
# #     try:
# #         param = np.polyfit(np.log(freq[~exclusion][ROI]), np.log(PSD_temp[~exclusion][ROI]), deg=1)
# #         # print(param)
# #         powerlaw_fit.append(param)
# #         plt.loglog(freq, freq**param[0]*np.exp(param[1]), 'k--')
# #     except:
# #         pass
# #     try:
# #         param = curve_fit(inverse_power_law, freq[ROI], PSD_temp[~exclusion][ROI], p0 = [1.5, 0.001, 1e-16])
# #         plt.loglog(freq, inverse_power_law(freq, *param[0]), 'r--')
# #         inverse_fit.append(param[0])
# #     except:
# #         inverse_fit.append([np.NaN]*3)
# #         pass
    
    
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
# # plt.plot(get_property(data_processed, 'field')[:,0][ROI_B], list(map(inverse_power_law_P, *np.transpose(inverse_fit))))
plt.plot(Zhi_data_int[:,0], Zhi_data_int[:,1],linestyle='-')
plt.show()
