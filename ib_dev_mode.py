### UNDER DEVELOPMENT ###
# this app imports and cleans .csv files from the equity options broker 2
import csv
import re

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
    filename = 'IB2018_test.csv'
else:
    filename = filename
# print(filename)

# contains a list of the trade data from the .csv file
trade_data_lst = []

# read the .csv data
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == 'trades' or row[0] == 'Trades':
            trade_rows = row
            trade_data_lst.append(trade_rows)

# contains unformatted options data
options_lst1 = []

# contains the commission and fee data
comm_fee_lst1 = []

# create_options_comm_fee_lst extracts the options data and the commission / fee data from the trade_data_lst
def create_options_comm_fee_lst(lst1):
    print("----------------TEST: create_options_comm_fee_lst func()----------------------- ")

    # remove the header line
    i = len(lst1)
    for row in lst1[1:i]:
        options_lst1.append([row[5:9],row[10]])
        comm_fee_lst1.append(row[11])

create_options_comm_fee_lst(trade_data_lst)

# options_dates_lst contains the options dates
options_dates_lst = []

# format_options_date() function formats the options date
def extract_options_date(lst1,lst2):
    print("--------------TEST: extract_options_date()---------------------")
    date_lst = []
    for row in lst1:
        date = row[0][1]
        if date == '':
            pass
        else:
            lst2.append(date[:10])
extract_options_date(options_lst1,options_dates_lst)

# options_year_lst contains the options year
options_year_lst = []

# extract the YYYY from the options_dates_lst
def extract_options_year(lst1, lst2):
    print("--------------TEST: extract_options_year()--------------------")
    i = len(lst1)
    for row in lst1[:i]:
        yr = row[:4]
        yr = int(yr)
        lst2.append(yr)
extract_options_year(options_dates_lst,options_year_lst)

# options_month_lst contains the options month
options_month_lst = []

def extract_options_month(lst1,lst2):
    print("-------------TEST: extract_options_month() func-----------------")
    i = len(lst1)
    for row in lst1[:i]:
        mo = row[5:7]
        mo = int(mo)
        lst2.append(mo)
extract_options_month(options_dates_lst,options_month_lst)

# options_day_lst contains the options day
options_day_lst = []

def extract_options_day(lst1,lst2):
    print("-------------TEST: extract_options_day() func-----------------")
    i = len(lst1)
    for row in lst1[:i]:
        day = row[8:10]
        day = int(day)
        lst2.append(day)
extract_options_day(options_dates_lst,options_day_lst)

# bought_sold_lst contains bought or sold options
bought_sold_lst = []

def extract_options_bought_sold(lst1,lst2):
    for row in lst1:
        buy_sell = row[0][2]
        if buy_sell == '':
            pass
        else:
            buy_sell = int(buy_sell)
            if buy_sell == 0:
                pass
            else:
                if buy_sell >0:
                    lst2.append('BOUGHT')
                elif buy_sell <0:
                    lst2.append('SOLD')
extract_options_bought_sold(options_lst1,bought_sold_lst)

# trade_size_lst contains the trade size
trade_size_lst = []

def extract_options_trade_size(lst1,lst2):
    for row in lst1:
        ctr = row[0][2]
        if ctr == '':
            pass
        else:
            ctr = int(ctr)
            if ctr == 0:
                pass
            else:
                lst2.append(ctr)
extract_options_trade_size(options_lst1,trade_size_lst)
