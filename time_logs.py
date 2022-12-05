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

while True:

    create_start_record = input("\nWould you like to create a new entry time log? Enter 'Y' or hit enter: ")
    if create_start_record == '' or create_start_record == 'Y' or create_start_record == 'y' or create_start_record == 'Yes' or create_start_record == 'yes' or \
        create_start_record == 'YES' or create_start_record == 'YEs' or create_start_record == 'YeS' or create_start_record == 'yES' or \
        create_start_record == 'yeS' or create_start_record == 'yEs':

            create_date_today = input("\nType 'Y' or hit enter to use today's date. Type 'N' to enter a date. Type any other key to exit: ")
            if create_date_today == '' or create_date_today == 'Y' or create_date_today == 'y' or create_date_today == 'Yes' or create_date_today == 'yes' or \
                create_date_today == 'YES' or create_date_today == 'YEs' or create_date_today == 'YeS' or create_date_today == 'yES' or \
                create_date_today == 'yeS' or create_date_today == 'yEs':

                while True:

                    entry_hr = input("\nEnter the start hour (HH) 0 <= HH <= 23 (e.g. 1:00 pm is '13'; 8:00 pm is '20'; 5:00 am is '05'): ")
                    if entry_hr.isnumeric() and len(entry_hr) == 2 and int(entry_hr) >= 0 and int(entry_hr) <= 23:

                        if int(entry_hr) >= 1 and int(entry_hr) <= 9:
                            print("\nYou entered",str(entry_hr[1]),"AM.")

                            verify_entry_hr = input("If this is correct type 'Y' or just hit enter: ")
                            if verify_entry_hr == '' or verify_entry_hr == 'Y' or verify_entry_hr == 'y' or verify_entry_hr == 'Yes' or verify_entry_hr == 'yes' or \
                                verify_entry_hr == 'YES' or verify_entry_hr == 'YEs' or verify_entry_hr == 'YeS' or verify_entry_hr == 'yES' or \
                                verify_entry_hr == 'yeS' or verify_entry_hr == 'yEs':

                                while True:

                                    entry_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                    if entry_min.isnumeric() and len(entry_min) == 2 and int(entry_min) >= 0 and int(entry_min) <= 59:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break

                                    elif entry_min.isnumeric() and len(entry_min) == 1 and int(entry_min) >= 0 and int(entry_min) <= 9:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break

                                    else:
                                        print("Reenter the minutes.")
                                        continue
                            else:
                                print("Reenter the hour.")
                                continue

                            break
                    
                        elif int(entry_hr) == 10 or int(entry_hr) == 11:
                            print("\nYou entered",str(entry_hr),"AM.")

                            verify_entry_hr = input("If this is correct type 'Y' or just hit enter: ")
                            if verify_entry_hr == '' or verify_entry_hr == 'Y' or verify_entry_hr == 'y' or verify_entry_hr == 'Yes' or verify_entry_hr == 'yes' or \
                                verify_entry_hr == 'YES' or verify_entry_hr == 'YEs' or verify_entry_hr == 'YeS' or verify_entry_hr == 'yES' or \
                                verify_entry_hr == 'yeS' or verify_entry_hr == 'yEs':

                                while True:

                                    entry_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                    if entry_min.isnumeric() and len(entry_min) == 2 and int(entry_min) >= 0 and int(entry_min) <= 59:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break

                                    elif entry_min.isnumeric() and len(entry_min) == 1 and int(entry_min) >= 0 and int(entry_min) <= 9:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break
                                    
                                    else:
                                        print("Reenter the minutes.")
                                        continue
                            else:
                                print("Reenter the hour.")
                                continue
                            
                            break

                        elif int(entry_hr) == 12:
                            print("\nYou entered", entry_hr, "noon.")

                            verify_entry_hr = input("If this is correct type 'Y' or just hit enter: ")
                            if verify_entry_hr == '' or  verify_entry_hr == 'Y' or verify_entry_hr == 'y' or verify_entry_hr == 'Yes' or verify_entry_hr == 'yes' or \
                                verify_entry_hr == 'YES' or verify_entry_hr == 'YEs' or verify_entry_hr == 'YeS' or verify_entry_hr == 'yES' or \
                                verify_entry_hr == 'yeS' or verify_entry_hr == 'yEs':

                                while True:

                                    entry_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                    if entry_min.isnumeric() and len(entry_min) == 2 and int(entry_min) >= 0 and int(entry_min) <= 59:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break

                                    elif entry_min.isnumeric() and len(entry_min) == 1 and int(entry_min) >= 0 and int(entry_min) <= 9:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break
                                    
                                    else:
                                        print("Reenter the minutes.")
                                        continue
                            else:
                                print("Reenter the hour.")
                                continue
                            
                            break
                        
                        elif int(entry_hr) >= 13 and int(entry_hr) <= 23:
                            HHPM = int(entry_hr) - 12
                            print("\nYou entered",HHPM,"PM.")
                            
                            verify_entry_hr = input("If this is correct type 'Y' or just hit enter: ")
                            if verify_entry_hr == '' or verify_entry_hr == 'Y' or verify_entry_hr == 'y' or verify_entry_hr == 'Yes' or verify_entry_hr == 'yes' or \
                                verify_entry_hr == 'YES' or verify_entry_hr == 'YEs' or verify_entry_hr == 'YeS' or verify_entry_hr == 'yES' or \
                                verify_entry_hr == 'yeS' or verify_entry_hr == 'yEs':

                                while True:

                                    entry_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                    if entry_min.isnumeric() and len(entry_min) == 2 and int(entry_min) >= 0 and int(entry_min) <= 59:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break

                                    elif entry_min.isnumeric() and len(entry_min) == 1 and int(entry_min) >= 0 and int(entry_min) <= 9:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break

                                    else:
                                        print("Reenter the minutes.")
                                        continue                     
                            else:
                                print("Reenter the hour.")
                                continue
                            
                            break

                        elif int(entry_hr) == 0:
                            print("\nYou entered 12 'AM' midnight.")
                            
                            verify_entry_hr = input("If this is correct type 'Y' or just hit enter: ")
                            if verify_entry_hr == '' or   verify_entry_hr == 'Y' or verify_entry_hr == 'y' or verify_entry_hr == 'Yes' or verify_entry_hr == 'yes' or \
                                verify_entry_hr == 'YES' or verify_entry_hr == 'YEs' or verify_entry_hr == 'YeS' or verify_entry_hr == 'yES' or \
                                verify_entry_hr == 'yeS' or verify_entry_hr == 'yEs':

                                while True:

                                    entry_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                    if entry_min.isnumeric() and len(entry_min) == 2 and int(entry_min) >= 0 and int(entry_min) <= 59:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break

                                    elif entry_min.isnumeric() and len(entry_min) == 1 and int(entry_min) >= 0 and int(entry_min) <= 9:

                                        verify_entry_min = input("If this is correct type 'Y' or just hit enter: ")
                                        if verify_entry_min == '' or verify_entry_min == 'Y' or verify_entry_min == 'y' or verify_entry_min == 'Yes' or verify_entry_min == 'yes' or \
                                            verify_entry_min == 'YES' or verify_entry_min == 'YEs' or verify_entry_min == 'YeS' or verify_entry_min == 'yES' or \
                                            verify_entry_min == 'yeS' or verify_entry_min == 'yEs':

                                            today = date.today()
                                            today_str = date.isoformat(today)
                                            year = today_str[:4]
                                            year = int(year)
                                            month = today_str[5:7]
                                            month = int(month)
                                            day = today_str[8:10]
                                            day = int(day)
                                            hr = int(entry_hr)
                                            min = int(entry_min)
                                            entry_date = datetime(year,month,day,hr,min)
                                            start_time_lst.append(entry_date)
                                            break

                                    else:
                                        print("Reenter the minutes.")
                                        continue
                            else:
                                print("Reenter the hour.")
                                continue

                            break

                    else:
                        print("Incorrect HH format.")
                        print("Use 24hr format (e.g. 5am is 05, 10pm is 22, 12 midnight is 00, etc...")
                        continue
                
                length_start_time_lst = int(len(start_time_lst))
                length_end_time_lst = int(len(end_time_lst))
                if length_start_time_lst - length_end_time_lst == 1:

                    while True:
                    
                        exit_hr = input("\nEnter the exit hour (HH) 0 <= HH <= 23 (e.g. 1:00 pm is '13'; 8:00 pm is '20'; 5:00 am is '05'): ")
                        if exit_hr.isnumeric() and int(exit_hr) >= int(entry_hr) and len(exit_hr) == 2 and int(exit_hr) >= 0 and int(exit_hr) <= 23:
                            print("exit hour", exit_hr)
                            
                            if int(exit_hr) >= 1 and int(exit_hr) <= 9:
                                print("\nYou entered",str(exit_hr[1]),"AM.")

                                verify_exit_hr = input("If this is correct type 'Y' or just hit enter: ")
                                if verify_exit_hr == '' or verify_exit_hr == 'Y' or verify_exit_hr == 'y' or verify_exit_hr == 'Yes' or verify_exit_hr == 'yes' or \
                                    verify_exit_hr == 'YES' or verify_exit_hr == 'YEs' or verify_exit_hr == 'YeS' or verify_exit_hr == 'yES' or \
                                    verify_exit_hr == 'yeS' or verify_exit_hr == 'yEs':

                                    while True:

                                        exit_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                        if int(exit_hr) == int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59 and int(exit_min) > int(entry_min):

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9 and int(exit_min) > int(entry_min):
                                                
                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                        elif int(exit_hr) > int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59:

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9:
                                                
                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                        else:
                                            print("Reenter the minutes.")
                                            continue
                                else:
                                    print("Reenter the hour.")
                                    continue

                                break


                            elif int(exit_hr) == 10 or int(exit_hr) == 11:
                                print("\nYou entered",str(exit_hr),"AM.")

                                verify_exit_hr = input("If this is correct type 'Y' or just hit enter: ")
                                if verify_exit_hr == '' or verify_exit_hr == 'Y' or verify_exit_hr == 'y' or verify_exit_hr == 'Yes' or verify_exit_hr == 'yes' or \
                                    verify_exit_hr == 'YES' or verify_exit_hr == 'YEs' or verify_exit_hr == 'YeS' or verify_exit_hr == 'yES' or \
                                    verify_exit_hr == 'yeS' or verify_exit_hr == 'yEs':

                                    while True:

                                        exit_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                        if int(exit_hr) == int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59 and int(exit_min) > int(entry_min):

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9 and int(exit_min) > int(entry_min):

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                        elif int(exit_hr) > int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59:

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9:
                                                
                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break
                                        
                                        else:
                                            print("Reenter the minutes.")
                                            continue
                                else:
                                    print("Reenter the hour.")
                                    continue

                                break

                            elif int(exit_hr) == 12:
                                print("\nYou entered", exit_hr, "noon.")

                                verify_exit_hr = input("If this is correct type 'Y' or just hit enter: ")
                                if verify_exit_hr == '' or  verify_exit_hr == 'Y' or verify_exit_hr == 'y' or verify_exit_hr == 'Yes' or verify_exit_hr == 'yes' or \
                                    verify_exit_hr == 'YES' or verify_exit_hr == 'YEs' or verify_exit_hr == 'YeS' or verify_exit_hr == 'yES' or \
                                    verify_exit_hr == 'yeS' or verify_exit_hr == 'yEs':

                                    while True:

                                        exit_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                        if int(exit_hr) == int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59 and int(exit_min) > int(entry_min):

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9 and int(exit_min) > int(entry_min):

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                        elif int(exit_hr) > int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59:

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9:
                                                
                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break
                                            
                                        else:
                                            print("Reenter the minutes.")
                                            continue
                                else:
                                    print("Reenter the hour.")
                                    continue

                                break

                            elif int(exit_hr) >= 13 and int(exit_hr) <= 23:
                                HHPM = int(exit_hr) - 12
                                print("\nYou entered",HHPM,"PM.")
                            
                                verify_exit_hr = input("If this is correct type 'Y' or just hit enter: ")
                                if verify_exit_hr == '' or verify_exit_hr == 'Y' or verify_exit_hr == 'y' or verify_exit_hr == 'Yes' or verify_exit_hr == 'yes' or \
                                    verify_exit_hr == 'YES' or verify_exit_hr == 'YEs' or verify_exit_hr == 'YeS' or verify_exit_hr == 'yES' or \
                                    verify_exit_hr == 'yeS' or verify_exit_hr == 'yEs':

                                    while True:

                                        exit_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                        if int(exit_hr) == int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59 and int(exit_min) > int(entry_min):

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9 and int(exit_min) > int(entry_min):

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                        elif int(exit_hr) > int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59:

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9:
                                                
                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                        else:
                                            print("Reenter the minutes.")
                                            continue                     
                                else:
                                    print("Reenter the hour.")
                                    continue

                                break

                            elif int(exit_hr) == 0:
                                print("\nYou entered 12 'AM' midnight.")
                            
                                verify_exit_hr = input("If this is correct type 'Y' or just hit enter: ")
                                if verify_exit_hr == '' or   verify_exit_hr == 'Y' or verify_exit_hr == 'y' or verify_exit_hr == 'Yes' or verify_exit_hr == 'yes' or \
                                    verify_exit_hr == 'YES' or verify_exit_hr == 'YEs' or verify_exit_hr == 'YeS' or verify_exit_hr == 'yES' or \
                                    verify_exit_hr == 'yeS' or verify_exit_hr == 'yEs':

                                    while True:

                                        exit_min = input("\nEnter the minutes (MM) 0 <= MM <= 59: ")
                                        if int(exit_hr) == int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59 and int(exit_min) > int(entry_min):

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9 and int(exit_min) > int(entry_min):

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break
                                        elif int(exit_hr) > int(entry_hr):
                                            if exit_min.isnumeric() and len(exit_min) == 2 and int(exit_min) >= 0 and int(exit_min) <= 59:

                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                            elif exit_min.isnumeric() and len(exit_min) == 1 and int(exit_min) >= 0 and int(exit_min) <= 9:
                                                
                                                verify_exit_min = input("If this is correct type 'Y' or just hit enter: ")
                                                if verify_exit_min == '' or verify_exit_min == 'Y' or verify_exit_min == 'y' or verify_exit_min == 'Yes' or verify_exit_min == 'yes' or \
                                                    verify_exit_min == 'YES' or verify_exit_min == 'YEs' or verify_exit_min == 'YeS' or verify_exit_min == 'yES' or \
                                                    verify_exit_min == 'yeS' or verify_exit_min == 'yEs':

                                                    today = date.today()
                                                    today_str = date.isoformat(today)
                                                    year = today_str[:4]
                                                    year = int(year)
                                                    month = today_str[5:7]
                                                    month = int(month)
                                                    day = today_str[8:10]
                                                    day = int(day)
                                                    hr = int(exit_hr)
                                                    min = int(exit_min)
                                                    exit_date = datetime(year,month,day,hr,min)
                                                    end_time_lst.append(exit_date)
                                                    break

                                        else:
                                            print("Reenter the minutes.")
                                            continue
                                else:
                                    print("Reenter the hour.")
                                    continue

                                break
                            
                        else:
                            if  exit_hr.isnumeric() and len(exit_hr) < 2:
                                print("\nIncorrect HH format...")
                                print("Use 24hr format (e.g. 5am is 05, 10pm is 22, 12 midnight is 00, etc...")
                                continue
                            
                            elif exit_hr.isnumeric() and int(exit_hr) < int(entry_hr):
                                print("\nThe end time hour must be >= start time hour")
                                continue

                            else:
                                print("Incorrect hour format. Redirecting...")
                                continue
                else:
                    print("You must have an entry log to proceed. Redirecting...")
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
        break

# verify_logs verifies the number of start and entry logs match
def verify_logs(lst1,lst20):
    pass

# export_time_logs matches and exports the time logs
def export_time_logs(lst1,lst2,lst3):
    pass

print("\n--------Entry Times---------")
for row in start_time_lst:
    print(row)

print("\n--------Exit Times---------")
for row in end_time_lst:
    print(row)

#     database.time_log_add_many(log_entry)
conn.close()
