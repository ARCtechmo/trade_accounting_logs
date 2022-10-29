### under development ###
import database
import fx
import td
import ib
from datetime import date
from datetime import datetime
import itertools

if __name__ == "__main__":
    print('app module is being run directly')
else:
    print('database module is being imported into the app module')

# connect to the database
import sqlite3
conn = sqlite3.connect('transactions_dev_mode.db')
cur = conn.cursor()

################################## Begin add fx_log RECORDS ################################################
# add fx_log records
# fx_log_rows contains a list of the rows in the fx_log table
fx_log_rows = []

# export_fx_log_entry_lst contains a list of the rows that will be exported into the fx_log table
export_fx_log_entry_lst = []

# export_fx_log_records function check for UNIQUE CONSTRANT ERRORS
# exports fx_log records into the fx_log table
def export_fx_log_records():
    fx_log_data = cur.execute(''' SELECT * FROM fx_log ''')
    for row in fx_log_data:
        fx_log_rows.append(row)
    try:
        log_entry = fx.fxlog_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in fx_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_fx_log_entry_lst.append(row)

        log_entry = export_fx_log_entry_lst
        database.fx_log_add_many(log_entry)
    
    except:
        pass
export_fx_log_records()
################################# End add fx_log RECORDS ################################################

################################# Begin add fx_unmatched RECORDS ######################################
# add fx_unmatched records to the database
def export_unmatched_records():
    try:
        log_entry = fx.fx_unmatched_export_records()
        database.fx_unmatched_add_many(log_entry)
    except:
        pass
export_unmatched_records()
################################# End add fx_unmatched RECORDS ######################################

############################ Begin add matched RECORDS TO fx_log RECORDS #########################
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


# function exports the matched transactions from fx_unmatched table to fx_log table
# function removes duplicates to avoid a UNIQUE CONSTRAINT ERROR
def export_matched_record():
    # matched_rows_lst contains rows with matched open / close transactions
    # however, some of these rows are duplicates in the fx_log table and may cause a UNIQUE CONSTRAINT ERROR
    matched_rows_lst = []

    # export_matched_rows_lst filters out the duplicate matched open / close transactions
    # these rows are exported into fx_log table
    export_matched_rows_lst = []

    # new_lst is a list that contains the fx_log rows
    new_lst = []

    fx_log_data = cur.execute(''' SELECT * FROM fx_log ''')
    for row in fx_log_data:
        new_lst.append(row)
        fx_log_data = new_lst
    log_entry = match()
    for item in log_entry:
        matched_rows_lst.append(item)

    # append the unique transaction identifier to each matched record from the unmatched table
    # create a unique key for each transaction
    key_lst = []
    for item in matched_rows_lst:
        item = list(item)
        item[11] = str(item[11])
        item[12] = str(item[12])
        entry_year_key = f'{item[0][2:4]}'
        entry_month_key = f'{item[0][5:7]}'
        entry_day_key = f'{item[0][8:10]}'
        exit_month_key = f'{item[5][5:7]}'
        exit_day_key = f'{item[5][8:10]}'
        close_open_key = item[11][-4:] + item[12][-4:]
        unique_key = f'{entry_year_key}{entry_month_key}{entry_day_key}{exit_month_key}{exit_day_key}{close_open_key}'

        entry_year_key = int(entry_year_key)
        entry_month_key = int(entry_month_key)
        entry_day_key = int(entry_day_key)
        exit_month_key = int(exit_month_key)
        exit_day_key = int(exit_day_key)

        close_open_key = int(close_open_key)
        unique_key = int(unique_key)
        key_lst.append(unique_key)

    # matched_rows_lst contains the matched rows from the unmatched tabel with unique transaction ids
    matched_rows_lst2 = []
    for record, key in zip(matched_rows_lst, key_lst):
        record = list(record)
        record.append(key)
        record = tuple(record)
        matched_rows_lst2.append((record))

    for entry in matched_rows_lst2:
        if entry in fx_log_data:
            print("\n-------------UNIQUE CONSRAINT: duplicate row------------")
            print(entry)
            pass
        else:
            export_matched_rows_lst.append(entry)

    log_entry = export_matched_rows_lst
    database.fx_log_add_many(log_entry)

export_matched_record()
############################ End add matched records to fx_log table #########################

############################ Begin add records to fx_commissions table #######################
# fx_commission_rows contains a list of the rows in the commissions table
fx_commission_rows = []

# export_fx_commission_entry_lst contains a list of the rows that will be exported into the fx_commissions table
export_fx_commission_entry_lst = []

