
# FIXME Security: Using string formats to create SQL statements (e.g., f"SELECT * FROM {table_name}") exposes the application to SQL injection attacks 
# TASK: Finish the query menu item functions

from tkinter import *
from tkinter import ttk
import database
import sqlite3


# Global variable to keep track of the query_output_frame
query_output_frame = None

# Function to display Gross P/L data within the tbl_frm
def display_gross_pl():
    
    # clear the current content
    global query_output_frame
    if query_output_frame:
        query_output_frame.destroy()
    
    # Retrieve year from entry
    year = year_entry.get()

    # Create a new frame to hold the labels
    query_output_frame = Frame(bg="white")
    query_output_frame.grid(
        row=6, column=0, columnspan=4, sticky=W, pady=10, padx=10
        ) 

    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    
    # SQL statement to fetch Gross P/L
    SQL_fx = "SELECT SUM(gross) FROM fx_log WHERE entry_year = ?;"
    SQL_ib = "SELECT SUM(gross) FROM ib_options_log WHERE year = ?;"
    SQL_td = "SELECT SUM(gross) FROM td_options_log WHERE year = ?;"
    
    # Execute the queries and fetch the results
    with conn:

        cur.execute(SQL_fx, (year,))
        records_fx = cur.fetchall()
        sum_fx = records_fx[0][0] if records_fx and records_fx[0][0] is not None else 0
        formatted_fx = "{:.2f}".format(sum_fx)

        cur.execute(SQL_ib, (year,))
        records_ib = cur.fetchall()
        sum_ib = records_ib[0][0] if records_ib and records_ib[0][0] is not None else 0
        formatted_ib = "{:.2f}".format(sum_ib)

        cur.execute(SQL_td, (year,))
        records_td = cur.fetchall()
        sum_td = records_td[0][0] if records_td and records_td[0][0] is not None else 0
        formatted_td = "{:.2f}".format(sum_td)

        # Calculate the total Gross P/L
        total_gross_pl = sum_fx + sum_ib + sum_td

        # Format the Gross P/L value to two decimal places
        formatted_gross_pl = "{:.2f}".format(total_gross_pl)

        # Create labels inside the output frame to display individual Gross P/L
        fx_label = Label(query_output_frame, text=f"FX Gross P/L: {formatted_fx}", bg="white", wraplength=250, justify="left",font='bold')
        fx_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        ib_label = Label(query_output_frame, text=f"IB Options Gross P/L: {formatted_ib}", bg="white", wraplength=250, justify="left",font='bold')
        ib_label.grid(row=1, column=0, padx=10, pady=10,sticky=W)

        td_label = Label(query_output_frame, text=f"TD Options Gross P/L: {formatted_td}", bg="white", wraplength=250, justify="left",font='bold')
        td_label.grid(row=2, column=0, padx=10, pady=10,sticky=W)

        gross_pl_label = Label(query_output_frame, text=f"Total Gross P/L: {formatted_gross_pl}", bg="white", wraplength=250, justify="left",font='bold')
        gross_pl_label.grid(row=3, column=0, padx=10, pady=10,sticky=W)  

    # close the cursor and database connections
    cur.close()
    conn.close()

