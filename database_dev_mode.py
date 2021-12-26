### This code is under development ###
# this is the database_dev_mode.py file that builds the transactions_dev_mode.db database
import sqlite3
# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect('transactions.db')
cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS time_log")
cur.executescript('''
CREATE TABLE IF NOT EXISTS brokers(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    broker TEXT NOT NULL UNIQUE
    );

CREATE TABLE IF NOT EXISTS activity_log(
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    activity TEXT NOT NULL UNIQUE
    );

CREATE TABLE IF NOT EXISTS time_log(
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    activity_log_id INTEGER,
    brokers_id INTEGER,
    PRIMARY KEY(activity_log_id, brokers_id)
    )
''')
conn.commit()
print("---------------------table creation successful----------------------")
conn.close()
