import database
import sqlite3
from tkinter import *
from tkinter import ttk

# connect to the database
import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# create the root widget and a title
root = Tk()
root.title("Root:-----Database Query GUI App-----")
root.geometry("25x25")

# eliminate tear-off menus from the app
root.option_add('*tearOff', FALSE)

# create a mainframe window inside the root widget
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

# expand the frame to fit window resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create a menubar
menubar = Menu(mainframe)

# TASK: place within a function
# same as root.option_add('*tearOff, False)
file = Menu(menubar, tearoff=0) 
edit = Menu(menubar, tearoff=0)
view = Menu(menubar, tearoff=0)
query = Menu(menubar, tearoff=0)
help = Menu(menubar, tearoff=0)
table_view = Menu(view, tearoff=0)

# TASK: place within a function
# add menu items
menubar.add_cascade(label='File', menu=file)
menubar.add_cascade(label='Edit', menu=edit)
menubar.add_cascade(label='View', menu=view)
menubar.add_cascade(label='Query',menu=query)
menubar.add_cascade(label='Help', menu=help)

# TASK: place within a function
# add file menu commands
file.add_command(label='New File', command= None)
file.add_command(label='Open...', command= None)
file.add_command(label='Save', command= None)
file.add_separator()
file.add_command(label='Exit', command= root.destroy)

# TASK: place within a function
# add edit menu commands
edit.add_command(label='Create', command=None)
edit.add_command(label='Read',command=None)
edit.add_command(label='Update', command=None)
edit.add_command(label='Delete', command=None)

# TASK: place within a function
# add view table_view submenus and commands
table_view = Menu(view)
view.add_command(label='Show Tables', command=database.tables_show_all)  
view.add_command(label='Show brokers', command=database.broker_show_all)

# START HERE NEXT 
# add label to print output of view results
results = StringVar()
query_label = ttk.Label(mainframe, text="Query Results").grid(column=0, columnspan=5, row=15, sticky=(W,E,N,S))
query_label = ttk.Label(mainframe, textvariable=results).grid(column=0, columnspan=5, row=5)

# TASK: place within a function
# add help menu command
help.add_command(label='Link to github documentation', command=None)


# use the gui to run the export.py program 
# task see the lambda function examples in radio buttons
def func():
    pass

# model to query the database
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


# close the database
conn.close()

# display menu
root.config(menu=menubar)

 # create the main loop of the program
root.mainloop()

