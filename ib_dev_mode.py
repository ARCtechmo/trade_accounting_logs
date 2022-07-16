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
    print(len(lst2))
extract_options_date(options_lst1,options_dates_lst)

# options_year_lst contains the options year
options_year_lst = []

# extract the YYYY from options_dates_lst
def extract_options_year(lst1, lst2):
    print("--------------TEST: extract_options_year()--------------------")
    i = len(lst1)
    for row in lst1[:i]:
        yr = row[:4]
        yr = int(yr)
        lst2.append(yr)
    print(len(lst2))
extract_options_year(options_dates_lst,options_year_lst)

# options_month_lst contains the options month
options_month_lst = []

# extract the month from options_lst1
def extract_options_month(lst1,lst2):
    print("-------------TEST: extract_options_month() func-----------------")
    i = len(lst1)
    for row in lst1[:i]:
        mo = row[5:7]
        mo = int(mo)
        lst2.append(mo)
    print(len(lst2))
extract_options_month(options_dates_lst,options_month_lst)

# options_day_lst contains the options day
options_day_lst = []

# extract the transaction day from options_lst1
def extract_options_day(lst1,lst2):
    print("-------------TEST: extract_options_day() func-----------------")
    i = len(lst1)
    for row in lst1[:i]:
        day = row[8:10]
        day = int(day)
        lst2.append(day)
    print(len(lst2))
extract_options_day(options_dates_lst,options_day_lst)

# bought_sold_lst contains bought or sold options
bought_sold_lst = []

# add bought or sold
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
    print(len(lst2))
extract_options_bought_sold(options_lst1,bought_sold_lst)

# trade_size_lst contains the trade size
trade_size_lst = []

# extract the contract trade size from options_lst1
def extract_options_trade_size(lst1,lst2):
    for row in lst1:
        num_ctr = row[0][2]
        if num_ctr == '':
            pass
        else:
            num_ctr = int(num_ctr)
            if num_ctr == 0:
                pass
            else:
                lst2.append(num_ctr)
    print(len(lst2))
extract_options_trade_size(options_lst1,trade_size_lst)

# mkt_lst contains a list of the markets
mkt_lst = []

# extract the markets from options_lst1
def extract_options_mkt(lst1,lst2):
    print("-------------TEST: extract_options_mkt() func------------------")
    for row in lst1:
        if row[0][2] == str(0):
            pass
        else:
            mkt = row[0][0][:3]
            if mkt == '':
                pass
            elif mkt == str(0):
                pass
            else:
                lst2.append(mkt)
    print(len(lst2))
extract_options_mkt(options_lst1,mkt_lst)

# call_put_lst contains the calls and puts options contracts
call_put_lst = []

# extract the call / put data from options_lst1
def extract_options_call_put(lst1,lst2):
    print("------------TEST: extract_options_call_put() funct--------------")
    for row in lst1:
        if row[0][2] == str(0):
            pass
        elif row[0][0] == '':
            pass
        else:
            call_put = row[0][0][-1]
            if call_put == '':
                pass
            elif call_put == 'C' or call_put == 'CALL':
                lst2.append(call_put)
            elif call_put == 'P' or call_put == 'PUT':
                lst2.append(call_put)
    print(len(lst2))
extract_options_call_put(options_lst1,call_put_lst)

# ctr_lst contains a list of the contract details
ctr_lst = []

# extract the contract details from options_lst1
def extract_options_ctr(lst1,lst2):
    print("--------------TEST: extract_options_ctr() func----------------")
    for row in lst1:
        if row[0][2] == str(0):
            pass
        else:
            ctr = row[0][0]
            if ctr == '':
                pass
            else:
                lst2.append(ctr)
    print(len(lst2))
extract_options_ctr(options_lst1,ctr_lst)

# price_lst contains the options price data
price_lst = []

# extract the price data from options_lst1
def extract_options_price(lst1,lst2):
    print("---------TEST: extract_options_price() func------------")
    for row in lst1:
        if row[0][2] == str(0):
            pass
        elif row[0][0] == '':
            pass
        else:
            price = row[0][3]
            price = float(price)
            lst2.append(price)
    print(len(lst2))
extract_options_price(options_lst1,price_lst)

# gross_lst contains the options gross amount data
gross_lst = []

# extract the gross amount from options_lst1
def extract_options_gross(lst1,lst2):
    print("-----------TEST: extract_options_gross()----------------")
    for row in lst1:
        if row[0][2] == str(0):
            pass
        elif row[0][0] == '':
            pass
        else:
            price = row[1]
            price = int(price)
            lst2.append(price)
    print(len(lst2))
extract_options_gross(options_lst1,gross_lst)


# options_lst2 fields: date,yr,mo,day,bought_sold,trade_size,mkt,call_put,ctr,price,gross
options_lst2 = []

# broker_id_lst contains the broker id that will be appended to options_lst2
broker_id_lst = [broker_id]

# compiles the column headers (fields) into a list; adds the broker_id
def compile_options_fields():
    print("---------TEST: compile_options_fields---------------------- ")
    for date,year,month,day,bought_sold,trade_size,mkt,call_put,ctr,price,gross,broker in zip(
        options_dates_lst,options_year_lst,options_month_lst,
        options_day_lst,bought_sold_lst,trade_size_lst,mkt_lst,
        call_put_lst,ctr_lst,price_lst,gross_lst,broker_id_lst):

        broker_id_lst.append(broker_id)
        options_lst2.append([date,year,month,day,bought_sold,trade_size,mkt,call_put,ctr,price,gross,broker])

    for row in options_lst2:
        print(row)
compile_options_fields()


### START HERE NEXT ###
# add a function to create the trans_key
# add the key to the list
