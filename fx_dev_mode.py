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
with open('fx_account_test.csv',newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile) # removes the header - comment out if .csv file has no header
    for row in reader:
        if row[4] != "":
            # print(row)
            fxlst.append(row)
print("\n-----------test list ----------------------")
# print(fxlst)
print("\n-----------test list ----------------------\n")
count = 0
for item in fxlst:
    count +=1
    # print(item)
print("\n-------------test count rows---------------------")
print(f'There are {count} returned rows with buy/sell data.\n')

# alert the user when there are missing opening transaction ids
transfxlst = []
count = 0
for item in fxlst:
    if item[2] == '':
        item[2] = '000000000'
    transfxlst.append(item[3])
    # print(f'close_id: {item[2]}, open_id: {item[3]}')
print("\n-----------------opening transaction id-----------------")
# print(transfxlst)
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
        print('open_transaction_id_matched:', matching_id)

### GOAL: each row needs both the entry and exit date; all other data is there ###
# insert the opening date from the opening transaction id into the the fxlist
## Task 1) print each row where the "opening transaction id"  in column 3 is in matched_lst


print("\n-------------------test: list of matched ids--------------------------")
# print(matched_lst)

# extract the entry_date transaction_id to the matched_id in the match_lst
entry_exit_lst = []
for row in fxlst:
    open_id = row[3]
    # print(row[3])
    # print(open_id)
    if open_id in matched_lst:
        # entry_exit_lst.append(row)
        # print(row)
        if row[2] == '000000000':
            entry_date = row[0]
            entry_exit_lst.append(entry_date)
            # print(entry_date,row)
    else:
        pass
### START HERE NEXT ###
# the code below is not quite correct
# get the entry dates inserted and matched with the open close
for row in fxlst:
    if row[2] == '000000000':
        pass
    else:

        for row in entry_exit_lst:
            entry_exit_lst.append(row)
print(entry_exit_lst)

### GOAL: clean and format the data in each column
