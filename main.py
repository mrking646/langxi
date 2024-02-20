
import pandas as pd
import attrs

# Sample data
row = 6
column = 26


dut = 'POC22_Main_762_99F'
lst_dut = []
lst_x = []
lst_y = []
x = 0
y = 0
dx = 822
dy = 822
for r in range(row):
    y = dy*r
    x = 0
    for c in range(column):
        x = dx*c

        position = f'{r+1}_{c+1}'
        lst_dut.append(dut+'_'+position)
        lst_x.append(x)
        lst_y.append(y)

print(lst_x)
        

def genPlan(dut, x, y, r, c, dx, dy):

    row = r
    column = c


    dut = dut
    lst_dut = []
    lst_x = []
    lst_y = []
    x = 0
    y = 0
    
     
    for r in range(row):
        y = dy*r
        x = 0
        for c in range(column):
            x = dx*c

            position = f'{r+1}_{c+1}'
            lst_dut.append(dut+'_'+position)
            lst_x.append(x)
            lst_y.append(y)



genPlan()




class Dut:
    row = attrs.field(kw_only=True)
    column = attrs.field(kw_only=True)
    dut_name = attrs.field(kw_only=True)
    x = attrs.field(kw_only=True,
                    default=0)
    y = attrs.field(kw_only=True, default=0)
    dx = attrs.field(kw_only=True, default=0)
    dy = attrs.field(kw_only=True, default=0)


main2 = Dut(row=2, column=26, dut_name='POC22_Main_762_77', x=0, y=)
    
lst_dut_name = ['POC22_Main_762_99F']



data = {
    'dut.name': lst_dut,
    'dut.x': lst_x,
    'dut.y': lst_y,
}

# Create DataFrame
df = pd.DataFrame(data)

# Write DataFrame to Excel
df.to_excel('output.xlsx', index=False)
