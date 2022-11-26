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

# time_lst contains a list of the time logs
time_lst = []

create_record = input("Would you like to create a new time log?: ")
if create_record == 'Y' or create_record == 'y' or create_record == 'Yes' or create_record == 'yes' or \
    create_record == 'YES' or create_record == 'YEs' or create_record == 'YeS' or create_record == 'yES' or \
    create_record == 'yeS' or create_record == 'yEs':

    while True:
        # log_year = input("Enter the year YYYY (e.g. 2023): ")

        create_date_today = input("Would you like to use today's date?  Type 'Y' or just hit enter: ")
        if create_date_today == '':

            hr = input("Enter the hour (HH) 0 <= HH <= 23 (e.g. 1:00 pm is '13'; 8:00 pm is '20'; 5:00 am is '05'): ")
            if hr.isnumeric() and len(hr) == 2 and int(hr) >= 0 and int(hr) <= 23:

                if int(hr) >= 1 and int(hr) <= 9:
                    print("\nYou entered",str(hr[1]),"AM.")

                    verify_hr = input( "Is this correct (Type'Y' or just hit enter): ")
                    if verify_hr == '':

                        min = input("\nEnter the minutes (MM) 0 <= mm <= 59: ")
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
                            print(entry_date)
                            break

                        elif min.isnumeric() and len(min) >= 1 and int(min) >= 0 and int(min) <= 9:
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
                            print(entry_date)
                            break

                    elif verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                    verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                    verify_hr == 'yeS' or verify_hr == 'yEs':
                        today = date.today()
                        today_str = date.isoformat(today)
                        year = today_str[:4]
                        year = int(year)
                        month = today_str[5:7]
                        month = int(month)
                        day = today_str[8:10]
                        day = int(day)
                        hr = int(hr)
                        entry_date = datetime(year,month,day,hr)
                        print(entry_date)
                        break

                    else:
                        print("Exiting...")
                        break

                elif int(hr) == 10 or int(hr) == 11:
                    print("\nYou entered",str(hr),"AM.")

                    verify_hr = input( "Is this correct (Type'Y' or just hit enter): ")
                    if verify_hr == '':

                        min = input("\nEnter the minutes (MM) 0 <= mm <= 59: ")
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
                            print(entry_date)
                            break

                        elif min.isnumeric() and len(min) >= 1 and int(min) >= 0 and int(min) <= 9:
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
                            print(entry_date)
                            break

                    elif verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                    verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                    verify_hr == 'yeS' or verify_hr == 'yEs':
                        today = date.today()
                        today_str = date.isoformat(today)
                        year = today_str[:4]
                        year = int(year)
                        month = today_str[5:7]
                        month = int(month)
                        day = today_str[8:10]
                        day = int(day)
                        hr = int(hr)
                        entry_date = datetime(year,month,day,hr)
                        print(entry_date)
                        break

                elif int(hr) == 12:
                    print("\nYou entered", hr, "noon.")

                    verify_hr = input( "Is this correct (Type'Y' or just hit enter): ")
                    if verify_hr == '':

                        min = input("\nEnter the minutes (MM) 0 <= mm <= 59: ")
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
                            print(entry_date)
                            break

                        elif min.isnumeric() and len(min) >= 1 and int(min) >= 0 and int(min) <= 9:
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
                            print(entry_date)
                            break

                    elif verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                    verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                    verify_hr == 'yeS' or verify_hr == 'yEs':
                        today = date.today()
                        today_str = date.isoformat(today)
                        year = today_str[:4]
                        year = int(year)
                        month = today_str[5:7]
                        month = int(month)
                        day = today_str[8:10]
                        day = int(day)
                        hr = int(hr)
                        entry_date = datetime(year,month,day,hr)
                        print(entry_date)
                        break
                
                elif int(hr) >= 13 and int(hr) <= 23:
                    HHPM = int(hr) - 12
                    print("\nYou entered",HHPM,"PM.")
                    verify_hr = input( "Is this correct (Type'Y' or just hit enter): ")
                    if verify_hr == '':
                        today = date.today()
                        today_str = date.isoformat(today)
                        year = today_str[:4]
                        year = int(year)
                        month = today_str[5:7]
                        month = int(month)
                        day = today_str[8:10]
                        day = int(day)
                        hr = int(hr)
                        entry_date = datetime(year,month,day,hr)
                        print(entry_date)
                        break

                    elif verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                    verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                    verify_hr == 'yeS' or verify_hr == 'yEs':
                        today = date.today()
                        today_str = date.isoformat(today)
                        year = today_str[:4]
                        year = int(year)
                        month = today_str[5:7]
                        month = int(month)
                        day = today_str[8:10]
                        day = int(day)
                        hr = int(hr)
                        entry_date = datetime(year,month,day,hr)
                        print(entry_date)
                        break

                elif int(hr) == 0:
                    print("\nYou entered 12 'AM' midnight.")
                    verify_hr = input( "Is this correct (Type'Y' or just hit enter): ")
                    if verify_hr == '':
                        today = date.today()
                        today_str = date.isoformat(today)
                        year = today_str[:4]
                        year = int(year)
                        month = today_str[5:7]
                        month = int(month)
                        day = today_str[8:10]
                        day = int(day)
                        hr = int(hr)
                        entry_date = datetime(year,month,day,hr)
                        print(entry_date)
                        break

                    elif verify_hr == 'Y' or verify_hr == 'y' or verify_hr == 'Yes' or verify_hr == 'yes' or \
                    verify_hr == 'YES' or verify_hr == 'YEs' or verify_hr == 'YeS' or verify_hr == 'yES' or \
                    verify_hr == 'yeS' or verify_hr == 'yEs':
                        today = date.today()
                        today_str = date.isoformat(today)
                        year = today_str[:4]
                        year = int(year)
                        month = today_str[5:7]
                        month = int(month)
                        day = today_str[8:10]
                        day = int(day)
                        hr = int(hr)
                        entry_date = datetime(year,month,day,hr)
                        print(entry_date)
                        break

            else:
                print("Incorrect HH format. Exiting...")
                break
else:
    print("Exiting...")
    pass

#     database.time_log_add_many(log_entry)
conn.close()