# export_fx_commissions_records() function checks for UNIQUE CONSTRANT ERRORS
# export_fx_commissions_records() function exports fx_commissions transactions into the fx_commissions table
def export_fx_commissions_records():
    fx_commission_data = cur.execute(''' SELECT * FROM fx_commissions''')
    for row in fx_commission_data:
        fx_commission_rows.append(row)
    try:
        log_entry = fx.fx_comm_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in fx_commission_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_fx_commission_entry_lst.append(row)

        log_entry = export_fx_commission_entry_lst
        database.fx_commissions_add_many(log_entry)
    except:
        pass
export_fx_commissions_records()
############################ End add records to fx_commissions table #########################

############################ Begin add records to interest_debit table #######################
# fx_int_debit_rows contains a list of the rows in the fx_interest_debit table
fx_int_debit_rows = []

# export_fx_int_debit_entry_lst contains a  list of the rows that will be exported into the fx_interest_debit table
export_fx_int_debit_entry_lst = []

# export_fx_interest_debit_records() function checks for UNIQUE CONSTRANT ERRORS
# export_fx_interest_debit_records() function exports fx_interest_debit transactions into the fx_interest_debit table
def export_fx_interest_debit_records():
    fx_int_debit_data = cur.execute(''' SELECT * FROM fx_interest_debit''')
    for row in fx_int_debit_data:
        fx_int_debit_rows.append(row)
    try:
        log_entry = fx.fx_int_debit_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in fx_int_debit_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_fx_int_debit_entry_lst.append(row)

        log_entry = export_fx_int_debit_entry_lst
        database.fx_interest_debit_add_many(log_entry)
    except:
        pass
export_fx_interest_debit_records()
############################ End add records to interest_debit table #########################

############################ Begin add records to fx_interest_income table #######################
# fx_int_credit_rows contains a list of the rows in the fx_interest_income table
fx_int_credit_rows = []

# export_fx_int_credit_entry_lst contains a  list of the rows that will be exported into the fx_interest_income table
export_fx_int_credit_entry_lst = []

def export_fx_interest_credit_records():
    fx_int_credit_data = cur.execute(''' SELECT * FROM fx_interest_income''')
    for row in fx_int_credit_data:
        fx_int_credit_rows.append(row)
    try:
        log_entry = fx.fx_int_credit_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in fx_int_credit_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_fx_int_credit_entry_lst.append(row)

        log_entry = export_fx_int_credit_entry_lst
        database.fx_interest_credit_add_many(log_entry)
    except:
        pass
export_fx_interest_credit_records()
############################ End add records to fx_interest_income table #########################

############################ Begin add records to fx_broker_credit_income table ###################
# fx_broker_credit_rows contains a list of the rows in the fx_broker_credit_income table
fx_broker_credit_rows = []

# export_fx_broker_credit_entry_lst contains a  list of the rows that will be exported into the fx_broker_credit_income table
export_fx_broker_credit_entry_lst = []

def export_fx_broker_credit_records():
    fx_broker_credit_data = cur.execute(''' SELECT * FROM fx_broker_credit_income''')
    for row in fx_broker_credit_data:
        fx_broker_credit_rows.append(row)
    try:
        log_entry = fx.fx_broker_credit_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in fx_broker_credit_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_fx_broker_credit_entry_lst.append(row)

        log_entry = export_fx_broker_credit_entry_lst
        database.fx_broker_credit_income_add_many(log_entry)
    except:
        pass
export_fx_broker_credit_records()
############################ End add records to broker_credit_income table #####################

################################## Begin add td_options_log RECORDS ##############################################
# add td_options_log records

# td_options_log_rows contains a list of the rows in the td_options_log table
td_options_log_rows = []

# export_td_options_log_entry_lst contains a list of the rows that will be exported into the td_options_log table
export_td_options_log_entry_lst = []

# export_td_options_log_records function check for UNIQUE CONSTRANT ERRORS
# exports the td broker options log records into the td_options_log table
def export_td_options_log_records():
    td_options_log_data = cur.execute(''' SELECT * FROM td_options_log ''')
    for row in td_options_log_data:
        td_options_log_rows.append(row)
    try:
        log_entry = td.options_log_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in td_options_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_td_options_log_entry_lst.append(row)

        log_entry = export_td_options_log_entry_lst
        database.td_options_log_add_many(log_entry)
    except:
        pass
export_td_options_log_records()
################################## End add td_options_log RECORDS ##############################################

