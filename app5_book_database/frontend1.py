#The first step of building this app, that will store data which is inputted by a user onto a back-end DB, will be to build the front end using tkinter.  This will be done in a similar approach as the app_tkinter folder.

from tkinter import *
import backend2

window=Tk()

#Its good practice to create wrapper functio


#Define the labels for our front end GUI - when designing the GUI and using grid it worth scketching the final outcome on paper so you know how to position it.
l1=Label(window,text='Title')
l1.grid(column=0,row=0)

l2=Label(window,text='Year')
l2.grid(column=0,row=1)

l3=Label(window,text='Author')
l3.grid(column=2,row=0)

l4=Label(window,text='ISBN')
l4.grid(column=2,row=1)

#Define the entry widgets Here
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

#Define the list box - this is the field where your results are shown when the DB is queried.
l1=Listbox(window, height=6, width=25)
l1.grid(column=0, row=2, columnspan=2, rowspan=6)
#next we create the scroll bar that we will use to scroll up/down the listbox.  The logic here is that we first create the scroll bar then we tell the scroll bar which list box it belongs to.  After that has been done we map the listbox to the scrollbar.
sb1=Scrollbar(window)
sb1.grid(column=2, row=2, rowspan=6)
#here we map the list and scrollbar together on the y axis
l1.configure(yscrollcommand=sb1.set)
sb1.configure(command=l1.yview)

#here the buttons that will call the functions will be defined
b1=Button(window,text="View All", width=12, command=backend2.read_data)
b1.grid(column=3,row=2)

b2=Button(window,text="Search All", width=12)
b2.grid(column=3,row=3)

b3=Button(window,text="Add Entry", width=12)
b3.grid(column=3,row=4)

b4=Button(window,text="Update Selected", width=12)
b4.grid(column=3,row=5)

b5=Button(window,text="Delete Selected", width=12)
b5.grid(column=3,row=6)

b6=Button(window,text="Close", width=12)
b6.grid(column=3,row=7)

window=mainloop()