# Function to display commissions  data within the tbl_frm
def display_commissions():

    # clear the current content
    global query_output_frame
    if query_output_frame:
        query_output_frame.destroy()
    
    # Retrieve year from entry
    year = year_entry.get()

    # Create a new frame to hold the labels
    query_output_frame = Frame(bg="white")
    query_output_frame.grid(
        row=6, column=0, columnspan=4, sticky=W, pady=10, padx=10
        ) 
    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    
    # SQL statement to fetch Gross P/L
    SQL_fx = "SELECT SUM(commissions_cost) FROM fx_commissions WHERE entry_year = ?;"
    SQL_ib = "SELECT SUM(comm_cost) FROM ib_commissions_fee WHERE year = ?;"
    SQL_td = "SELECT SUM(comm_cost) FROM td_commissions WHERE year = ?;"
    
    # Execute the queries and fetch the results
    with conn:

        cur.execute(SQL_fx,(year,))
        records_fx = cur.fetchall()
        sum_fx = records_fx[0][0] if records_fx and records_fx[0][0] is not None else 0
        formatted_fx = "{:.2f}".format(sum_fx)

        cur.execute(SQL_ib,(year,))
        records_ib = cur.fetchall()
        sum_ib = records_ib[0][0] if records_ib and records_ib[0][0] is not None else 0
        formatted_ib = "{:.2f}".format(sum_ib)
        
        cur.execute(SQL_td,(year,))
        records_td = cur.fetchall()
        sum_td = records_td[0][0] if records_td and records_td[0][0] is not None else 0
        formatted_td = "{:.2f}".format(sum_td)

        # Calculate the total commissions
        total_gross_pl = sum_fx + sum_ib + sum_td

        # Format commissions value to two decimal places
        formatted_gross_pl = "{:.2f}".format(total_gross_pl)

        # Create labels inside the output frame to display individual commissions
        fx_label = Label(query_output_frame, text=f"FX comm: {formatted_fx}", bg="white", wraplength=250, justify="left",font='bold')
        fx_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        ib_label = Label(query_output_frame, text=f"IB Options comm: {formatted_ib}", bg="white", wraplength=250, justify="left",font='bold')
        ib_label.grid(row=1, column=0, padx=10, pady=10,sticky=W, columnspan=3)

        td_label = Label(query_output_frame, text=f"TD Options comm: {formatted_td}", bg="white", wraplength=250, justify="left",font='bold')
        td_label.grid(row=2, column=0, padx=10, pady=10,sticky=W)

        gross_pl_label = Label(query_output_frame, text=f"Total comm: {formatted_gross_pl}", bg="white", wraplength=250, justify="left",font='bold')
        gross_pl_label.grid(row=3, column=0, padx=10, pady=10,sticky=W)  

    # close the cursor and database connections
    cur.close()
    conn.close()

# Function to display interest data within the tbl_frm
def interest():
    
    # clear the current content
    global query_output_frame
    if query_output_frame:
        query_output_frame.destroy()
    
    # Retrieve year from entry
    year = year_entry.get()

    # Create a new frame to hold the labels
    query_output_frame = Frame(bg="white")
    query_output_frame.grid(
        row=6, column=0, columnspan=4, sticky=W, pady=10, padx=10
        ) 

    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    
    # SQL statement to fetch Gross P/L
    SQL_fx_debit = "SELECT SUM(interest_debit) FROM fx_interest_debit WHERE entry_year = ?;"
    SQL_fx_income = "SELECT SUM(interest_credit) FROM fx_interest_income WHERE entry_year = ?;"
    SQL_td_debit = "SELECT SUM(int_adj_debit) FROM td_interest_debit WHERE year = ?;"
    SQL_td_credit = "SELECT SUM(int_adj_income) FROM td_interest_income WHERE year = ?;"
    
    # Execute the queries and fetch the results
    with conn:

        cur.execute(SQL_fx_debit, (year,))
        records_fx_int_debit = cur.fetchall()
        sum_fx_int_debit = records_fx_int_debit[0][0] if records_fx_int_debit and records_fx_int_debit[0][0] is not None else 0
        formatted_fx_int_debit = "{:.2f}".format(sum_fx_int_debit)

        cur.execute(SQL_fx_income, (year,))
        records_fx_int_income = cur.fetchall()
        sum_fx_int_income = records_fx_int_income[0][0] if records_fx_int_income and records_fx_int_income[0][0] is not None else 0
        formatted_fx_int_credit = "{:.2f}".format(sum_fx_int_income)
       
        cur.execute(SQL_td_debit, (year,))
        records_td_int_debit = cur.fetchall()
        sum_td_int_debit = records_td_int_debit[0][0] if records_td_int_debit and records_td_int_debit[0][0] is not None else 0
        formatted_td_int_debit = "{:.2f}".format(sum_td_int_debit)

        cur.execute(SQL_td_credit, (year,))
        records_td_int_credit = cur.fetchall()
        sum_td_int_income = records_td_int_credit[0][0] if records_td_int_credit and records_td_int_credit[0][0] is not None else 0
        formatted_td_int_credit = "{:.2f}".format(sum_td_int_income)

        # Calculate the total net interest
        fx_net_int = sum_fx_int_debit + sum_fx_int_income 
        td_net_int = sum_td_int_debit + sum_td_int_income

        # Format the net interest value to two decimal places
        formatted_fx_net_int = "{:.2f}".format(fx_net_int)
        formatted_td_net_int = "{:.2f}".format(td_net_int)

        # Create labels inside the output frame to display interest
        fx_label_debit = Label(query_output_frame, text=f"FX_interest_debit: {formatted_fx_int_debit}", bg="white", wraplength=250, justify="left",font='bold')
        fx_label_debit.grid(row=0, column=0, padx=10, pady=0, sticky=W)
        fx_label_income = Label(query_output_frame, text=f"FX_interest_income: {formatted_fx_int_credit}", bg="white", wraplength=250, justify="left",font='bold')
        fx_label_income.grid(row=1, column=0, padx=10, pady=0, sticky=W)
        net_fx_int_label = Label(query_output_frame, text=f"Net_FX_interest: {formatted_fx_net_int}", bg="white", wraplength=250, justify="left",font='bold')
        net_fx_int_label.grid(row=2, column=0, padx=10, pady=0,sticky=W)  
        td_label_int_debit = Label(query_output_frame, text=f"\nTD_interest_debit: {formatted_td_int_debit}", bg="white", wraplength=250, justify="left",font='bold')
        td_label_int_debit.grid(row=3, column=0, padx=10, pady=0,sticky=W)
        td_label_int_credit = Label(query_output_frame, text=f"TD_interest_income: {formatted_td_int_credit}", bg="white", wraplength=250, justify="left",font='bold')
        td_label_int_credit.grid(row=4, column=0, padx=10, pady=0,sticky=W)
        net_td_int_label = Label(query_output_frame, text=f"Net_TD_interest: {formatted_td_net_int}", bg="white", wraplength=250, justify="left",font='bold')
        net_td_int_label.grid(row=5, column=0, padx=10, pady=0,sticky=W)  

    # close the cursor and database connections
    cur.close()
    conn.close()