################################## Begin add td_commissions log RECORDS ##############################################
# add td_commissions log records

# td_comm_log_rows contains a list of the rows in the td_commissions table
td_comm_log_rows = []

# export_td_comm_log_entry_lst contains a list of the rows that will be exported into the td_commissions table
export_td_comm_log_entry_lst = []

# export_td_comm_log_records function check for UNIQUE CONSTRANT ERRORS
# exports the td broker commissions log records into the td_commissions table
def export_td_comm_log_records():
    td_comm_log_data = cur.execute(''' SELECT * FROM td_commissions ''')
    for row in td_comm_log_data:
        td_comm_log_rows.append(row)
    try:
        log_entry = td.comm_log_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in td_comm_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_td_comm_log_entry_lst.append(row)
    
        log_entry = export_td_comm_log_entry_lst
        database.td_commissions_log_add_many(log_entry)
    except:
        pass
export_td_comm_log_records()
################################## End add td_commissions log RECORDS ################################################

################################## Begin add td_regulation_fee log RECORDS ############################################
# add td_regulation_fee log records

# td_reg_fee_log_rows contains a list of the rows in the td_regulation_fee table
td_reg_fee_log_rows = []

# export_td_reg_fee_log_entry_lst contains a list of the rows that will be exported into the td_regulation_fee table
export_td_reg_fee_log_entry_lst = []

# export_td_reg_fee_log_records function check for UNIQUE CONSTRANT ERRORS
# exports the td broker regulation fee log records into the td_regulation_fee table
def export_td_reg_fee_log_records():
    td_reg_fee_log_data = cur.execute(''' SELECT * FROM td_regulation_fee ''')
    for row in td_reg_fee_log_data:
        td_reg_fee_log_rows.append(row)
    try:
        log_entry = td.reg_fee_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in td_reg_fee_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_td_reg_fee_log_entry_lst.append(row)

        log_entry = export_td_reg_fee_log_entry_lst
        database.td_reg_fee_log_add_many(log_entry)
    except:
        pass
export_td_reg_fee_log_records()
################################## End add td_regulation_fee log RECORDS ##############################################

################################## Begin add td_misc_income log RECORDS ############################################
# add td_misc_income log records

# td_misc_income_log_rows contains a list of the rows in the td_misc_income table
td_misc_income_log_rows = []

# export_td_misc_income_log_entry_lst contains a list of the rows that will be exported into the td_misc_income table
export_td_misc_income_log_entry_lst = []

# export_td_misc_income_log_records function check for UNIQUE CONSTRANT ERRORS
# exports the td broker miscellaneous income log records into the td_misc_income table
def export_td_misc_income_log_records():
    td_misc_income_log_data = cur.execute(''' SELECT * FROM td_misc_income ''')
    for row in td_misc_income_log_data:
        td_misc_income_log_rows.append(row)
    try:
        log_entry = td.misc_income_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in td_misc_income_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_td_misc_income_log_entry_lst.append(row)

        log_entry = export_td_misc_income_log_entry_lst
        database.td_misc_income_log_add_many(log_entry)
    except:
        pass
export_td_misc_income_log_records()
################################## End add td_misc_income log RECORDS ############################################

################################## Begin add td_misc_debit log RECORDS ############################################
# add td_misc_debit log records

# td_misc_debit_log_rows contains a list of the rows in the td_misc_debit table
td_misc_debit_log_rows = []

# export_td_misc_debit_log_entry_lst contains a list of the rows that will be exported into the td_misc_debit table
export_td_misc_debit_log_entry_lst = []

# export_td_misc_debit_log_records function check for UNIQUE CONSTRANT ERRORS
# exports the td broker miscellaneous debit log records into the td_misc_debit table
def export_td_misc_debit_log_records():
    td_misc_debit_log_data = cur.execute(''' SELECT * FROM td_misc_debit ''')
    for row in td_misc_debit_log_data:
        td_misc_debit_log_rows.append(row)
    try:
        log_entry = td.misc_debit_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in td_misc_debit_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_td_misc_debit_log_entry_lst.append(row)

        log_entry = export_td_misc_debit_log_entry_lst
        database.td_misc_debit_log_add_many(log_entry)
    except:
        pass
export_td_misc_debit_log_records()
################################## End add td_misc_debit log RECORDS ############################################


################################## Begin add td_interest_income log RECORDS ############################################
# add td_interest_income log records

# td_interest_income_log_rows contains a list of the rows in the td_interest_income table
td_interest_income_log_rows = []

