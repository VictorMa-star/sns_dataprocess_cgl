import time
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
import h5py
import matplotlib.colors as mcolors
import matplotlib._color_data as mcd

from matplotlib import pyplot as plt
import sys
import os

# for integrated noise
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter


sys.path.insert(0, '../python')
from SNS_function import SNS_data, get_property, inverse_power_law, inverse_power_law_P, lorentzian_0
from importlib import import_module

result_path = '../result/'

# fileName = 'SNS_R_IP_322o5K_site8.h5'
# fileName = 'SNS_R_IP_325K_site8.h5'
# fileName = 'SNS_R_IP_330K_site8.h5'
# fileName = 'SNS_R_IP_335K_site8.h5'
# fileName = 'SNS_R_IP_337o5K_site8.h5'
# fileName = 'SNS_R_IP_340K_site8.h5'
# fileName = 'SNS_R_IP_342o5K_site8.h5'
# fileName = 'SNS_R_IP_345K_site8.h5'

# fileName = 'SNS_E_IP_325K_site8_633nm_2.h5'
# fileName = 'SNS_E_IP_320K_site8_633nm_2.h5'
# fileName = 'SNS_E_OOP_335K_site8_730nm.h5'
fileName = 'SNS_R_OOP_800nm_330K_0822.h5' ##!!file name need to be modified here1!!

f = h5py.File(result_path + fileName, 'r')
# # demonstration
# f_shot = h5py.File(result_path + 'shot_noise(noPBS).h5', 'r')
# f_intensity = h5py.File(result_path + 'intensity_noise(noPBS).h5', 'r')
f_electronic = h5py.File(result_path + 'electronic_noise.h5', 'r')

electronic_noise = []
for name in f_electronic.keys():
    electronic_noise.append(SNS_data(f_electronic, name))
f_electronic.close()


# processed_path = '../processed/'
# fileName_processed = 'SNS_R_IP_site8_T_dependence_P.h5'

data = []
SNS_dataset = import_module('SNS_dataset')
for name in f.keys():
    if '..\\20220822\\' + name in getattr(SNS_dataset, fileName[:-3]):##!!file name need to be modified here2!!
        data.append(SNS_data(f, name))
        
        # # # extract Z position
        # data[-1].Z = float(name.split('_')[0][name.find('Z=')+2:])

f.close()

# breakpoint()
# https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string#:~:text=Python%20defines%20an%20__import__function%2C%20which%20takes%20a%20string,to%20interpret%20the%20name%20in%20a%20package%20context.
# x = fileName[:-3]
# from SNS_dataset.locals()[x] as name_list

'''processing'''
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


'''calculation'''
seg_len = np.shape(data[0].PSD)[0]*2 # Nyquist
sr = data[0].sr
df = sr/seg_len
freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6

## try different cutoff@!!!!!!!!!!!!!!!!!!!!!!!!!!
# P_cutoff = [0.0005, 0.3]
P_cutoff = [0.001, 0.3]
ROI_P = (freq>P_cutoff[0]) & (freq<P_cutoff[1])
for datum in data:
    PSD_spline = interp1d(freq[ROI_P], datum.PSD[:,0][ROI_P]/datum.factor**2, kind='cubic')
    datum.P = np.sum(PSD_spline(freq[ROI_P])) #it is where the intergrated noise comes from

# # write P result into file
# # ---------------------------------------------------------------------
# if os.path.isfile(processed_path + fileName_processed):
#     P_file = h5py.File(processed_path + fileName_processed, 'a')
# else:
#     P_file = h5py.File(processed_path+ fileName_processed, 'w')

# try:
#     dset_name = fileName
#     P_file.create_dataset(dset_name, data=np.array([get_property(data_processed, 'field')[:,0], \
#                                                     get_property(data_processed, 'P')]).T, dtype = np.float32)

#     P_file[dset_name].attrs['P_cuttoff'] = P_cutoff
#     P_file[dset_name].attrs['T (K)'] = data[0].T
# except RuntimeError:
#         print(f'check if "{dset_name}" already exist')
# except:
#     print('something goes wrong!!!')

# P_file.close()
# # ---------------------------------------------------------------------

p0 = [1e-12, 0.1]
# P = []
# P_fit = []
param = []
cutoff_low = 0.0020 # in MHz
cutoff_high = 0.25

for datum in data_processed:    
    ROI = (freq>cutoff_low) & (freq<cutoff_high)
    param_temp = curve_fit(lorentzian_0, freq[ROI], datum.PSD[:,0][ROI], maxfev=10000, p0=p0)[0] # maxfev ???
    param.append(param_temp)

# order = np.argsort(B_list)
# B_list = np.array(B_list)[order]
# P_list = np.array(P_list)[order]
# rotation_noise = rotation_noise[order]

'''exclusion'''
# include 800Gs
f_ex = 0.0276
Df = 0.001
# enough to mask all except for 800Gs
# f_ex = 4.5e-2
# Df = 0.2e-2
exclusion = [False]*len(freq)
exclusion_list = []
for n in range(1,3):
    exclusion = exclusion | ((freq > n*f_ex - Df) & (freq < n*f_ex + Df))
    exclusion_list.append((freq > n*f_ex - Df) & (freq < n*f_ex + Df))


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


'''visualziation'''
text_prop = {'fontsize': 16}
title_prop = {'fontsize': 18}
### P
plt.figure()
ax = plt.axes()
# plt.plot(get_property(data_processed, 'field')[:,0], get_property(data_processed, 'sig_V0')*1e-20/3, '-bo')
plt.plot(get_property(data_processed, 'field')[:,0], get_property(data_processed, 'P'), '-bo')
max_field = 1.05*np.max(np.abs(get_property(data_processed, 'field')[:,0]))
plt.xlim(-max_field, max_field)
# plt.xlim(np.min(get_property(data_processed, 'Z')), np.max(get_property(data_processed, 'Z')))