# Function to display fees data within the tbl_frm
def fees():

    # clear the current content
    global query_output_frame
    if query_output_frame:
        query_output_frame.destroy()
    
    # Retrieve year from entry
    year = year_entry.get()

    # Create a new frame to hold the labels
    query_output_frame = Frame(bg="white")
    query_output_frame.grid(
        row=6, column=0, columnspan=4, sticky=W, pady=10, padx=10
        ) 
    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    
    # SQL statement to fetch fees
    SQL_ib = "SELECT SUM(fee) FROM ib_other_fee WHERE year = ?;"
    SQL_td = "SELECT SUM(reg_fee) FROM td_regulation_fee WHERE year = ?;"
    
    # Execute the queries and fetch the results
    with conn:

        cur.execute(SQL_ib,(year,))
        records_ib = cur.fetchall()
        sum_ib = records_ib[0][0] if records_ib and records_ib[0][0] is not None else 0
        formatted_ib = "{:.2f}".format(sum_ib)
        
        cur.execute(SQL_td,(year,))
        records_td = cur.fetchall()
        sum_td = records_td[0][0] if records_td and records_td[0][0] is not None else 0
        formatted_td = "{:.2f}".format(sum_td)

        # Calculate the total fees
        total_fees = sum_ib + sum_td

        # Format fee values to two decimal places
        formatted_fees = "{:.2f}".format(total_fees)

        # Create labels inside the output frame to display individual fees
        ib_label = Label(query_output_frame, text=f"IB Fees: {formatted_ib}", bg="white", wraplength=250, justify="left",font='bold')
        ib_label.grid(row=0, column=0, padx=10, pady=10,sticky=W, columnspan=3)

        td_label = Label(query_output_frame, text=f"TD Fees: {formatted_td}", bg="white", wraplength=250, justify="left",font='bold')
        td_label.grid(row=1, column=0, padx=10, pady=10,sticky=W)

        gross_fee_label = Label(query_output_frame, text=f"Total Fees: {formatted_fees}", bg="white", wraplength=250, justify="left",font='bold')
        gross_fee_label.grid(row=2, column=0, padx=10, pady=10,sticky=W)  

    # close the cursor and database connections
    cur.close()
    conn.close()

