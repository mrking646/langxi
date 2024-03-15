import pandas as pd
import os
from extract_c import getCapDict
# Directory containing CSV files
bv_directory = 'SC002_auto_fullMap_'
cap_directory = 'SC002_auto_fullMap_C'

# Target voltage
target_voltage = 100

# Create an empty list to store results

def getBVdict(dir):
# Iterate through each file in the directory
    results = []
    for filename in os.listdir(bv_directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(bv_directory, filename)
            
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(filepath)
            
            # Find the row with the nearest voltage to the target
            closest_row = df.iloc[(df['voltage']-target_voltage).abs().argsort()[:1]]
            ele = filename.split('_')
            # print(ele)
            shot_x = ele[0]
            shot_y = ele[1]
            dut = '_'.join(ele[2:-3])
            r = ele[-3]
            c = ele[-2]
            # print(dut)
            # Check if any row matches the voltage
            if not closest_row.empty:
                # Get the corresponding current
                current_at_target_voltage = closest_row.iloc[0]['current']
                actual_voltage = closest_row.iloc[0]['voltage']
                # Append result to the list
                results.append({'shot_x': shot_x, 'shot_y': shot_y, 'dut': dut, 'r': r, 'c': c,  'Voltage': actual_voltage, 'Current': current_at_target_voltage})
            else:
                print(f"No data found for {target_voltage}V in file {filename}")
    return results
cap_list = getCapDict(cap_directory)
bv_list = getBVdict(bv_directory)
df_bv = pd.DataFrame(bv_list)
df_cap = pd.DataFrame(cap_list)
print(df_cap)
merged_df = pd.merge(df_cap, df_bv, on=['shot_x', 'shot_y', 'dut', 'r', 'c'], how='right')
merged_df.to_csv('results.csv')


# # Convert the list of dictionaries to a DataFrame
# result_df = pd.DataFrame(results)

# # Save the results to a CSV file
# result_df.to_csv('voltage_current_results.csv', index=False)

# print("Results saved to voltage_current_results.csv")
