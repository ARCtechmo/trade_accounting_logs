### UNDER DEVELOPMENT ###
# this app imports and cleans the forex broker data from a .csv file
import csv
import re
import os.path
from pathlib import Path

# confirm working directory
print("This is the fx broker app that formats and exports the .csv file")
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

        # comm_lst contains commissions
        comm_lst = []

        # int_lst contains financing categories
        int_lst = []

        # fxlst is a list of trades only (no commission or fee data is included)
        fxlst = []

        broker_credit_lst = []
        broker_id = 3

        # separate the buy / se//, commission, financing, and interest credit items
        filename = input("enter the entire .csv filename including the extension (example: test_file.csv): ")

        # definee the directory and path of the .csv file
        if os.path.isfile(filename):
            split_tup = os.path.splitext(filename)
            file_ext = split_tup[1]
            if file_ext == '.csv':
                header_option = input("Does the file have a header? (Y/N): ")
                if header_option == "N" or header_option == 'n' or header_option == "No" or \
                   header_option == 'no' or header_option =='NO' or header_option == 'nO':
                    with open(filename, newline='') as csvfile:
                        reader = csv.reader(csvfile)
                        for row in reader:
                            if row[4] != "":
                                fxlst.append(row)
                            elif 'COMMISSION' in row[1]:
                                comm_lst.append(row)
                            elif 'FINANCING' in row[1]:
                                int_lst.append(row)
                            elif 'Active' in row[1] or 'Credit' in row[1]:
                                broker_credit_lst.append(row)
                elif header_option == "Y" or header_option == 'y' or header_option == "Yes" or \
                     header_option == 'yes' or header_option =='YES' or header_option == 'YEs' or \
                     header_option == 'YeS' or header_option == 'yES' or header_option == 'yeS' or \
                     header_option == 'yEs':
                     with open(filename, newline='') as csvfile:
                         reader = csv.reader(csvfile)
                         next(reader)
                         for row in reader:
                             if row[4] != "":
                                 fxlst.append(row)
                             elif 'COMMISSION' in row[1]:
                                 comm_lst.append(row)
                             elif 'FINANCING' in row[1]:
                                 int_lst.append(row)
                             elif 'Active' in row[1] or 'Credit' in row[1]:
                                 broker_credit_lst.append(row)
                else:
                    print("Invalid input. No logs imported.")
                    pass

                # count the number of trade transactions
                def fx_count_trade_transactions():
                    count = 0
                    for item in fxlst:
                        count +=1
                    print(f'There are {count} returned rows with buy/sell data.')
                # fx_count_trade_transactions()

                # transfxlst consists of only the open / closed transaction ids
                transfxlst = []

                # match the open / closed transaction ids
                def fx_get_open_close_trans_ids(lst1,lst2):
                    for item in lst1:
                        if item[2] == '':
                            # insert 000000000 in field 2 to identify rows that have the entry times
                            item[2] = '000000000'
                        lst2.append(item[3])
                fx_get_open_close_trans_ids(fxlst,transfxlst)

                # matched_lst contains all transaction ids that have open and close ids
                matched_lst = []

                # unmatched_lst contains all transactions ids that do not have open and close ids
                unmatched_lst = []

                # match the open / closed transaction ids
                def fx_create_dict_open_close_trans_ids(lst1,lst2,lst3):
                    # dictionary gets a count of the transaction ids
                    di = dict()
                    for num in lst1:
                        di[num] = di.get(num,0) + 1
                    for key,value in di.items():

                        # alert the user when there are missing opening transaction ids
                        if value <2:
                            missing_id = key
                            lst2.append(missing_id)
                        else:
                            matching_id = key
                            lst3.append(matching_id)

                fx_create_dict_open_close_trans_ids(transfxlst,unmatched_lst,matched_lst)

                # fxlst2 contains rows only with open and closed /  open transactions
                fxlst2 = []

                # remove the missing transaction id identified in the dictionary from fxlst
                def fx_remove_missing_open_close_trans_ids(lst1,lst2):
                    for row in lst1:
                        open_id = row[3]
                        if open_id in matched_lst:
                            lst2.append(row)

                fx_remove_missing_open_close_trans_ids(fxlst,fxlst2)

                # unmatched_lst2 contains additional open ids without matches (edge case)
                # NOTE: new function added for an edge case that causes a missing row 
                unmatched_lst2 = []
                def fx_get_open_id(lst1,lst2,lst3):
                    for row in lst1:
                        quant = row[7]
                        quant = int(quant)
                        openid = row[3]
                        openid = int(openid)
                        if (quant > 0 and row[5] == 'No') or (quant > 0 and row[5] == 'no') or (quant > 0 and row[5] == 'NO'):
                            lst3.append(openid)
                        elif str(openid) in lst2:
                            lst3.append(openid)
                fx_get_open_id(fxlst,unmatched_lst,unmatched_lst2)

                # open_trans_lst contains tuples with the open dates and open transaction ids
                open_trans_lst = []

                # extract dates from the rows that have the opening date and insert into the rows
                def fx_extract_open_trans_dates(lst1,lst2):
                    for item in lst1:
                        if item[2] == '000000000':
                            entry_date = item[0]
                            lst2.append((entry_date, item[3]))
                        else:
                            pass
                fx_extract_open_trans_dates(fxlst2,open_trans_lst)

                # fxlst3 contains all trade transaction rows with the needed data ready for formatting
                fxlst3 = []

                # match inserts the opening date to the row with the matching closed date
                def fx_match_insert_open_close_dates(lst1,lst2):
                    for x in lst1:
                        for tup in open_trans_lst:
                            # extract the columns with closing date '000000000'
                            if x[2] != '000000000' and x[3] == tup[1]:
                                lst2.append([tup[0],x])
                fx_match_insert_open_close_dates(fxlst,fxlst3)

                # fxlst4 contains the entry dates formatted to YYY-MM-DD-HH:MM
                fxlst4 = []

                # extract and format the entry date to YYYY-MM-DD-HH:MM
                def fx_format_entry_date(lst1,lst2):
                    for dmy in lst1:

                        # DD/MM/YYYY
                        if dmy[0][2] == '/' and dmy[0][5] =='/':
                            entry_yr = dmy[0][6:10]
                            entry_mo = dmy[0][3:5]
                            entry_day = dmy[0][:2]
                            entry_time = dmy[0][11:]

                            # DD/MM/YYYY H:MM
                            if len(entry_time) == 4 and entry_time[1] == ':':
                                entry_time = f'0{dmy[0][11:15]}'
                                formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
                                lst2.append(formatted_entry_date)
                            
                            # DD/MM/YYYY HH:MM
                            elif len(entry_time) >= 5 and entry_time[2] == ':':
                                entry_time = dmy[0][11:16]
                                formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
                                lst2.append(formatted_entry_date)
                                                
                        # DD/M/YYYY
                        elif dmy[0][2] == '/' and dmy[0][4] =='/':
                            entry_yr = dmy[0][5:9]
                            entry_mo = dmy[0][3]
                            entry_mo = f'0{entry_mo}'
                            entry_day = dmy[0][:2]
                            entry_time = dmy[0][10:]

                            # DD/M/YYYY H:MM
                            if len(entry_time) == 4 and entry_time[1] == ':':
                                entry_time = f'0{dmy[0][10:14]}'
                                formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
                                lst2.append(formatted_entry_date)

                            # DD/M/YYYY HH:MM
                            elif len(entry_time) >= 5 and entry_time[2] == ':':
                                entry_time = dmy[0][10:15]
                                formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
                                lst2.append(formatted_entry_date)

                        # D/MM/YYYY
                        elif dmy[0][1] == '/' and dmy[0][4] =='/':
                            entry_yr = dmy[0][5:9]
                            entry_mo = dmy[0][2:4]
                            entry_day = dmy[0][0]
                            entry_day = f'0{entry_day}'
                            entry_time = dmy[0][10:]

                            # D/MM/YYYY H:MM
                            if len(entry_time) == 4 and entry_time[1] == ':':
                                entry_time = f'0{dmy[0][10:14]}'
                                formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
                                lst2.append(formatted_entry_date)

                            # D/MM/YYYY HH:MM
                            elif len(entry_time) >= 5 and entry_time[2] == ':':
                                entry_time = dmy[0][10:15]
                                formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
                                lst2.append(formatted_entry_date)

                        # D/M/YYYY
                        elif dmy[0][1] == '/' and dmy[0][3] =='/':
                            entry_yr = dmy[0][4:8]
                            entry_mo = dmy[0][2]
                            entry_mo = f'0{entry_mo}'
                            entry_day = dmy[0][0]
                            entry_day = f'0{entry_day}'
                            entry_time = dmy[0][9:]

                            # D/M/YYYY H:MM
                            if len(entry_time) == 4 and entry_time[1] == ':':
                                entry_time = f'0{dmy[0][9:13]}'
                                formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
                                lst2.append(formatted_entry_date)

                            # D/M/YYYY HH:MM
                            elif len(entry_time) >= 5 and entry_time[2] == ':':
                                entry_time = dmy[0][9:14]
                                formatted_entry_date = f'{entry_yr}-{entry_mo}-{entry_day} {entry_time}'
                                lst2.append(formatted_entry_date)

                fx_format_entry_date(fxlst3,fxlst4)

                # fxlst5 contains the exit dates formatted to YYYY-MM-DD-HH:MM
                fxlst5 = []

                # extract and format the exit date to YYYY-MM-DD-HH:MM
                def fx_format_exit_date(lst1,lst2):
                    for dmy in lst1:

                        # DD/MM/YYYY
                        if dmy[1][0][2] == '/' and dmy[1][0][5] =='/':
                            exit_yr = dmy[1][0][6:10]
                            exit_mo = dmy[1][0][3:5]
                            exit_day = dmy[1][0][:2]
                            exit_time = dmy[1][0][11:]

                            # DD/MM/YYYY H:MM
                            if len(exit_time) == 4 and exit_time[1] == ':':
                                exit_time = f'0{dmy[1][0][11:15]}'
                                formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
                                lst2.append(formatted_exit_date)
                            
                            # DD/MM/YYYY HH:MM
                            elif len(exit_time) >= 5 and exit_time[2] == ':':
                                exit_time = dmy[1][0][11:16]
                                formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
                                lst2.append(formatted_exit_date)

                        # DD/M/YYYY    
                        elif dmy[1][0][2] == '/' and dmy[1][0][4] =='/':
                            exit_yr = dmy[1][0][5:9]
                            exit_mo = dmy[1][0][3]
                            exit_mo = f'0{exit_mo}'
                            exit_day = dmy[1][0][:2]
                            exit_time = dmy[1][0][10:]

                            # DD/M/YYYY H:MM
                            if len(exit_time) == 4 and exit_time[1] == ':':
                                exit_time = f'0{dmy[1][0][10:14]}'
                                formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
                                lst2.append(formatted_exit_date)
                            
                            # DD/M/YYYY HH:MM
                            elif len(exit_time) >= 5 and exit_time[2] == ':':
                                exit_time = dmy[1][0][10:15]
                                formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
                                lst2.append(formatted_exit_date)

                        # D/MM/YYYY
                        elif dmy[1][0][1] == '/' and dmy[1][0][4] =='/':
                            exit_yr = dmy[1][0][5:9]
                            exit_mo = dmy[1][0][2:4]
                            exit_day = dmy[1][0][0]
                            exit_day = f'0{exit_day}'
                            exit_time = dmy[1][0][10:]

                            # D/MM/YYYY H:MM
                            if len(exit_time) == 4 and exit_time[1] == ':':
                                exit_time = f'0{dmy[1][0][10:14]}'
                                formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
                                lst2.append(formatted_exit_date)
                            
                            # D/MM/YYYY HH:MM
                            elif len(exit_time) >= 5 and exit_time[2] == ':':
                                exit_time = dmy[1][0][10:15]
                                formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
                                lst2.append(formatted_exit_date)

                        # D/M/YYYY
                        elif dmy[1][0][1] == '/' and dmy[1][0][3] =='/':
                            exit_yr = dmy[1][0][4:8]
                            exit_mo = dmy[1][0][2]
                            exit_mo = f'0{exit_mo}'
                            exit_day = dmy[1][0][0]
                            exit_day = f'0{exit_day}'
                            exit_time = dmy[1][0][9:]

                            # D/M/YYYY H:MM
                            if len(exit_time) == 4 and exit_time[1] == ':':
                                exit_time = f'0{dmy[1][0][9:13]}'
                                formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
                                lst2.append(formatted_exit_date)
                            
                            # D/M/YYYY HH:MM
                            elif len(exit_time) >= 5 and exit_time[2] == ':':
                                exit_time = dmy[1][0][9:14]
                                formatted_exit_date = f'{exit_yr}-{exit_mo}-{exit_day} {exit_time}'
                                lst2.append(formatted_exit_date)

                fx_format_exit_date(fxlst3,fxlst5)

                # marketlst contains the formatted market (e.g. EURUSD, AUDJPY, etc...)
                marketlst = []

                # extract the currency pairs from fxlst3
                def fx_extract_currency_pairs(lst1,lst2):
                    for mkt in lst1:
                        if len(mkt[1][1]) == 13:
                            market = mkt[1][1]
                            market2 = re.split(' ',market)
                            market3 = market2[3]
                            lst2.append(market3)
                        elif len(mkt[1][1]) == 12:
                            market = mkt[1][1]
                            market2 = re.split(' ',market)
                            market3 = market2[2]
                            lst2.append(market3)
                        elif len(mkt[1][1]) == 11:
                            market = mkt[1][1]
                            market2 = re.split(' ',market)
                            market3 = market2[1]
                            lst2.append(market3)
                fx_extract_currency_pairs(fxlst3,marketlst)

                # close_id_lst contains the closing transaction ids
                close_id_lst = []

                # extract the closing transaction ids from fxlst3
                def fx_extract_close_trans_ids(lst1,lst2):
                    for elements in lst1:
                        close_id = elements[1][2]
                        close_id = int(close_id)
                        lst2.append(close_id)
                fx_extract_close_trans_ids(fxlst3,close_id_lst)

                # open_id_lst contains the opening transaction ids
                open_id_lst = []

                # extract the opening transaction ids from fxlst3
                def fx_extract_open_trans_ids(lst1,lst2):
                    for elements in lst1:
                        open_id = elements[1][3]
                        open_id = int(open_id)
                        lst2.append(open_id)
                fx_extract_open_trans_ids(fxlst3,open_id_lst)

                # buy_sell_lst contains buy or sell transactions
                buy_sell_lst = []

                # extract the buy / sell from fxlst3
                def fx_extract_buy_sell_trans(lst1,lst2):
                    for action in lst1:
                        buy_sell = action[1][4]
                        lst2.append(buy_sell)
                fx_extract_buy_sell_trans(fxlst3,buy_sell_lst)

                # trade_size_lst contains the size of the trades taken
                trade_size_lst = []

                # extract the trade_size from fxlst3
                def fx_extract_trade_size(lst1,lst2):
                    for size in lst1:
                        trade_size = size[1][6]
                        trade_size = trade_size.split('.')
                        trade_size = trade_size[0]
                        trade_size = int(trade_size)
                        lst2.append(trade_size)
                fx_extract_trade_size(fxlst3,trade_size_lst)

                # open_price_lst contains the opening price
                open_price_lst = []

                # extract the open_price from fxlst3
                def fx_extract_open_price(lst1,lst2):
                    for openpr in lst1:
                        openpr = openpr[1][8]
                        openpr = float(openpr)
                        lst2.append(openpr)
                fx_extract_open_price(fxlst3,open_price_lst)

                # close_price_lst contains the closing price
                close_price_lst = []

                # extract the close_price from fxlst3
                def fx_extract_close_price(lst1,lst2):
                    for closepr in lst1:
                        closepr = closepr[1][9]
                        closepr = float(closepr)
                        lst2.append(closepr)
                fx_extract_close_price(fxlst3,close_price_lst)

                # gross_lst contains the gross profit / loss
                gross_lst = []

                # extract the gross from fxlst3
                def fx_extract_gross(lst1,lst2):
                    for gross in lst1:
                        gross = gross[1][12]
                        gross = float(gross)
                        lst2.append(gross)
                fx_extract_gross(fxlst3,gross_lst)

                # net_lst contains the gross profit / loss
                net_lst = []

                # extract the net from fxlst3
                def fx_extract_net(lst1,lst2):
                    for net in lst1:
                        net = net[1][12]
                        net = float(net)
                        lst2.append(net)
                fx_extract_net(fxlst3,net_lst)

                # fxlog_lst_1 contains the formatted list absent the unique transaction identifier
                fxlog_lst_1 = []

                # the broker_id is a list to make it iterable to add to the transaction list
                broker_id_lst = [broker_id]

                def fx_create_trade_log_1(lst):
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
                        lst.append(
                                    [entry, entry_yr, entry_mo, entry_day, entry_time,
                                    exit, exit_yr, exit_mo, exit_day, exit_time,
                                    market, close_id, open_id, buy_sell, trade_size, open, close, gross, net,
                                    broker]
                                    )

                fx_create_trade_log_1(fxlog_lst_1)

                # create a unique key for each transaction
                key_lst = []

                # create the unique identifier for each trade transaction record
                def fx_create_log_key(lst1,lst2):
                    for num in lst1:
                        entry_year_key = f'{num[0][2:4]}'
                        entry_month_key = f'{num[0][5:7]}'
                        entry_day_key = f'{num[0][8:10]}'
                        exit_month_key = f'{num[5][5:7]}'
                        exit_day_key = f'{num[5][8:10]}'
                        open_trans_id = str(num[11])
                        close_trans_id = str(num[12])
                        open_partial_trans_id = open_trans_id[-4::]
                        close_partial_trans_id = close_trans_id[-4::]
                        close_open_key = f'{open_partial_trans_id}{close_partial_trans_id}'
                        unique_key = f'{entry_year_key}{entry_month_key}{entry_day_key}{exit_month_key}{exit_day_key}{close_open_key}'
                        unique_key = int(unique_key)
                        lst2.append(unique_key)

                fx_create_log_key(fxlog_lst_1,key_lst)

                # fxlog_lst_2 contains the finalized list of the matched trade transactions
                fxlog_lst_2 = []

                # create finalized matched trade transaction logs
                def fx_create_trade_log_2(lst):
                    for entry, exit, market, close_id, open_id, buy_sell, trade_size, open, close, gross, net, broker, key in zip(
                        fxlst4, fxlst5, marketlst,
                        close_id_lst, open_id_lst,
                        buy_sell_lst, trade_size_lst,
                        open_price_lst, close_price_lst,
                        gross_lst, net_lst, broker_id_lst, key_lst
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

                        broker_id_lst.append(broker_id)
                        lst.append(
                                    [entry, entry_yr, entry_mo, entry_day, entry_time,
                                    exit, exit_yr, exit_mo, exit_day, exit_time,
                                    market, close_id, open_id, buy_sell, trade_size, open, close, gross, net,
                                    broker, key]
                                    )

                fx_create_trade_log_2(fxlog_lst_2)

                # unmatched_fxlst contains rows with open transactionns only (no open and close)
                unmatched_fxlst = []
                
                # NOTE: modifications to this function addresses edge cases for a missing row
                # NOTE: new function added for an edge case that causes a missing row 
                def fx_unmatched_get_open_trans_id(lst1,lst2,lst3):
                    for row in lst1:
                        unmatched_open_id = row[3]
                        unmatched_open_id = int(unmatched_open_id)
                        if unmatched_open_id in lst2 and row[2] == '000000000':
                            lst3.append(row)
                fx_unmatched_get_open_trans_id(fxlst,unmatched_lst2,unmatched_fxlst)

                # unmatched_open_date_lst contains the open date in YYYY-MM-DD HH:MM format
                unmatched_open_date_lst = []

                # format the open dates in unmatched_fxlst
                def fx_unmatched_format_open_dates(lst1,lst2):
                    for item in lst1:
                        if item[2] == '000000000':
                            for dmy in lst1:

                                # DD/MM/YYY
                                if dmy[0][2] == '/' and dmy [0][5] == '/':
                                    unmatched_entry_yr = dmy[0][6:10]
                                    unmatched_entry_mo = dmy[0][3:5]
                                    unmatched_entry_day = dmy[0][:2]
                                    unmatched_entry_time = dmy[0][11:]

                                    # DD/MM/YYY H:MM
                                    if len(unmatched_entry_time) == 4 and unmatched_entry_time[1] == ':':
                                        unmatched_entry_time = f'0{[0][11:15]}'
                                        formatted_unmatched_entry_date = f'{unmatched_entry_yr}-{unmatched_entry_mo}-{unmatched_entry_day} {unmatched_entry_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                    
                                    # DD/MM/YYY HH:MM
                                    elif len(unmatched_entry_time) >= 5 and unmatched_entry_time[2] == ':':
                                        unmatched_entry_time = dmy[0][11:16]
                                        formatted_unmatched_entry_date = f'{unmatched_entry_yr}-{unmatched_entry_mo}-{unmatched_entry_day} {unmatched_entry_time}'
                                        lst2.append(formatted_unmatched_entry_date)

                                # DD/M/YYYY
                                elif dmy[0][2] == '/' and dmy[0][4] == '/':
                                    unmatched_entry_yr = dmy[0][5:9]
                                    unmatched_entry_mo = dmy[0][3]
                                    unmatched_entry_mo = f'0{unmatched_entry_mo}'
                                    unmatched_entry_day = dmy[0][:2]
                                    unmatched_entry_time = dmy[0][10:]

                                    # DD/M/YYYY H:MM
                                    if len(unmatched_entry_time) == 4 and unmatched_entry_time[1] == ':':
                                        unmatched_entry_time = f'0{[0][10:14]}'
                                        formatted_unmatched_entry_date = f'{unmatched_entry_yr}-{unmatched_entry_mo}-{unmatched_entry_day} {unmatched_entry_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                    
                                    # DD/M/YYYY HH:MM
                                    elif len(unmatched_entry_time) >= 5 and unmatched_entry_time[2] == ':':
                                        unmatched_entry_time = dmy[0][10:15]
                                        formatted_unmatched_entry_date = f'{unmatched_entry_yr}-{unmatched_entry_mo}-{unmatched_entry_day} {unmatched_entry_time}'
                                        lst2.append(formatted_unmatched_entry_date)

                                # D/MM/YYYY
                                elif dmy[0][1] == '/' and dmy[0][4] == '/':
                                    unmatched_entry_yr = dmy[0][5:9]
                                    unmatched_entry_mo = dmy[0][2:4]
                                    unmatched_entry_day = dmy[0][0]
                                    unmatched_entry_day = f'0{unmatched_entry_day}'
                                    unmatched_entry_time = dmy[0][10:]

                                    # D/MM/YYYY H:MM
                                    if len(unmatched_entry_time) == 4 and unmatched_entry_time[1] == ':':
                                        unmatched_entry_time = f'0{[0][10:14]}'
                                        formatted_unmatched_entry_date = f'{unmatched_entry_yr}-{unmatched_entry_mo}-{unmatched_entry_day} {unmatched_entry_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                    
                                    # D/MM/YYYY HH:MM
                                    elif len(unmatched_entry_time) >= 5 and unmatched_entry_time[2] ==':':
                                        unmatched_entry_time = dmy[0][10:15]
                                        formatted_unmatched_entry_date = f'{unmatched_entry_yr}-{unmatched_entry_mo}-{unmatched_entry_day} {unmatched_entry_time}'
                                        lst2.append(formatted_unmatched_entry_date)

                                # D/M/YYYY
                                elif dmy[0][1] == '/' and dmy[0][3] == '/':
                                    unmatched_entry_yr = dmy[0][4:8]
                                    unmatched_entry_mo = dmy[0][2]
                                    unmatched_entry_mo = f'0{unmatched_entry_mo}'
                                    unmatched_entry_day = dmy[0][0]
                                    unmatched_entry_day = f'0{unmatched_entry_day}'
                                    unmatched_entry_time = dmy[0][9:]

                                    # D/M/YYYY H:MM
                                    if len(unmatched_entry_time) == 4 and unmatched_entry_time[1] == ':':
                                        unmatched_entry_time = f'0{[0][9:13]}'
                                        formatted_unmatched_entry_date = f'{unmatched_entry_yr}-{unmatched_entry_mo}-{unmatched_entry_day} {unmatched_entry_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                    
                                    # D/M/YYYY HH:MM
                                    elif len(unmatched_entry_time) >= 5 and unmatched_entry_time[2] == ':':
                                        unmatched_entry_time = dmy[0][9:14]
                                        formatted_unmatched_entry_date = f'{unmatched_entry_yr}-{unmatched_entry_mo}-{unmatched_entry_day} {unmatched_entry_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                        else:
                            lst2.append('0000-00-00 00:00')

                fx_unmatched_format_open_dates(unmatched_fxlst,unmatched_open_date_lst)

                # unmatched_close_date_lst contains the close date in YYYY:MM:DD HH:MM format
                unmatched_close_date_lst = []

                # format the closed dates in unmatched_fxlst
                # *** bug to fix: format just like fx_format_exit_date()***
                def fx_unmatched_format_closed_dates(lst1,lst2):
                    for item in lst1:
                        if item[2] != '000000000':
                            for dmy in lst1:

                                # DD/MM/YYYY
                                if dmy[0][2] == '/' and dmy [0][5] == '/':
                                    unmatched_exit_yr = dmy[0][6:10]
                                    unmatched_exit_mo = dmy[0][3:5]
                                    unmatched_exit_day = dmy[0][:2]
                                    unmatched_exit_time = dmy[0][11:]

                                    # DD/MM/YYYY H:MM
                                    if len(unmatched_exit_time) == 4 and unmatched_exit_time[1] ==':':
                                        unmatched_exit_time = f'0{[0][11:15]}'
                                        formatted_unmatched_entry_date = f'{unmatched_exit_yr}-{unmatched_exit_mo}-{unmatched_exit_day} {unmatched_exit_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                    
                                    # DD/MM/YYYY HH:MM
                                    elif len(unmatched_exit_time) >= 5 and unmatched_exit_time[2] ==':':
                                        unmatched_exit_time = dmy[0][11:16]
                                        formatted_unmatched_entry_date = f'{unmatched_exit_yr}-{unmatched_exit_mo}-{unmatched_exit_day} {unmatched_exit_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                
                                # DD/M/YYYY
                                elif dmy[0][2] == '/' and dmy[0][4] == '/':
                                    unmatched_exit_yr = dmy[0][5:9]
                                    unmatched_exit_mo = dmy[0][3]
                                    unmatched_exit_mo = f'0{unmatched_exit_mo}'
                                    unmatched_exit_day = dmy[0][:2]
                                    unmatched_exit_time = dmy[0][10:]

                                    # DD/M/YYYY H:MM
                                    if len(unmatched_exit_time) == 4 and unmatched_exit_time[1] == ':':
                                        unmatched_exit_time = f'0{[0][10:14]}'
                                        formatted_unmatched_entry_date = f'{unmatched_exit_yr}-{unmatched_exit_mo}-{unmatched_exit_day} {unmatched_exit_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                    
                                    # DD/M/YYYY HH:MM
                                    elif len(unmatched_exit_time) >= 5 and unmatched_exit_time[2] ==':':
                                        unmatched_exit_time = dmy[0][10:15]
                                        formatted_unmatched_entry_date = f'{unmatched_exit_yr}-{unmatched_exit_mo}-{unmatched_exit_day} {unmatched_exit_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                
                                # D/MM/YYYY 
                                elif dmy[0][1] == '/' and dmy[0][4] == '/':
                                    unmatched_exit_yr = dmy[0][5:9]
                                    unmatched_exit_mo = dmy[0][2:4]
                                    unmatched_exit_day = dmy[0][0]
                                    unmatched_exit_day = f'0{unmatched_exit_day}'
                                    unmatched_exit_time = dmy[0][10:]

                                    # D/MM/YYYY H:MM
                                    if len(unmatched_exit_time) == 4 and unmatched_exit_time[1] ==':':
                                        unmatched_exit_time = f'0{[0][10:14]}'
                                        formatted_unmatched_entry_date = f'{unmatched_exit_yr}-{unmatched_exit_mo}-{unmatched_exit_day} {unmatched_exit_time}'
                                        lst2.append(formatted_unmatched_entry_date)

                                    # D/MM/YYYY HH:MM
                                    elif len(unmatched_exit_time) >= 5 and unmatched_exit_time[2] ==':':
                                        unmatched_exit_time = dmy[0][10:15]
                                        formatted_unmatched_entry_date = f'{unmatched_exit_yr}-{unmatched_exit_mo}-{unmatched_exit_day} {unmatched_exit_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                
                                # D/M/YYYY
                                elif dmy[0][1] == '/' and dmy[0][3] == '/':
                                    unmatched_exit_yr = dmy[0][4:8]
                                    unmatched_exit_mo = dmy[0][2]
                                    unmatched_exit_mo = f'0{unmatched_exit_mo}'
                                    unmatched_exit_day = dmy[0][0]
                                    unmatched_exit_day = f'0{unmatched_exit_day}'
                                    unmatched_exit_time = dmy[0][9:]

                                     # D/M/YYYY H:MM
                                    if len(unmatched_exit_time) == 4 and unmatched_exit_time[1] == ':':
                                        unmatched_exit_time = f'0{[0][9:13]}'
                                        formatted_unmatched_entry_date = f'{unmatched_exit_yr}-{unmatched_exit_mo}-{unmatched_exit_day} {unmatched_exit_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                                    
                                     # D/M/YYYY HH:MM
                                    elif len(unmatched_exit_time) >= 5 and unmatched_exit_time[2] == ':':
                                        unmatched_exit_time = dmy[0][9:14]
                                        formatted_unmatched_entry_date = f'{unmatched_exit_yr}-{unmatched_exit_mo}-{unmatched_exit_day} {unmatched_exit_time}'
                                        lst2.append(formatted_unmatched_entry_date)
                        else:
                            lst2.append('0000-00-00 00:00')

                fx_unmatched_format_closed_dates(unmatched_fxlst,unmatched_close_date_lst)
             
                # unmatched_marketlst contains the currency pair
                unmatched_marketlst = []

                def fx_unmatched_extract_currency_pairs(lst1,lst2):
                    for mkt in lst1:
                        if len(mkt[1]) == 13:
                            market = mkt[1]
                            market2 = re.split(' ',market)
                            market3 = market2[3]
                            lst2.append(market3)
                        elif len(mkt[1]) == 12:
                            market = mkt[1]
                            market2 = re.split(' ',market)
                            market3 = market2[2]
                            lst2.append(market3)
                        elif len(mkt[1]) == 11:
                            market = mkt[1]
                            market2 = re.split(' ',market)
                            market3 = market2[1]
                            lst2.append(market3)

                fx_unmatched_extract_currency_pairs(unmatched_fxlst,unmatched_marketlst)

                # unmatched_close_id_lst is a place holder for the close_id
                unmatched_close_id_lst = []

                # extract the unmatched close transactions
                def fx_unmatched_extract_close_trans_id(lst1,lst2):
                    for elements in lst1:
                        unmatched_close_id = elements[2]
                        unmatched_close_id = int(unmatched_close_id)
                        lst2.append(unmatched_close_id)

                fx_unmatched_extract_close_trans_id(unmatched_fxlst,unmatched_close_id_lst)

                # unmatched_open_id_lst is a place holder for the close_id
                unmatched_open_id_lst = []

                # extract the unmatched open transactions
                def fx_unmatched_extract_open_trans_id(lst1,lst2):
                    for elements in lst1:
                        unmatched_open_id = elements[3]
                        unmatched_open_id = int(unmatched_open_id)
                        lst2.append(unmatched_open_id)

                fx_unmatched_extract_open_trans_id(unmatched_fxlst,unmatched_open_id_lst)

                # unmatched_buy_sell_lst contains the action taken
                unmatched_buy_sell_lst = []

                # extract unmatched buy and sell transactions
                def fx_unmatched_extract_buy_sell_trans(lst1,lst2):
                    for action in lst1:
                        unmatched_buy_sell = action[4]
                        lst2.append(unmatched_buy_sell)

                fx_unmatched_extract_buy_sell_trans(unmatched_fxlst,unmatched_buy_sell_lst)

                # unmatched_trade_size_lst contains the trade size
                unmatched_trade_size_lst = []

                # extract unmatched trade size transactions
                def fx_unmatched_extract_trade_size_trans(lst1,lst2):
                    for size in lst1:
                        unmatched_trade_size = size[6]
                        unmatched_trade_size = unmatched_trade_size.split('.')
                        unmatched_trade_size = unmatched_trade_size[0]
                        unmatched_trade_size = int(unmatched_trade_size)
                        lst2.append(unmatched_trade_size)

                fx_unmatched_extract_trade_size_trans(unmatched_fxlst,unmatched_trade_size_lst)

                # unmatched_open_price_lst contains the open price
                unmatched_open_price_lst = []

                # extract unmatched open price transactions
                def fx_unmatched_extract_open_price_trans(lst1,lst2):
                    for openpr in lst1:
                        unmatched_openpr = openpr[8]
                        unmatched_openpr = float(unmatched_openpr)
                        lst2.append(unmatched_openpr)

                fx_unmatched_extract_open_price_trans(unmatched_fxlst,unmatched_open_price_lst)

                # unmatched_close_price_lst contains the close prices
                unmatched_close_price_lst = []

                # extract unmatched close price transactions
                def fx_unmatched_extract_close_price_trans(lst1,lst2):
                    for closepr in lst1:
                        if closepr[2] == '000000000':
                            closepr = float(0)
                            lst2.append(closepr)
                        else:
                            closepr = float(closepr[9])
                            lst2.append(closepr)

                fx_unmatched_extract_close_price_trans(unmatched_fxlst,unmatched_close_price_lst)

                # unmatched_gross_lst contains the gross gain / loss
                unmatched_gross_lst = []

                # extract unmatched gross transactions
                def fx_unmatched_extract_gross_trans(lst1,lst2):
                    for gross in lst1:
                        if gross[2] == '000000000':
                            gross = 0
                            gross = float(gross)
                            lst2.append(gross)
                        else:
                            gross = gross[12]
                            gross = float(gross)
                            lst2.append(gross)

                fx_unmatched_extract_gross_trans(unmatched_fxlst,unmatched_gross_lst)

                # unmatched_net_lst contains the gross gain / loss
                unmatched_net_lst = []

                # extract unmatched net transactions
                def fx_unmatched_extract_net_trans(lst1,lst2):
                    for net in lst1:
                        if net[2] == '000000000':
                            net = 0
                            net = float(net)
                            lst2.append(net)
                        else:
                            net = net[12]
                            net = float(net)
                            lst2.append(net)

                fx_unmatched_extract_net_trans(unmatched_fxlst,unmatched_net_lst)

                # unmatched_fxlog contains the list of unmatched transactions to be exported into the database
                # unmatched_fxlog does not have a unique identifier key
                # keys will get added after being matched in the databased with the open transactions
                unmatched_fxlog = []
                for unmatched_entry, unmatched_exit, unmatched_market, unmatched_close_id, \
                    unmatched_open_id, unmatched_buy_sell, unmatched_trade_size, \
                    unmatched_open, unmatched_close, unmatched_gross, unmatched_net, broker  \
                    in zip(
                        unmatched_open_date_lst, unmatched_close_date_lst, unmatched_marketlst, \
                        unmatched_close_id_lst, unmatched_open_id_lst, unmatched_buy_sell_lst, \
                        unmatched_trade_size_lst, unmatched_open_price_lst,
                        unmatched_close_price_lst, unmatched_gross_lst, \
                        unmatched_net_lst, broker_id_lst
                        ):

                        unmatched_entry_yr = unmatched_entry[:4]
                        unmatched_entry_yr = int(unmatched_entry_yr)
                        unmatched_entry_mo = unmatched_entry[5:7]
                        unmatched_entry_mo = int(unmatched_entry_mo)
                        unmatched_entry_day = unmatched_entry[8:10]
                        unmatched_entry_day = int(unmatched_entry_day)
                        unmatched_entry_time = unmatched_entry[11:16]

                        unmatched_exit_yr = unmatched_exit[:4]
                        unmatched_exit_yr = int(unmatched_exit_yr)
                        unmatched_exit_mo = unmatched_exit[5:7]
                        unmatched_exit_mo = int(unmatched_exit_mo)
                        unmatched_exit_day = unmatched_exit[8:10]
                        unmatched_exit_day = int(unmatched_exit_day)
                        unmatched_exit_time = unmatched_exit[11:16]

                        broker_id_lst.append(broker_id)
                        unmatched_fxlog.append(
                            [unmatched_entry, unmatched_entry_yr, unmatched_entry_mo,
                             unmatched_entry_day, unmatched_entry_time,
                             unmatched_exit, unmatched_exit_yr, unmatched_exit_mo,
                             unmatched_exit_day, unmatched_exit_time,
                             unmatched_market, unmatched_close_id, unmatched_open_id,
                             unmatched_buy_sell, unmatched_trade_size,
                             unmatched_open, unmatched_close, unmatched_gross, unmatched_net, broker]
                            )                 
                ################################# begin COMMISSIONS section #################################
                # fx_comm_ymd_lst contains year-month-date formatted dates for the commissions logs
                fx_comm_ymd_lst = []

                # fx_comm_yr_lst contains formatted year dates for the commissions logs
                fx_comm_yr_lst = []

                # fx_comm_mo_lst contains formatted month dates for the commissions logs
                fx_comm_mo_lst = []

                # fx_comm_day_lst contains formatted day ates for the commissions logs
                fx_comm_day_lst = []

                # extract and format the dates of the commission transaction to YYYY-MM-DD
                def fx_format_comm_date():
                    for item in comm_lst:
                        dmy = item[0]

                        # DD/MM/YYYY
                        if dmy[2] == '/' and dmy[5] == '/':
                            comm_yr = dmy[6:10]
                            comm_mo = dmy[3:5]
                            comm_day = dmy[:2]
                            comm_ymd = f'{comm_yr}-{comm_mo}-{comm_day}'
                            comm_yr = int(comm_yr)
                            comm_mo = int(comm_mo)
                            comm_day = int(comm_day)
                            fx_comm_ymd_lst.append(comm_ymd)
                            fx_comm_yr_lst.append(comm_yr)
                            fx_comm_mo_lst.append(comm_mo)
                            fx_comm_day_lst.append(comm_day)

                        # DD/M/YYYY
                        elif dmy[2] == '/' and dmy[4] == '/':
                            comm_yr = dmy[5:9]
                            comm_mo = dmy[3]
                            comm_day = dmy[:2]
                            comm_ymd = f'{comm_yr}-0{comm_mo}-{comm_day}'
                            comm_yr = int(comm_yr)
                            comm_mo = int(comm_mo)
                            comm_day = int(comm_day)
                            fx_comm_ymd_lst.append(comm_ymd)
                            fx_comm_yr_lst.append(comm_yr)
                            fx_comm_mo_lst.append(comm_mo)
                            fx_comm_day_lst.append(comm_day)

                        # D/MM/YYYY
                        elif dmy[1] == '/' and dmy[4] == '/':
                            comm_yr = dmy[5:9]
                            comm_mo = dmy[2:4]
                            comm_day = dmy[0]
                            comm_ymd = f'{comm_yr}-{comm_mo}-0{comm_day}'
                            comm_yr = int(comm_yr)
                            comm_mo = int(comm_mo)
                            comm_day = int(comm_day)
                            fx_comm_ymd_lst.append(comm_ymd)
                            fx_comm_yr_lst.append(comm_yr)
                            fx_comm_mo_lst.append(comm_mo)
                            fx_comm_day_lst.append(comm_day)

                        # D/M/YYYY
                        elif dmy[1] == '/' and dmy[3] == '/':
                            comm_yr = dmy[4:8]
                            comm_mo = dmy[2]
                            comm_day = dmy[0]
                            comm_ymd = f'{comm_yr}-0{comm_mo}-0{comm_day}'
                            comm_yr = int(comm_yr)
                            comm_mo = int(comm_mo)
                            comm_day = int(comm_day)
                            fx_comm_ymd_lst.append(comm_ymd)
                            fx_comm_yr_lst.append(comm_yr)
                            fx_comm_mo_lst.append(comm_mo)
                            fx_comm_day_lst.append(comm_day)

                fx_format_comm_date()

                # fx_comm_transid_lst contains the transaction ids for the commissions logs
                fx_comm_transid_lst = []

                # add and format the transaction ids commissions logs
                def fx_comm_add_transid():
                    for item in comm_lst:
                        trans_id = int(item[3])
                        fx_comm_transid_lst.append(trans_id)

                fx_comm_add_transid()

                # fx_comm_cost_lst contains a list of the commissions cost
                fx_comm_cost_lst = []

                # add and format the commissioin costs
                def fx_comm_cost():
                    for item in comm_lst:
                        comm_cost = float(item[12][0:7])
                        fx_comm_cost_lst.append(comm_cost)

                fx_comm_cost()

                # contains the uniquely formatted transaction numbers for the commissions logs
                fx_comm_transnum_lst = []

                # create a unique transaction id for the commissions logs
                # use fx_comm_ymd_lst to create the key becuase the dates have gone through formatting
                def fx_comm_create_trans_num():
                    for date, id in zip(fx_comm_ymd_lst,fx_comm_transid_lst):
                        id = str(id)
                        comm_unique_key = f'{date[:2]}{date[5:7]}{date[8:10]}{id[-4::]}'
                        comm_unique_key = int(comm_unique_key)
                        fx_comm_transnum_lst.append(comm_unique_key)

                fx_comm_create_trans_num()

                # comm_lst2 contains the entrie commissions logs
                comm_lst2 = []

                # create the commissions log
                def fx_comm_format_logs():
                    for date,year,month,day,transid,comm_cost,broker,transnum \
                    in zip(fx_comm_ymd_lst,fx_comm_yr_lst,fx_comm_mo_lst,fx_comm_day_lst, \
                           fx_comm_transid_lst,fx_comm_cost_lst,broker_id_lst,fx_comm_transnum_lst
                           ):
                        broker_id_lst.append(broker_id)
                        comm_lst2.append([date,year,month,day,transid,comm_cost,broker,transnum])

                fx_comm_format_logs()

                ################################# begin FINANCING section #################################
                # fx_int_debit_ymd_lst contains the formatted YYYY-MM-DD for the debit interest logs
                fx_int_debit_ymd_lst = []

                # fx_int_debit_yr_lst contains the formatted year for the debit interest logs
                fx_int_debit_yr_lst = []

                # fx_int_debit_mo_lst contains the formatted mo for the debit interest logs
                fx_int_debit_mo_lst = []

                # fx_int_debit_day_lst contains the formatted day for the debit interest logs
                fx_int_debit_day_lst = []

                # extract and format the dates of the debit interest transaction to YYYY-MM-DD
                def fx_int_debit_format_date():
                    for item in int_lst:
                        int_item = item[12][:7]
                        int_item = float(int_item)
                        dmy = item[0]
                        if int_item < 0:

                            # DD/MM/YYYY
                            if dmy[2] == '/' and dmy[5] == '/':
                                int_debit_yr = dmy[6:10]
                                int_debit_mo = dmy[3:5]
                                int_debit_day = dmy[:2]
                                int_debit_ymd = f'{int_debit_yr}-{int_debit_mo}-{int_debit_day}'
                                int_debit_yr = int(int_debit_yr)
                                int_debit_mo = int(int_debit_mo)
                                int_debit_day = int(int_debit_day)
                                fx_int_debit_ymd_lst.append(int_debit_ymd)
                                fx_int_debit_yr_lst.append(int_debit_yr)
                                fx_int_debit_mo_lst.append(int_debit_mo)
                                fx_int_debit_day_lst.append(int_debit_day)

                            # DD/M/YYYY
                            elif dmy[2] == '/' and dmy[4] == '/':
                                int_debit_yr = dmy[5:9]
                                int_debit_mo = dmy[3]
                                int_debit_day = dmy[:2]
                                int_debit_ymd = f'{int_debit_yr}-0{int_debit_mo}-{int_debit_day}'
                                int_debit_yr = int(int_debit_yr)
                                int_debit_mo = int(int_debit_mo)
                                int_debit_day = int(int_debit_day)
                                fx_int_debit_ymd_lst.append(int_debit_ymd)
                                fx_int_debit_yr_lst.append(int_debit_yr)
                                fx_int_debit_mo_lst.append(int_debit_mo)
                                fx_int_debit_day_lst.append(int_debit_day)

                            # D/MM/YYYY
                            elif dmy[1] == '/' and dmy[4] == '/':
                                int_debit_yr = dmy[5:9]
                                int_debit_mo = dmy[2:4]
                                int_debit_day = dmy[0]
                                int_debit_ymd = f'{int_debit_yr}-{int_debit_mo}-0{int_debit_day}'
                                int_debit_yr = int(int_debit_yr)
                                int_debit_mo = int(int_debit_mo)
                                int_debit_day = int(int_debit_day)
                                fx_int_debit_ymd_lst.append(int_debit_ymd)
                                fx_int_debit_yr_lst.append(int_debit_yr)
                                fx_int_debit_mo_lst.append(int_debit_mo)
                                fx_int_debit_day_lst.append(int_debit_day)

                            # D/M/YYYY
                            elif dmy[1] == '/' and dmy[3] == '/':
                                int_debit_yr = dmy[4:8]
                                int_debit_mo = dmy[2]
                                int_debit_day = dmy[0]
                                int_debit_ymd = f'{int_debit_yr}-0{int_debit_mo}-0{int_debit_day}'
                                int_debit_yr = int(int_debit_yr)
                                int_debit_mo = int(int_debit_mo)
                                int_debit_day = int(int_debit_day)
                                fx_int_debit_ymd_lst.append(int_debit_ymd)
                                fx_int_debit_yr_lst.append(int_debit_yr)
                                fx_int_debit_mo_lst.append(int_debit_mo)
                                fx_int_debit_day_lst.append(int_debit_day)

                fx_int_debit_format_date()

                # fx_int_debit_transid_lst contains transaction ids for the debit interest logs
                fx_int_debit_transid_lst = []

                # add the transaction ids for the debit interest logs
                def fx_int_debit_add_transid():
                    for item in int_lst:
                        int_item = item[12][:7]
                        int_item = float(int_item)
                        if int_item < 0:
                            transid = item[3]
                            transid = int(transid)
                            fx_int_debit_transid_lst.append(transid)

                fx_int_debit_add_transid()

                # contains the debit interest cost logs
                fx_int_debit_cost_lst = []

                # add the debit interest costs
                def fx_int_debit_add_cost():
                    for item in int_lst:
                        int_item = item[12][:7]
                        int_item = float(int_item)
                        if int_item < 0:
                            fx_int_debit_cost_lst.append(int_item)

                fx_int_debit_add_cost()

                # contains the unique identifiers for the debit interest items
                fx_int_debit_transnum_lst = []

                # create unique identifier transaction number
                # use fx_int_debit_ymd_lst to build the unique num since it has the properly formatted dates
                def fx_int_debit_create_transnum():
                    for date, id in zip(fx_int_debit_ymd_lst,fx_int_debit_transid_lst):
                        id = str(id)
                        int_debit_unique_key = f'{date[:2]}{date[5:7]}{date[8:10]}{id[-4::]}'
                        int_debit_unique_key = int(int_debit_unique_key)
                        fx_int_debit_transnum_lst.append(int_debit_unique_key)

                fx_int_debit_create_transnum()

                # int_debit_lst contains the final debit interest logs
                int_debit_lst = []

                # create the debit interest logs
                def fx_int_debit_format_logs():
                    for date,year,month,day,transid,int_debit,broker,transnum \
                    in zip(fx_int_debit_ymd_lst,fx_int_debit_yr_lst,fx_int_debit_mo_lst, \
                           fx_int_debit_day_lst,fx_int_debit_transid_lst,fx_int_debit_cost_lst, \
                           broker_id_lst,fx_int_debit_transnum_lst \
                           ):
                        broker_id_lst.append(broker_id)
                        int_debit_lst.append([date,year,month,day,transid,int_debit,broker,transnum])

                fx_int_debit_format_logs()

                ################################# begin interest credit section #################################
                # fx_int_credit_ymd_lst contains the formatted YYYY-MM-DD for the credit interest logs
                fx_int_credit_ymd_lst = []

                # fx_int_credit_yr_lst contains the formatted year for the credit interest logs
                fx_int_credit_yr_lst = []

                # fx_int_credit_mo_lst contains the formatted mo for the credit interest logs
                fx_int_credit_mo_lst = []

                # fx_int_credit_day_lst contains the formatted day for the credit interest logs
                fx_int_credit_day_lst = []

                # extract and format the dates of the interest credit transaction to YYYY-MM-DD
                def fx_int_credit_format_date():
                    for item in int_lst:
                        int_item = item[12][:7]
                        int_item = float(int_item)
                        dmy = item[0]
                        if int_item > 0:

                            # DD/MM/YYYY
                            if dmy[2] == '/' and dmy[5] == '/':
                                int_credit_yr = dmy[6:10]
                                int_credit_mo = dmy[3:5]
                                int_credit_day = dmy[:2]
                                int_credit_ymd = f'{int_credit_yr}-{int_credit_mo}-{int_credit_day}'
                                int_credit_yr = int(int_credit_yr)
                                int_credit_mo = int(int_credit_mo)
                                int_credit_day = int(int_credit_day)
                                fx_int_credit_ymd_lst.append(int_credit_ymd)
                                fx_int_credit_yr_lst.append(int_credit_yr)
                                fx_int_credit_mo_lst.append(int_credit_mo)
                                fx_int_credit_day_lst.append(int_credit_day)

                            # DD/M/YYYY
                            elif dmy[2] == '/' and dmy[4] == '/':
                                int_credit_yr = dmy[5:9]
                                int_credit_mo = dmy[3]
                                int_credit_day = dmy[:2]
                                int_credit_ymd = f'{int_credit_yr}-0{int_credit_mo}-{int_credit_day}'
                                int_credit_yr = int(int_credit_yr)
                                int_credit_mo = int(int_credit_mo)
                                int_credit_day = int(int_credit_day)
                                fx_int_credit_ymd_lst.append(int_credit_ymd)
                                fx_int_credit_yr_lst.append(int_credit_yr)
                                fx_int_credit_mo_lst.append(int_credit_mo)
                                fx_int_credit_day_lst.append(int_credit_day)

                            # D/MM/YYYY
                            elif dmy[1] == '/' and dmy[4] == '/':
                                int_credit_yr = dmy[5:9]
                                int_credit_mo = dmy[2:4]
                                int_credit_day = dmy[0]
                                int_credit_ymd = f'{int_credit_yr}-{int_credit_mo}-0{int_credit_day}'
                                int_credit_yr = int(int_credit_yr)
                                int_credit_mo = int(int_credit_mo)
                                int_credit_day = int(int_credit_day)
                                fx_int_credit_ymd_lst.append(int_credit_ymd)
                                fx_int_credit_yr_lst.append(int_credit_yr)
                                fx_int_credit_mo_lst.append(int_credit_mo)
                                fx_int_credit_day_lst.append(int_credit_day)

                            # D/M/YYYY
                            elif dmy[1] == '/' and dmy[3] == '/':
                                int_credit_yr = dmy[4:8]
                                int_credit_mo = dmy[2]
                                int_credit_day = dmy[0]
                                int_credit_ymd = f'{int_credit_yr}-0{int_credit_mo}-0{int_credit_day}'
                                int_credit_yr = int(int_credit_yr)
                                int_credit_mo = int(int_credit_mo)
                                int_credit_day = int(int_credit_day)
                                fx_int_credit_ymd_lst.append(int_credit_ymd)
                                fx_int_credit_yr_lst.append(int_credit_yr)
                                fx_int_credit_mo_lst.append(int_credit_mo)
                                fx_int_credit_day_lst.append(int_credit_day)

                fx_int_credit_format_date()


                # fx_int_credit_transid_lst contains transaction ids for the credit interest logs
                fx_int_credit_transid_lst = []

                # add the transaction ids for the credit interest logs
                def fx_int_credit_add_transid():
                    for item in int_lst:
                        int_item = item[12][:7]
                        int_item = float(int_item)
                        if int_item > 0:
                            transid = item[3]
                            transid = int(transid)
                            fx_int_credit_transid_lst.append(transid)

                fx_int_credit_add_transid()

                # contains the credit interest logs
                fx_int_credit_gain_lst = []

                # add the credit interest logs
                def fx_int_credit_add_gain():
                    for item in int_lst:
                        int_item = item[12][:7]
                        int_item = float(int_item)
                        if int_item > 0:
                            fx_int_credit_gain_lst.append(int_item)

                fx_int_credit_add_gain()


                # contains the unique identifiers for the credit interest items
                fx_int_credit_transnum_lst = []

                # create unique identifier transaction number
                # use fx_int_credit_ymd_lst to build the unique num since it has the properly formatted dates
                def fx_int_credit_create_transnum():
                    for date, id in zip(fx_int_credit_ymd_lst,fx_int_credit_transid_lst):
                        id = str(id)
                        int_credit_unique_key = f'{date[:2]}{date[5:7]}{date[8:10]}{id[-4::]}'
                        int_credit_unique_key = int(int_credit_unique_key)
                        fx_int_credit_transnum_lst.append(int_credit_unique_key)

                fx_int_credit_create_transnum()

                # int_credit_lst contains the final credit interest logs
                int_credit_lst = []

                # create the credit interest logs
                def fx_int_credit_format_logs():
                    for date,year,month,day,transid,int_credit,broker,transnum \
                    in zip(fx_int_credit_ymd_lst,fx_int_credit_yr_lst,fx_int_credit_mo_lst, \
                           fx_int_credit_day_lst,fx_int_credit_transid_lst,fx_int_credit_gain_lst, \
                           broker_id_lst,fx_int_credit_transnum_lst \
                           ):
                        broker_id_lst.append(broker_id)
                        int_credit_lst.append([date,year,month,day,transid,int_credit,broker,transnum])

                fx_int_credit_format_logs()

                ################################# begin broker credit section #################################
                # fx_bkr_credit_ymd_lst contains year-month-date formatted dates for the broker credit logs
                fx_bkr_credit_ymd_lst = []

                # fx_bkr_credit_yr_lst contains formatted year dates for the broker credit logs
                fx_bkr_credit_yr_lst = []

                # fx_bkr_credit_mo_lst contains formatted month dates for the broker credit logs
                fx_bkr_credit_mo_lst = []

                # fx_bkr_credit_day_lst contains formatted day ates for the broker credit logs
                fx_bkr_credit_day_lst = []

                # extract and format the dates of the broker credit transactions to YYYY-MM-DD
                def fx_broker_credit_format_date():
                    for item in broker_credit_lst:
                        dmy = item[0]

                        # DD/MM/YYYY
                        if dmy[2] == '/' and dmy[5] == '/':
                            broker_credit_yr = dmy[6:10]
                            broker_credit_mo = dmy[3:5]
                            broker_credit_day = dmy[:2]
                            broker_credit_ymd = f'{broker_credit_yr}-{broker_credit_mo}-{broker_credit_day}'
                            broker_credit_yr = int(broker_credit_yr)
                            broker_credit_mo = int(broker_credit_mo)
                            broker_credit_day = int(broker_credit_day)
                            fx_bkr_credit_ymd_lst.append(broker_credit_ymd)
                            fx_bkr_credit_yr_lst.append(broker_credit_yr)
                            fx_bkr_credit_mo_lst.append(broker_credit_mo)
                            fx_bkr_credit_day_lst.append(broker_credit_day)

                        # DD/M/YYYY
                        elif dmy[2] == '/' and dmy[4] == '/':
                            broker_credit_yr = dmy[5:9]
                            broker_credit_mo = dmy[3]
                            broker_credit_day = dmy[:2]
                            broker_credit_ymd = f'{broker_credit_yr}-0{broker_credit_mo}-{broker_credit_day}'
                            broker_credit_yr = int(broker_credit_yr)
                            broker_credit_mo = int(broker_credit_mo)
                            broker_credit_day = int(broker_credit_day)
                            fx_bkr_credit_ymd_lst.append(broker_credit_ymd)
                            fx_bkr_credit_yr_lst.append(broker_credit_yr)
                            fx_bkr_credit_mo_lst.append(broker_credit_mo)
                            fx_bkr_credit_day_lst.append(broker_credit_day)

                        # D/MM/YYYY
                        elif dmy[1] == '/' and dmy[4] == '/':
                            broker_credit_yr = dmy[5:9]
                            broker_credit_mo = dmy[2:4]
                            broker_credit_day = dmy[0]
                            broker_credit_ymd = f'{broker_credit_yr}-{broker_credit_mo}-0{broker_credit_day}'
                            broker_credit_yr = int(broker_credit_yr)
                            broker_credit_mo = int(broker_credit_mo)
                            broker_credit_day = int(broker_credit_day)
                            fx_bkr_credit_ymd_lst.append(broker_credit_ymd)
                            fx_bkr_credit_yr_lst.append(broker_credit_yr)
                            fx_bkr_credit_mo_lst.append(broker_credit_mo)
                            fx_bkr_credit_day_lst.append(broker_credit_day)

                        # D/M/YYYY
                        elif dmy[1] == '/' and dmy[3] == '/':
                            broker_credit_yr = dmy[4:8]
                            broker_credit_mo = dmy[2]
                            broker_credit_day = dmy[0]
                            broker_credit_ymd = f'{broker_credit_yr}-0{broker_credit_mo}-0{broker_credit_day}'
                            broker_credit_yr = int(broker_credit_yr)
                            broker_credit_mo = int(broker_credit_mo)
                            broker_credit_day = int(broker_credit_day)
                            fx_bkr_credit_ymd_lst.append(broker_credit_ymd)
                            fx_bkr_credit_yr_lst.append(broker_credit_yr)
                            fx_bkr_credit_mo_lst.append(broker_credit_mo)
                            fx_bkr_credit_day_lst.append(broker_credit_day)

                fx_broker_credit_format_date()

                # fx_bkr_credit_gain_lst contains a list of the broker credits
                fx_bkr_credit_gain_lst = []

                # add and format the broker credits
                def fx_bkr_credit_add_gain():
                    for item in broker_credit_lst:
                        credit_received = item[12]
                        credit_received = float(credit_received)
                        fx_bkr_credit_gain_lst.append(credit_received)

                fx_bkr_credit_add_gain()

                # fx_bkr_credit_transnum_lst contains the unique transaction numbers for the broker credit logs
                fx_bkr_credit_transnum_lst = []

                # create transaction numbers broker credit logs
                def fx_bkr_credit_create_transnum():
                    for date, num in zip(fx_bkr_credit_ymd_lst,fx_bkr_credit_gain_lst):
                        num = str(num)
                        num = num.split('.')
                        bkr_credit_unique_key = f'{date[:2]}{date[5:7]}{date[8:10]}{num[0]}{num[1]}'
                        bkr_credit_unique_key = int(bkr_credit_unique_key)
                        fx_bkr_credit_transnum_lst.append(bkr_credit_unique_key)

                fx_bkr_credit_create_transnum()

                # broker_credit_lst2 contains the final formatted list of the broker credit transactions
                broker_credit_lst2 = []

                # create the commissions log
                def fx_broker_credit_format_logs():
                    for date,year,month,day,broker_credit,broker,transnum \
                    in zip(fx_bkr_credit_ymd_lst,fx_bkr_credit_yr_lst,fx_bkr_credit_mo_lst, \
                            fx_bkr_credit_day_lst,fx_bkr_credit_gain_lst,broker_id_lst, \
                            fx_bkr_credit_transnum_lst \
                           ):
                        broker_id_lst.append(broker_id)
                        broker_credit_lst2.append([date,year,month,day,broker_credit,broker,transnum])

                fx_broker_credit_format_logs()

                # print matched trade transactions
                def fxlog_print_records(lst):
                    print("\n---------fx logs---------------")
                    for log in lst:
                        print(log)
                # fxlog_print_records(fxlog_lst_2)

                # print unmatched trade transactions
                def fxlog_print_unmatched_records(lst1):
                    print("\n---------fx unmatched logs---------------")
                    for log in lst1:
                        print(log)
                # fxlog_print_unmatched_records(unmatched_fxlog)

                # print commission records
                def fx_comm_print_records(lst):
                    print("------------fx commissions------------------")
                    for log in lst:
                        print(log)
                # fx_comm_print_records(comm_lst2)

                # print debit interest records
                def fx_int_debit_print_records(lst):
                    print("------------fx interest debit ------------------")
                    for log in lst:
                        print(log)
                # fx_int_debit_print_records(int_debit_lst)

                # print credit interest records
                def fx_int_credit_print_records(lst):
                    print("------------fx interest credit ------------------")
                    for log in lst:
                        print(log)
                # fx_int_credit_print_records(int_credit_lst)

                # print broker credit interest records
                def fx_broker_credit_print_records(lst):
                    print("------------fx broker credit ------------------")
                    for log in lst:
                        print(log)
                # fx_broker_credit_print_records(broker_credit_lst2)

                # function exports the trade transaction records to the log_metrics_app.py app
                def fxlog_export_records():
                    print("----------test: fxlog_export_records() func------------------")
                    return fxlog_lst_2

                # function exports unmatched trade transaction records to the log_metrics_app.py app
                def fx_unmatched_export_records():
                    return unmatched_fxlog

                # function exports the commission transaction records to the log_metrics_app.py app
                def fx_comm_export_records():
                    return comm_lst2

                # function exports the interest debit transaction records to the log_metrics_app.py app
                def fx_int_debit_export_records():
                    return int_debit_lst

                # function exports the interest credit transaction records to the log_metrics_app.py app
                def fx_int_credit_export_records():
                    return int_credit_lst

                # function exports the broker credit records to log_metrics_app.py app
                def fx_broker_credit_export_records():
                    return broker_credit_lst2

            else:
                print(f'{filename} is not a .csv file...')
                print("Exiting fx upload...\n")
                pass
        else:
            print(filename,'does not exist.')
            print("Exiting fx upload...\n")
            pass
    else:
        print("No fx .csv files uploaded")
        print("Exiting fx upload...\n")
        pass
else:
    print("Exiting fx upload...\n")
    pass
