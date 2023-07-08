
# import the modules
import database
import sqlite3
from tkinter import *
from tkinter import ttk

# clear the previoius query results before adding new ones
def clear_results():
    return print('------------------TEST: clear previous results---------------------')

# function to query the database and display the results in a separate window
# TASK THE FUNCTIONN WORKS!!  Next add a scroll bar.  
def td_comm_show_all(table_name):

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


# Root Widget Method 1: create the root widget, a title, and eliminate tear-off menus from the app
# Note: The 'tearoff' feature may or may not work depending on the operating system
root = Tk()
root.title("Root:-----Database Query GUI App-----")
root.geometry("25x25") 
root.option_add('*tearOff', FALSE)

# expand the frame to fit window resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# use the gui to run the export.py program 
# NOTE: see the lambda function examples in radio buttons
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

# create a mainframe window inside the root widget
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

# create a menubar
menubar = Menu(mainframe)

############### Begin: No tear off model ##################
# menubar = Menu(root)
# notearoff = Menu(menubar, tearoff=0)
# notearoff.add_command(label="No Tearoff")
# menubar.add_cascade(label="No Tearoff", menu=notearoff)
############### End: No tear off model ##################

# create the 'File' and its options
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label='New File', command=file_functionality)
file_menu.add_command(label='Open...', command=file_functionality)
file_menu.add_command(label='Save', command=file_functionality)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
# menubar.add_cascade(label='File', menu=file_menu)
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


### TASK THIS WORKS!!  Use the model to create buttons for all of the other tables ####
### TASK Think about a more efficient method instead of creating a button for each table (e.g. a dropdown box or radio buttons)
# create a button to show all rows in the  td_commissions table
button = ttk.Button(mainframe, text='Show All TD Commissions', command=lambda: td_comm_show_all('td_commissions'))
button.grid(column=1, row=2, sticky=(W,E))


# create the main loop of the program
root.mainloop()