# Function to display commissions  data within the tbl_frm
def misc_debit_credit():

    # clear the current content
    global query_output_frame
    if query_output_frame:
        query_output_frame.destroy()
    
    # Retrieve year from entry
    year = year_entry.get()

    # Create a new frame to hold the labels
    query_output_frame = Frame(bg="white")
    query_output_frame.grid(
        row=6, column=0, columnspan=4, sticky=W, pady=10, padx=10
        ) 
    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    
    # SQL statement to fetch Gross P/L
    SQL_fx = "SELECT SUM(broker_credit) FROM fx_broker_credit_income WHERE entry_year = ?;"
    SQL_td_misc_debit = "SELECT SUM(misc_debit) FROM td_misc_debit WHERE year = ?;"
    SQL_td_misc_income = "SELECT SUM(misc_credit) FROM td_misc_income WHERE year = ?;"
    
    # Execute the queries and fetch the results
    with conn:

        cur.execute(SQL_fx,(year,))
        records_fx = cur.fetchall()
        sum_fx = records_fx[0][0] if records_fx and records_fx[0][0] is not None else 0
        formatted_fx = "{:.2f}".format(sum_fx)
        
        cur.execute(SQL_td_misc_debit,(year,))
        records_td_misc_debit = cur.fetchall()
        sum_td_misc_debit = records_td_misc_debit[0][0] if records_td_misc_debit and records_td_misc_debit[0][0] is not None else 0
        formatted_td_misc_debit = "{:.2f}".format(sum_td_misc_debit)

        cur.execute(SQL_td_misc_income,(year,))
        records_td_misc_income = cur.fetchall()
        sum_td_misc_income = records_td_misc_income[0][0] if records_td_misc_income and records_td_misc_income[0][0] is not None else 0
        formatted_td_misc_income = "{:.2f}".format(sum_td_misc_income)

        # Create labels inside the output frame to display individual commissions
        fx_label = Label(query_output_frame, text=f"FX Broker Credit: {formatted_fx}", bg="white", wraplength=250, justify="left",font='bold')
        fx_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        td_label_misc_debit = Label(query_output_frame, text=f"TD Misc Debit: {formatted_td_misc_debit}", bg="white", wraplength=250, justify="left",font='bold')
        td_label_misc_debit.grid(row=1, column=0, padx=10, pady=10,sticky=W)

        td_label_misc_income = Label(query_output_frame, text=f"TD Misc Credit: {formatted_td_misc_income}", bg="white", wraplength=250, justify="left",font='bold')
        td_label_misc_income.grid(row=1, column=0, padx=10, pady=10,sticky=W)

    # close the cursor and database connections
    cur.close()
    conn.close()

# Function to handle menu item selection
def menuItemSelected(option=None):

    # clear the current content
    global query_output_frame
    if query_output_frame:
        query_output_frame.destroy()

    if option == "Gross P/L":
        display_gross_pl()

    elif option == "Commissions":
        display_commissions()

    elif option == "Interest":
        interest()

    elif option == "Fees":
        fees()

    elif option == "Misc Credits/Debits":
        misc_debit_credit()

    elif option == "Clear Results":
        if query_output_frame:
            query_output_frame.destroy()
    else:
        print('Other options selected')

# create the root and window size
root = Tk()
root.title("Root:-----Database Query GUI App-----")
root.geometry("50x50") 
root.option_add('*tearOff', FALSE)

# Create menu bar
menubar = Menu(root)
root.config(menu=menubar)

# Create file menu
fileMenu = Menu(menubar)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=menuItemSelected)
fileMenu.add_command(label="Save", command=menuItemSelected)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# Create edit menu
editMenu = Menu(menubar)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=menuItemSelected)
editMenu.add_command(label="Copy", command=menuItemSelected)
editMenu.add_command(label="Paste", command=menuItemSelected)

