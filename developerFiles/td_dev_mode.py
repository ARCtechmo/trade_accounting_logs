### UNDER DEVELOPMENT ###
# this app imports and cleans the .csv files from the equity options broker 1
import csv
import re
import os.path
from pathlib import Path

# confirm working directory
print("\nThis is the TD options broker app that formats and exports the .csv file")
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
        broker_id = 5

        # buy_sell_remove_lst contains all buy, sell, and removal transactions
        buy_sell_remove_lst = []

        # int_income_lst contains the interest earned transactions
        int_lst = []

        # misc_lst contains the miscellaneous transactions
        misc_lst = []

        # input the .csv filename
        filename = input("enter the entire .csv filename including the extension (example: test_file.csv): ")
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
                            if row[2][:4] == 'Sold' or row[2][:6] == 'Bought' or row[2][:7] == 'REMOVAL':
                                buy_sell_remove_lst.append(row)
                            elif 'MISCELLANEOUS' in row[2]:
                                misc_lst.append(row)
                            elif 'FREE' in row[2] or 'INTEREST' in row[2]:
                                int_lst.append(row)
                            else:
                                pass

                elif header_option == "Y" or header_option == 'y' or header_option == "Yes" or \
                     header_option == 'yes' or header_option =='YES' or header_option == 'YEs' or \
                     header_option == 'YeS' or header_option == 'yES' or header_option == 'yeS' or \
                     header_option == 'yEs':
                     with open(filename, newline='') as csvfile:
                         reader = csv.reader(csvfile)
                         next(csvfile)
                         for row in reader:
                             if row[2][:4] == 'Sold' or row[2][:6] == 'Bought' or row[2][:7] == 'REMOVAL':
                                 buy_sell_remove_lst.append(row)
                             elif 'MISCELLANEOUS' in row[2]:
                                 misc_lst.append(row)
                             elif 'FREE' in row[2] or 'INTEREST' in row[2]:
                                 int_lst.append(row)
                             else:
                                 pass
                else:
                    print("Invalid input. No logs imported.")
                    pass

                # options_lst contains all rows with options transactions
                options_lst = []

                # comm_lst contains all of the commissions
                comm_lst = []

                # reg_fee_lst contains all of the regulation fees
                reg_fee_lst = []

                for row in buy_sell_remove_lst:
                    if row[2][:7] == 'REMOVAL':
                        options_lst.append(row[:6])
                    elif row[4][-3:] == 'Put' or row[4][-4:] == "Call":
                        options_lst.append([row[0],row[1],row[2],row[3],row[4],row[5],row[7]])
                        comm_lst.append([row[0],row[1],row[6]])
                        reg_fee_lst.append([row[0],row[1],row[8]])

                # misc_income_lst contains the miscellaneous income transactions
                misc_income_lst = []

                # misc_income_lst contains the miscellaneous income transactions
                misc_debit_lst = []

                for row in misc_lst:
                    if float(row[7]) >=0:
                        row[7] = float(row[7])
                        misc_income_lst.append([row[0],row[1],row[2],row[7]])
                    elif float(row[7]) <0:
                        row[7] = float(row[7])
                        misc_debit_lst.append([row[0],row[1],row[2],row[7]])

                # int_income_lst contains the interest earned transactions
                int_income_lst = []

                # int_income_lst contains the interest earned transactions
                int_debit_lst = []

                for row in int_lst:
                    if float(row[7]) >=0:
                        row[7] = float(row[7])
                        int_income_lst.append([row[0],row[1],row[2],row[7]])
                    elif float(row[7]) <0:
                        row[7] = float(row[7])
                        int_debit_lst.append([row[0],row[1],row[2],row[7]])

                # options_lst2 contains all rows with options transactions with properly formatted dates
                options_lst2 = []

                # options_date_format() function formats all of the dates to YYYY-MM-DD for the option transactions
                def options_date_format():
                    for row in options_lst:

                        # M/DD/YYYY
                        if row[0][1] == '/' and row[0][4] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2:4]
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[3] = int(row[3])
                            if row[2][0] == 'B' or row[2][0] == 'S':
                                row[5] = float(row[5])
                                row[6] = float(row[6])
                                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],row[5],row[6]])
                            elif row[2][0] == 'R':
                                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],0.00,0.00])

                        # M/D/YYYY
                        elif row[0][1] == '/' and row[0][3] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][4:8]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[3] = int(row[3])
                            if row[2][0] == 'B' or row[2][0] == 'S':
                                row[5] = float(row[5])
                                row[6] = float(row[6])
                                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],row[5],row[6]])
                            elif row[2][0] == 'R':
                                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],0.00,0.00])

                        # MM/D/YYYY
                        elif row[0][2] == '/' and row[0][4] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[3] = int(row[3])
                            if row[2][0] == 'B' or row[2][0] == 'S':
                                row[5] = float(row[5])
                                row[6] = float(row[6])
                                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],row[5],row[6]])
                            elif row[2][0] == 'R':
                                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],0.00,0.00])

                        # MM/DD/YYYY
                        elif row[0][2] == '/' and row[0][5] == '/':
                            trans_yr = row[0][6:10]
                            trans_mo = row[0][:2]
                            trans_day = row[0][3:5]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[3] = int(row[3])
                            if row[2][0] == 'B' or row[2][0] == 'S':
                                row[5] = float(row[5])
                                row[6] = float(row[6])
                                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],row[5],row[6]])
                            elif row[2][0] == 'R':
                                options_lst2.append([formatted_date,row[1],row[2],row[3],row[4],0.00,0.00])

                options_date_format()

                # comm_lst2 contains all rows with commission transactions and properly formatted dates
                comm_lst2 = []

                # comm_date_format() function formats the dates to YYYY-MM-DD for the commission transactions
                def comm_date_format():
                    for row in comm_lst:

                        # M/DD/YYYY
                        if row[0][1] == '/' and row[0][4] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2:4]
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[2] = float(row[2])
                            comm_lst2.append([formatted_date,row[1],row[2]])

                        # M/D/YYYY
                        elif row[0][1] == '/' and row[0][3] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][4:8]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[2] = float(row[2])
                            comm_lst2.append([formatted_date,row[1],row[2]])

                        # MM/D/YYYY
                        elif row[0][2] == '/' and row[0][4] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[2] = float(row[2])
                            comm_lst2.append([formatted_date,row[1],row[2]])

                        # MM/DD/YYYY
                        elif row[0][2] == '/' and row[0][5] == '/':
                            trans_yr = row[0][6:10]
                            trans_mo = row[0][:2]
                            trans_day = row[0][3:5]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[2] = float(row[2])
                            comm_lst2.append([formatted_date,row[1],row[2]])

                comm_date_format()

                # reg_fee_lst2 contains all rows with regulation fee transactions and properly formatted dates
                reg_fee_lst2 = []

                # reg_fee_date_format() function formats the dates to YYYY-MM-DD for the regulation fee transactions
                def reg_fee_date_format():
                    for row in reg_fee_lst:

                        # M/DD/YYYY
                        if row[0][1] == '/' and row[0][4] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2:4]
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[2] = float(row[2])
                            reg_fee_lst2.append([formatted_date,row[1],row[2]])

                        # M/D/YYYY
                        elif row[0][1] == '/' and row[0][3] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][4:8]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[2] = float(row[2])
                            reg_fee_lst2.append([formatted_date,row[1],row[2]])

                        # MM/D/YYYY
                        elif row[0][2] == '/' and row[0][4] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[2] = float(row[2])
                            reg_fee_lst2.append([formatted_date,row[1],row[2]])

                        # MM/DD/YYYY
                        elif row[0][2] == '/' and row[0][5] == '/':
                            trans_yr = row[0][6:10]
                            trans_mo = row[0][:2]
                            trans_day = row[0][3:5]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            row[2] = float(row[2])
                            reg_fee_lst2.append([formatted_date,row[1],row[2]])

                reg_fee_date_format()

                # misc_income_lst2 contains the miscellaneous income transactions with properly formatted dates
                misc_income_lst2 = []

                # misc_income_date_format() function formats the dates to YYYY-MM-DD for the miscellaneous fee transactions
                def misc_income_date_format():
                    for row in misc_income_lst:

                        # M/DD/YYYY
                        if row[0][1] == '/' and row[0][4] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2:4]
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            misc_income_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # M/D/YYYY
                        elif row[0][1] == '/' and row[0][3] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][4:8]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            misc_income_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # MM/D/YYYY
                        elif row[0][2] == '/' and row[0][4] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            misc_income_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # MM/DD/YYYY
                        elif row[0][2] == '/' and row[0][5] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3:5]
                            trans_yr = row[0][6:10]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            misc_income_lst2.append([formatted_date,row[1],row[2],row[3]])

                misc_income_date_format()

                # misc_debit_lst2 contains the miscellaneous debit transactions with properly formatted dates
                misc_debit_lst2 = []

                # misc_debit_date_format() function formats the dates to YYYY-MM-DD for the miscellaneous fee transactions
                def misc_debit_date_format():
                    for row in misc_debit_lst:

                        # M/DD/YYYY
                        if row[0][1] == '/' and row[0][4] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2:4]
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            misc_debit_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # M/D/YYYY
                        elif row[0][1] == '/' and row[0][3] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][4:8]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            misc_debit_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # MM/D/YYYY
                        elif row[0][2] == '/' and row[0][4] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            misc_debit_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # MM/DD/YYYY
                        elif row[0][2] == '/' and row[0][5] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3:5]
                            trans_yr = row[0][6:10]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            misc_debit_lst2.append([formatted_date,row[1],row[2],row[3]])

                misc_debit_date_format()

                # int_income_lst2 contains the interest income transactions with properly formatted dates
                int_income_lst2 = []

                # int_income_date_format() function formats the dates to YYYY-MM-DD for the interest income transactions
                def int_income_date_format():

                    for row in int_income_lst:

                        # M/DD/YYYY
                        if row[0][1] == '/' and row[0][4] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2:4]
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            int_income_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # M/D/YYYY
                        elif row[0][1] == '/' and row[0][3] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][4:8]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            int_income_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # MM/D/YYYY
                        elif row[0][2] == '/' and row[0][4] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            int_income_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # MM/DD/YYYY
                        elif row[0][2] == '/' and row[0][5] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3:5]
                            trans_yr = row[0][6:10]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            int_income_lst2.append([formatted_date,row[1],row[2],row[3]])

                int_income_date_format()

                # int_debit_lst2 contains the interest debit transactions with properly formatted dates
                int_debit_lst2 = []

                # int_debit_date_format() function formats the dates to YYYY-MM-DD for the interest debit transactions
                def int_debit_date_format():

                    for row in int_debit_lst:

                        # M/DD/YYYY
                        if row[0][1] == '/' and row[0][4] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2:4]
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            int_debit_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # M/D/YYYY
                        elif row[0][1] == '/' and row[0][3] == '/':
                            trans_mo = row[0][0]
                            trans_mo = f'0{trans_mo}'
                            trans_day = row[0][2]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][4:8]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            int_debit_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # MM/D/YYYY
                        elif row[0][2] == '/' and row[0][4] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3]
                            trans_day = f'0{trans_day}'
                            trans_yr = row[0][5:9]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            int_debit_lst2.append([formatted_date,row[1],row[2],row[3]])

                        # MM/DD/YYYY
                        elif row[0][2] == '/' and row[0][5] == '/':
                            trans_mo = row[0][:2]
                            trans_day = row[0][3:5]
                            trans_yr = row[0][6:10]
                            formatted_date = f'{trans_yr}-{trans_mo}-{trans_day}'
                            row[1] = int(row[1])
                            int_debit_lst2.append([formatted_date,row[1],row[2],row[3]])

                int_debit_date_format()

                # options_lst3 contains the options log records along with another unique transaction number
                options_lst3 = []

                # options_add_trans_num() formats the log, adds the broker id, and creates a unique transaction number for each options log record
                def format_options_log():
                    for row in options_lst2:
                        # print(row)
                        trans_date = row[0]
                        row[1] = str(row[1])
                        trans_num = f'{row[0][2:4]}{row[0][5:7]}{row[0][8:10]}{row[1][-6:]}'
                        trans_num = int(trans_num)
                        trans_yr = int(row[0][:4])
                        trans_mo = int(row[0][5:7])
                        trans_day = int(row[0][8:10])
                        trans_id = int(row[1])
                        trade_size = row[3]
                        ctr = row[4]
                        price = float(row[5])
                        gross = float(row[6])

                        if row[2][:6] == 'Bought':
                            # print(row)
                            if row[4][3] == ' ' and row[4][-4:] == 'Call':
                                mkt = row[4][:3]
                                call = row[4][-4:]
                                trans_bought = row[2][:6]
                                options_lst3.append([trans_date,trans_yr,trans_mo,trans_day,trans_id,trans_bought,trade_size,mkt,call,ctr,price,gross,broker_id,trans_num])

                            elif row[4][4] == ' ' and row[4][-4:] == 'Call':
                                mkt = row[4][:4]
                                call = row[4][-4:]
                                trans_bought = row[2][:6]
                                options_lst3.append([trans_date,trans_yr,trans_mo,trans_day,trans_id,trans_bought,trade_size,mkt,call,ctr,price,gross,broker_id,trans_num])

                            elif row[4][3] == ' ' and row[4][-3:] == 'Put':
                                mkt = row[4][:3]
                                put = row[4][-3:]
                                trans_bought = row[2][:6]
                                options_lst3.append([trans_date,trans_yr,trans_mo,trans_day,trans_id,trans_bought,trade_size,mkt,put,ctr,price,gross,broker_id,trans_num])

                            elif row[4][4] == ' ' and row[4][-3:] == 'Put':
                                mkt = row[4][:4]
                                put = row[4][-3:]
                                trans_bought = row[2][:6]
                                options_lst3.append([trans_date,trans_yr,trans_mo,trans_day,trans_id,trans_bought,trade_size,mkt,put,ctr,price,gross,broker_id,trans_num])

                        elif row[2][:4] == 'Sold':
                            if row[4][3] == ' ' and row[4][-4:] == 'Call':
                                mkt = row[4][:3]
                                call = row[4][-4:]
                                trans_sold = row[2][:4]
                                options_lst3.append([trans_date,trans_yr,trans_mo,trans_day,trans_id,trans_sold,trade_size,mkt,call,ctr,price,gross,broker_id,trans_num])

                            elif row[4][4] == ' ' and row[4][-4:] == 'Call':
                                mkt = row[4][:4]
                                call = row[4][-4:]
                                trans_sold = row[2][:4]
                                options_lst3.append([trans_date,trans_yr,trans_mo,trans_day,trans_id,trans_sold,trade_size,mkt,call,ctr,price,gross,broker_id,trans_num])

                            elif row[4][3] == ' ' and row[4][-3:] == 'Put':
                                mkt = row[4][:3]
                                put = row[4][-3:]
                                trans_sold = row[2][:4]
                                options_lst3.append([trans_date,trans_yr,trans_mo,trans_day,trans_id,trans_sold,trade_size,mkt,put,ctr,price,gross,broker_id,trans_num])

                            elif row[4][4] == ' ' and row[4][-3:] == 'Put':
                                mkt = row[4][:4]
                                put = row[4][-3:]
                                trans_sold = row[2][:4]
                                options_lst3.append([trans_date,trans_yr,trans_mo,trans_day,trans_id,trans_sold,trade_size,mkt,put,ctr,price,gross,broker_id,trans_num])

                        elif row[2][:7] == 'REMOVAL':
                            line = row[2]
                            regex = re.compile('([\(]|[\(\d])([A-Z]{3,4}|[A-Z]{3,4})')
                            mkt = regex.findall(line)
                            mkt = mkt[0][1]
                            regex2 = re.compile('(\d{3}|[A-Z]{1}[a-z]{2,3})(\))')
                            call_put = regex2.findall(line)
                            call_put = call_put[0][0]
                            price = 0.00
                            gross = 0.00
                            options_lst3.append([trans_date,trans_yr,trans_mo,trans_day,trans_id,'Expired',trade_size,mkt,call_put,ctr,price,gross,broker_id,trans_num])

                format_options_log()

                # comm_lst3 contains the commissions log records along with another unique transaction number
                comm_lst3 = []

                # format_comm_log() formats the log, adds the broker id, and creates a unique transaction number for each commission log record
                def format_comm_log():
                    for row in comm_lst2:
                        row[1] = str(row[1])
                        trans_num = f'{row[0][2:4]}{row[0][5:7]}{row[0][8:10]}{row[1][-6:]}'
                        trans_num = int(trans_num)
                        trans_yr = int(row[0][:4])
                        trans_mo = int(row[0][5:7])
                        trans_day = int(row[0][8:10])
                        trans_id = int(row[1])
                        comm_lst3.append([row[0],trans_yr,trans_mo,trans_day,trans_id,row[2],broker_id,trans_num])

                format_comm_log()

                # contains the regulation fee log records to be exported into the database
                reg_fee_lst3 = []

                # format_reg_fee_log() formats the log, adds the broker id, and creates a unique transaction number for each regulation fee log record
                def format_reg_fee_log():
                    for row in reg_fee_lst2:
                        row[1] = str(row[1])
                        trans_num = f'{row[0][2:4]}{row[0][5:7]}{row[0][8:10]}{row[1][-6:]}'
                        trans_num = int(trans_num)
                        trans_yr = int(row[0][:4])
                        trans_mo = int(row[0][5:7])
                        trans_day = int(row[0][8:10])
                        trans_id = int(row[1])
                        reg_fee_lst3.append([row[0],trans_yr,trans_mo,trans_day,trans_id,row[2],broker_id,trans_num])

                format_reg_fee_log()

                # contains the miscellaneous income log records to be exported into the database
                misc_income_lst3 = []

                # format_misc_income_log() formats the log, adds the broker id, and creates a unique transaction number for each miscellaneous log record
                def format_misc_income_log():
                    for row in misc_income_lst2:
                        row[1] = str(row[1])
                        trans_num = f'{row[0][2:4]}{row[0][5:7]}{row[0][8:10]}{row[1][-6:]}'
                        trans_num = int(trans_num)
                        trans_yr = int(row[0][:4])
                        trans_mo = int(row[0][5:7])
                        trans_day = int(row[0][8:10])
                        trans_id = int(row[1])
                        misc_income_lst3.append([row[0],trans_yr,trans_mo,trans_day,trans_id,row[3],broker_id,trans_num])

                format_misc_income_log()

                # contains the miscellaneous debit log records to be exported into the database
                misc_debit_lst3 = []

                # format_misc_debit_log() formats the log, adds the broker id, and creates a unique transaction number for each miscellaneous log record
                def format_misc_debit_log():
                    for row in misc_debit_lst2:
                        row[1] = str(row[1])
                        trans_num = f'{row[0][2:4]}{row[0][5:7]}{row[0][8:10]}{row[1][-6:]}'
                        trans_num = int(trans_num)
                        trans_yr = int(row[0][:4])
                        trans_mo = int(row[0][5:7])
                        trans_day = int(row[0][8:10])
                        trans_id = int(row[1])
                        misc_debit_lst3.append([row[0],trans_yr,trans_mo,trans_day,trans_id,row[3],broker_id,trans_num])

                format_misc_debit_log()

                # contains the interest income log records to be exported into the database
                int_income_lst3 = []

                # format_int_income_log() formats the log, adds the broker id, and creates a unique transaction number for each interest log record
                def format_int_income_log():
                    for row in int_income_lst2:
                        row[1] = str(row[1])
                        trans_num = f'{row[0][2:4]}{row[0][5:7]}{row[0][8:10]}{row[1][-6:]}'
                        trans_num = int(trans_num)
                        trans_yr = int(row[0][:4])
                        trans_mo = int(row[0][5:7])
                        trans_day = int(row[0][8:10])
                        trans_id = int(row[1])
                        int_income_lst3.append([row[0],trans_yr,trans_mo,trans_day,trans_id,row[3],broker_id,trans_num])

                format_int_income_log()

                # contains the interest debit log records to be exported into the database
                int_debit_lst3 = []

                # format_int_debit_log() formats the log, adds the broker id, and creates a unique transaction number for each interest log record
                def format_int_debit_log():
                    for row in int_debit_lst2:
                        row[1] = str(row[1])
                        trans_num = f'{row[0][2:4]}{row[0][5:7]}{row[0][8:10]}{row[1][-6:]}'
                        trans_num = int(trans_num)
                        trans_yr = int(row[0][:4])
                        trans_mo = int(row[0][5:7])
                        trans_day = int(row[0][8:10])
                        trans_id = int(row[1])
                        int_debit_lst3.append([row[0],trans_yr,trans_mo,trans_day,trans_id,row[3],broker_id,trans_num])

                format_int_debit_log()

                # export the options log data
                def options_log_export_records():
                    i = len(options_lst3)
                    logs = options_lst3[:i]
                    print('There are',len(logs),'records to be exported from the options_log_export_records() func')
                    return logs
                # options_log_export_records()

                # export the commissions log data
                def comm_log_export_records():
                    i = len(comm_lst3)
                    logs = comm_lst3[:i]
                    print('There are',len(logs),'records to be exported from the comm_log_export_records() func')
                    return logs
                # comm_log_export_records()

                # export the regulation fee log data
                def reg_fee_export_records():
                    i = len(reg_fee_lst3)
                    logs = reg_fee_lst3[:i]
                    print('There are',len(logs),'records to be exported from the reg_fee_export_records() func')
                    return logs
                # reg_fee_export_records()

                # export the miscellaneous income log data
                def misc_income_export_records():
                    i = len(misc_income_lst3)
                    logs = misc_income_lst3[:i]
                    print('There are',len(logs),'records to be exported from the misc_income_export_records() func')
                    return logs
                # misc_income_export_records()

                # export the miscellaneous debit log data
                def misc_debit_export_records():
                    i = len(misc_debit_lst3)
                    logs = misc_debit_lst3[:i]
                    print('There are',len(logs),'records to be exported from the misc_debit_export_records() func')
                    return logs
                # misc_debit_export_records()

                # export the interest income log data
                def int_income_export_records():
                    i = len(int_income_lst3)
                    logs = int_income_lst3[:i]
                    print('There are',len(logs),'records to be exported from the int_income_export_records() func')
                    return logs
                # int_income_export_records()

                # export the interest debit log data
                def int_debit_export_records():
                    i = len(int_debit_lst3)
                    logs = int_debit_lst3[:i]
                    print('There are',len(logs),'records to be exported from the int_debit_export_records() func')
                    return logs
                # int_debit_export_records()
            else:
                print(f'{filename} is not a .csv file...')
                print("Exiting fx upload...\n")
                pass
        else:
            print("No td options .csv files uploaded.")
            print("Exiting td options upload...\n")
            pass
    else:
        print("No td options .csv files uploaded.")
        print("Exiting td options upload...\n")
        pass
else:
    print("Exiting td options upload...\n")
    pass
