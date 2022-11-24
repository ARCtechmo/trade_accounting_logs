## Under Development ##
# Use this file to input non-trading expenses and revenue. 
import database

# connect to the database
import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# create an expense record
log_entry = []
create_expense = input("Would you like to add an expense record?: ")
if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
    create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
    create_expense == 'yeS' or create_expense == 'yEs':

    exp_year = input("Enter the year YYYY (e.g 2023): ")
    if exp_year.isnumeric() and len(exp_year) == 4 and exp_year[0] == '2' and exp_year[1] == '0':

        exp_month = input("Enter the month MM (e.g 01, 02, 10, 12): ")
        if exp_month.isnumeric() and len(exp_month) == 2 and int(exp_month) > 0 and int(exp_month) <= 12:
            
            exp_day = input("Enter the year DD (e.g 01,02,15): ")
            if exp_day.isnumeric() and len(exp_day) == 2 and int(exp_day) > 0 and int(exp_day) <=31:

                exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                if len(exp_description) <= 50:

                    ### START HERE NEXT ### 
                    # Task: fix the amount entry to account for decimals (floats)
                    exp_amt = (input("Enter the amount without commas (e.g 25, 10000): "))
                    if type(exp_amt) == 'int' or type(exp_amt) == 'float':

                        exp_date = f'{exp_year}-{exp_month}-{exp_day}'
                        exp_year = int(exp_year)
                        exp_month = int(exp_month)
                        exp_day = int(exp_day)
                        exp_amt = float(exp_amt)
                        log_entry.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                    else:
                        print("Incorrect amount format. Exiting...")
                        pass
                else:
                    print("Incorrect description format. Exiting...")
                    pass
            else:
                print("Incorrect entry day format. Exiting...")
                pass
        else:
            print("Incorrect entry month format. Exiting...")
            pass

    else:
        print("Incorrect entry year format. Exiting...")
        pass
else:
    print("Exiting...")
    pass
for log in log_entry:
    print(log)