# Create view query menu
viewMenu = Menu(menubar)
menubar.add_cascade(label="View Query", menu=viewMenu)
viewMenu.add_command(label="Gross P/L", command=lambda: menuItemSelected("Gross P/L"))
viewMenu.add_command(label="Commissions", command=lambda: menuItemSelected("Commissions"))
viewMenu.add_command(label="Interest", command=lambda: menuItemSelected("Interest"))
viewMenu.add_command(label="Fees", command=lambda: menuItemSelected("Fees"))
viewMenu.add_command(label="Misc Credits/Debits", command=lambda: menuItemSelected("Misc Credits/Debits"))
viewMenu.add_command(label="Non Trading Revenue", command=lambda: menuItemSelected("Non Trading Revenue"))
viewMenu.add_command(label="Non Trading Expense", command=lambda: menuItemSelected("Non Trading Expense"))
viewMenu.add_command(label="Roundtrip Trades", command=lambda: menuItemSelected("Roundtrip Trades"))
viewMenu.add_command(label="Clear Results", command=lambda: menuItemSelected("Clear Results"))

# Create help menu
helpMenu = Menu(menubar)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=menuItemSelected)
helpMenu.add_command(label="Help", command=menuItemSelected)

# names of the query options
query_names = {
                'show all':'return all columns and rows',
                'by year': 'return selected columns by year'
               }
# variable converts the queries into a string
query_name = StringVar()

# variables to store the selected columns
selected_columns = []
checkboxes = []

# display all tables
def display_tables():

    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # SQL statement to retrieve the table
    SQL = "SELECT name FROM sqlite_master WHERE type='table';"

    # Retrieve the table names using SQLite's PRAGMA statement
    with conn:
        cur.execute(SQL)
        table_names = [table[0] for table in cur.fetchall()]
            
    # close the cursor and database connections
    cur.close()
    conn.close()

    # return the tables
    return table_names

def format_records(column_names, records):

    # get the maximum width of each column
    column_widths = [len(name) for name in column_names]
    for record in records:
        for i, cell in enumerate(record):
            column_widths[i] = max(column_widths[i], len(str(cell)))

    # create format string with appropriate width for each column
    format_string = " | ".join("{:<" + str(width) + "}" for width in column_widths)

    # format each row
    formatted_records = [format_string.format(*record) for record in records]
    
    # format column names and add them at the start
    formatted_records.insert(0, format_string.format(*column_names))

    return formatted_records

# error message for invalid entries when selecting tables and fields
def show_error(message):
    error_window = Toplevel(root)
    error_window.title("Error")
    error_label = Label(error_window, text=message, wraplength=250, justify="left")
    error_label.grid(row=0, column=0, padx=20, pady=10)

# get column names for a given table
def get_columns(table_name):

    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # SQL statement to get columns
    SQL = f"PRAGMA table_info({table_name})"
    with conn:
        cur.execute(SQL)
        columns = [column[1] for column in cur.fetchall()]

    # close the cursor and database connections
    cur.close()
    conn.close()

    return columns

# function queries the database and displays the results in a separate window
# add event parameter to show_all_rows function
# accept events triggered from listbox selection/double-clicks
def show_all_rows(event=None):

    # get selected table name from the listbox
    table_name = lbox.get(ACTIVE)

    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # create and name a new window 
    window = Toplevel(root)
    window.title(f'Show All Query Results for {table_name}')

    # create the SQL statement
    SQL = f"SELECT * FROM {table_name}"

    # run the query and format the string output with one record on each line
    with conn:
        cur.execute(SQL)
        records = cur.fetchall()

        # get column names
        column_names = [desc[0] for desc in cur.description]
        formatted_records = format_records(column_names, records)

        # create a text widget to display the results
        text_widget = Text(window, width=40, height=10, font='Courier')

        # Configure tags for odd and even rows
        text_widget.tag_configure('odd', background='white')
        text_widget.tag_configure('even', background='#e6f2f0')
        text_widget.tag_configure('bold', font=('Arial', 10, 'bold'))

        # *** DO NOT DELETE THIS BLOCK OF CODE ***
        # Insert records with appropriate tag (odd or even)
        for i, record in enumerate(formatted_records):
            tag = 'odd' if i % 2 == 0 else 'even'
            text_widget.insert(END, record + "\n", tag)
        # *** DO NOT DELETE THIS BLOCK OF CODE ***
        
        text_widget.grid(row=0,column=0, sticky=(N,S,E,W))

        # create a scrollbar and associate it with the text widget
        my_scrollbar = Scrollbar(window, command=text_widget.yview)
        my_scrollbar.grid(row=0, column=1, sticky=((N,S)))
        text_widget.config(yscrollcommand=my_scrollbar.set)

    # Configure the grid to expand with window resizing
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # close the cursor and database connections
    cur.close()
    conn.close()

