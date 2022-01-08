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
print("\n-------------------test: list of matched ids--------------------------")
# print(matched_lst)

### fxlst is the list that contains the transactions but may have missing data
# print(fxlst)
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

### Refine fxlst2
# fxlst2 contains matching opening transactions
# extract dates from the rows that have the opening date and ...
# ...insert into the rows
# print(fxlst2)
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
# fxlst3 is an array witth the opening date,[column data as a list]
for y in fxlst3:
    print(y)

### task: split the fxlst3 into a new lst; the goals is to get one list

### task: clean and format the data in each column
