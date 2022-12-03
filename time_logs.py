## Under Development ##
# Use this file to create the time logs
import database
from datetime import datetime
from datetime import date
from datetime import time

# connect to the database
import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# start_time_lst contains a list of the start times
start_time_lst = []

# end_time_lst contains a list of the end times
end_time_lst = []

# time_log_lst
time_log_lst = []

create_start_record = input("Would you like to create a new entry time log?: ")
if create_start_record == 'Y' or create_start_record == 'y' or create_start_record == 'Yes' or create_start_record == 'yes' or \
    create_start_record == 'YES' or create_start_record == 'YEs' or create_start_record == 'YeS' or create_start_record == 'yES' or \
    create_start_record == 'yeS' or create_start_record == 'yEs':

        create_date_today = input("\nType 'Y' or hit enter to use today's date. Type 'N' to enter a date. Type any other key to exit: ")
        if create_date_today == '' or create_date_today == 'Y' or create_date_today == 'y' or create_date_today == 'Yes' or create_date_today == 'yes' or \
            create_date_today == 'YES' or create_date_today == 'YEs' or create_date_today == 'YeS' or create_date_today == 'yES' or \
            create_date_today == 'yeS' or create_date_today == 'yEs':

            hr = input("\nEnter the hour (HH) 0 <= HH <= 23 (e.g. 1:00 pm is '13'; 8:00 pm is '20'; 5:00 am is '05'): ")
            if hr.isnumeric() and len(hr) == 2 and int(hr) >= 0 and int(hr) <= 23:

                if int(hr) >= 1 and int(hr) <= 9:
                    print("\nYou entered",str(hr[1]),"AM.")

                    verify_hr = input("If this is correct type 'Y' or just hit enter: ")
                    if verify_hr == '' or verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                        verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                        verify_hr == 'yeS' or verify_hr == 'yEs':

                        while True:

                            min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                            if min.isnumeric() and len(min) == 2 and int(min) >= 0 and int(min) <= 59:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break

                            elif min.isnumeric() and len(min) == 1 and int(min) >= 0 and int(min) <= 9:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break

                            else:
                                print("Incorrect minutes format. Reenter the minutes.")
                                continue
                    else:
                        print("Incorrect hour. Exiting...")
                        pass

                elif int(hr) == 10 or int(hr) == 11:
                    print("\nYou entered",str(hr),"AM.")

                    verify_hr = input("If this is correct type 'Y' or just hit enter: ")
                    if verify_hr == '' or verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                        verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                        verify_hr == 'yeS' or verify_hr == 'yEs':

                        while True:

                            min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                            if min.isnumeric() and len(min) == 2 and int(min) >= 0 and int(min) <= 59:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break

                            elif min.isnumeric() and len(min) == 1 and int(min) >= 0 and int(min) <= 9:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break
                            
                            else:
                                print("Incorrect minutes format. Reenter the minutes.")
                                continue

                    else:
                        print("Incorrect hour. Exiting...")
                        pass

                elif int(hr) == 12:
                    print("\nYou entered", hr, "noon.")
                    pass

                    verify_hr = input("If this is correct type 'Y' or just hit enter: ")
                    if verify_hr == '' or  verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                        verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                        verify_hr == 'yeS' or verify_hr == 'yEs':

                        while True:

                            min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                            if min.isnumeric() and len(min) == 2 and int(min) >= 0 and int(min) <= 59:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break

                            elif min.isnumeric() and len(min) == 1 and int(min) >= 0 and int(min) <= 9:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break
                            
                            else:
                                print("Incorrect minutes format. Reenter the minutes.")
                                continue
                    else:
                        print("Incorrect hour. Exiting...")
                        pass
                
                elif int(hr) >= 13 and int(hr) <= 23:
                    HHPM = int(hr) - 12
                    print("\nYou entered",HHPM,"PM.")
                    
                    verify_hr = input("If this is correct type 'Y' or just hit enter: ")
                    if verify_hr == '' or verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                        verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                        verify_hr == 'yeS' or verify_hr == 'yEs':

                        while True:

                            min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                            if min.isnumeric() and len(min) == 2 and int(min) >= 0 and int(min) <= 59:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break

                            elif min.isnumeric() and len(min) == 1 and int(min) >= 0 and int(min) <= 9:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break

                            else:
                                print("Incorrect minutes format. Reenter the minutes.")
                                continue                     
                    else:
                        print("Incorrect hour. Exiting...")
                        pass

                elif int(hr) == 0:
                    print("\nYou entered 12 'AM' midnight.")
                    
                    verify_hr = input("If this is correct type 'Y' or just hit enter: ")
                    if verify_hr == '' or   verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                        verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                        verify_hr == 'yeS' or verify_hr == 'yEs':

                        while True:

                            min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                            if min.isnumeric() and len(min) == 2 and int(min) >= 0 and int(min) <= 59:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break

                            elif min.isnumeric() and len(min) == 1 and int(min) >= 0 and int(min) <= 9:
                                today = date.today()
                                today_str = date.isoformat(today)
                                year = today_str[:4]
                                year = int(year)
                                month = today_str[5:7]
                                month = int(month)
                                day = today_str[8:10]
                                day = int(day)
                                hr = int(hr)
                                min = int(min)
                                entry_date = datetime(year,month,day,hr,min)
                                start_time_lst.append(entry_date)
                                break

                            else:
                                print("Incorrect minutes format. Reenter the minutes.")
                                continue
                    else:
                        print("Incorrect hour Exiting...")
                        pass
            else:
                print("Incorrect HH format Exiting...")
                print("\nUse 24hr format (e.g. 5am is 05, 10pm is 22, 12 midnight is 00, etc...")
                pass
        
        elif create_date_today == 'N' or create_date_today == 'n' or create_date_today == 'No' or create_date_today == 'no' or \
        create_date_today == 'NO' or create_date_today == 'nO':
            print("Manual entry of date.....")
            pass
        
        
        else:
            print("You chose not to create a date. Exiting...")
            pass
else:
    print("Exiting...")
    pass


# verify_logs verifies the number of start and entry logs match
def verify_logs(lst1,lst20):
    pass

# export_time_logs matches and exports the time logs
def export_time_logs(lst1,lst2,lst3):
    pass

print("\n--------Entry Times---------")
for row in start_time_lst:
    print(row)

#     database.time_log_add_many(log_entry)
conn.close()
