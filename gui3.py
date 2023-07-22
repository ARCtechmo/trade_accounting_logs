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

# clear the previous query results before adding new ones
def clear_results():
    return print('------------------TEST: clear previous results---------------------')

# function to query the database and display the results in a separate window
def show_all_rows(table_name):

    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # clear the previous results
    clear_results()

    # create and name a new window 
    window = Toplevel(root)
    window.title(f'Show All Query Results for {table_name}')

    # create the SQL statement
    SQL = f"SELECT * FROM {table_name}"

    # run the query and format the string output with one record on each line
    with conn:
        cur.execute(SQL)
        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"

        # create a text widget to display the results
        text_widget = Text(window, width=40, height=10)
        text_widget.insert(END, print_records)
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

# names of the query options
query_names = {
                'show all':'return all rows',
                'by year': 'return by year'
               }
# variables
query_name = StringVar()

# function return the query values
def run_query():
    pass


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

# create a button to run the query 
run_query_btn = ttk.Button(tbl_frm, 
                         text='Run Query',
                         command=show_all_rows,
                         default='active' )



# grid all the widgets
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
scrollbar.grid(column=1, row=0, rowspan=6, sticky=(N,S))
lbl.grid(column=2, row=1, padx=10, pady=5)
b1.grid(column=2, row=2, sticky=W, padx=20)
b2.grid(column=2, row=3, sticky=W, padx=20)
run_query_btn.grid(column=2, row=5, sticky=E, padx=5, pady=5)

# frame expands as the window expands and fixes row in place  
tbl_frm.grid_columnconfigure(0, weight=1)
tbl_frm.grid_rowconfigure(5, weight=1)

# set event bindings for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key
lbox.bind('<<ListboxSelect>>',show_all_rows)
lbox.bind('<Double-1>', show_all_rows)
root.bind('<Return>', show_all_rows)


# create the main loop of the program
root.mainloop()