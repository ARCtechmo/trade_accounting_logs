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
### update this section with user input and pass user input to a variable ##
# add records
# log_entry = [
#             ('2022-01-04 00:00','2022-00-00 00:00',2,2),
#             ('2022-01-05 00:00','2022-00-00 00:00',3,3)
#             ]


# database_dev_mode.time_log_add_many(log_entry)
# print("---------------successfully added records to the db------------------\n")
# database_dev_mode.time_log_show_all()
################################# Add time_log RECORDS #######################################


################################# Add corrected duplicates to fx_log table ##########################
#### START HERE NEXT (1) ####
# correct the duplicate then export the function

# the dictionary contains a count of duplicate close_id or open_id in the broker data
# the count in the dictionary is used to identify duplicate transaction ids
di = dict()

# duplicate_close_id_lst is a list that contains the duplicate close_ids
duplicate_close_id_lst = []

# duplicate_open_id_lst is a list that contains the duplicate open_ids
duplicate_open_id_lst = []

# list contains modified close / open transaction ids
modified_duplicate_lst = []

# function corrects duplicate close_ids / open_ids and exports the rows into the fx_log table
def corrected_duplicates():
    print("--------------------------------test of corrected_duplicates() function--------------------------------")
    log_entry = fx_dev_mode.fxlog_add_records()
    for row in log_entry:
        row = row[11]
        di[row] = di.get(row,0) + 1
    for key,value in di.items():
        if value > 1:
            print("duplicate id: ", key)
            for row in log_entry:
                if row[11] == key:
                    print("\n---------------------TEST: duplicate close_id error in broker data----------------------")
                    row = tuple(row)
                    print(row)
                    duplicate_close_id_lst.append(row)
                elif row[12] == key:
                    print("\n---------------------TEST: duplicate open_id error in broker data----------------------\n")
                    row = tuple(row)
                    print(row)
                    duplicate_open_id_lst.append(row)

    print("\n----------------------TEST: list of rows with duplicate close_id not exported--------------------------")
    for row in duplicate_close_id_lst:
        print(row)

    print("\n-----------------------TEST: list of rows with duplicate open_id not exported--------------------------")
    for row in duplicate_open_id_lst:
        print(row)
# corrected_duplicates()
################################# Add corrected duplicates to fx_log table ##############################

################################# Add fx_log RECORDS ######################################
# add fx_log records

# fx_log_rows contains a list of the rows in the fx_log table
fx_log_rows = []

# export_fx_log_entry_lst contains a list of the rows that will be exported into the fx_log table
export_fx_log_entry_lst = []

# export_fx_log_records function check for UNIQUE CONSTRANT ERRORS
# exports fx_log records into the fx_log table
def export_fx_log_records():
    fx_log_data = cur.execute(''' SELECT * FROM fx_log ''')
    print("\n--------------TEST: export_fx_log_records function: log_entry records----------------")
    for row in fx_log_data:
        fx_log_rows.append(row)
    print(fx_log_rows)

    print("\n--------------TEST: export_fx_log_records function: log_entry records--------------------")
    for row in log_entry:
        row = tuple(row)
        if row in fx_log_rows:
            print("\n-------------TRUE TEST FOR UNIQUE CONSRAINT: duplicate row------------")
            print(row)
            pass

        ### START HERE NEXT (2) ###
        #### TEST ####
        # test the corrected_duplicates function on this part of the loop
        elif row in duplicate_close_id_lst:
            print("\n-------------TRUE TEST FOR UNIQUE CONSRAINT: duplicate close_id------------")
            print(row)
            pass

        ### START HERE NEXT (3) ###
        #### TEST ####
        # test the corrected_duplicates function on this part of the loop
        # create a modified .csv file for july and add in duplicate open_ids to test this
        elif row in duplicate_open_id_lst:
            print("\n-------------TRUE TEST FOR UNIQUE CONSRAINT: duplicate open_id------------")
            print(row)
            pass

        else:
            print("\n-------------FALSE TEST FOR UNIQUE CONSRAINT-------------")
            print(row)
            export_fx_log_entry_lst.append(row)

    print("\n--------------TEST: rows to export into fx_log table-------------------")
    print(export_fx_log_entry_lst)
    log_entry = export_fx_log_entry_lst
    database_dev_mode.fx_log_add_many(log_entry)

    print("---------------successfully added fx_log records to the db------------------\n")

# export_fx_log_records()
################################# Add fx_log RECORDS ################################################

################################# Add fx_unmatched RECORDS ######################################
# add fx_unmatched records to the database
def export_unmatched_records():
    log_entry = fx_dev_mode.fx_unmatched_add_records()
    database_dev_mode.fx_unmatched_add_many(log_entry)
    print("---------------successfully added fx_log records to the db------------------\n")
# export_unmatched_records()
################################# Add fx_unmatched RECORDS ######################################

############################ Add matched RECORDS TO fx_log RECORDS #########################
print("\n---------------------rows from fx_unmatched ready to be imported into fx_log-----------------")

# matched_lst contains the combined matched entry and exit into one row
matched_lst = []

# function combines rows in fx_unmatched table with the same open_id into a single row
def match():
    data = cur.execute(''' SELECT * FROM fx_unmatched GROUP BY open_id, close_id ''' )
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


### Potential Bug: edge case with broker data ###
### see the solution in the first section and modify it to fit the function below ###
# function exports the matched transactions from fx_unmatched table to fx_log table
# function removes duplicates to avoid a UNIQUE CONSTRAINT ERROR
def export_matched_record():
    print("--------------check_constraint function test -------------")

    # matched_rows_lst contains rows with matched open / close transactions
    # however, some of these rows are duplicates in the fx_log table...
    # and cause a UNIQUE CONSTRAINT ERROR
    matched_rows_lst = []

    # export_matched_rows_lst filters out the duplicate matched open / close transactions
    # these rows are exported into fx_log table
    export_matched_rows_lst = []

    # new_lst is a list that contains the fx_log rows
    new_lst = []

    print("\n---------rows in fx_log table----------")
    fx_log_data = cur.execute(''' SELECT * FROM fx_log ''')
    for row in fx_log_data:
        new_lst.append(row)
        fx_log_data = new_lst
    print(fx_log_data)

    print("\n------------matched rows-----------")
    log_entry = match()
    for item in log_entry:
        matched_rows_lst.append(item)
    print(matched_rows_lst)

    for entry in matched_rows_lst:
        if entry in fx_log_data:
            print("\n-------------TRUE TEST FOR UNIQUE CONSRAINT------------")
            print(entry)
            pass
        else:
            print("\n-------------FALSE TEST FOR UNIQUE CONSRAINT-------------")
            print(entry)
            export_matched_rows_lst.append(entry)

    print("\n-----test of list to export---------")
    print(export_matched_rows_lst)
    log_entry = export_matched_rows_lst
    database_dev_mode.fx_log_add_many(log_entry)

# export_matched_record()
############################ Add matched records to fx_log table #########################


######################### Show all rows in the fx_log table #########################
def show_all():
    database_dev_mode.fx_log_show_all()
# show_all()
######################### Show all rows in the fx_log table #########################

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