# function returns values by year selection
def show_by_year(table_name, year):

    if not selected_columns:
        return show_error("Please select at least one column.")
        
    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # Determine if the table has 'year' or 'entry_year' field
    SQL_check_year_field = f"PRAGMA table_info({table_name})"
    cur.execute(SQL_check_year_field)
    columns = [column[1] for column in cur.fetchall()]

    # Include only the selected columns
    selected_columns_sql = ', '.join(column for column in selected_columns if column in columns)
    year_field = 'year' if 'year' in columns else 'entry_year' if 'entry_year' in columns else None

    if year_field:

        # create and name a new window 
        window = Toplevel(root)
        window.title(f'Show All Query Results for {table_name} in {year}')
        
        # create the SQL statement
        SQL = f"SELECT {selected_columns_sql} FROM {table_name} WHERE {year_field}={year}"

        # run the query and format the string output with one record on each line
        with conn:
            cur.execute(SQL)
            records = cur.fetchall()

            # get column names
            column_names = [desc[0] for desc in cur.description]
            formatted_records = format_records(column_names, records)

            # create a text widget to display the results
            text_widget = Text(window, width=40, height=10, font='Courier')

            # Configure tags for odd and even rows
            text_widget.tag_configure('odd', background='white')
            text_widget.tag_configure('even', background='#e6f2f0')
            text_widget.tag_configure('bold', font=('Arial', 10, 'bold'))

            # *** DO NOT DELETE THIS BLOCK OF CODE ***
            # Insert records with appropriate tag (odd or even)
            for i, record in enumerate(formatted_records):
                tag = 'odd' if i % 2 == 0 else 'even'
                text_widget.insert(END, record + "\n", tag)
            # *** DO NOT DELETE THIS BLOCK OF CODE ***
            
            text_widget.grid(row=0,column=0, sticky=(N,S,E,W))

            # create a scrollbar and associate it with the text widget
            my_scrollbar = Scrollbar(window, command=text_widget.yview)
            my_scrollbar.grid(row=0, column=1, sticky=((N,S)))
            text_widget.config(yscrollcommand=my_scrollbar.set)

        # Configure the grid to expand with window resizing
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

    else:
        show_error(f"Table {table_name} does not contain 'year' or 'entry_year' field")

    # close the cursor and database connections
    cur.close()
    conn.close()

# apply selected column
def apply_selected_columns():
    selected_columns.clear()
    for column, column_var in checkboxes:
        if column_var.get():
            selected_columns.append(column)
    year = year_entry.get()
    table_name = lbox.get(ACTIVE)
    if not year:
        return show_error("apply_selected_columns() func:------Enter a year.-----.")
    if year and not year.isdigit():
        return show_error("apply_selected_columns() func:------Year must be a number-----.")
    else:
        return show_by_year(table_name, year)

# NOTE: FUNCTION MUST BE BELOW THE FUNCTION apply_selected_columns()
# NOTE: FUNCTION MUST BE BELOW THE FUNCTION get_columns()
# Create checkboxes for the columns 
def select_columns(event):

    # clear previous checkboxes
    checkboxes.clear()

    # retrieve column names
    table_name = lbox.get(ACTIVE)
    columns = get_columns(table_name)

    select_columns_window = Toplevel(root)
    select_columns_window.title(f'Select Columns for {table_name}')

    for column in columns:
        column_var = BooleanVar()
        checkbox = Checkbutton(select_columns_window, text=column, variable=column_var)
        checkbox.grid(sticky=W)
        checkboxes.append((column, column_var))

    apply_button = Button(select_columns_window, text="Apply", command=apply_selected_columns)
    apply_button.grid()

