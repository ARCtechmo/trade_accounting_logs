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


### START HERE NEXT ###
# successfully added time_log records
# test adding and deleting a few records
# input records then test foreign key relationships using the SELECT command
log_entry = [('12/27/2021 16:00','12/27/2021 16:30',1,1)]
database_dev_mode.time_log_add_many(log_entry)
print("---------------successfully added records to the db------------------\n")
database_dev_mode.time_log_show_all()


#  optional - create a function to get user input for the log entry
