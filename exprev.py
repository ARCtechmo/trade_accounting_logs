## Under Development ##
# Use this file to input non-trading expenses and revenue. 
import database

# connect to the database
import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# expense_lst contains a list of expense records as n-tuples
expense_lst = []
create_expense = input("Would you like to add an expense record?: ")

if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
    create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
    create_expense == 'yeS' or create_expense == 'yEs':

    while True:
        exp_year = input("Enter the year YYYY (e.g 2023): ")
        if exp_year.isnumeric() and len(exp_year) == 4 and exp_year[0] == '2' and exp_year[1] == '0':

            exp_month = input("Enter the month MM (e.g 01, 02, 10, 12): ")
            if exp_month.isnumeric() and len(exp_month) == 2 and int(exp_month) >= 10 and int(exp_month) <= 12:
                
                exp_day = input("Enter the day DD (e.g 01,02,15): ")
                if exp_day.isnumeric() and len(exp_day) == 2 and int(exp_day) >= 10 and int(exp_day) <= 31:

                    exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(exp_description) <= 50:

                        exp_amt = input("Enter the amount without commas (e.g 25, 10000): ")
                        if exp_amt.isnumeric():
                            exp_date = f'{exp_year}-{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))

                        elif exp_amt[:2].isnumeric() and exp_amt[-3] == '.':
                            exp_date = f'{exp_year}-{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))

                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break

                    create_expense = input("Would you like to add an expense record?: ")
                    if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
                    create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
                    create_expense == 'yeS' or create_expense == 'yEs':
                        continue
                    else:
                        break
                
                elif exp_day.isnumeric() and len(exp_day) == 1 and int(exp_day) >= 1 and int(exp_day) <= 9:
                    
                    exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(exp_description) <= 50:

                        exp_amt = input("Enter the amount without commas (e.g 25, 10000): ")
                        if exp_amt.isnumeric():
                            exp_date = f'{exp_year}-{exp_month}-0{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        elif exp_amt[:2].isnumeric() and exp_amt[-3] == '.':
                            exp_date = f'{exp_year}-{exp_month}-0{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))

                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break

                    create_expense = input("Would you like to add an expense record?: ")
                    if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
                    create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
                    create_expense == 'yeS' or create_expense == 'yEs':
                        continue
                    else:
                        break

                elif exp_day.isnumeric() and len(exp_day) == 2 and int(exp_day) >= 1 and int(exp_day) <= 9:

                    exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(exp_description) <= 50:

                        exp_amt = input("Enter the amount without commas (e.g 25, 10000): ")
                        if exp_amt.isnumeric():
                            exp_date = f'{exp_year}-{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        elif exp_amt[:2].isnumeric() and exp_amt[-3] == '.':
                            exp_date = f'{exp_year}-{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))

                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                else:
                    print("Incorrect entry day format. Exiting...")
                    pass
                    break
                
                create_expense = input("Would you like to add an expense record?: ")
                if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
                create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
                create_expense == 'yeS' or create_expense == 'yEs':
                    continue
                else:
                    break

            elif exp_month.isnumeric() and len(exp_month) == 1 and int(exp_month) >= 1 and int(exp_month) <= 9:

                exp_day = input("Enter the day DD (e.g 01,02,15): ")
                if exp_day.isnumeric() and len(exp_day) == 2 and int(exp_day) >= 10 and int(exp_day) <= 31:

                    exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(exp_description) <= 50:

                        exp_amt = input("Enter the amount without commas (e.g 25, 10000): ")
                        if exp_amt.isnumeric():
                            exp_date = f'{exp_year}-0{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        elif exp_amt[:2].isnumeric() and exp_amt[-3] == '.':
                            exp_date = f'{exp_year}-0{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break

                    create_expense = input("Would you like to add an expense record?: ")
                    if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
                    create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
                    create_expense == 'yeS' or create_expense == 'yEs':
                        continue
                    else:
                        break

                elif exp_day.isnumeric() and len(exp_day) == 1 and int(exp_day) >= 1 and int(exp_day) <= 9:

                    exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(exp_description) <= 50:

                        exp_amt = input("Enter the amount without commas (e.g 25, 10000): ")
                        if exp_amt.isnumeric():
                            exp_date = f'{exp_year}-0{exp_month}-0{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        elif exp_amt[:2].isnumeric() and exp_amt[-3] == '.':
                            exp_date = f'{exp_year}-0{exp_month}-0{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break

                    create_expense = input("Would you like to add an expense record?: ")
                    if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
                    create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
                    create_expense == 'yeS' or create_expense == 'yEs':
                        continue
                    else:
                        break

                elif exp_day.isnumeric() and len(exp_day) == 2 and int(exp_day) >= 1 and int(exp_day) <= 9:

                    exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(exp_description) <= 50:

                        exp_amt = input("Enter the amount without commas (e.g 25, 10000): ")
                        if exp_amt.isnumeric():
                            exp_date = f'{exp_year}-0{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        elif exp_amt[:2].isnumeric() and exp_amt[-3] == '.':
                            exp_date = f'{exp_year}-0{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                else:
                    print("Incorrect entry day format. Exiting...")
                    pass
                    break

                create_expense = input("Would you like to add an expense record?: ")
                if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
                create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
                create_expense == 'yeS' or create_expense == 'yEs':
                    continue
                else:
                    break

            elif exp_month.isnumeric() and len(exp_month) == 2 and int(exp_month) >= 1 and int(exp_month) <= 9:

                exp_day = input("Enter the day DD (e.g 01,02,15): ")
                if exp_day.isnumeric() and len(exp_day) == 2 and int(exp_day) >= 10 and int(exp_day) <= 31:

                    exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(exp_description) <= 50:

                        exp_amt = input("Enter the amount without commas (e.g 25, 10000): ")
                        if exp_amt.isnumeric():
                            exp_date = f'{exp_year}-{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        elif exp_amt[:2].isnumeric() and exp_amt[-3] == '.':
                            exp_date = f'{exp_year}-{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                    
                    create_expense = input("Would you like to add an expense record?: ")
                    if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
                    create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
                    create_expense == 'yeS' or create_expense == 'yEs':
                        continue
                    else:
                        break

                elif exp_day.isnumeric() and len(exp_day) == 1 and int(exp_day) >= 1 and int(exp_day) <= 9:

                    exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(exp_description) <= 50:

                        exp_amt = input("Enter the amount without commas (e.g 25, 10000): ")
                        if exp_amt.isnumeric():
                            exp_date = f'{exp_year}-{exp_month}-0{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        elif exp_amt[:2].isnumeric() and exp_amt[-3] == '.':
                            exp_date = f'{exp_year}-{exp_month}-0{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break

                    create_expense = input("Would you like to add an expense record?: ")
                    if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
                    create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
                    create_expense == 'yeS' or create_expense == 'yEs':
                        continue
                    else:
                        break
                
                elif exp_day.isnumeric() and len(exp_day) == 2 and int(exp_day) >= 1 and int(exp_day) <= 9:

                    exp_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(exp_description) <= 50:

                        exp_amt = input("Enter the amount without commas (e.g 25, 10000): ")
                        if exp_amt.isnumeric():
                            exp_date = f'{exp_year}-{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))
                        
                        elif exp_amt[:2].isnumeric() and exp_amt[-3] == '.':
                            exp_date = f'{exp_year}-{exp_month}-{exp_day}'
                            exp_year = int(exp_year)
                            exp_month = int(exp_month)
                            exp_day = int(exp_day)
                            exp_amt = float(exp_amt)
                            expense_lst.append((exp_date,exp_year,exp_month,exp_day,exp_description,exp_amt))

                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                else:
                    print("Incorrect entry day format. Exiting...")
                    pass
                    break

                create_expense = input("Would you like to add an expense record?: ")
                if create_expense == 'Y' or create_expense == 'y' or create_expense == 'Yes' or create_expense == 'yes' or \
                create_expense == 'YES' or create_expense == 'YEs' or create_expense == 'YeS' or create_expense == 'yES' or \
                create_expense == 'yeS' or create_expense == 'yEs':
                    continue
                else:
                    break
            else:
                print("Incorrect entry month format. Exiting...")
                pass
                break
        else:
            print("Incorrect entry year format. Exiting...")
            pass
            break