# export_td_interest_income_log_entry_lst contains a list of the rows that will be exported into the td_interest_income table
export_td_interest_income_log_entry_lst = []

# export_td_interest_income_log_records function check for UNIQUE CONSTRANT ERRORS
# exports the td broker miscellaneous debit log records into the td_interest_income table
def export_td_interest_income_log_records():
    td_interest_income_log_data = cur.execute(''' SELECT * FROM td_interest_income ''')
    for row in td_interest_income_log_data:
        td_interest_income_log_rows.append(row)
    try:
        log_entry = td.int_income_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in td_interest_income_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_td_interest_income_log_entry_lst.append(row)

        log_entry = export_td_interest_income_log_entry_lst
        database.td_interest_income_log_add_many(log_entry)
    except:
        pass
export_td_interest_income_log_records()
################################## End add td_interest_income log RECORDS ############################################

################################## Begin add td_interest_debit log RECORDS ############################################
# add td_interest_debit log records

# td_interest_debit_log_rows contains a list of the rows in the td_interest_debit table
td_interest_debit_log_rows = []

# export_td_interest_debit_log_entry_lst contains a list of the rows that will be exported into the td_interest_debit table
export_td_interest_debit_log_entry_lst = []

# export_td_interest_debit_log_records function check for UNIQUE CONSTRANT ERRORS
# exports the td broker miscellaneous debit log records into the td_interest_debit table
def export_td_interest_debit_log_records():
    td_interest_debit_log_data = cur.execute(''' SELECT * FROM td_interest_debit ''')
    for row in td_interest_debit_log_data:
        td_interest_debit_log_rows.append(row)
    try:
        log_entry = td.int_debit_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in td_interest_debit_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_td_interest_debit_log_entry_lst.append(row)

        log_entry = export_td_interest_debit_log_entry_lst
        database.td_interest_debit_log_add_many(log_entry)
    except:
        pass
export_td_interest_debit_log_records()
################################## End add td_interest_debit log RECORDS ############################################

################################# Begin add ib_options_log RECORDS ##############################################
# add ib_options_log records

# ib_options_log_rows contains a list of the rows in the ib_options_log table
ib_options_log_rows = []

# export_ib_options_log_entry_lst contains a list of the rows that will be exported into the ib_options_log table
export_ib_options_log_entry_lst = []

# export_ib_options_log_records function check for UNIQUE CONSTRANT ERRORS
# exports the ib broker options log records into the ib_options_log table
def export_ib_options_log_records():
    ib_options_log_data = cur.execute(''' SELECT * FROM ib_options_log ''')
    for row in ib_options_log_data:
        ib_options_log_rows.append(row)
    try:
        log_entry = ib.options_log_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in ib_options_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_ib_options_log_entry_lst.append(row)

        log_entry = export_ib_options_log_entry_lst
        database.ib_options_log_add_many(log_entry)
    except:
        pass

export_ib_options_log_records()
################################## End add ib_options_log RECORDS ##############################################
################################## Begin add ib_commissions_fee log RECORDS ##############################################
# add ib_commissions_fee log records

# ib_comm_fee_log_rows contains a list of the rows in the ib_commissions_fee table
ib_comm_fee_log_rows = []


# export_ib_comm_fee_log_entry_lst contains a list of the rows that will be exported into the ib_commissions_fee table
export_ib_comm_fee_log_entry_lst = []

# export_ib_comm_fee_log_records function check for UNIQUE CONSTRANT ERRORS
# exports the ib broker commissions log records into the ib_commissions_fee table
def export_ib_comm_fee_log_records():
    ib_comm_fee_log_data = cur.execute(''' SELECT * FROM ib_commissions_fee ''')
    for row in ib_comm_fee_log_data:
        ib_comm_fee_log_rows.append(row)
    try:
        log_entry = ib.comm_fee_log_export_records()
        for row in log_entry:
            row = tuple(row)
            if row in ib_comm_fee_log_rows:
                print("\n----------------UNIQUE CONSRAINT: duplicate row----------------------")
                print(row)
                pass
            else:
                export_ib_comm_fee_log_entry_lst.append(row)

        log_entry = export_ib_comm_fee_log_entry_lst
        database.ib_commissions_fee_log_add_many(log_entry)
    except:
        pass
export_ib_comm_fee_log_records()
################################## End add ib_commissions_fee log RECORDS ##############################################

############################## CLOSE THE DATABASE ##################################
print("app closed....")
conn.close()
############################## QUERY THE DATABASE ##################################
