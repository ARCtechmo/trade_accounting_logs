### This code is under development ###
# this is the file that will interact with the database.py file
import database_dev_mode
import fx_dev_mode
from datetime import date
from datetime import datetime
if __name__ == "__main__":
    print('app module is being run directly')
else:
    print('database module is being imported into the app module')

# connect to the database
import sqlite3
conn = sqlite3.connect('transactions_dev_mode.db')
cur = conn.cursor()

################################# BROKER / ACTIVITY TABLES #########################
# bk_name = [
#             (1, 'No_Broker'),
#             (2, 'Archer_Daniel_Midland'),
#             (3, 'FOREX_com'),
#             (4, 'Interactive_Brokers'),
#             (5, 'TD_Ameritrade'),
#             (6, 'Tradestation'),
#             (7, 'Tradingview')
#           ]
# activity_name = [ (1,'trading_analysis'),
#                   (2,'accounting_logging'),
#                   (3,'market_research'),
#                   (4,'performance_review'),
#                   (5,'business_plan_development'),
#                   (6,'trade_plan_development'),
#                   (7,'professional_development'),
#                   (8,'backtesting')
#                 ]
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
################################# BROKER / ACTIVITY TABLES #########################

################################ ADD time_log RECORDS #########################################
# add records
# log_entry = [
#             ('2022-01-04 00:00','2022-00-00 00:00',2,2),
#             ('2022-01-05 00:00','2022-00-00 00:00',3,3)
#             ]


# database_dev_mode.time_log_add_many(log_entry)
# print("---------------successfully added records to the db------------------\n")
# database_dev_mode.time_log_show_all()
################################# ADD time_log RECORDS #######################################

################################# ADD fx_log RECORDS ######################################
# add fx_log records
# log_entry = fx_dev_mode.fxlog_add_records()
# database_dev_mode.fx_log_add_many(log_entry)
# print("---------------successfully added fx_log records to the db------------------\n")
# database_dev_mode.fx_log_show_all()
################################# ADD fx_log RECORDS ######################################


################################# ADD fx_unmatched RECORDS ######################################
# add fx_unmatched records to the database
# log_entry = fx_dev_mode.fx_unmatched_add_records()
# database_dev_mode.fx_unmatched_add_many(log_entry)
# print("---------------successfully added fx_log records to the db------------------\n")
# database_dev_mode.fx_unmatched_show_all()
################################# ADD fx_unmatched RECORDS ######################################


### START HERE NEXT ###
## process ##

# there are 4 records (jan and feb with unamtched records) in the DB to work with
# 3) query the fx_unmatched table for matching open_ids
#  - returned rows consists of the following:
#  - opening transactions with the entry dates and open_ids
#  - closing transactions with the exit dates and both close_id and open_ids

# 4) insert the entry YYYY-MM-DD HH:MM, YY, MM, DD, HH:MM into the matched row
#  - identify rows with matching open_ids (there should only be two rows)
#  - insert the entry YYYY-MM-DD HH:MM, YY, MM, DD, HH:MM into the closing transaction row
#  - the insert is accomplished via an SQL INSERT statement via the database_dev_mode.[function_name]


############################## QUERY THE DATABASE ##################################
######  query the time_log table ######
# print("\n----------test result: successful------------")
# data = cur.execute('''
# SELECT
#  time_log.start_time as start,
#  time_log.end_time as end,
#  time_log.activity_id,
#  activity,
#  time_log.broker_id,
#  broker
# FROM time_log
#     LEFT JOIN activity_log
#     ON time_log.activity_id = activity_log.activity_id
#
#     LEFT JOIN brokers
#     ON time_log.activity_id = brokers.broker_id
# WHERE '2022-01-04 10:00' NOT IN (start)
# ''')
# for row in data:
#     print(row)
######  query the time_log table ######

##### query the fx_log #####
# data = cur.execute('''
# SELECT *
# FROM fx_log
#     LEFT JOIN brokers
#     ON fx_log.broker_id = brokers.broker_id
# /* WHERE gross <0 */
# /* WHERE gross >0 */
# /* WHERE broker LIKE 'interactive%' */
# /* WHERE entry_time > '10:00' */
# ''')
# for row in data:
#     print(row)

# data = cur.execute('''
# SELECT COUNT(*)
# FROM fx_log
# WHERE gross <0
# ''')
# for row in data:
#     print(row)
##### query the fx_log #####
############################## QUERY THE DATABASE ##################################

############################## CLOSE THE DATABASE ##################################
conn.close()
print("app closed....")
############################## QUERY THE DATABASE ##################################
