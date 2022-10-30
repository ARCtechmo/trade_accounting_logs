## Under Development ##
# Use this file to create the time logs
import database

# connect to the database
import sqlite3
conn = sqlite3.connect('transactions_dev_mode.db')
cur = conn.cursor()

# add records
create_record = input("Would you like to create a new time log?: ")
if create_record == 'Y' or create_record == 'y' or create_record == 'Yes' or create_record == 'yes' or \
    create_record == 'YES' or create_record == 'YEs' or create_record == 'YeS' or create_record == 'yES' or \
    create_record == 'yeS' or create_record == 'yEs':
    log_entry = [
                ('2022-10-06 00:00','2022-10-06 00:00',2,2),
                ('2022-10-07 00:00','2022-10-07 00:00',3,3)
                ]
    database.time_log_add_many(log_entry)
else:
    pass
############################## Close the database ##################################
print("app closed....")
conn.close()
############################## Close the database ##################################
