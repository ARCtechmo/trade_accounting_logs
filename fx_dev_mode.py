### UNDER DEVELOPMENT ###
# this app will import and clean the forex broker data from a .csv file
import csv
import re

# read the .csv data
# filename = input("enter the .csv filename: ")
# with open(filename, newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     next(csvfile) # removes the header - comment out if .csv file has no header
#     for row in reader:
#         print(row[])

# extract rows containing commission and financing
# fxlst is a list of trades only (no commission or fee data is included)
fxlst = []
filename = input("enter the .csv filename: ")
if filename == '':
    filename = 'fx_oct_test.csv'
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    # next(csvfile) # removes the header - comment out if .csv file has no header
    for row in reader:
        if row[4] != "":
            fxlst.append(row)
# print(fxlst)

# count rows of transaction trades only
count = 0
for item in fxlst:
    count +=1
# print(f'There are {count} returned rows with buy/sell data.')

# first step to match the open / closed transaction ids
# transfxlst consists of only the open / closed transaction ids
transfxlst = []
for item in fxlst:
    if item[2] == '':
        # insert 000000000 in field 2 to identify rows that have the entry times
        item[2] = '000000000'
    transfxlst.append(item[3])
# print(transfxlst)

# step to to match the open / closed transaction ids
# dictionary gets a count of the transaction ids
# matched_lst contains all transaction ids that have open and close ids
matched_lst = []
di = dict()
for num in transfxlst:
    di[num] = di.get(num,0) + 1
print("\n-----------------missing opening transaction id-----------------")
for key,value in di.items():

    # alert the user when there are missing opening transaction ids
    if value <2:
        missing_id = key
        print('missing open transaction id data for: ', missing_id)
    else:
        matching_id = key
        matched_lst.append(matching_id)
        # print('open_transaction_id_matched:', matching_id)
print("-----------------missing opening transaction id-----------------\n")
# print(matched_lst)

# step 3 to match open / closed transaction ids
# remove the missing transaction id identified in the dictionary from fxlst
# fxlst2 contains rows only with open and closed /  open transactions
fxlst2 = []
for row in fxlst:
    open_id = row[3]
    # print(open_id)
    if open_id in matched_lst:
        fxlst2.append(row)
# print("---------------fxlst2: open-close transactions--------------------")
# for row in fxlst2:
#     print(row)
# print("---------------fxlst2: open-close transactions--------------------\n")


# step 4 to match open / closed transaction ids
# extract dates from the rows that have the opening date and insert into the rows
# opentrans is a list of tuples with the open dates and open transaction ids
# print("---------------tuples: opening: transaction ids--------------------")
opentrans = []
for item in fxlst2:
    # print(item)
    if item[2] == '000000000':
        entry_date = item[0]
        opentrans.append((entry_date, item[3]))
    else:
        pass
# print(opentrans)
# print("---------------tuples: opening: transaction ids--------------------\n")

# step 5 matches inserts the opening date to the row with the matching closed date
# extract the columns with closing date '000000000'
# fxlst3 contains all rows with the needed data now ready for formatting
print("---------------fxlst3: matched open-close transactions--------------------")
fxlst3 = []
for x in fxlst:
    for tup in opentrans:
        if x[2] != '000000000' and x[3] == tup[1]:
            fxlst3.append([tup[0],x])

for row in fxlst3:
    print(row)
print("---------------fxlst3: matched open-close transactions--------------------\n")

# extract and format the entry date to YYYY-MM-DD-HH:MM
fxlst4 = []
for dmy in fxlst3:
    # print(dmy[0])
    if dmy[0][2] == '/' and dmy[0][5] =='/':
        # print(dmy[0])
        entry_yr = dmy[0][6:10]
        entry_mo = dmy[0][3:5]
        entry_day = dmy[0][:2]
        entry_time = dmy[0][11:16]
        if len(entry_time) < 5:
            entry_time = f'0{dmy[0][11:16]}'
            formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
            fxlst4.append(formatted_entry_date)
        elif len(entry_time) == 5:
            entry_time = dmy[0][11:16]
            formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
            fxlst4.append(formatted_entry_date)
    elif dmy[0][2] == '/' and dmy[0][4] =='/':
        # print(dmy[0])
        entry_yr = dmy[0][5:9]
        entry_mo = dmy[0][3]
        entry_mo = f'0{entry_mo}'
        entry_day = dmy[0][:2]
        entry_time = dmy[0][10:15]
        if len(entry_time) < 5:
            entry_time = f'0{dmy[0][10:15]}'
            formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
            fxlst4.append(formatted_entry_date)
        elif len(entry_time) == 5:
            entry_time = dmy[0][10:15]
            formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
            fxlst4.append(formatted_entry_date)
    elif dmy[0][1] == '/' and dmy[0][4] =='/':
        # print(dmy[0])
        entry_yr = dmy[0][5:9]
        entry_mo = dmy[0][2:4]
        entry_day = dmy[0][0]
        entry_day = f'0{entry_day}'
        entry_time = dmy[0][10:14]
        if len(entry_time) < 5:
            entry_time = f'0{dmy[0][10:14]}'
            formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
            fxlst4.append(formatted_entry_date)
        elif len(entry_time) == 5:
            entry_time = dmy[0][10:14]
            formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
            fxlst4.append(formatted_entry_date)
    elif dmy[0][1] == '/' and dmy[0][3] =='/':
        # print(dmy[0])
        entry_yr = dmy[0][4:8]
        entry_mo = dmy[0][2]
        entry_mo = f'0{entry_mo}'
        entry_day = dmy[0][0]
        entry_day = f'0{entry_day}'
        entry_time = dmy[0][9:13]
        if len(entry_time) < 5:
            entry_time = f'0{dmy[0][9:13]}'
            formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
            fxlst4.append(formatted_entry_date)
        elif len(entry_time) == 5:
            entry_time = dmy[0][9:13]
            formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
            fxlst4.append(formatted_entry_date)

