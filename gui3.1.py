# TASK: test all of the functions and the conditionals to ensure error messages reutrn correctly 
# TASK: added more functions for sql queries (see the sql file in the downloads directory)

from tkinter import *
from tkinter import ttk
import database
import sqlite3

# Function to handle menu item selection
def menuItemSelected():
    pass  # Replace with your desired functionality

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

# Create view menu
viewMenu = Menu(menubar)
menubar.add_cascade(label="View Query", menu=viewMenu)
viewMenu.add_command(label="Query 1", command=menuItemSelected)
viewMenu.add_command(label="Query 2", command=menuItemSelected)

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
                                command=lambda: select_columns(None))

# create a button to run the query
# link the show_all_rows function to the "Run Query" button 
run_query_btn = ttk.Button(tbl_frm, 
                         text='Run Query',
                         command=run_query,
                         default='active' )

# grid all the widgets
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
scrollbar.grid(column=1, row=0, rowspan=6, sticky=(N,S))
lbl.grid(column=2, row=1, padx=10, pady=5, sticky=W)
b1.grid(column=2, row=2, sticky=W, padx=20)
b2.grid(column=2, row=3, sticky=W, padx=20)
run_query_btn.grid(column=2, row=7, sticky=E, padx=5, pady=5)

# place the year entry label on the grid
# place the select column button below the year entry label
# year_label.grid(column=2, row=4, sticky=E, padx=5, pady=5)
year_entry.grid(column=3, row=4, sticky=W, padx=5, pady=5)
select_columns_btn.grid(column=2, row=4, sticky=E, padx=5, pady=5)

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

