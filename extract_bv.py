import pandas as pd
import os
from extract_c import getCapDict
from configs import max_y, max_x
# Directory containing CSV files
bv_directory = 'SC002_auto_fullMap_'
cap_directory = 'SC002_auto_fullMap_C'



dut_r_c = {
    "POC22_Main_762_99F": (6,26),
    "POC22_Main_762_77": (2,26),
    "POC22_Main_381_77F": (8,49),
    "POC22_Main_508_88F": (12,38),
    "POC22_Main_508_44": (6,38),
    "POC22_Main_508_47": (2,38),

}





# Target voltage
target_voltage = 100
max_columns = 0
max_rows = 0

for k, v in dut_r_c.items():
    columns = v[1]
    rows = v[0]
    max_rows+=rows
    if columns>=max_columns:
        max_columns = columns
# Create an empty list to store results
original_x = max_rows*max_y+1
original_y = max_columns*max_x+1
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
            maxr = dut_r_c[dut][0]
            maxc = dut_r_c[dut][1]
            initial_rows_that_dut_exists = 1
            for k, v in dut_r_c.items():
                if k == dut:
                    break
                initial_rows_that_dut_exists += v[0]
            
            x = original_x + max_columns*int(shot_x) + int(c)
            y = original_y - int(shot_y)*max_rows + initial_rows_that_dut_exists + int(r)
            #   100 - 1*20 + 3 + r
            
            

            # print(dut)
            # Check if any row matches the voltage
            if not closest_row.empty:
                # Get the corresponding current
                current_at_target_voltage = closest_row.iloc[0]['current']
                actual_voltage = closest_row.iloc[0]['voltage']
                # Append result to the list
                results.append({'shot_x': shot_x, 'shot_y': shot_y, 'dut': dut, 'r': r, 'c': c, 'x':x, 'y':y,  'Voltage': actual_voltage, 'Current': current_at_target_voltage})
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
