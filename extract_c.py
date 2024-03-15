import csv
import os
import pandas as pd

# Directory containing CSV files
directory = 'SC002_auto_fullMap_C'

# Target voltage
target_voltage = 100

def getCapDict(dir):
# Create an empty list to store results
    results = []
    field_names = ['prefix', 'cap', 'D']
    cap_results = []
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            ele = filename.split('.')[0].split('_')
            # print(ele)
            shot_x = ele[0]
            shot_y = ele[1]
            dut = '_'.join(ele[2:-2])
            r = ele[-2]
            c = ele[-1]
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as f:
                line = f.readline().strip()
                # print(line)
                if line:
                    
                    cap = line.split(',')[0]
                    D = line.split(',')[1]
                    prefix = filename.split('.')[0]
                    d = {
                        'shot_x': shot_x, 'shot_y': shot_y, 'dut': dut, 'r': r, 'c': c,
                        'cap': cap,
                        'D': D
                    }
                    cap_results.append(d)
    return cap_results


# with open('results_c.csv', 'w', newline='') as csvfile: 
#     writer = csv.DictWriter(csvfile, fieldnames = field_names) 
#     writer.writeheader() 
#     writer.writerows(cap_results) 

        


# print("Results saved to voltage_current_results.csv")