else:
    print("Exiting...")
    pass

# revenue_lst conans a list of the revenue records as n-tuples
revenue_lst = []
create_revenue = input("Would you like to add a revenue record?: ")

if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
    create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
    create_revenue == 'yeS' or create_revenue == 'yEs':
    
    while True:

        rev_year = input("Enter the year YYYY (e.g. 2023): ")
        if rev_year.isnumeric() and len(rev_year) == 4 and rev_year[0] == '2' and rev_year[1] == '0':
            
            rev_month = input("Enter the month MM (e.g. 01, 01, 10, 12): ")
            if rev_month.isnumeric() and len(rev_month) == 2 and int(rev_month) >= 10 and int(rev_month) <= 12:

                rev_day = input("Enter the day DD (e.g. 01,02,15): ")
                if rev_day.isnumeric() and len(rev_day) == 2 and int(rev_day) >= 10 and int(rev_day) <= 31:

                    rev_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(rev_description) <= 50:

                        rev_amt = input("Enter the amount without commas (e.g. 25, 10000): ")
                        if rev_amt.isnumeric():
                            rev_date = f'{rev_year}-{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))

                        elif rev_amt[:2].isnumeric() and rev_amt[-3] == '.':
                            rev_date = f'{rev_year}-{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                    
                    create_revenue = input("Would you like to add a revenue record?: ")
                    if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
                    create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
                    create_revenue == 'yeS' or create_revenue == 'yEs':
                        continue
                    else:
                        break

                elif rev_day.isnumeric() and len(rev_day) == 1 and int(rev_day) >= 1 and int(rev_day) <= 9:

                    rev_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(rev_description) <= 50:

                        rev_amt = input("Enter the amount without commas (e.g. 25, 10000): ")
                        if rev_amt.isnumeric():
                            rev_date = f'{rev_year}-{rev_month}-0{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))

                        elif rev_amt[:2].isnumeric() and rev_amt[-3] == '.':
                            rev_date = f'{rev_year}-{rev_month}-0{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                    
                    create_revenue = input("Would you like to add a revenue record?: ")
                    if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
                    create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
                    create_revenue == 'yeS' or create_revenue == 'yEs':
                        continue
                    else:
                        break
                
                elif rev_day.isnumeric() and len(rev_day) == 2 and int(rev_day) >= 1 and int(rev_day) <= 9:

                    rev_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(rev_description) <= 50:

                        rev_amt = input("Enter the amount without commas (e.g. 25, 10000): ")
                        if rev_amt.isnumeric():
                            rev_date = f'{rev_year}-{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))

                        elif rev_amt[:2].isnumeric() and rev_amt[-3] == '.':
                            rev_date = f'{rev_year}-{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                else:
                    print("Incorrect entry day format. Exiting...")
                
                create_revenue = input("Would you like to add a revenue record?: ")
                if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
                create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
                create_revenue == 'yeS' or create_revenue == 'yEs':
                    continue
                else:
                    break

            elif rev_month.isnumeric() and len(rev_month) == 1 and int(rev_month) >= 1 and int(rev_month) <= 9:

                rev_day = input("Enter the day DD (e.g. 01,02,15): ")
                if rev_day.isnumeric() and len(rev_day) == 2 and int(rev_day) >= 10 and int(rev_day) <= 31:

                    rev_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(rev_description) <= 50:

                        rev_amt = input("Enter the amount without commas (e.g. 25, 10000): ")
                        if rev_amt.isnumeric():
                            rev_date = f'{rev_year}-0{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))

                        elif rev_amt[:2].isnumeric() and rev_amt[-3] == '.':
                            rev_date = f'{rev_year}-0{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                    
                    create_revenue = input("Would you like to add a revenue record?: ")
                    if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
                    create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
                    create_revenue == 'yeS' or create_revenue == 'yEs':
                        continue
                    else:
                        break

                elif rev_day.isnumeric() and len(rev_day) == 1 and int(rev_day) >= 1 and int(rev_day) <= 9:

                    rev_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(rev_description) <= 50:

                        rev_amt = input("Enter the amount without commas (e.g. 25, 10000): ")
                        if rev_amt.isnumeric():
                            rev_date = f'{rev_year}-0{rev_month}-0{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))

                        elif rev_amt[:2].isnumeric() and rev_amt[-3] == '.':
                            rev_date = f'{rev_year}-0{rev_month}-0{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                    
                    create_revenue = input("Would you like to add a revenue record?: ")
                    if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
                    create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
                    create_revenue == 'yeS' or create_revenue == 'yEs':
                        continue
                    else:
                        break
                    
                elif rev_day.isnumeric() and len(rev_day) == 2 and int(rev_day) >= 1 and int(rev_day) <= 9:

                    rev_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(rev_description) <= 50:

                        rev_amt = input("Enter the amount without commas (e.g. 25, 10000): ")
                        if rev_amt.isnumeric():
                            rev_date = f'{rev_year}-0{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))

                        elif rev_amt[:2].isnumeric() and rev_amt[-3] == '.':
                            rev_date = f'{rev_year}-0{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                else:
                    print("Incorrect entry day format. Exiting...")
                    pass
                    break

                create_revenue = input("Would you like to add a revenue record?: ")
                if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
                create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
                create_revenue == 'yeS' or create_revenue == 'yEs':
                    continue
                else:
                    break
            
            elif rev_month.isnumeric() and len(rev_month) == 2 and int(rev_month) >= 1 and int(rev_month) <= 9:

                rev_day = input("Enter the day DD (e.g. 01,02,15): ")
                if rev_day.isnumeric() and len(rev_day) == 2 and int(rev_day) >= 10 and int(rev_day) <= 31:
                    
                    rev_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(rev_description) <= 50:

                        rev_amt = input("Enter the amount without commas (e.g. 25, 10000): ")
                        if rev_amt.isnumeric():
                            rev_date = f'{rev_year}-{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))

                        elif rev_amt[:2].isnumeric() and rev_amt[-3] == '.':
                            rev_date = f'{rev_year}-{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                    
                    create_revenue = input("Would you like to add a revenue record?: ")
                    if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
                    create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
                    create_revenue == 'yeS' or create_revenue == 'yEs':
                        continue
                    else:
                        break

                elif rev_day.isnumeric() and len(rev_day) == 1 and int(rev_day) >= 1 and int(rev_day) <= 9:

                    rev_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(rev_description) <= 50:

                        rev_amt = input("Enter the amount without commas (e.g. 25, 10000): ")
                        if rev_amt.isnumeric():
                            rev_date = f'{rev_year}-{rev_month}-0{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))

                        elif rev_amt[:2].isnumeric() and rev_amt[-3] == '.':
                            rev_date = f'{rev_year}-{rev_month}-0{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                    
                    create_revenue = input("Would you like to add a revenue record?: ")
                    if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
                    create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
                    create_revenue == 'yeS' or create_revenue == 'yEs':
                        continue
                    else:
                        break

                elif rev_day.isnumeric() and len(rev_day) == 2 and int(rev_day) >= 1 and int(rev_day) <= 9:

                    rev_description = input("Enter a description of the expense (max 75 char numbers or letters): ")
                    if len(rev_description) <= 50:

                        rev_amt = input("Enter the amount without commas (e.g. 25, 10000): ")
                        if rev_amt.isnumeric():
                            rev_date = f'{rev_year}-{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))

                        elif rev_amt[:2].isnumeric() and rev_amt[-3] == '.':
                            rev_date = f'{rev_year}-{rev_month}-{rev_day}'
                            rev_year = int(rev_year)
                            rev_month = int(rev_month)
                            rev_day = int(rev_day)
                            rev_amt = float(rev_amt)
                            revenue_lst.append((rev_date,rev_year,rev_month,rev_day,rev_description,rev_amt))
                        
                        else:
                            print("Incorrect amount format. Exiting...")
                            pass
                            break
                    else:
                        print("Incorrect description format. Exiting...")
                        pass
                        break
                else:
                    print("Incorrect entry day format. Exiting...")
                    pass
                    break

                create_revenue = input("Would you like to add a revenue record?: ")
                if create_revenue == 'Y' or create_revenue == 'y' or create_revenue == 'Yes' or create_revenue == 'yes' or \
                create_revenue == 'YES' or create_revenue == 'YEs' or create_revenue == 'YeS' or create_revenue == 'yES' or \
                create_revenue == 'yeS' or create_revenue == 'yEs':
                    continue
                else:
                    break
            else:
                print("Incorrect entry month format. Exiting...")
                pass
                break
        else:
            print("Incorrect entry year format. Exiting...")
            pass
            break
