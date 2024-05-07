import h5py
import re
import numpy as np

processfile = "D:\\c102sns\\SNS\\test_MTY\\test_processed_MTY.h5"
plotfile = "D:\\c102sns\\SNS\\test_MTY\\test_processed_draw_MTY.h5"
processed_fields = set()  # 用于存储已处理的 field 值
def convert_to_tuples(input_list):
   # Use the zip function to transpose the list of lists
   transposed_list = zip(*input_list)
   
   # Convert the transposed list into a list of tuples
   list_of_tuples = [tuple(sublist) for sublist in transposed_list]
   
   return list_of_tuples
# 打开源文件和目标文件
with h5py.File(processfile, 'r') as source_h5, h5py.File(plotfile, 'w') as target_h5:
    # 遍历源文件中的数据
    for group_name, group in source_h5.items():
        # 对每个 group，在目标文件中创建一个对应的 group
        seg_len = group.attrs['segment length'] # Nyquist
        sr = group.attrs['sample rate(MHz)']*1e6
        df = sr/seg_len
        freq = list(np.linspace(0, df*seg_len/2, seg_len//2)/1e6)
        target_group = target_h5.create_group(group_name)
        typeposilist = [("Frequency/MHz","f8")]
        group_dataposi = [freq]
        typenegalist = [("Frequency/MHz","f8")]
        group_datanega = [freq]        
        for dataset_name, dataset in group.items():
            # 使用正则表达式匹配形如 "field3." 和 "field=[-2.3" 中的浮点数
            match = re.search(r'field=\[([-+]?\d+\.\d+), ([-+]?\d+\.\d+)', dataset_name)  
            if match:
                # 提取 field_value 并创建 compound dataset member
                field_value = float(match.group(1))
                background = float(match.group(2))            
                if background > 0:
                    typeposilist.append((str(field_value) + 'Gs', 'f8'))  
                    group_dataposi.append(list(dataset[:, 0]))
                    processed_fields.add(field_value)
                elif background <= 0:
                    typenegalist.append((str(field_value) + 'Gs', 'f8'))  
                    group_datanega.append(list(dataset[:, 0]))
                    processed_fields.add(field_value)                    
        compound_memberposi = convert_to_tuples(group_dataposi)
        compound_membernega = convert_to_tuples(group_datanega)
        typeposi = np.dtype(typeposilist)
        typenega = np.dtype(typenegalist)
        target_group.create_dataset(f'posi', data = compound_memberposi, dtype=typeposi)
        target_group.create_dataset(f'nega', data = compound_membernega, dtype=typenega)         