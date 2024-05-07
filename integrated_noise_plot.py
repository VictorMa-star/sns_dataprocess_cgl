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
from SNS_function import P_data

processed_path = '../processed/'
fileName_processed = 'SNS_R_IP_site8_T_dependence_P.h5'

'''import data'''
P_files = h5py.File(processed_path + fileName_processed, 'r')
data = []
for name in P_files.keys():
    print(name)
    data.append(P_data(P_files, name))
    print(P_data(P_files, name).P)
plt.figure()
ax = plt.axes(projection='3d')
colors = plt.cm.brg(np.linspace(0,1,len(data)))
for j, datum in enumerate(data):
    ax.plot3D([datum.T]*np.shape(datum.P)[0], datum.P[:,0], datum.P[:,1], 'o', c=colors[j])
    ax.plot3D([datum.T]*np.shape(datum.P)[0], datum.P[:,0], datum.P[:,1], '-', c=colors[j])

plt.show()
