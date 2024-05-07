import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib._color_data as mcd
import pandas as pd
import BG_noise
# import raw_offset

# file_list = raw.sam1_site6_T_dependence

# file_list = raw.sam1_site6_345K_nirvana
# file_list = raw.sam1_site6_345K_nirvana
# file_list = raw.spot_size
# file_list = raw.sam1_site6_340K_nirvana

# ### compare 3 detectors!!!!
# # file_list = raw.sam1_site6_335K_nirvana
# # savename = 'sam1_site6_335K_nirvana'
# file_list = raw.sam1_site6_335K_thorlabs
# savename = 'sam1_site6_335K_thorlabs'
# # file_list = raw.sam1_site6_335K
# # savename = 'sam1_site6_335K'

# # for demonstration
# file_list = raw.sam1_site6_345K
# savename = 'sam1_site6_345K_newfocus'
# file_list = raw.sam1_site6_340K
# savename = 'sam1_site6_340K_newfocus'

### trial and error
# file_list = raw_offset.thorlabs_DC_feedback_330K + raw_offset.thorlabs_DC_feedback_296K
# savename = 'thorlabs_DC_feedback_330K'

# file_list = BG_noise.I_noise_relevent
file_list = BG_noise.shot_noise
savename = 'test'


figure_path = 'test/'

data = []
data_scale = []

'''value must be deivided by 1e6 since time domain data are measured in microseconds'''
for file in file_list:
    data.append(pd.read_csv(file, sep='\t', header=None).T/1e6)
    data_scale.append(pd.read_csv(file[:-4] + ' scale', sep='\t', header=None))
    # df = data_scale[-1][1][0]

    ### if lowB and highB data are also stored, then this will import those data as well
    try:
        data[-1][1] = pd.read_csv(file + ' highB', sep='\t', header=None).T/1e6
        data[-1][2] = pd.read_csv(file + ' lowB', sep='\t', header=None).T/1e6
        data[-1].columns = ['PSD', 'highB', 'lowB']
    except:
        data[-1].columns = ['PSD']




'''processing'''
# def lorentzian( x, x0, a, FWHM, y0 ):
#     return y0 + a * FWHM**2 / (  FWHM**2 + 4 * (x-x0)**2  )
# p0 = [0, 1e-15, 1, 0]

def lorentzian_0(x, a, FWHM, y0):
    return a*FWHM**2 / (FWHM**2 + 4*(x)**2 )
    # return a*FWHM**2 / (FWHM**2 + 4*(x)**2 )

p0 = [1e-12, 0.1, 0]
P = []
P_fit = []
param = []
cutoff_low = 0.10 # in MHz
cutoff_high = 1
for i in range(len(data)):
    df = data_scale[i][1][0]

    ### calculate integrated noise directly from data
    P.append(np.sum(data[i]['PSD'][int(cutoff_low/df):int(cutoff_high/df)])*df)
    # print(np.sum(data[i]['PSD'][int(1.5/df):int(2.5/df)]), np.std(data[i]['PSD'][int(1.5/df):int(2.5/df)]))

    ### Lorentzian fitting
    X = np.arange(0, len(data[i])*df, df)
    ROI = (X>cutoff_low) & (X<cutoff_high)
    param_temp = curve_fit(lorentzian_0, X[ROI], data[i]['PSD'][ROI], maxfev=10000, p0=p0)[0] # maxfev ???
    param_temp[1] = np.abs(param_temp[1])
    P_fit.append(param_temp[0]*param_temp[1]*np.pi/4)
    
    param.append(param_temp)

'''factor'''
if savename.find('thorlabs')!=-1:
    # ### thorlabs 1 MHz
    # factor = 3 * 2 # (V), I_0 includes both channels (voltage measure when one the channels is blockes = 3V)
    factor = 1 # with DC feedback, factor is already taken into account, only the factor 2 in expression for rotation angle: \delta V / V0 = 2*\theta   has to be considered
                # which is not to be included here
elif savename.find('nirvana')!=-1:
    ### nirvana 125 kHz
    factor = 0.3 * 2 * 10 * 25 # (V), voltage measure when one the channels is blockes = 3V，single channel 300.0 mV + SRSamp25 + 10X
else:
    ### newport 600 MHz
    factor = 0.5 *2  # voltage measure when one the channels is blockes = 0.5V 


# ### fitting attempts --> power law?
# #_________________________________________________________________________________________________________________________________________________________
# param_try = []
# for i in range(3,6):
#     df = data_scale[i][1][0]
#     X = np.arange(0, len(data[i])*df, df)
#     ROI = (X>cutoff_low) & (X<cutoff_high) & (data[i]['PSD']>0)
#     param_try.append(np.polyfit(np.log(X[ROI]), np.log(data[i]['PSD'][ROI]), deg=1))

# param_try = pd.DataFrame(param_try, columns=['slope', 'intercept'])
# print(param_try)
# plt.figure()
# df = data_scale[0][1][0]
# X = np.arange(0, len(data[0])*df, df)
# for i in range(3):
#     ROI = (data[i]['PSD']>0)
#     plt.plot(np.log(X[1:]), np.log(X[1:])*param_try['slope'][i] + param_try['intercept'][i])
#     plt.plot(np.log(X[1:]), np.log(data[3+i]['PSD'][1:]), lw=1)
# #_________________________________________________________________________________________________________________________________________________________


'''visualization'''
text_prop = {'fontsize': 16}
title_prop = {'fontsize': 18}
# cmap = plt.cm.twilight
# # plt.cm.cividis, plt.cm.viridis, plt.cm.plasma
# cmaplist = [cmap(i) for i in range(cmap.N)] # contains a list of tuples representing the RGB color code, (R, G, B)

