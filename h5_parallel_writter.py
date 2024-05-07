import os
import time
import numpy as np
import pandas as pd
import h5py
import json
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from create_Zhijie_dataset import get_files_with_prefix_and_suffix

def load_data(file):
   data = pd.read_csv(file, sep='\t', header=None).T.astype(float) / 1e6
   try:
       data.columns = ['PSD', 'highB', 'lowB']
   except:
       data.columns = ['PSD']
   metadata_path = file[:file.rfind('_')] + '_metadata'
   return (file, data, metadata_path)

def write_hdf5(save_path, fileName, data_file):
   file, data, metadata_path = data_file
   dset_name = os.path.basename(file)
   with h5py.File(os.path.join(save_path, fileName), 'a') as f:
       if dset_name in f:
           print(f'{dset_name} already exists in HDF5.')
       else:
           f.create_dataset(dset_name, data=data, dtype=np.float32)
           if os.path.isfile(metadata_path):
               with open(metadata_path, 'r') as ipt:
                   metadata = json.load(ipt)
                   for key in metadata.keys():
                       f[dset_name].attrs[key] = metadata[key]

           timestamp = time.strftime('%Y%m%d-%H:%M', time.localtime(os.path.getmtime(file)))
           f[dset_name].attrs['timestamp'] = timestamp
           # print(f'{dset_name} written to HDF5.')
#TODO：实现按时间排序
if __name__ == '__main__':
   start_time = time.time()
   file_path = r"D:\c102sns\SNS\0506_310K"
   save_path = '../test_MTY/'
   fileName = '310K_1.h5'
   file_list = get_files_with_prefix_and_suffix(file_path, '', '0PSD')

   # multiprocessing 加速
   with Pool(processes=16) as pool:
       loaded_data = list(tqdm(pool.imap(load_data, file_list), total=len(file_list), desc="Loading data"))

   # 在主线程中处理所有写入操作，确保HDF5文件的线程安全
   for data_file in tqdm(loaded_data, desc="Writing to HDF5"):
       write_hdf5(save_path, fileName, data_file)

   print(f'Load and Write HDF5 time cost (s): {time.time() - start_time}')