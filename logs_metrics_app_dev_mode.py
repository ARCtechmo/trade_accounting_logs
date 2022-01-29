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
log_entry = fx_dev_mode.fx_unmatched_add_records()
database_dev_mode.fx_unmatched_add_many(log_entry)
print("---------------successfully added fx_log records to the db------------------\n")
database_dev_mode.fx_unmatched_show_all()
################################# ADD fx_unmatched RECORDS ######################################

############################ ADD matched RECORDS TO fx_log RECORDS #########################
print("\n---------------------rows from fx_unmatched ready to be imported into fx_log-----------------")
# 4) add the fx_log function to export the matched rows into fx_log table

# matched_lst contains the combined matched entry and exit into one row
matched_lst = []

# function combines rows in fx_unmatched table with the same open_id into a single row
def match():
    data = cur.execute(
    '''
    SELECT *
    FROM fx_unmatched
    GROUP BY open_id, close_id
    '''
    )
    # entry_lst contains rows with only open_ids
    # exit_lst contains rows with only close_id
    entry_lst = []
    exit_lst = []
    for row in data:
        if row[11] == 0:
            entry_lst.append(row)
        else:
            exit_lst.append(row)

    for item in zip(entry_lst, exit_lst):
        if item[0][12] == item[1][12]:
            matched_lst.append(
            (item[0][0],item[0][1],item[0][2],item[0][3],item[0][4], \
            item[1][5],item[1][6],item[1][7],item[1][8],item[1][9], \
            item[1][10],item[1][11],item[1][12],item[1][13],item[1][14], \
            item[1][15],item[1][16],item[1][17],item[1][18],item[1][19])
            )
    return matched_lst

### START HERE NEXT ###
# clean up and test this function
# the goal is to avoid a UNIQUE CONSTRAINT ERROR
# the function identifies and removes rows in fx_unmatched that are in fx_table
def check_constraint():
    print("--------------check_constraint function test -------------")
    fx_log_rows_lst = []
    log_entry = match()
    fx_log_data = cur.execute(''' SELECT * FROM fx_log ''')
    for row in fx_log_data:
        fx_log_rows_lst.append(row)
    for item in log_entry:
        if item in fx_log_rows_lst:
            return print("-----TRUE TEST FOR UNIQUE CONSRAINT------")
            pass
        else:
            database_dev_mode.fx_log_add_many(item)
            return database_dev_mode.fx_log_show_all()
check_constraint()

## extract and export the matched transactions from fx_unmatched into fx_log table ##

# log_entry = match()
# database_dev_mode.fx_log_add_many(log_entry)
# print("---------successfully added fx_log records to the db from the fx_unmatched--------\n")
# database_dev_mode.fx_log_show_all()
############################ ADD matched RECORDS TO fx_log RECORDS #########################

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
