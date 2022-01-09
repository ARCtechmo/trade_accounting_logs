### UNDER DEVELOPMENT ###
# this app will import and clean the forex broker data from a .csv file
import csv

# read the .csv data
# with open('fx_account_test.csv',newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     next(csvfile) # removes the header - comment out if .csv file has no header
#     for row in reader:
#         print(row[])

# extract rows only with open and closed trades (e.g. no commission or financing rows)
# append the data to a list where to do further cleaning
fxlst = []
filename = input("enter the .csv filename: ")
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile) # removes the header - comment out if .csv file has no header
    for row in reader:
        if row[4] != "":
            fxlst.append(row)

# fxlst is a list of trades only (no commission or fee data is included)
# count rows of transaction trades only
count = 0
for item in fxlst:
    count +=1
print(f'There are {count} returned rows with buy/sell data.')

# create a new list consisting of only the transaction ids with open dates only
transfxlst = []
count = 0
for item in fxlst:
    if item[2] == '':
        item[2] = '000000000'
    transfxlst.append(item[3])

# alert the user when there are missing opening transaction ids
# create a dictionary to get transaction id numbers and the count
# this will separate matching from missing id numbers
di = dict()
for num in transfxlst:
    di[num] = di.get(num,0) + 1
print("\n-----------------missing opening transaction id-----------------")
matched_lst = []
for key,value in di.items():
    # print(k,v)
    if value <2:
        missing_id = key
        print('missing open transaction id data for: ', missing_id)
    else:
        matching_id = key
        matched_lst.append(matching_id)
        # print('open_transaction_id_matched:', matching_id)
print("-----------------missing opening transaction id-----------------\n")

# matched_lst contains all transaction ids that have open and close matches
# print(matched_lst)

# fxlst is the list that contains the transactions but may have missing data
# for s in fxlst:
#     print(s)

# remove the missing data from fxlst
# only include entry_date transaction_id to the matched_id in the match_lst
fxlst2 = []
for row in fxlst:
    open_id = row[3]
    # print(open_id)
    if open_id in matched_lst:
        fxlst2.append(row)

# fxlst2 contains matching opening transactions
# extract dates from the rows that have the opening date and insert into the rows
opentrans = []
for item in fxlst2:
    # print(item)
    if item[2] == '000000000':
        entry_date = item[0]
        opentrans.append((entry_date, item[3]))
    else:
        pass
# opentrans is a list of tuples with the entry dates and transaction ids
# this extracts the columns with closing date '000000000'
fxlst3 = []
for tup in opentrans:
    # print(tup)
    for x in fxlst2:
        if x[2] != '000000000' and tup[1] == x[3]:
            fxlst3.append([tup[0],x])

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


### START HERE NEXT ###
# the entry and exit dates appear to be properly formatted
# download more .csv files and run them through the program to test
# compare the original entry date format to the formatted entry dates
print("---------Unformatted Entry Dates-------------------")
for y in fxlst3:
    print(y[0])
print("----------------------------------------------\n")

# fxlst4 is a list of clean and properly formatted entry dates
print("---------Formatted Entry Dates-------------------")
for item in fxlst4:
    print(item)
print("------------------------------------------------\n")

# compare the original exit date format to the formatted exit dates
print("---------Unformatted Exit Dates-------------------")
for y in fxlst3:
    print(y[1][0])
print("------------------------------------------------\n")


# fxlst5 is a list of clean and properly formatted entry dates
print("---------Formatted Exit Dates-------------------")
for item in fxlst5:
    print(item)
