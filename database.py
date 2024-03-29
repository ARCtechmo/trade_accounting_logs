### This code is under development ###
# this file builds the database
import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS brokers(
    broker_id INTEGER NOT NULL PRIMARY KEY,
    broker TEXT NOT NULL UNIQUE
    );

CREATE TABLE IF NOT EXISTS activity(
    activity_id INTEGER NOT NULL PRIMARY KEY,
    activity TEXT NOT NULL UNIQUE
    );

CREATE TABLE IF NOT EXISTS time_log(
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    activity_id INTEGER NOT NULL,
    broker_id INTEGER NOT NULL,
    FOREIGN KEY(activity_id) REFERENCES activity (activity_id)
        ON UPDATE CASCADE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS non_trading_expense(
    date TEXT,
    year INTEGER NOT NULL,
    month INTEGER,
    day INTEGER,
    description TEXT NOT NULL,
    expense INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS non_trading_revenue(
    date TEXT,
    year INTEGER NOT NULL,
    month INTEGER,
    day INTEGER,
    description TEXT NOT NULL,
    revenue INTEGER NOT NULL
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
    );

CREATE TABLE IF NOT EXISTS ib_options_log(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
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

CREATE TABLE IF NOT EXISTS ib_commissions_fee(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    comm_cost REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS ib_other_fee(
    date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    description TEXT NOT NULL,
    fee REAL NOT NULL,
    broker_id INTEGER NOT NULL,
    transaction_number INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(broker_id) REFERENCES brokers (broker_id)
        ON UPDATE CASCADE
    )

''')
# brokers_table_functions
def broker_add_many(bk_name):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO brokers VALUES(?,?)", (bk_name), )
        conn.commit()

def broker_show_all():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.execute("SELECT * FROM brokers")
        items = cur.fetchall()
        for item in items:
            print(item)

# activity table_functions
def activity_add_many(activity_name):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO activity VALUES(?,?)", (activity_name), )
        conn.commit()

def activity_delete_one(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.execute("DELETE FROM activity WHERE rowid=? ",(id,) )
        conn.commit()

def activity_show_all():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.execute("SELECT * FROM activity")
        items = cur.fetchall()
        for item in items:
            print(item)

# insert data into the time_log_table
def time_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO time_log VALUES(?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the non_trading_expense table
def non_trading_expense_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO non_trading_expense VALUES(?,?,?,?,?,?)", (log_entry), )
        conn.commit

# insert data into the non_trading_revenue table
def non_trading_revenue_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO non_trading_revenue VALUES(?,?,?,?,?,?)", (log_entry), )
        conn.commit

# insert data into the fx_log_table
def fx_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO fx_log VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the fx_unmatched table
def fx_unmatched_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO fx_unmatched VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the fx_commissions table
def fx_commissions_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO fx_commissions VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the fx_interest_debit table
def fx_interest_debit_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO fx_interest_debit VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the fx_interest_income table
def fx_interest_credit_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO fx_interest_income VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the fx_broker_credit_income table
def fx_broker_credit_income_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO fx_broker_credit_income VALUES(?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the td_options log table
def td_options_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO td_options_log VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the td_commissions log table
def td_commissions_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO td_commissions VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the td_regulation_fee log table
def td_reg_fee_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO td_regulation_fee VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the td_misc_income table
def td_misc_income_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO td_misc_income VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the td_misc_debit table
def td_misc_debit_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO td_misc_debit VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the td_interest_income table
def td_interest_income_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO td_interest_income VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the td_interest_debit table
def td_interest_debit_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO td_interest_debit VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the ib_options_log table
def ib_options_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO ib_options_log VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the ib_commissions_fee log table
def ib_commissions_fee_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO ib_commissions_fee VALUES(?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

# insert data into the ib_other_fee log table
def ib_other_fee_log_add_many(log_entry):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.executemany("INSERT INTO ib_other_fee VALUES(?,?,?,?,?,?,?,?)", (log_entry), )
        conn.commit()

conn.commit()
############################# CLOSE THE DATABASE ##############################
# print("\n-------------database closed---------------------")
conn.close()
############################# CLOSE THE DATABASE ##############################
