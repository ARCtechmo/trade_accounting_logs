### This code is under development ###
# this is the file that will interact with the database.py file
import database_dev_mode
from datetime import date
from datetime import datetime

if __name__ == "__main__":
    print('app module is being run directly')
else:
    print('database module is being imported into the app module')
bk_name = [
            (1, 'Archer_Daniel_Midland'),
            (2, 'FOREX_com'),
            (3, 'Interactive_Broker'),
            (4, 'TD_Ameritrade'),
            (5, 'Tradestation')
          ]
activity_name = [ (1,'trading_analysis'),
                  (2,'accounting_logging'),
                  (3,'market_research'),
                  (4,'performance_review'),
                  (5,'business_plan_development'),
                  (6,'trade_plan_development'),
                  (7,'professional_development'),
                  (8,'backtesting')
                ]
# add broker records
# database_dev_mode.broker_add_many(bk_name)
# print("---------------successfully added records to the db------------------\n")
# database_dev_mode.broker_show_all()

# delete broker record
# database_dev_mode.broker_delete_one(6)
# print("---------------successfully deleted record to the db------------------\n")
# database_dev_mode.broker_show_all()

# add activity_log records
# database_dev_mode.activity_add_many(activity_name)
# print("---------------successfully added records to the db------------------\n")
# database_dev_mode.activity_show_all()

# delete activity_log record
# database_dev_mode.activity_delete_one(9)
# print("---------------successfully deleted record to the db------------------\n")
# database_dev_mode.activity_show_all()

# add records
# log_entry = [
#             ('1/03/2022 16:00','1/03/2022 16:30',1,1),
#             ('1/03/2022 16:00','1/03/2022 16:30',1,1),
#             ('1/03/2022 16:00','1/03/2022 16:30',1,1),
#             ('1/04/2022 16:00','1/04/2022 16:30',2,2),
#             ('1/04/2022 16:00','1/04/2022 16:30',2,2),
#             ('1/04/2022 16:00','1/04/2022 16:30',2,2),
#             ('1/05/2022 16:00','1/05/2022 16:30',3,3),
#             ('1/05/2022 16:00','1/05/2022 16:30',3,3),
#             ('1/05/2022 16:00','1/05/2022 16:30',3,3)
#             ]

log_entry = [
            ('1/03/2022 16:00','1/03/2022 16:30',1,1),
            ('1/04/2022 16:00','1/04/2022 16:30',2,2),
            ('1/05/2022 16:00','1/05/2022 16:30',3,3)
            ]


# database_dev_mode.time_log_add_many(log_entry)
# print("---------------successfully added records to the db------------------\n")
# database_dev_mode.time_log_show_all()

### problem: if you delete record "1" repeatedly it will not delete all of the records...
### ... in other words the rowid may say "1" but the original record is row "5" and it will not delete
# delete time_log record
# database_dev_mode.time_log_delete_one(3)
# print("---------------successfully deleted record to the db------------------\n")
# database_dev_mode.time_log_show_all()


# connect to the database
import sqlite3
conn = sqlite3.connect('transactions_dev_mode.db')
cur = conn.cursor()

# query the time_log table
# test two foreign keyS, LEFT JOIN ON, conditional WHERE OR clauses, case insensitivity -
print("\n----------test result: successful------------")
data = cur.execute('''
SELECT
 time_log.start_time as start,
 time_log.end_time as end,
 time_log.activity_id,
 activity,
 time_log.broker_id,
 broker
FROM time_log
    LEFT JOIN activity_log
    ON time_log.activity_id = activity_log.activity_id

    LEFT JOIN brokers
    ON time_log.activity_id = brokers.broker_id
WHERE broker LIKE 'forex%'
OR activity LIKE 'TRADING%'
''')
for row in data:
    print(row)

### START HERE NEXT ###
# date and time format
# read the tutorial on sqlite3 date and time
# insert dummy data with the correct date and time format
# build on the previous command statemrns to query the year, month, and day
print("\n----------test result: ???------------")


conn.close()