else:
    print("Exiting...")
    pass


# contains a list of the rows in the non_trading_expense table
non_trading_expense_rows = []

# export_expense_lst contains a list of the non-trading expenses that will be exported to the non_trading_expense table
export_expense_lst = []

def export_expense(lst1,lst2,lst3):
    expense_log_data = cur.execute(''' SELECT * FROM non_trading_expense ''')
    for row in expense_log_data:
        lst1.append(row)
    try:
        for row in lst2:
            if row in lst1:
                print("\n---------------duplicate row--------------------")
                print(row)
                pass
            else:
                lst3.append(row)
        log_entry = lst3
        database.non_trading_expense_add_many(log_entry)

    except:
        pass
# export_expense(non_trading_expense_rows,expense_lst,export_expense_lst)


# contains a list of the rows in the non_trading_expense table
non_trading_revenue_rows = []

# export_expense_lst contains a list of the non-trading expenses that will be exported to the export_revenue_lst table
export_revenue_lst = []

def export_revenue(lst1,lst2,lst3):
    revenue_log_data = cur.execute(''' SELECT * FROM non_trading_revenue ''')
    for row in revenue_log_data:
        lst1.append(row)
    try:
        for row in lst2:
            if row in lst1:
                print("\n---------------duplicate row--------------------")
                print(row)
                pass
            else:
                lst3.append(row)
        log_entry = lst3
        database.non_trading_revenue_add_many(log_entry)

    except:
        pass
# export_revenue(non_trading_revenue_rows,revenue_lst,export_revenue_lst)

print("--------------TEST: expense-----------------")
for row in expense_lst:
    print(row)

print("--------------TEST: revenue-----------------")
for row in revenue_lst:
    print(row)