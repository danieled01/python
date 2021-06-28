from tkinter import *
#now that the backend4 script has been reworked as a class we import in the manner below
from backend4 import Database

#as the class created in backend4 only acts as a blueprint in order to use it we need to map an object to it like we map a variable to a value.  Functions within a class are known as methods.
database=Database("books.db")
#Once the object has been created we need to replace all of the in this script which instructs to import the methods from backend4 - backend4.view() to database.view() as the mthods are now being called by referencing the object that has been mapped to the class.  We also passed the "books.db" parameter as we have declared 2 parameters for our __init__ function and books.db is passed as db.

def getselectedrow(evt):
    try:
        global whole_line
        index=lb1.curselection()[0]
        whole_line=lb1.get(index)
        e1.delete(0,END)
        e1.insert(END,whole_line[1])
        e2.delete(0,END)
        e2.insert(END,whole_line[2])
        e3.delete(0,END)
        e3.insert(END,whole_line[3])
        e4.delete(0,END)
        e4.insert(END,whole_line[4])
    except IndexError:
        pass

def view_command():
    lb1.delete(0,END)
    for row in database.read_data():
       lb1.insert(END,row)
def search_command():
    lb1.delete(0,END)
    for row in database.search_data(title_value.get(),author_value.get(),year_value.get(),(isbn_value.get())):
        lb1.insert(END,row)

def add_command():
    database.add_data(title_value.get(),author_value.get(),year_value.get(),(isbn_value.get()))
    lb1.delete(0,END)
    lb1.insert(END,database.search_data(title_value.get(),author_value.get(),year_value.get(),(isbn_value.get()))[-1])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def delete_command():
    database.delete_data(whole_line[0])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    view_command()

def update_command():
    database.update_data(whole_line[0],title_value.get(),author_value.get(),year_value.get(),(isbn_value.get()))
    view_command()

window=Tk()

window.wm_title("Book Store App")

l1=Label(window,text='Title')
l1.grid(column=0,row=0)

l2=Label(window,text='Year')
l2.grid(column=0,row=1)

l3=Label(window,text='Author')
l3.grid(column=2,row=0)

l4=Label(window,text='ISBN')
l4.grid(column=2,row=1)

title_value=StringVar()
e1=Entry(window, textvariable=title_value)
e1.grid(column=1,row=0)

year_value=StringVar()
e2=Entry(window, textvariable=year_value)
e2.grid(column=1,row=1)

author_value=StringVar()
e3=Entry(window, textvariable=author_value)
e3.grid(column=3,row=0)

isbn_value=StringVar()
e4=Entry(window, textvariable=isbn_value)
e4.grid(column=3,row=1)

lb1=Listbox(window, height=6, width=25)
lb1.grid(column=0, row=2, columnspan=2, rowspan=6)
sb1=Scrollbar(window)
sb1.grid(column=2, row=2, rowspan=6)
lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

lb1.bind('<<ListboxSelect>>', getselectedrow)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(column=3,row=2)

b2=Button(window,text="Search All",width=12,command=search_command)
b2.grid(column=3,row=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(column=3,row=4)

b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(column=3,row=5)

b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(column=3,row=6)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(column=3,row=7)

window=mainloop()