# return the query values when user clicks on the query button
def run_query():

    # get table name from selected listbox item
    table_name = lbox.get(ACTIVE)

    # get radio button value
    query_type = query_name.get()

    # select function to run based on radio button value
    if query_type == 'show all':
        return show_all_rows(table_name)
        
    elif query_type == 'by year':
        year = year_entry.get()
        if not year:
            return show_error("run_query() func:----Please enter a year.----")
        if not year.isdigit():
            return show_error("run_query() func:----Year must be a number.----")
        if not any (column_var.get() for _, column_var in checkboxes):
            return show_error("run_query() func:----Please select at least one column.----")
    else:
        year = year_entry.get()
        return show_by_year(table_name, year)

# function executed when user double-clicks on a table in the listbox
def on_double_click(event):

    # get table name from selected listbox item
    table_name = lbox.get(ACTIVE)

    # get radio button value
    query_type = query_name.get()

    # select function to run based on radio button value
    if query_type == 'show all':
        return show_all_rows(table_name)
        
    elif query_type == 'by year':
        year = year_entry.get()
        if not year:
            return show_error("on_double_click() func:----Please enter a year.----")
        if not year.isdigit():
            return show_error("on_double_click() func:----Year must be a number.----")
        if not any (column_var.get() for _, column_var in checkboxes):
            return show_error("on_double_click() func:----Please select at least one column.----")
    else:
        year = year_entry.get()
        return show_by_year(table_name, year)

# create the frame for the tables and place on the grid
tbl_frm = ttk.Frame(root, padding=(5,5,12,0))
tbl_frm.grid(column=0, row=0, sticky=(N,W,E,S))

 # Configure the grid to expand with window resizing
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# create a listbox that contains the tables within the frame
tables = StringVar(value=display_tables())
lbox = Listbox(tbl_frm, listvariable=tables, height=15, width=30)

# create a vertical scrollbar
scrollbar = Scrollbar(tbl_frm, orient=VERTICAL)

# link the scrollbar to the listbox
lbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lbox.yview)

# create a label for the query options and place on the grid
lbl = ttk.Label(tbl_frm, text="Select a query option:")
year_entry = ttk.Entry(tbl_frm)

# create the radio buttons for the query options
b1 = ttk.Radiobutton(tbl_frm, 
                     text=query_names["show all"],
                     variable=query_name,
                     value='show all'
                     )  

b2 = ttk.Radiobutton(tbl_frm, 
                     text=query_names["by year"],
                     variable=query_name,
                     value='by year'
                     )  

select_columns_btn = ttk.Button(tbl_frm, 
                                text='Select columns and enter year.',
                                command=lambda: select_columns(None)
                                )

# create a button to run the query
# link the show_all_rows function to the "Run Query" button 
run_query_btn = ttk.Button(root, 
                         text='Run Query',
                         command=run_query,
                         default='active',
                         width=10)

# grid all the widgets
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
scrollbar.grid(column=1, row=0, rowspan=6, sticky=(N,S))
lbl.grid(column=2, row=1, padx=10, pady=5, sticky=W)
b1.grid(column=2, row=2, sticky=W, padx=20)
b2.grid(column=2, row=3, sticky=W, padx=20)

# place the year entry label on the grid
# place the select column button below the year entry label
# year_label.grid(column=2, row=4, sticky=E, padx=5, pady=5)
year_entry.grid(column=3, row=4, sticky=W, padx=5, pady=5)
select_columns_btn.grid(column=2, row=4, sticky=E, padx=5, pady=5)
run_query_btn.grid(column=2, row=6, sticky=(S,E), padx=5, pady=5)

# frame expands as the window expands and fixes row in place  
tbl_frm.grid_columnconfigure(0, weight=1)
tbl_frm.grid_rowconfigure(5, weight=1)

# set event bindings 
# events fire when the selection in the listbox changes
# when the user double clicks the list
lbox.bind('<Double-1>', on_double_click)

# set the starting state of the interface
# Select the first table in the listbox and the first radio button as the default
lbox.selection_set(0)
query_name.set('show all')

# colorize alternating lines of the Listbox
for i in range(0,len(lbox.get(0, END)),2):
    lbox.itemconfigure(i, background='#f0f0ff')

# create the main loop of the program
root.mainloop()

