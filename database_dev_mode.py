### This code is under development ###
# this is the database_dev_mode.py file that builds the transactions_dev_mode.db database
import sqlite3
# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect('transactions_dev_mode.db')
cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS activity_log")
# cur.execute("DROP TABLE IF EXISTS brokers")
# cur.execute("DROP TABLE IF EXISTS time_log")
cur.executescript('''
CREATE TABLE IF NOT EXISTS brokers(
    broker_id INTEGER NOT NULL PRIMARY KEY,
    broker TEXT NOT NULL UNIQUE
    );

CREATE TABLE IF NOT EXISTS activity_log(
    activity_id INTEGER NOT NULL PRIMARY KEY,
    activity TEXT NOT NULL UNIQUE
    );

CREATE TABLE IF NOT EXISTS time_log(
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    activity_id INTEGER NOT NULL,
    broker_id INTEGER NOT NULL,
    FOREIGN KEY(activity_id) REFERENCES activity_log (activity_id)
        ON UPDATE CASCADE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    )
''')
print("---------------------table creation successful----------------------")
# brokers_table_functions
def broker_add_many(bk_name):
    with conn:
        cur.executemany("INSERT INTO brokers VALUES(?,?)", (bk_name), )
        print("-------------add_many executed successfully-----------------")
        conn.commit()
print("-------------broker_add_many_func created successfully----------------")
print("record added successfully--------------")
def broker_delete_one(id):
    with conn:
        cur.execute("DELETE FROM brokers WHERE rowid=? ",(id,) )
        conn.commit()
print("-------------broker_delete_one_func created successfully----------------")
print("record deleted successfully--------------")
def broker_show_all():
    with conn:
        cur.execute("SELECT * FROM brokers")
        print("-----------------show_all func executed successfully---------------")
        items = cur.fetchall()
        for item in items:
            print(item)
print("-------------broker_show_all_func created successfully----------------")
conn.commit()

# activity_log_table_functions
def activity_add_many(activity_name):
    with conn:
        cur.executemany("INSERT INTO activity_log VALUES(?,?)", (activity_name), )
        print("-------------add_many executed successfully-----------------")
        conn.commit()
print("-------------activity_log_add_many_func created successfully----------------")
print("record added successfully--------------")
def activity_delete_one(id):
    with conn:
        cur.execute("DELETE FROM activity_log WHERE rowid=? ",(id,) )
        conn.commit()
print("-------------activity_log_delete_one_func created successfully----------------")
print("record deleted successfully--------------")
def activity_show_all():
    with conn:
        cur.execute("SELECT * FROM activity_log")
        print("-----------------show_all func executed successfully---------------")
        items = cur.fetchall()
        for item in items:
            print(item)
print("-------------activity_log_show_all_func created successfully----------------")

### START HERE NEXT ###
# insert data into the time_log_table
def time_log_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO time_log VALUES(?,?,?,?)", (log_entry), )
        print("-------------add_many executed successfully-----------------")
        conn.commit()
print("-------------time_log_add_many_func created successfully----------------")
print("record added successfully--------------")
def time_log_delete_one(log_entry):
    with conn:
        cur.execute("DELETE FROM time_log WHERE rowid=? ",(log_entry,) )
        conn.commit()
print("-------------time_log_delete_one_func created successfully----------------")
print("record deleted successfully--------------")
def time_log_show_all():
    with conn:
        cur.execute("SELECT * FROM time_log")
        print("-----------------show_all func executed successfully---------------")
        items = cur.fetchall()
        for item in items:
            print(item)
print("-------------time_log_show_all_func created successfully----------------")
conn.commit()
conn.close()
