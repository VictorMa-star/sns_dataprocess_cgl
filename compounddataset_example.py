import h5py
import numpy as np

# 创建一个 HDF5 文件并写入 compound dataset
with h5py.File('example.h5', 'w') as f:
    dt = np.dtype([('temperature', 'f8'), ('pressure', 'f8')])  # 定义 compound dataset 的数据类型
    dset = f.create_dataset('compound_data', shape=(10,), dtype=dt)  # 创建 compound dataset
with h5py.File('example.h5', 'a') as f:
    dset = f['compound_data']
    data = np.array([(25.3, 101.2), (26.1, 99.8), (24.9, 100.5)], dtype=dt)  # 要写入的数据
    dset[0:3] = data  # 将数据写入 compound dataset 的前三个元素
