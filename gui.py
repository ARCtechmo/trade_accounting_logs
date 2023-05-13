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
root.title("Database Query GUI App")
root.geometry("50x50")


# use the gui to run the export.py program 
# task see the lambda function examples in radio buttons
def func():
    pass

# model to query the database
def query():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.execute("SELECT * FROM ib_options_log")
        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        query_label = Label(root, text=print_records)
        query_label.grid(row=1,column=0,columnspan=7)
    conn.commit()


# table selections

# display tables function 

# use radio button selection to feed into the query 



# dropdown box selection

# query button


# quit button



# close the database
conn.close()

 # create the main loop of the program
root.mainloop()