color_list = mcd.CSS4_COLORS # mcd.XKCD_COLORS,
solid_style_list = [name[1] for name in list(enumerate(color_list))[30:]]
dashed_style_list = [name[1] for name in list(enumerate(color_list))[30:]]


B_list = [float(name[name.find('G(low)')-8:name.find('G(low)')-1].split(' ')[-1]) for name in file_list]
print(B_list)
P_dataframe = pd.DataFrame(np.array([B_list, P]).T, columns=['B', 'P'])
P_dataframe['P_fit'] = P_fit
P_dataframe = P_dataframe.sort_values(by='B')
print(P_dataframe)
P_dataframe['P_fit'] = P_dataframe['P_fit'].mask(np.abs(P_dataframe['P_fit']) > P_dataframe['P']*10, None)
# P_dataframe['P_fit'] = P_dataframe['P_fit'].mask(P_dataframe['P_fit']<0, None)


#---------------------------  power 
# V0 = list(np.linspace(100,600,6)) + list(np.linspace(800,1000,3)) + [1200]
# V0 = list(np.linspace(400,600,3)) + list(np.linspace(800,1000,3)) + [1200]
V0 = list(np.linspace(200,300,2))*2



# fig_P_B = plt.figure(figsize=(8,6))
# ax = plt.axes()
# plt.plot(P_dataframe['B'], P_dataframe['P'], label=f'integrated, {cutoff_low} < f < {cutoff_high} MHz')
# plt.plot(P_dataframe['B'], P_dataframe['P_fit'], label='integrated from Lorentzian fitting')
# plt.title(r'integrated noise v.s. magnetic field', title_prop)
# plt.tick_params(axis='both', which='both', labelsize=14)
# ax.yaxis.get_offset_text().set_fontsize(14)
# plt.xlabel('external magnetic field (Gs)', text_prop)
# plt.ylabel(r'integrated noise ($V^2$)', text_prop)
# plt.legend()
# plt.tight_layout()
# # plt.savefig(figure_path + savename + '_P_B' + '.png')

# fig_raw = plt.figure(figsize=(8,6))
# ax = plt.axes()

# for i in P_dataframe.index:
#     df = data_scale[i][1][0]
#     X = np.arange(0, len(data[i])*df, df)
#     # plt.loglog(X, data[i]['highB'], '-', color=solid_style_list[i], label=f'{B_list[i]} Gs')
#     plt.plot(X, data[i]['PSD']*(1e6/(factor*2))**2, '-', color=solid_style_list[i], label=f'{B_list[i]} Gs')

# plt.xlabel('frequency (MHz)', text_prop)
# plt.ylabel(r'PSD ($\mu rad^2/Hz$)', text_prop)
# # plt.title('power dependence measurement', title_prop)
# plt.title('Lorentzian fit loglog plot', title_prop)
# plt.tick_params(axis='both', which='both', labelsize=14)
# ax.yaxis.get_offset_text().set_fontsize(14)
# plt.ylim(-1, 1)
# plt.xlim(0.005, 2)
# plt.legend()
# plt.tight_layout()
# # plt.savefig(figure_path + savename + '_loglog' + '.png')



fig_offset = plt.figure(figsize=(8,6))
ax = plt.axes()
median_list = []
cut1_list = []
cut2_list = []
for i in P_dataframe.index:
    df = data_scale[i][1][0]
    X = np.arange(0, len(data[i])*df, df)
    # plt.plot(X, data[i]['highB']*(1e6/(factor*2))**2, '-', color=solid_style_list[i], label=f'{B_list[i]} Gs')
    plt.plot(X, data[i]['highB']*(1e6/(factor*2))**2, '-', color=solid_style_list[i], label=f'{V0[i]} mV')
    
    cut1_list.append(data[i]['highB'][0.16//df])
    cut2_list.append(data[i]['highB'][0.4//df])
    median_list.append(np.median(data[i]['highB'][len(data[i]['highB'])//5*3:]))

# plt.plot([cutoff_low, cutoff_low], [0, max([data[i]['PSD'][3:].max() for i in range(len(data))])*10], 'k-')
y_upper_lim = 10
# plt.ylim(-.5e-15, y_upper_lim)
plt.ylim(0, y_upper_lim)

plt.xlim(0.005, 2)
# plt.xlim(0.005, .125)
plt.title('comp offset', title_prop)
plt.tick_params(axis='both', which='both', labelsize=14)
ax.yaxis.get_offset_text().set_fontsize(14)
plt.xlabel('frequency (MHz)', text_prop)
plt.ylabel(r'PSD ($\mu rad^2/Hz$)', text_prop)
# plt.ylabel(r'PSD ($n rad^2/Hz$)', text_prop)
plt.legend()
plt.tight_layout()
# plt.savefig(figure_path + savename + '_offset' + '.png')



plt.figure()
median_list = np.array(median_list)
cut1_list = np.array(cut1_list)
cut2_list = np.array(cut2_list)


# plt.plot(V0, median_list, 'o')
plt.plot(V0, np.sqrt(1/median_list), 'o', label='median tail, 1/sqrt')
plt.plot(V0, np.sqrt(1/cut1_list), 'o', label='0.16Mhz, 1/sqrt')
plt.plot(V0, np.sqrt(1/cut2_list), 'o', label='0.4Mhz, 1/sqrt')
plt.legend()
# breakpoint()

plt.show()