plt.title(fileName, title_prop)
plt.tick_params(axis='both', which='both', labelsize=14)
ax.yaxis.get_offset_text().set_fontsize(14)
plt.xlabel('in-plane B (Gs)', text_prop)
plt.ylabel('integrated noise', text_prop)
plt.text(-1,0,'P_cutoff = '+str(P_cutoff))
plt.tight_layout()


# def g1(x, x0, b, A):
#     w = (2*((x-x0)/b)**2 + 1)**0.5
#     return A/w

# def g2(x, x0, b, A):
#     w = (2*((x-x0)/b)**2 + 1)**0.5
#     return A/w**2

# def g_nu(x, x0, b, A, nu):
#     w = (2*((x-x0)/b)**2 + 1)**0.5
#     return A/w**nu

# ### P dependence on Z position (i.e., spot size)
# plt.figure()
# ax = plt.axes()
# Z_position = get_property(data_processed, 'Z')
# plt.plot(get_property(data_processed, 'Z'), get_property(data_processed, 'P'), 'bo', label='raw')

# # ROI_Z = (Z_position>=-2) & (Z_position<=0.5)
# # ROI_Z = (Z_position>=-4.5) & (Z_position<=-2.25)
# ROI_Z = (Z_position>=-4.5) & (Z_position<=-2)

# param_Z_1 = curve_fit(g1, Z_position[ROI_Z], get_property(data_processed, 'P')[ROI_Z], p0 = [-3.38087254e+00, 1.5e-01, 4.39906066e-10])
# param_Z_2 = curve_fit(g2, Z_position[ROI_Z], get_property(data_processed, 'P')[ROI_Z], p0 = [-3.5, .4, 3e-10])

# ### try:
# # param_Z_nu = curve_fit(g_nu, Z_position[ROI_Z], get_property(data_processed, 'P')[ROI_Z], p0 = [-3.38087254e+00, 1.5e-01, 4.39906066e-10, 1.5])

# print('perimeter law: ', param_Z_1)
# print('area law: ', param_Z_2)
# Z_list = np.linspace(Z_position[ROI_Z].min(), Z_position[ROI_Z].max(), 100)
# plt.plot(Z_list, g1(Z_list, *param_Z_1[0]), 'r-', label='perimeter law fit')
# plt.plot(Z_list, g2(Z_list, *param_Z_2[0]), 'g-', label='area law fit')
# # plt.plot(Z_list, g_nu(Z_list, *param_Z_nu[0]), 'k--', label='test nu law fit')

# # plt.plot(Z_list, g1(Z_list, *[-3.38087254e+00,  1.8e-01,  4.39906066e-10]), 'g-', label='perimeter law fit')

# plt.title('P v.s. Z pos', title_prop)
# plt.tick_params(axis='both', which='both', labelsize=14)
# ax.yaxis.get_offset_text().set_fontsize(14)
# plt.xlabel(r'Z position (10 $\mu$m)', text_prop)
# plt.ylabel('integrated noise', text_prop)
# plt.legend()
# plt.tight_layout()

# breakpoint()

### plot raw - BG
fig = plt.figure(figsize=(6,5))
ax = plt.axes()
freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6
data_plot = data_processed

field_L = 0.4
field_R = 0.8
for i in range(len(data_plot)):
    if data_plot[i].field[0]==field_L:
        field_L_ind = i
    elif data_plot[i].field[0]==field_R:
        field_R_ind = i

colors = plt.cm.brg(np.linspace(0,1,field_R_ind-field_L_ind))
for j in range(field_L_ind,field_R_ind):
    # plt.semilogy(freq, (datum['PSD'] - electronic_noise[1]['PSD'])/datum['factor']**2, label=datum['label'])
    datum = data_plot[j]
    # plt.plot(freq, -BG_0field + datum.PSD[:,0]/datum.factor**2, color=colors[j], label=f"{str(datum.field[0])} (Gs)")
    
    # raw
    plt.plot(freq, datum.PSD[:,0]/datum.factor**2, color=colors[j-field_L_ind], label=f"{str(datum.field[0])} (Gs)")

    # plt.plot(freq, datum.PSD[:,0]/datum.factor**2, color=colors[j], label=f"{str(datum.field[0])} (Gs)")
    # plt.plot(freq[~exclusion], datum.PSD[:,0][~exclusion]/datum.factor**2, color=colors[j], label=f"{str(datum.field[0])} (Gs)")

    # fill the gaps with spline interpolation
    # plt.plot(freq, interp1d(freq[~exclusion], datum.PSD[:,0][~exclusion]/datum.factor**2, kind='cubic')(freq), color=colors[j], label=f"{str(datum.field[0])} (Gs)")
    
    # # mask the spikes
    # for exclusion_range in exclusion_list:
    #     plt.plot(freq[exclusion_range], datum.PSD[:,0][exclusion_range]/datum.factor**2, 'w')

plt.xlim(0, 0.05)
plt.ylim(0, 6e-12)

plt.title(fileName, title_prop)
plt.tick_params(axis='both', which='both', labelsize=14)
ax.yaxis.get_offset_text().set_fontsize(14)
plt.xlabel('frequency (MHz)', text_prop)
plt.ylabel(r'relative noise ($1/Hz$)', text_prop)

plt.legend()
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

plt.show()
