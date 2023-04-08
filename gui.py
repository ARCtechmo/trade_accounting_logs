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


# ttk setup from the docs
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(row=0,column=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(row=1,column=0)


# create a test widget and place it on the screen
# my_Label = Label(root, text="Hello World")
# my_Label.grid(row=0,column=0)

# use the gui to run the export.py program 
def export_records():
    # import export
    pass
    # conn = sqlite3.connect('database.db')
    # cur = conn.cursor()
    # export.export_fx_log_records()

# export_btn = Button(root, text="Export Records", command=export_records)
# export_btn.grid(row=1,column=0,columnspan=2,padx=10,pady=10)


# display tables function 
# use radio button selection to feed into the query 



# model to query the database
def query():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    with conn:
        cur.execute("SELECT * FROM fx_commissions")
        records = cur.fetchall()
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
        query_label = Label(root, text=print_records)
        query_label.grid(row=0,column=1,columnspan=7)
    conn.commit()

query_btn = Button(root, text="Show All Records", command=query)
query_btn.grid(row=3,column=0, columnspan=2, padx=10, pady=10)

# close the database
conn.close()

 # create the main loop of the program
root.mainloop()

