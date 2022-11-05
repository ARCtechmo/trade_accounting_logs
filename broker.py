## Under Development ##
# Use this file to create the broker names and trading activity
## These are used as foreign keys ## 
import database

# connect to the database
import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()

bk_name = [
            (1, 'No_Broker'),
            (2, 'Archer_Daniel_Midland'),
            (3, 'FOREX_com'),
            (4, 'Interactive_Brokers'),
            (5, 'TD_Ameritrade'),
            (6, 'Tradestation'),
            (7, 'Tradingview')
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
create_bkr = input("Would you like to create a new broker foreign key?: ")
if create_bkr == 'Y' or create_bkr == 'y' or create_bkr == 'Yes' or create_bkr == 'yes' \
   or create_bkr == 'YES' or create_bkr == 'YEs' or create_bkr == 'YeS' or create_bkr == 'yES' \
   or create_bkr == 'yeS' or create_bkr == 'yEs':
   database.broker_add_many(bk_name)
else:
  pass

# add activity_log records
create_activity = input("Would you like to create a new activity foreign key?: ")
if create_activity == 'Y' or create_activity == 'y' or create_activity == 'Yes' or create_activity == 'yes' \
   or create_activity == 'YES' or create_activity == 'YEs' or create_activity == 'YeS' or create_activity == 'yES' \
   or create_activity == 'yeS' or create_activity == 'yEs':  
   database.activity_add_many(activity_name)
else:
  pass

############################## CLOSE THE DATABASE ##################################
print("app closed....")
conn.close()
############################## QUERY THE DATABASE ##################################
