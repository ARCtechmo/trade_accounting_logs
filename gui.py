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

# display menu
root.config(menu=menubar)

# TASK: place within a function
file_menu = Menu(menubar, tearoff=0) 
edit_menu = Menu(menubar, tearoff=0)
view_menu = Menu(menubar, tearoff=0)
query_menu = Menu(menubar, tearoff=0)
help_menu = Menu(menubar, tearoff=0)
table_view = Menu(view_menu, tearoff=0)

# TASK: place within a function
# add menu items
menubar.add_cascade(label='File', menu=file_menu)
menubar.add_cascade(label='Edit', menu=edit_menu)
menubar.add_cascade(label='View', menu=view_menu)
menubar.add_cascade(label='Query',menu=query_menu)
menubar.add_cascade(label='Help', menu=help_menu)

# TASK: place within a function
# add file menu commands

file_menu.add_command(label='New File', command=None)
file_menu.add_command(label='Open...', command=None)
file_menu.add_command(label='Save', command=None)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

# TASK: place within a function
# add edit menu commands
edit_menu.add_command(label='Clear', command=None)
edit_menu.add_command(label='Cut',command=None)
edit_menu.add_command(label='Copy', command=None)
edit_menu.add_command(label='Paste', command=None)
edit_menu.add_command(label='Paste Selection', command=None)
edit_menu.add_command(label='Undo', command=None)

# TASK: place within a function
# add view table_view submenus and commands
# fixme maybe use Menubutton
table_view = Menu(view_menu)
view_menu.add_command(label='Show Tables', command=database.tables_show_all)
test_menu_button = ttk.Menubutton(text="test Menubutton")


# FIXME get this to print within the GUI
# todo Read binding event handlers
# add label to print output of view results
view_results_label = ttk.Label(mainframe, text="View Results").grid(column=0, columnspan=5, row=5, sticky=(W,E,N,S))
# view_results_label = ttk.Label(root, text=testFunc).grid(column=0, columnspan=5, row=5, sticky=(W,E,N,S))

# FIXME: Button Command - get this to print within the GUI
def testFunc():
    # view_label = ttk.Label(mainframe, text='Test String')
    print_records = ''
    tables = database.tables_show_all()
    for record in tables:
        print_records += str(record) + "\n"
    view_label = ttk.Label(mainframe, text=print_records)
    view_label.grid(column=0, row=10, columnspan=5)
test_btn = ttk.Button(mainframe, text="Show Records", command=testFunc)
test_btn2 = ttk.Button(mainframe, text="Event click", command=lambda: testFunc()).grid()
test_btn.grid(column=0, row=5, columnspan=5)

    


# TASK: place within a function
# add help menu command
help_menu.add_command(label='Link to github documentation', command=None)


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


 # create the main loop of the program
root.mainloop()

