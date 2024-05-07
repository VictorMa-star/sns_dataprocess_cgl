import os
import sys
import time
import numpy as np
import pandas as pd
import h5py
import json
# import CSS_SNS
from create_Zhijie_dataset import get_files_with_prefix_and_suffix
from tqdm import tqdm
'''this program integrated a chunck of csv files which belongs to the dataset into a single HDF5 file.
at some point, you should save the attrs directly with Labview program, which are to be transfered directly into attrs of the resulting h5 file with this program.
'''
start_time = time.time()
file_list = []
fileName = 'test_MTY.h5'
file_list =get_files_with_prefix_and_suffix(r"D:\\c102sns\SNS\\330KTest",'','0PSD')
# file_path = '../20220216/'
save_path = '../test_MTY/'

# fileName  = sys.argv[1:]

'''import data'''
# file_list = test_filelist.I_noise_relevent

# print(file_list)
data = []
data_scale = []
# breakpoint()
for file in tqdm(file_list, desc="loading data", unit="file"):
    data.append(pd.read_csv(file, sep='\t', header=None).T.astype(float)/1e6)
    try:
        # Maybe it's ['PSD', 'lowB','highB']--MTY
        data[-1].columns = ['PSD', 'highB', 'lowB']
    except:
        data[-1].columns = ['PSD']

mid_time = time.time()
print(f'load data time cost (s): {time.time() - start_time}')


'''write into HDF5'''
if os.path.isfile(save_path + fileName):
    f = h5py.File(save_path + fileName, 'a')
else:
    f = h5py.File(save_path+ fileName, 'w')


for i in range(len(data)):
    try:
        dset_name = os.path.basename(file_list[i])
        f.create_dataset(dset_name, data=data[i], dtype = np.float32)
        with open(file_list[i][:file_list[i].rfind('_')] + '_metadata', 'r') as ipt:
            metadata = json.load(ipt)
            for key in metadata.keys():
                f[dset_name].attrs[key] = metadata[key]
            ipt.close()
        
        source_name = file_list[i]
        timestamp = time.strftime('%Y%m%d-%H:%M', time.localtime(os.path.getmtime(source_name)))
        f[dset_name].attrs['timestamp'] = timestamp

        # f[dset_name].attrs['power'] = dset_name.find()
    except RuntimeError:
        print(f'check if "{os.path.basename(file_list[i])}" already exist')
    except:
        print('something goes wrong!!!')


f.close()

print(f'HDF5 related time cost (s): {time.time() - mid_time}')

'''HDF5 tricks'''
# basics
# https://docs.h5py.org/en/stable/high/dataset.html
# combining h5 files --> probably unneessary, use  external links
# https://stackoverflow.com/questions/18492273/combining-hdf5-files
