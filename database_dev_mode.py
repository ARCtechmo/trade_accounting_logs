### This code is under development ###
# this is the database_dev_mode.py file that builds the transactions_dev_mode.db database
import sqlite3
# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect('transactions_dev_mode.db')
cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS activity_log")
# cur.execute("DROP TABLE IF EXISTS brokers")
# cur.execute("DROP TABLE IF EXISTS time_log")
# cur.execute("DROP TABLE IF EXISTS fx_log")
# cur.execute("DROP TABLE IF EXISTS fx_unmatched")
# cur.execute("DROP TABLE IF EXISTS fx_commissions")
# cur.execute("DROP TABLE IF EXISTS fx_interest_debit")
# cur.execute("DROP TABLE IF EXISTS fx_interest_income")
# cur.execute("DROP TABLE IF EXISTS fx_broker_credit_income")

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
    );

CREATE TABLE IF NOT EXISTS fx_log(
    entry_date TEXT NOT NULL,
    entry_year INTEGER NOT NULL,
    entry_month INTEGER NOT NULL,
    entry_day INTEGER NOT NULL,
    entry_time TEXT NOT NULL,
    exit_date TEXT NOT NULL,
    exit_year INTEGER NOT NULL,
    exit_month INTEGER NOT NULL,
    exit_day INTEGER NOT NULL,
    exit_time TEXT NOT NULL,
    market TEXT NOT NULL,
    close_id INTEGER NOT NULL,
    open_id INTEGER NOT NULL,
    close_buy_sell TEXT NOT NULL,
    trade_size INTEGER NOT NULL,
    open_price REAL NOT NULL,
    close_price REAL NOT NULL,
    gross REAL NOT NULL,
    net REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS fx_unmatched(
    entry_date TEXT,
    entry_year INTEGER,
    entry_month INTEGER,
    entry_day INTEGER,
    entry_time TEXT,
    exit_date TEXT,
    exit_year INTEGER,
    exit_month INTEGER,
    exit_day INTEGER,
    exit_time TEXT,
    market TEXT NOT NULL,
    close_id INTEGER NOT NULL,
    open_id INTEGER NOT NULL,
    close_buy_sell TEXT,
    trade_size INTEGER NOT NULL,
    open_price REAL,
    close_price REAL,
    gross REAL,
    net REAL,
    broker_id INTEGER NOT NULL,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS fx_commissions(
    entry_date TEXT,
    entry_year INTEGER,
    entry_month INTEGER,
    entry_day INTEGER,
    transaction_id INTEGER NOT NULL,
    commissions_cost INTEGER,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS fx_interest_debit(
    entry_date TEXT,
    entry_year INTEGER,
    entry_month INTEGER,
    entry_day INTEGER,
    transaction_id INTEGER NOT NULL,
    interest_debit INTEGER,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS fx_interest_income(
    entry_date TEXT,
    entry_year INTEGER,
    entry_month INTEGER,
    entry_day INTEGER,
    transaction_id INTEGER NOT NULL,
    interest_credit INTEGER,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS fx_broker_credit_income(
    entry_date TEXT,
    entry_year INTEGER,
    entry_month INTEGER,
    entry_day INTEGER,
    broker_credit INTEGER,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS td_options_log(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    trans_id INTEGER NOT NULL,
    bought_sold TEXT NOT NULL,
    trade_size INTEGER NOT NULL,
    market TEXT NOT NULL,
    call_put TEXT NOT NULL,
    contract TEXT NOT NULL,
    price REAL NOT NULL,
    gross REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS td_commissions(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    trans_id INTEGER NOT NULL,
    comm_cost REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS td_regulation_fee(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    trans_id INTEGER NOT NULL,
    reg_fee REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS td_interest_income(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    trans_id INTEGER NOT NULL,
    int_adj_income REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS td_interest_debit(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    trans_id INTEGER NOT NULL,
    int_adj_debit REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS td_misc_income(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    trans_id INTEGER NOT NULL,
    misc_credit REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS td_misc_debit(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    trans_id INTEGER NOT NULL,
    misc_debit REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
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
# insert data into the fx_log_table
def fx_log_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO fx_log VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------add_many executed successfully-----------------\n")
        conn.commit()
print("\n-------------fx_log_add_many_func created successfully----------------\n")
print("record added successfully--------------")
def fx_log_show_all():
    with conn:
        cur.execute("SELECT * FROM fx_log")
        print("-----------------show_all func executed successfully---------------")
        items = cur.fetchall()
        for item in items:
            print(item)
print("-------------fx_log_show_all_func created successfully----------------")
# insert data into the fx_unmatched table
def fx_unmatched_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO fx_unmatched VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------add_many executed successfully-----------------")
        conn.commit()
print("-------------fx_unmatched_add_many func created successfully----------------")
print("record added successfully--------------")
def fx_unmatched_show_all():
    with conn:
        cur.execute("SELECT * FROM fx_unmatched")
        print("\n-----------------show_all func executed successfully---------------\n")
        items = cur.fetchall()
        for item in items:
            print(item)
print("------------- fx_unmatched_show_all func created successfully----------------")

# insert data into the fx_commissions table
def fx_commissions_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO fx_commissions VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------fx_commissions_add_many executed successfully-----------------")
        conn.commit()
print("-------------fx_commissions_add_many func created successfully----------------")
print("record added successfully--------------")
def fx_commissions_show_all():
    with conn:
        cur.execute("SELECT * FROM fx_commissions")
        print("\n-----------------show_all func executed successfully---------------\n")
        items = cur.fetchall()
        for item in items:
            print(item)
print("------------- fx_commissions_show_all func created successfully----------------")

# insert data into the fx_interest_debit table
def fx_interest_debit_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO fx_interest_debit VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------fx_interest_debit_add_many executed successfully-----------------")
        conn.commit()
print("-------------fx_interest_debit_add_many func created successfully----------------")
print("record added successfully--------------")
def fx_interest_debit_show_all():
    with conn:
        cur.execute("SELECT * FROM fx_interest_debit")
        print("\n-----------------show_all func executed successfully---------------\n")
        items = cur.fetchall()
        for item in items:
            print(item)
print("------------- fx_interest_debit_show_all func created successfully----------------")

# insert data into the fx_interest_income table
def fx_interest_credit_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO fx_interest_income VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------fx_interest_credit_add_many() func executed successfully-----------------")
        conn.commit()
print("-------------fx_interest_credit_add_many() func func created successfully----------------")
print("record added successfully--------------")
def fx_interest_credit_show_all():
    with conn:
        cur.execute("SELECT * FROM fx_interest_income")
        print("\n-----------------show_all func executed successfully---------------\n")
        items = cur.fetchall()
        for item in items:
            print(item)
print("------------- fx_interest_credit_show_all func created successfully----------------")

# insert data into the fx_broker_credit_income table
def fx_broker_credit_income_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO fx_broker_credit_income VALUES(?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------fx_broker_credit_income_add_many() func executed successfully-----------------")
        conn.commit()
print("-------------fx_broker_credit_income_add_many() func func created successfully----------------")
print("record added successfully--------------")
def fx_broker_credit_income_add_many_show_all():
    with conn:
        cur.execute("SELECT * FROM fx_broker_credit_income")
        print("\n-----------------show_all func executed successfully---------------\n")
        items = cur.fetchall()
        for item in items:
            print(item)
print("------------- fx_broker_credit_income_add_many_show_all func created successfully----------------")

# insert data into the td_options log table
def td_options_log_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO td_options_log VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------add_many executed successfully-----------------\n")
        conn.commit()
print("\n-------------td_options_log_add_many created successfully----------------\n")
print("record added successfully--------------")
def td_log_show_all():
    with conn:
        cur.execute("SELECT * FROM td_options_log")
        print("-----------------show_all func executed successfully---------------")
        items = cur.fetchall()
        for item in items:
            print(item)
print("-------------td_options_log_show_all_func created successfully----------------")

# insert data into the td_commissinos log table
def td_commissions_log_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO td_commissions VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------add_many executed successfully-----------------\n")
        conn.commit()
print("\n-------------td_commissions_log_add_many created successfully----------------\n")
print("record added successfully--------------")
def td_comm_log_show_all():
    with conn:
        cur.execute("SELECT * FROM td_commissions")
        print("-----------------show_all func executed successfully---------------")
        items = cur.fetchall()
        for item in items:
            print(item)
print("-------------td_commissions_log_show_all_func created successfully----------------")

# insert data into the td_regulation_fee log table
def td_reg_fee_log_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO td_regulation_fee VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------add_many executed successfully-----------------\n")
        conn.commit()
print("\n-------------td_reg_fee_log_add_many created successfully----------------\n")
print("record added successfully--------------")
def td_reg_fee_log_show_all():
    with conn:
        cur.execute("SELECT * FROM td_regulation_fee")
        print("-----------------td_reg_fee_log_show_all func executed successfully---------------")
        items = cur.fetchall()
        for item in items:
            print(item)
print("-------------td_commissions_log_show_all_func created successfully----------------")

# insert data into the td_misc_income table
def td_misc_income_log_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO td_misc_income VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------td_misc_income_log_add_many executed successfully-----------------\n")
        conn.commit()
print("\n-------------td_misc_income_log_add_many created successfully----------------\n")
print("record added successfully--------------")
def td_misc_income_log_show_all():
    with conn:
        cur.execute("SELECT * FROM td_misc_income")
        print("-----------------td_misc_income_log_show_all func executed successfully---------------")
        items = cur.fetchall()
        for item in items:
            print(item)
print("-------------td_misc_income_log_show_all created successfully----------------")

# insert data into the td_misc_debit table
def td_misc_debit_log_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO td_misc_debit VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------td_misc_debit_log_add_many executed successfully-----------------\n")
        conn.commit()
print("\n-------------td_misc_debit_log_add_many created successfully----------------\n")
print("record added successfully--------------")
def td_misc_debit_log_show_all():
    with conn:
        cur.execute("SELECT * FROM td_misc_debit")
        print("-----------------td_misc_debit_log_show_all func executed successfully---------------")
        items = cur.fetchall()
        for item in items:
            print(item)
print("-------------td_misc_debit_log_show_all created successfully----------------")

# insert data into the td_interest_income table
def td_interest_income_log_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO td_interest_income VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------td_interest_income_log_add_many executed successfully-----------------\n")
        conn.commit()
print("\n-------------td_interest_income_log_add_many created successfully----------------\n")
print("record added successfully--------------")
def td_interest_income_log_show_all():
    with conn:
        cur.execute("SELECT * FROM td_interest_income")
        print("\n-------------td_interest_income_log_show_all func executed successfully----------------\n")
        items = cur.fetchall()
        for item in items:
            print(item)
print("\n-------------td_interest_income_log_show_all func created successfully----------------\n")

# insert data into the td_interest_debit table
def td_interest_debit_log_add_many(log_entry):
    with conn:
        cur.executemany("INSERT INTO td_interest_debit VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        print("\n-------------td_interest_debit_log_add_many executed successfully-----------------\n")
        conn.commit()
print("\n-------------td_interest_debit_log_add_many created successfully----------------\n")
print("record added successfully--------------")
def td_interest_debit_log_show_all():
    with conn:
        cur.execute("SELECT * FROM td_interest_debit")
        print("\n-------------td_interest_debit_log_show_all func executed successfully----------------\n")
        items = cur.fetchall()
        for item in items:
            print(item)
print("\n-------------td_interest_debit_log_show_all func created successfully----------------\n")

conn.commit()
############################# CLOSE THE DATABASE ##############################
print("\n-------------database closed---------------------")
conn.close()
############################# CLOSE THE DATABASE ##############################
