### UNDER DEVELOPMENT ###
# this app imports and cleans .csv files from the equity options broker 
import csv
import os.path
from pathlib import Path

print("\nThis is the IB options broker app that formats and exports the .csv file")
print("Make sure you are in the correct directory where all of your files are located.")
print(Path.cwd())
confirm_dir = input("Is this the correct directory: (Y/N): ")
if confirm_dir == "Y" or confirm_dir  == "y" or confirm_dir == "Yes" or \
     confirm_dir == "yes" or confirm_dir == "YES" or confirm_dir == "YEs" or \
     confirm_dir == "YeS" or confirm_dir == "yES" or confirm_dir == "yeS" or \
     confirm_dir == "yEs":

    upload_response = input("Would you like to upload a .csv file? (Y/N): ")
    if upload_response == "Y" or upload_response  == "y" or upload_response == "Yes" or \
         upload_response == "yes" or upload_response == "YES" or upload_response == "YEs" or \
         upload_response == "YeS" or upload_response == "yES" or upload_response == "yeS" or \
         upload_response == "yEs":

        # define the broker id for the foreign key in the database
        broker_id = 4

        # contains a list of the trade data from the .csv file
        trade_data_lst = []
        
        # contains a list of 'other fees' from the .csv file
        other_fee_data_lst = []

        # input the .csv filename
        filename = input("enter the entire .csv filename including the extension (example: test_file.csv): ")
        if os.path.isfile(filename):
            split_tup = os.path.splitext(filename)
            file_ext = split_tup[1]
            if file_ext == '.csv':
                with open(filename, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if row[0] == 'trades' or row[0] == 'Trades':
                            trade_rows = row
                            trade_data_lst.append(trade_rows)
                        elif row[2] == 'Other Fees' or row[2] == 'other fees' or row[2] == 'Other fees'\
                            or row[2] == 'other Fees' or row[2] == 'OTHER FEES':
                            other_fee_data_lst.append(row)
                
                # contains unformatted options data
                options_lst1 = []

                # contains the commission and fee data
                comm_fee_lst1 = []

                # create_options_comm_fee_lst extracts the options data and the commission / fee  / other data from the trade_data_lst
                def create_options_comm_fee_lst(lst1):
                    # remove the header line
                    i = len(lst1)
                    for row in lst1[1:i]:
                        options_lst1.append([row[5:9],row[10]])
                        comm_fee_lst1.append([row[6],row[7],row[11]])
                create_options_comm_fee_lst(trade_data_lst)

                # options_dates_lst contains the options dates
                options_dates_lst = []

                # options_time_lst contains a list of the HH:MM:SS (used to create a unique transaction id)
                options_time_lst = []

                # format_options_date() function formats the options date
                def extract_options_date(lst1,lst2,lst3):
                    for row in lst1:
                        date = row[0][1]
                        if date == '':
                            pass
                        else:
                            lst2.append(date[:10])
                            lst3.append(date[12:])
                extract_options_date(options_lst1,options_dates_lst,options_time_lst)
    
                # options_year_lst contains the options year
                options_year_lst = []

                # extract the YYYY from options_dates_lst
                def extract_options_year(lst1, lst2):
                    i = len(lst1)
                    for row in lst1[:i]:
                        yr = row[:4]
                        yr = int(yr)
                        lst2.append(yr)
                extract_options_year(options_dates_lst,options_year_lst)

                # options_month_lst contains the options month
                options_month_lst = []

                # extract the month from options_lst1
                def extract_options_month(lst1,lst2):
                    i = len(lst1)
                    for row in lst1[:i]:
                        mo = row[5:7]
                        mo = int(mo)
                        lst2.append(mo)
                extract_options_month(options_dates_lst,options_month_lst)

                # options_day_lst contains the options day
                options_day_lst = []

                # extract the transaction day from options_lst1
                def extract_options_day(lst1,lst2):
                    i = len(lst1)
                    for row in lst1[:i]:
                        day = row[8:10]
                        day = int(day)
                        lst2.append(day)
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
                extract_options_trade_size(options_lst1,trade_size_lst)

                # mkt_lst contains a list of the markets
                mkt_lst = []

                # extract the markets from options_lst1
                def extract_options_mkt(lst1,lst2):
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
                extract_options_mkt(options_lst1,mkt_lst)

                # call_put_lst contains the calls and puts options contracts
                call_put_lst = []

                # extract the call / put data from options_lst1
                def extract_options_call_put(lst1,lst2):
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
                                call_put = 'Call'
                                lst2.append(call_put)
                            elif call_put == 'P' or call_put == 'PUT':
                                call_put = 'Put'
                                lst2.append(call_put)
                extract_options_call_put(options_lst1,call_put_lst)

                # ctr_lst contains a list of the contract details
                ctr_lst = []

                # extract the contract details from options_lst1
                def extract_options_ctr(lst1,lst2):
                    for row in lst1:
                        if row[0][2] == str(0):
                            pass
                        else:
                            ctr = row[0][0]
                            if ctr == '':
                                pass
                            else:
                                lst2.append(ctr)
                extract_options_ctr(options_lst1,ctr_lst)

                # price_lst contains the options price data
                price_lst = []

                # extract the price data from options_lst1
                def extract_options_price(lst1,lst2):
                    for row in lst1:
                        if row[0][2] == str(0):
                            pass
                        elif row[0][0] == '':
                            pass
                        else:
                            price = row[0][3]
                            price = float(price)
                            lst2.append(price)
                extract_options_price(options_lst1,price_lst)

                # gross_lst contains the options gross amount data
                gross_lst = []

                # extract the gross amount from options_lst1
                def extract_options_gross(lst1,lst2):
                    for row in lst1:
                        if row[0][2] == str(0):
                            pass
                        elif row[0][0] == '':
                            pass
                        else:
                            price = row[1]
                            price = int(price)
                            lst2.append(price)
                extract_options_gross(options_lst1,gross_lst)


                # options_lst2 fields: date,yr,mo,day,bought_sold,trade_size,mkt,call_put,ctr,price,gross
                options_lst2 = []

                # broker_id_lst contains the broker id that will be appended to options_lst2
                broker_id_lst = [broker_id]

                # compiles the column headers (fields) into a list; adds the broker_id
                def compile_options_fields():
                    for date,year,month,day,bought_sold,trade_size,mkt,call_put,ctr,price,gross,broker in zip(
                        options_dates_lst,options_year_lst,options_month_lst,
                        options_day_lst,bought_sold_lst,trade_size_lst,mkt_lst,
                        call_put_lst,ctr_lst,price_lst,gross_lst,broker_id_lst):

                        broker_id_lst.append(broker_id)
                        options_lst2.append([date,year,month,day,bought_sold,trade_size,mkt,call_put,ctr,price,gross,broker])

                compile_options_fields()

                # options_time_lst2 contains formatted HH:MM:SS (used to create a unique transaction id)
                options_time_lst2 = []

                def format_options_time(lst1,lst2):
                    for row in lst1:
                        # HH:MM:SS
                        if row[2] == ':' and row[5] == ':' and len(row) == 8:
                            time_id = f'{row[:2]}{row[3:5]}{row[6:]}'
                            lst2.append(time_id)
                        # H:MM:SS
                        elif row[1] == ':' and row[4] == ':' and len(row) == 7:
                            time_id = f'0{row[0]}{row[2:4]}{row[5:]}'
                            lst2.append(time_id)
                        # HH:M:SS
                        elif row[2] == ':' and row[4] == ':' and len(row) == 7:
                            time_id = f'{row[:2]}0{row[3]}{row[5:]}'
                            lst2.append(time_id)
                        # HH:MM
                        elif row[2] == ':' and len(row) == 5:
                            time_id = f'{row[:2]}{row[3:]}00'
                            lst2.append(time_id)
                        # HH:M
                        elif row[2] == ':' and len(row) == 4:
                            time_id = f'{row[:2]}0{row[3]}00'
                            lst2.append(time_id)
                        # H:MM
                        elif row[1] == ':' and len(row) == 4:
                            time_id = f'0{row[0]}{row[2:4]}00'
                            lst2.append(time_id)
                format_options_time(options_time_lst,options_time_lst2)

                # key_lst1 contains a list of unque identifiers
                key_lst1 = []

               # key_lst2 contains all fields and rows for the options transaction data and a unique identifier
                key_lst2 = []

                # creates a unique identifier and adds it to key_lst2
                def create_key(lst1,lst2,lst3,lst4):
                    indxLst = []
                    i = len(lst1)
                    for row, timeNum in zip(lst1,lst2):
                        valYY = row[0][2:4]
                        valMM = row[0][5:7]
                        valDD = row[0][8:10]
                        valBS = ord(row[4][0].upper())
                        valCP = ord(row[7][0].upper())
                        valHHMMSS = timeNum
                        trans_num = f'{valYY}{valMM}{valDD}{valBS}{valCP}{valHHMMSS}'
                        lst3.append(trans_num)
                    
                    for num in range(i):
                        if num < 10:
                            num = (str(num))
                            num = num.zfill(2)
                            indxLst.append(num)
                        else:
                            num = str(num)
                            indxLst.append(num)

                    for index, id in zip(lst3,indxLst):
                        lst4.append((f'{index}{id}'))

                    for id in lst4:
                        id = int(id)
                    
                create_key(options_lst2,options_time_lst2,key_lst1,key_lst2)
                
                # options_lst3 contains all of the fields and the unique transaction id column
                options_lst3 = []

                def append_key(lst1,lst2,lst3):
                    # tmp_lst = []
                    for col1, col2 in zip(lst1,lst2):
                            lst3.append([col1[0],col1[1],col1[2],col1[3],col1[4],
                            col1[5],col1[6],col1[7],col1[8],
                            col1[9],col1[10],col1[11],col2])
                   
                append_key(options_lst2,key_lst2,options_lst3)

                # comm_fee_lst2 contains the formatted commission and fee transactions
                comm_fee_lst2 = []

                # add dates and format the commissions and fee transaction data list
                def format_comm_fee_data(lst1,lst2):
                    indxLst=[]
                    for row in lst1:
                        if row[1] == '':
                            pass
                        elif row[1] == '0':
                            pass
                        else:
                            indxLst.append(row)

                    for line in indxLst:
                        comm_date = line[0][0:10]
                        YY = comm_date[:4]
                        MM = comm_date[5:7]
                        DD = comm_date[8:10]
                        HHMM = line[0][12:14]+line[0][15:17]
                        fee = line[2]
                        entry = comm_date, YY, MM, DD, fee, broker_id, HHMM
                        entry  = list(entry)
                        lst2.append(entry)
            
                format_comm_fee_data(comm_fee_lst1,comm_fee_lst2)

                # contains list of comm_fee transactions with a unique transaction number identifier
                comm_fee_lst3 = []

                # contains index values of each item in the comm_fee_lst2
                cf_index_lst1 = []

                # creates and appends a a unique transaction identifier to the comm_fee_lst2
                def create_comm_fee_key(lst1,lst2,lst3):
                    i = len(lst1)
                    for i in range(i):
                        if i < 10:
                            i = str(i)
                            i = i.zfill(2)
                            lst2.append(i)
                        else:
                            i = str(i)
                            lst2.append(i)

                    for num, index in zip(lst1, lst2):
                        trans_num = f'{num[1][2:4]}{num[2]}{num[3]}{index}'
                        row  = num[0], num[1], num[2], num[3], num[4], num[5],trans_num
                        row = list(row)
                        lst3.append(row)
                       
                create_comm_fee_key(comm_fee_lst2,cf_index_lst1,comm_fee_lst3)

                # contains fee dates
                fee_dates_lst1 = []

                # contains the fee categories
                other_fees_descriptions_lst1 = []

                # contains fees for the other categories
                other_fees_lst1 = []

                # function extracts the broker, opra, and exchange fee into separate lists
                def create_options_other_fee_lst(lst1,lst2,lst3,lst4):
                    # remove the header
                    i = len(lst1)
                    for row in lst1[3:i]:
                        lst2.append(row[4])
                        lst3.append(row[5])
                        lst4.append(row[6])                        
                create_options_other_fee_lst(other_fee_data_lst,fee_dates_lst1,other_fees_descriptions_lst1,other_fees_lst1)

                # contains the year for the options fees
                options_fee_year_lst1 = []

                # extract the YYYY from the fee_dates_lst1
                def extract_options_fee_year(lst1,lst2):
                    i = len(lst1)
                    for row in lst1[:i]:
                        lst2.append(row[-4:])
                extract_options_fee_year(fee_dates_lst1,options_fee_year_lst1)

                # contains the month for the options fees
                options_fee_month_lst1 = []

                # extract the M or MM from the fee_dates_lst1
                def extract_options_fee_month(lst1,lst2):
                    i = len(lst1)
                    for row in lst1[:i]:
                        if len(row) == 8:
                            mo = row[0]
                            lst2.append(mo)
                
                        elif len(row) == 9:
                            mo = row[:2]
                            lst2.append(mo)
                extract_options_fee_month(fee_dates_lst1,options_fee_month_lst1)

                # contains the day for the options fees
                options_fee_day_lst1 = []

                # extract the D or DD from the fee_dates_lst1
                def extract_options_fee_day(lst1,lst2):
                    i = len(lst1)
                    for row in lst1[:i]:
                        if len(row) == 8:
                            day = row[2]
                            lst2.append(day)

                        elif len(row) == 9:
                            day = row[3]
                            lst2.append(day)
                extract_options_fee_day(fee_dates_lst1,options_fee_day_lst1)

                # contains the formatted fee date
                options_fee_date_lst1 = []

                # compile and format the options fee dates
                def create_options_fee_dates(lst1,lst2,lst3,lst4):
                    for year,month,day in zip(lst1,lst2,lst3):
                        if len(month) == 1:
                            date = f'{year}-0{month}-{day}'
                            lst4.append(date)
                        else:
                            date = f'{year}-{month}-{day}'
                            lst4.append(date)
                create_options_fee_dates(options_fee_year_lst1,options_fee_month_lst1,options_fee_day_lst1,options_fee_date_lst1)
                
                # contains formatted fee descriptions
                other_fees_descriptions_lst2 = []

                # format the fee descriptions
                def format_fee_descriptions(lst1,lst2):
                    i = len(lst1)
                    for row in lst1[:i]:
                        if row[0] == 'C' or row[0] == 'c':
                            other_fees_descriptions_lst2.append(row[10:])
                        elif row[:7] == 'Balance' or row[:7] == 'balance':
                            other_fees_descriptions_lst2.append(row)
                format_fee_descriptions(other_fees_descriptions_lst1,other_fees_descriptions_lst2)
            
                # contains the formatted fee fields
                other_fees_lst2 = []

                # compile and format the fee fields
                def compile_fees(lst1,lst2,lst3,lst4,lst5,lst6,lst7):
                    for date,year,month,day,description,fee,broker in zip(lst1,lst2,lst3,lst4,lst5,lst6,lst7):
                        lst7.append(broker_id)
                        other_fees_lst2.append([date,int(year),int(month),int(day),description,float(fee),broker])
                compile_fees(options_fee_date_lst1,options_fee_year_lst1,options_fee_month_lst1,options_fee_day_lst1,other_fees_descriptions_lst2,other_fees_lst1,broker_id_lst)
               
                # bug missing rows in ib2018.csv file
                # task go back and check the other functions and verify all rows are picked up
                for i in other_fees_lst2:
                    print(i)
                    
                # contains a list of unique identifiers for the fees
                fee_key_lst1 = [] 

                # create a unique identifier for each fee transaction
                def create_fee_key(lst1,lst2):
                    for row in lst1:
                        xVar = row[4][-9::]
                        mo = xVar[1:4]
                        mo_fval = ord(mo[0].upper())
                        mo_fval = str(mo_fval)
                        mo_mval = ord(mo[1].upper())
                        mo_mval = str(mo_mval)
                        mo_lval = ord(mo[2].upper())
                        mo_lval = str(mo_lval)
                        val1 = ord(row[4][0].upper())
                        val2 = ord(row[4][1].upper())
                        val3 = mo_fval+mo_mval+mo_lval
                        if len(row[0][5:7]) == 1:
                            trans_num = f'{row[0][2:4]}{row[0][5:7]}0{row[0][8]}{str(val1)}{str(val2)}{val3}'
                            int(trans_num)
                            lst2.append(trans_num)
                        
                        elif len(row[0][5:7]) == 2:
                            trans_num = f'{row[0][2:4]}{row[0][5:7]}{row[0][8]}{str(val1)}{str(val2)}{val3}'
                            int(trans_num)
                            lst2.append(trans_num)
                create_fee_key(other_fees_lst2,fee_key_lst1)

                # contains the other fee list with all fields and the unique transaction number
                other_fees_lst3 = []

                # append the key to other_fees_lst2
                def append_fee_key(lst1,lst2,lst3):
                    for col1, col2 in zip(lst1,lst2):
                        lst3.append([col1[0],col1[1],col1[2],col1[3],col1[4],col1[5],col1[6],int(col2)])
                append_fee_key(other_fees_lst2,fee_key_lst1,other_fees_lst3)

                # export the options log data
                def options_log_export_records():
                    i = len(options_lst3)
                    logs = options_lst3[:i]
                    print('There are',len(logs),'records to be exported from the options_log_export_records() func')
                    return logs
                # options_log_export_records()

                # export the commissions and fee data
                def comm_fee_log_export_records():
                    i = len(comm_fee_lst3)
                    logs = comm_fee_lst3[:i]
                    print('There are',len(logs),'records to be exported from the comm_fee_log_export_records() func')
                    return logs
                # comm_fee_log_export_records()

                # export the other fee data
                def other_fee_log_export_records():
                    i = len(other_fees_lst3)
                    logs = other_fees_lst3[:i]
                    print('There are',len(logs),'records to be exported from the other_fee_log_export_records() func')
                    return logs
                # other_fee_log_export_records()
                
            else:
                print(f'{filename} is not a .csv file...')
                print("Exiting ib options upload...\n")
                pass
        else:
            print("No ib options .csv files uploaded.")
            print("Exiting ib options upload...\n")
            pass
    else:
        print("No ib options .csv files uploaded.")
        print("Exiting ib options upload...\n")
        pass
else:
    print("Exiting ib options upload...\n")
    pass
