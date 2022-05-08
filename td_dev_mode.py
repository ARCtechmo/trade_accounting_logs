### UNDER DEVELOPMENT ###
# this app will import and clean .csv files from the equity options broker 1
import csv

# define the broker id for the foreign key in the database
broker_id = input("enter the options broker id: ")
if broker_id == "":
    broker_id = 4
else:
    broker_id = broker_id
# print("broker id: ", broker_id)

# input the .csv filename
filename = input("enter the .csv filename: ")
if filename == "":
    filename = 'TD2018_test.csv'
else:
    filename = filename
# print(filename)

# buy_sell_remove_lst contains all buy, sell, and removal transactions
buy_sell_remove_lst = []

# int_income_lst contains the interest earned transactions
int_lst = []

# misc_lst contains the miscellaneous transactions
misc_lst = []

# read the .csv data
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile)
    for row in reader:
        if row[2][:4] == 'Sold' or row[2][:6] == 'Bought' or row[2][:7] == 'REMOVAL':
            buy_sell_remove_lst.append(row)
        elif 'MISCELLANEOUS' in row[2]:
            misc_lst.append(row)
        elif 'FREE' in row[2] or 'INTEREST' in row[2]:
            int_lst.append(row)
        else:
            pass

# options_lst contains all rows with options transactions
options_lst = []

# comm_lst contains all of the commissions
comm_lst = []

# reg_fee_lst contains all of the regulation fees
reg_fee_lst = []

for row in buy_sell_remove_lst:
    if row[2][:7] == 'REMOVAL':
        options_lst.append(row[:6])
    elif row[4][-3:] == 'Put' or row[4][-4:] == "Call":
        options_lst.append([row[0],row[1],row[2],row[3],row[4],row[5],row[7]])
        comm_lst.append([row[0],row[1],row[6]])
        reg_fee_lst.append([row[0],row[1],row[8]])

# misc_income_lst contains the miscellaneous income transactions
misc_income_lst = []

# misc_income_lst contains the miscellaneous income transactions
misc_debit_lst = []

for row in misc_lst:
    if float(row[7]) >=0:
        row[7] = float(row[7])
        misc_income_lst.append([row[0],row[1],row[2],row[7]])
    elif float(row[7]) <0:
        row[7] = float(row[7])
        misc_debit_lst.append([row[0],row[1],row[2],row[7]])

# int_income_lst contains the interest earned transactions
int_income_lst = []

# int_income_lst contains the interest earned transactions
int_debit_lst = []

for row in int_lst:
    if float(row[7]) >=0:
        row[7] = float(row[7])
        int_income_lst.append([row[0],row[1],row[2],row[7]])
    elif float(row[7]) <0:
        row[7] = float(row[7])
        int_debit_lst.append([row[0],row[1],row[2],row[7]])

# symbol_info contains the symbols of the options transactions
symbol_info = []

### START HERE NEXT ###
# 1) the values with 1 are the option expirations so match those items with the rows with "REMOVAL"
# 2) idea: sold / symbol put matched with bought / put
# match_symbols function matches the the buy / sell trades using the symbol column
def match_symbols():
    count = 0
    di = dict()
    for row in options_lst:
        symbol_info.append(row[4])
    for symb in symbol_info:
        di[symb] = di.get(symb,0) +1
    for key,value in di.items():
        print(key, value)
match_symbols()
for row in symbol_info:
    pass
    # print(row)
