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

# options_lst2 contains all rows with options transactions with properly formatted dates
options_lst2 = []

# for mat all of the dates to YYYY-MM-DD
def options_date_format():
    for row in options_lst:

        # M/DD/YYYY
        if row[0][1] == '/' and row[0][4] == '/':
            trans_mo = row[0][0]
            trans_mo = f'0{trans_mo}'
            trans_day = row[0][2:4]
            trans_yr = row[0][5:9]
            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
            row[1] = int(row[1])
            row[3] = int(row[3])
            if row[2][0] == 'B' or row[2][0] == 'S':
                row[5] = float(row[5])
                row[6] = float(row[6])
                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],row[5],row[6]])
            elif row[2][0] == 'R':
                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],0.00,0.00])

        # M/D/YYYY
        elif row[0][1] == '/' and row[0][3] == '/':
            trans_mo = row[0][0]
            trans_mo = f'0{trans_mo}'
            trans_day = row[0][2]
            trans_day = f'0{trans_day}'
            trans_yr = row[0][4:8]
            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
            row[1] = int(row[1])
            row[3] = int(row[3])
            if row[2][0] == 'B' or row[2][0] == 'S':
                row[5] = float(row[5])
                row[6] = float(row[6])
                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],row[5],row[6]])
            elif row[2][0] == 'R':
                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],0.00,0.00])

        # MM/D/YYYY
        elif row[0][2] == '/' and row[0][4] == '/':
            trans_mo = row[0][:2]
            trans_day = row[0][3]
            trans_day = f'0{trans_day}'
            trans_yr = row[0][5:9]
            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
            row[1] = int(row[1])
            row[3] = int(row[3])
            if row[2][0] == 'B' or row[2][0] == 'S':
                row[5] = float(row[5])
                row[6] = float(row[6])
                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],row[5],row[6]])
            elif row[2][0] == 'R':
                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],0.00,0.00])

        # MM/DD/YYYY
        # Note: this code works but I don't know understand why
        # trans_yr = row[0][6:10] produces output '[]' for the year
        # I removed trans_yr and it got the correct result; should have produced an error
        elif row[0][2] == '/' and row[0][5] == '/':
            trans_mo = row[0][:2]
            trans_day = row[0][3:5]
            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
            row[1] = int(row[1])
            row[3] = int(row[3])
            if row[2][0] == 'B' or row[2][0] == 'S':
                row[5] = float(row[5])
                row[6] = float(row[6])
                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],row[5],row[6]])
            elif row[2][0] == 'R':
                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],0.00,0.00])

    for row in options_lst2:
        print(row)
        # pass
    print('-------------compare lengths-------------------')
    print('Options_transactions_unformatted_dates_list_length: ',len(options_lst))
    print('options_transactions_formatted_dates_list_length: ',len(options_lst2))
options_date_format()

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
# match_symbols()
for row in symbol_info:
    pass
    # print(row)