# extract and format the exit date to YYYY-MM-DD-HH:MM
fxlst5 = []
for dmy in fxlst3:
    # print(dmy[0])
    if dmy[1][0][2] == '/' and dmy[1][0][5] =='/':
        # print(dmy[0])
        exit_yr = dmy[1][0][6:10]
        exit_mo = dmy[1][0][3:5]
        exit_day = dmy[1][0][:2]
        exit_time = dmy[1][0][11:16]
        if len(exit_time) < 5:
            exit_time = f'0{dmy[1][0][11:16]}'
            formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
            fxlst5.append(formatted_exit_date)
        elif len(exit_time) == 5:
            exit_time = dmy[1][0][11:16]
            formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
            fxlst5.append(formatted_exit_date)
    elif dmy[1][0][2] == '/' and dmy[1][0][4] =='/':
        # print(dmy[0])
        exit_yr = dmy[1][0][5:9]
        exit_mo = dmy[1][0][3]
        exit_mo = f'0{exit_mo}'
        exit_day = dmy[1][0][:2]
        exit_time = dmy[1][0][10:15]
        if len(exit_time) < 5:
            exit_time = f'0{dmy[1][0][10:15]}'
            formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
            fxlst5.append(formatted_exit_date)
        elif len(exit_time) == 5:
            exit_time = dmy[1][0][10:15]
            formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
            fxlst5.append(formatted_exit_date)
    elif dmy[1][0][1] == '/' and dmy[1][0][4] =='/':
        # print(dmy[0])
        exit_yr = dmy[1][0][5:9]
        exit_mo = dmy[1][0][2:4]
        exit_day = dmy[1][0][0]
        exit_day = f'0{exit_day}'
        exit_time = dmy[1][0][10:14]
        if len(exit_time) < 5:
            exit_time = f'0{dmy[1][0][10:14]}'
            formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
            fxlst5.append(formatted_exit_date)
        elif len(exit_time) == 5:
            exit_time = dmy[1][0][10:14]
            formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
            fxlst5.append(formatted_exit_date)
    elif dmy[1][0][1] == '/' and dmy[1][0][3] =='/':
        # print(dmy[0])
        exit_yr = dmy[1][0][4:8]
        exit_mo = dmy[1][0][2]
        exit_mo = f'0{exit_mo}'
        exit_day = dmy[1][0][0]
        exit_day = f'0{exit_day}'
        exit_time = dmy[1][0][9:13]
        if len(exit_time) < 5:
            exit_time = f'0{dmy[1][0][9:13]}'
            formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
            fxlst5.append(formatted_exit_date)
        elif len(exit_time) == 5:
            exit_time = dmy[1][0][9:13]
            formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
            fxlst5.append(formatted_exit_date)

# tested the entry and exit dates for one one year of data and the code works
# print("---------Unformatted Entry Dates-------------------")
# for y in fxlst3:
#     print(y[0])
# print("----------------------------------------------\n")

# fxlst4 is a list of clean and properly formatted entry dates
# print("---------Formatted Entry Dates-------------------")
# for item in fxlst4:
#     print(item)
# print("------------------------------------------------\n")

# compare the original exit date format to the formatted exit dates
# print("---------Unformatted Exit Dates-------------------")
# for y in fxlst3:
#     print(y[1][0])
# print("------------------------------------------------\n")

# fxlst5 is a list of clean and properly formatted entry dates
# print("---------Formatted Exit Dates-------------------\n")
# for item in fxlst5:
#     print(item)

# extract the currency pairs from fxlst3
# marketlst contains the formatted market (e.g. EURUSD, AUDJPY, etc...)
marketlst = []
for mkt in fxlst3:
    market = mkt[1][1]
    market2 = re.split(' ',market)
    market3 = market2[3]
    marketlst.append(market3)

# extract the closing transaction ids from fxlst3
# close_id_lst contains the closing transaction ids
close_id_lst = []
for elements in fxlst3:
    close_id = elements[1][2]
    close_id_lst.append(close_id)

# extract the opening transaction ids from fxlst3
# open_id_lst contains the opening transaction ids
open_id_lst = []
for elements in fxlst3:
    open_id = elements[1][3]
    open_id_lst.append(open_id)

# fxloglst will contain the finalized formatted list to import into the app
fxlog = []
print("\n-----------test of complete fxloglst----------------")
for entry, exit, market, close_id, open_id in zip(fxlst4,fxlst5,marketlst,close_id_lst,open_id_lst):
    entry_yr = entry[0:4]
    entry_mo = entry[5:7]
    entry_day = entry[8:10]
    entry_time = entry[11:]

    exit_yr = exit[0:4]
    exit_mo = exit[5:7]
    exit_day = exit[8:10]
    exit_time = exit[11:]

    fxlog.append(
                [entry, entry_yr, entry_mo, entry_day, entry_time,
                exit, exit_yr, exit_mo, exit_day, exit_time,
                market,
                close_id, open_id]
                )
for log in fxlog:
    print(log)
print("\n-----------test of complete fxloglst----------------")
