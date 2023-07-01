
# import the modules
import database
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

####################### Begin: ChatGpt code ###########################
# function to query the database and display the results
def query_database(sql_statement):

    # connect to the database
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # execute the query
    cur.execute(f"SELECT * FROM {sql_statement}")

    # fetch all rows
    rows = cur.fetchall()

    # close the database connection
    cur.close()
    conn.close()

    # display the rows in a messagebox
    messagebox.showinfo('Query Results', str(rows))
####################### End: ChatGpt code ###########################

##### TEST #####
def query_database2(sql_statement):
    return messagebox.showinfo("Query results", str(sql_statement))
##### TEST #####

# potential model to query the database
# def query():
#     conn = sqlite3.connect('database.db')
#     cur = conn.cursor()
#     with conn:
#         cur.execute("SELECT * FROM ib_options_log")
#         records = cur.fetchall()
#         print_records = ''
#         for record in records:
#             print_records += str(record) + "\n"
#         query_label = Label(root, text=print_records)
#         query_label.grid(row=1,column=0,columnspan=7)
#     conn.commit()


# use the gui to run the export.py program 
# task see the lambda function examples in radio buttons
def func():
    pass

# function to hanlde the "File" menu options
def file_functionality():
    pass # add file menu functionality

# function to hanlde the "Edit" menu options
def edit_functionality():
    pass # add edit menu functionality

# function to hanlde the "View Query" menu options
def view_query_functionality():
    pass # add view query menu functionality


# function to hanlde the "Help" menu options
def help_functionality():
    pass # add help menu functionality

# create the root widget and a title
root = Tk()
root.title("Root:-----Database Query GUI App-----")
root.geometry("25x25")

# expand the frame to fit window resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# FIXME option menus are detatching  
# eliminate tear-off menus from the app
# root.option_add('*tearOff', FALSE)

# create a mainframe window inside the root widget
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

# create a menubar
menubar = Menu(mainframe)

# create the 'File' and its options
file_menu = Menu(menubar, tearoff=0) 
file_menu.add_command(label='New File', command=file_functionality)
file_menu.add_command(label='Open...', command=file_functionality)
file_menu.add_command(label='Save', command=file_functionality)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=file_menu)

# create the 'Edit' and its options
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label='Clear', command=edit_functionality)
edit_menu.add_command(label='Cut',command=edit_functionality)
edit_menu.add_command(label='Copy', command=edit_functionality)
edit_menu.add_command(label='Paste', command=edit_functionality)
edit_menu.add_command(label='Paste Selection', command=edit_functionality)
edit_menu.add_command(label='Undo', command=edit_functionality)
menubar.add_cascade(label='Edit', menu=edit_menu)

# create the 'View' and its options
# FIXME work on getting the output of the lamda function to display in a separate messagebox
view_query_menu = Menu(menubar, tearoff=0)
view_query_menu.add_command(label="All Rows", command=lambda: view_query_functionality(database.broker_show_all))
menubar.add_cascade(label='View Query', menu=view_query_menu)

# create the 'Help' and its options
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label='About', command=help_functionality)
help_menu.add_command(label='Link to github documentation', command=help_functionality)
menubar.add_cascade(label='Help', menu=help_menu)

# display menu
root.config(menu=menubar)

################ Begin: chatGPT code #####################
# create a button to trigger the qeury
button = ttk.Button(mainframe, text='Query Database', command=lambda: query_database2(database.tables_show_all()))
button.grid(column=1, row=2, sticky=(W,E))
################ End: chatGPT code #######################


# create the main loop of the program
root.mainloop()

