import os
import time
import numpy as np
import pandas as pd

'''for quick inspection'''
TD = np.loadtxt()

file_list = []

data = []
data_scale = []
# breakpoint()
for file in file_list:
    data.append(pd.read_csv(file, sep='\t', header=None).T/1e6)
    try:
        data[-1].columns = ['PSD', 'highB', 'lowB']
    except:
        data[-1].columns = ['PSD']

print(np.sum(data[-1]['PSD']))
