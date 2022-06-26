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

# transposed_trade_data_lst contains the trade datawith the rows and columns transposed for easier indexing
transposed_trade_data_lst = []

#  transpose function extract the options trade data from the trade_data_lst
def transpose(lst1,lst2):
    print("-----------------TEST: transpose_rows_columns function----------------------")

    # remove the header line
    i = len(lst1)
    for row in lst1[1:i]:
        lst2.append([row[5:9],row[10]])

    for line in lst2:
        print(line)

    # zip(*) unpacks the list for indexing


transpose(trade_data_lst,transposed_trade_data_lst)
