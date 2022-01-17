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
broker_id = int(input("enter the broker_id from the database (2-7): "))
### come back to this later ###
# embed the entire program under a while loop to catch incorrect broker_id entry
# while True:
#     if broker_id <=1 or broker_id >7:
#         print("you must enter a digit between 2-7")
#         break
#     else:
#         break
filename = input("enter the .csv filename: ")
if filename == '':
    filename = 'fx_sept_test.csv'
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

# step 2 to to match the open / closed transaction ids
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
# print("---------------fxlst3: matched open-close transactions--------------------")
fxlst3 = []
for x in fxlst:
    for tup in opentrans:
        if x[2] != '000000000' and x[3] == tup[1]:
            fxlst3.append([tup[0],x])
# for row in fxlst3:
#     print(row)
# print("---------------fxlst3: matched open-close transactions--------------------\n")

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
    close_id = int(close_id)
    close_id_lst.append(close_id)

# extract the opening transaction ids from fxlst3
# open_id_lst contains the opening transaction ids
open_id_lst = []
for elements in fxlst3:
    open_id = elements[1][3]
    open_id = int(open_id)
    open_id_lst.append(open_id)

# extract the buy / sell from fxlst3
# buy_sell_lst contains buy or sell transactions
buy_sell_lst = []
for action in fxlst3:
    buy_sell = action[1][4]
    buy_sell_lst.append(buy_sell)

# extract the trade_size from fxlst3
# trade_size_lst contains the size of the trades taken
trade_size_lst = []
for size in fxlst3:
    trade_size = size[1][6]
    trade_size = trade_size.split('.')
    trade_size = trade_size[0]
    trade_size = int(trade_size)
    trade_size_lst.append(trade_size)

# extract the open_price from fxlst3
# open_price_lst contains the opening price
open_price_lst = []
for openpr in fxlst3:
    openpr = openpr[1][8]
    openpr = float(openpr)
    open_price_lst.append(openpr)

# extract the close_price from fxlst3
# close_price_lst contains the closing price
close_price_lst = []
for closepr in fxlst3:
    closepr = closepr[1][9]
    closepr = float(closepr)
    close_price_lst.append(closepr)

# extract the gross from fxlst3
# gross_lst contains the gross profit / loss
gross_lst = []
for gross in fxlst3:
    gross = gross[1][12]
    gross = float(gross)
    gross_lst.append(gross)

# extract the net from fxlst3
# net_lst contains the gross profit / loss
net_lst = []
for net in fxlst3:
    net = net[1][12]
    net = float(net)
    net_lst.append(net)

# fxloglst will contain the finalized formatted list to import into the app
fxlog = []
count = 0

# the broker_id is a list to make it iterable to add the broker key during the loop
broker_id_lst = [broker_id]


# print("\n-----------complete fxloglst----------------")
for entry, exit, market, close_id, open_id, buy_sell, trade_size, open, close, gross, net, broker in zip(
    fxlst4, fxlst5, marketlst,
    close_id_lst, open_id_lst,
    buy_sell_lst, trade_size_lst,
    open_price_lst, close_price_lst,
    gross_lst, net_lst, broker_id_lst
    ):

    entry_yr = entry[0:4]
    entry_yr = int(entry_yr)
    entry_mo = entry[5:7]
    entry_mo = int(entry_mo)
    entry_day = entry[8:10]
    entry_day = int(entry_day)
    entry_time = entry[11:]

    exit_yr = exit[0:4]
    exit_yr = int(exit_yr)
    exit_mo = exit[5:7]
    exit_mo = int(exit_mo)
    exit_day = exit[8:10]
    exit_day = int(exit_day)
    exit_time = exit[11:]

    # the zip() function will loop based on the shortest list
    # the broker_id_lst length is one so append the broker_id with each loop
    # oterwise it will only loop one time and return one row
    broker_id_lst.append(broker_id)
    fxlog.append(
                [entry, entry_yr, entry_mo, entry_day, entry_time,
                exit, exit_yr, exit_mo, exit_day, exit_time,
                market, close_id, open_id, buy_sell, trade_size, open, close, gross, net,
                broker]
                )
########################### print all rows #################################
# def fxlog_add_records(fxlog):
#     for log in fxlog:
#         print(log)
# fxlog_add_records(fxlog)
########################### print all rows #################################

########################### export records #################################
# function exports the records into the import the log_metrics_app.py app
# def fxlog_add_records():
#     print("-----test of fxlog_add_records function()------------")
#     return fxlog
########################### export records #################################


### START HERE NEXT ###
############################ export unmatched records #########################
## process ##
# 1) fx_dev_mode.py identifies the unmatched record open_ids,
# 2) fx_dev_mode.py formats and extracts the unmatched record
# 3) fx_dev_mode.py exports the unmatched records into logs_metrics_app_dev_mode.py

# fxlst is the original list
for row in fxlst:
    print(row)

############################ export unmatched records #########################
