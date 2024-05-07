import time
from joblib import PrintTime
import numpy as np
import pandas as pd
import h5py
import json
from matplotlib import pyplot as plt
import sys

sys.path.insert(0, '../python')
from SNS_function import SNS_data

extract_path = './'
result_path = '../result/'
fileName = 'SNS_R_IP_332o5K_site8.h5'

f = h5py.File(result_path + fileName, 'r')

data = []
import SNS_dataset
print()
for name in f.keys():
    if "..\\20220312\\" + name in SNS_dataset.SNS_R_IP_332o5K_site8:
        # data.append(SNS_data(f, name))
        np.savetxt(extract_path + name + '(extracted)', f[name][:])

        property_dict = {}
        for item in f[name].attrs.keys():
            property_dict[item] = np.array([f[name].attrs[item]]).tolist()[0]
            # this is to solve the error, "int32 is not serializable",; i.e.m json cannot recognize dtype unique to numpy
            # "int32" would be converted to "int" after this line
            # https://stackoverflow.com/questions/49795525/typeerror-object-of-type-int32-is-not-json-serializable
        print(property_dict)
        with open(extract_path + name[:-4] + 'metadata' + '(extracted)' , "w") as metadata_file:
            # metadata = json.dumps(property_dict)
            json.dump(property_dict, metadata_file)
            metadata_file.close()

f.close()
# print(property_dict)


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
