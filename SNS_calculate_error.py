import os
import numpy as np
import re
import matplotlib.pyplot as plt
import math

def process_directory(folder_path):
    # Get a list of all txt files in the given folder
    txt_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.startswith('int')]
    
    output_data = []

    # Process each txt file
    for file in txt_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            # Remove the last line
            lines = lines[:-1]
            raw_data = [float(line.strip().split()[0]) for line in lines]
            mod_0_elements = [value for index, value in enumerate(raw_data) if index % 4 == 0 ]
            mod_1_elements = [value for index, value in enumerate(raw_data) if index % 4 == 1 ]
            mod_2_elements = [value for index, value in enumerate(raw_data) if index % 4 == 2]
            mod_3_elements = [value for index, value in enumerate(raw_data) if index % 4 == 3]
            # Remove nan
            to_remove = np.zeros(len(raw_data))
            for i in range(len(mod_0_elements)):
                if (np.isnan(mod_0_elements[i]) or mod_0_elements[i] > 1e-5 or
                    np.isnan(mod_1_elements[i]) or mod_1_elements[i] > 1e-5 or
                    np.isnan(mod_2_elements[i]) or mod_2_elements[i] > 1e-5 or
                    np.isnan(mod_3_elements[i]) or mod_3_elements[i] > 1e-5):
                    to_remove[i] = 1  
            mod_0_elements_filtered = [value for index, value in enumerate(mod_0_elements) if not to_remove[index]]
            mod_1_elements_filtered = [value for index, value in enumerate(mod_1_elements) if not to_remove[index]]
            mod_2_elements_filtered = [value for index, value in enumerate(mod_2_elements) if not to_remove[index]]
            mod_3_elements_filtered = [value for index, value in enumerate(mod_3_elements) if not to_remove[index]]
            low_B_elements = [(x + y) / 2 for x, y in zip(mod_0_elements_filtered, mod_1_elements_filtered)]
            high_B_elements = [(x + y) / 2 for x, y in zip(mod_2_elements_filtered, mod_3_elements_filtered)]
            # Calculate the difference between corresponding elements in the two lists           
            column_data = [x - y for x, y in zip(low_B_elements, high_B_elements)]
            # Calculate the average and standard deviation of the data
            average = np.mean(column_data)
            std_dev = np.std(column_data)
            # Use regular expression to extract the number from the file name
            field = re.search(r'\[(.*?),', os.path.basename(file))
            field_str = field.group(1) 
            field_float = float(field_str)
            output_data.append([field_float, average, std_dev])
            # Cut off
    # Sort the data based on the magnetic field
    return sorted(output_data, key=lambda x: float(x[0]))

# Set folder paths
folder_path_1 = r'D:\SNS\0428_SNS_330K\\'
# folder_path_2 = r'd:\SNS\2023_SNS_data/20231130_test_720nm_320K_200muW/waiting_effect/600ms\\'
# folder_path_3 = r'd:\SNS\2023_SNS_data/20231130_test_720nm_320K_200muW/waiting_effect/1000ms\\'
# folder_path_4 = r'd:\SNS\2023_SNS_data/20231130_test_720nm_320K_200muW/waiting_effect/3000ms\\'
# folder_path_5 = r'd:\SNS\2023_SNS_data/20231130_test_720nm_320K_200muW/waiting_effect/5000ms\\'
result_fig_path = r'D:\SNS\0428_SNS_330K\\'


# Process the first folder
output_data_1 = process_directory(folder_path_1)

# Process the second folder
# output_data_2 = process_directory(folder_path_2)
# output_data_3 = process_directory(folder_path_3)
# output_data_4 = process_directory(folder_path_4)
# output_data_5 = process_directory(folder_path_5)



# Plot for output_data_1
# x_values_1 = np.array(output_data_1)[:, 0].astype(float)
# y_values_1 = np.array(output_data_1)[:, 1].astype(float)
# error_values_1 = np.array(output_data_1)[:, 2].astype(float)
# print(y_values_1)
# plt.errorbar(x_values_1, y_values_1, yerr=error_values_1, fmt='o', linestyle='-', capsize=3, label='centering', color='purple')

# Plot for output_data_2
# x_values_2 = np.array(output_data_2)[:, 0].astype(float)
# y_values_2 = np.array(output_data_2)[:, 1].astype(float)
# error_values_2 = np.array(output_data_2)[:, 2].astype(float)
# plt.errorbar(x_values_2, y_values_2, yerr=error_values_2, fmt='o', linestyle='-', capsize=3, label='600ms', color='orange')

# x_values_3 = np.array(output_data_3)[:, 0].astype(float)
# y_values_3 = np.array(output_data_3)[:, 1].astype(float)
# error_values_3 = np.array(output_data_3)[:, 2].astype(float)
# plt.errorbar(x_values_3, y_values_3, yerr=error_values_3, fmt='o', linestyle='-', capsize=3, label='1000ms', color='black')

# x_values_4 = np.array(output_data_4)[:, 0].astype(float)
# y_values_4 = np.array(output_data_4)[:, 1].astype(float)
# error_values_4 = np.array(output_data_4)[:, 2].astype(float)
# plt.errorbar(x_values_4, y_values_4, yerr=error_values_4, fmt='o', linestyle='-', capsize=3, label='3000ms', color='red')

# x_values_5 = np.array(output_data_5)[:, 0].astype(float)
# y_values_5 = np.array(output_data_5)[:, 1].astype(float)
# error_values_5 = np.array(output_data_5)[:, 2].astype(float)
# plt.errorbar(x_values_5, y_values_5, yerr=error_values_5, fmt='o', linestyle='-', capsize=3, label='5000ms', color='green')


# plt.xlabel('Field/gs')
# plt.ylabel('Integrated_noise_waiting_effect')  
# plt.title('')  
# plt.grid(True)

# Output to txt files
with open(os.path.join(folder_path_1, 'output_data_centering.txt'), 'w') as f:
    for data in output_data_1:
        f.write('\t'.join(str(i) for i in data) + '\n')

# with open(os.path.join(folder_path_2, 'output_data_asymmetry.txt'), 'w') as f:
#     for data in output_data_2:
#         f.write('\t'.join(str(i) for i in data) + '\n')

# plt.legend()
# plt.savefig(result_fig_path + 'int_result_fig.png')
# plt.show()
# Save the swell
# plt.clf
# wait_time = [300,600,1000,3000,5000]
# swell = []
# values = [(x_values_1,y_values_1), (x_values_2,y_values_2),(x_values_3,y_values_3),(x_values_4,y_values_4),(x_values_5,y_values_5)]
# for i in values:
#     swell_index = next((j for j, x in enumerate(i[0]) if x == 0), None)
#     result_elements = i[1][swell_index]
#     swell.append(result_elements)
# print(swell)    
# plt.plot(wait_time,swell,label='Waiting_effect for zero', marker='o', linestyle='-')
# plt.savefig(result_fig_path + 'Waiting_effect for zero.png')
