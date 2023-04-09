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

# ttk setup from the docs
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(row=0,column=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(row=1,column=0)

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


def clicked(value):
    my_sel = Label(root, text=value)
    my_sel.grid(row=1,column=2)


# table selections
tables = [
    ("fx_log","fx_log"),
    ("ib_options_log", "ib_options_log"),
    ("td_options_log","td_options_log")
]
# display tables function 
# use radio button selection to feed into the query 
tab= StringVar()
tab.set("fx_log")

for text, table in tables:
    Radiobutton(root, text=text,variable=tab, value=table,
                command=lambda: clicked(tab.get())).grid(row=1, column=0)
  
sel_btn = Button(root, text="Selection", 
                 command=lambda: clicked(tab.get())).grid(row=3,column=0)

# model for dropdown box selection

# query button
query_btn = Button(root,text="Show All Records",command=query)
query_btn.grid(row=0,column=0,columnspan=1,padx=10,pady=10)

# quit button
exit_btn = Button(root,text="Exit Program",command=root.quit)
exit_btn.grid(row=0,column=1,columnspan=1,padx=10,pady=10)



# close the database
conn.close()

 # create the main loop of the program
root.mainloop()

