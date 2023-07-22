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

# function to query the database and display the results in a separate window
def display_tables():

    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # SQL statement to retrieve the table
    # SQL = f'SELECT * FROM {table_name}'
    SQL = "SELECT name FROM sqlite_master WHERE type='table';"

    # Retrieve the table names using SQLite's PRAGMA statement
    with conn:
        cur.execute(SQL)
        table_names = [table[0] for table in cur.fetchall()]
        # records = cur.fetchall()
        # print_records = []
        # for record in records:
        #     print_records.append(str(record))
      
    # close the cursor and database connections
    cur.close()
    conn.close()

    # return print_records
    return table_names

# create the frame for the tables and place on the grid
tbl_frm = ttk.Frame(root, padding=(5,5,12,0))
tbl_frm.grid(column=0, row=0, sticky=(N,W,E,S))

 # Configure the grid to expand with window resizing
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# create a listbox that contains the tables within the frame
# table_items = ['table 1', 'table 2', 'table 3','table 4', 'table 5', 'table 6']
# tables = StringVar(value=table_items) 
# lbox = Listbox(tbl_frm, listvariable=tables, height=5)
# tables = StringVar(value=display_tables('brokers'))
tables = StringVar(value=display_tables())
lbox = Listbox(tbl_frm, listvariable=tables, height=15, width=30)
lbox.grid(column=0, row=0, rowspan=10, sticky=(N,S,E,W))

# create a vertical scrollbar
scrollbar = Scrollbar(tbl_frm, orient=VERTICAL)
scrollbar.grid(column=1, row=0, rowspan=6, sticky=(N,S))

# link the scrollbar to the listbox
lbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lbox.yview)

# create the main loop of the program
root.mainloop()