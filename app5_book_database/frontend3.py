#Once we completed the backend.py script we had to tweak the frontend script so that we could manipulate the data on the back-end database.


from tkinter import *
import backend4

#as this funtion is bound to an event we need to declare event as a parameter as python expects that.
def getselectedrow(evt):
    try:
# the global line below is required as if we were to call the function from another function apart from the click event we would get an error as it would expect a paramater to be passed as 'event' is declared.  So instead of calling the function and returnig the value we let the function execute when the user clicks the row and the globa variable is created.
        global whole_line
#in order to grab the selected line we use the curseselection() method.  this will return the index number we also need to get the full line.  for that we will use the get() method
        index=lb1.curselection()[0]
        whole_line=lb1.get(index)
#the lines below will clear our wntry widgets and fill the with their corresponding fields grabbed fron the wlole_line tuple
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

#as we have seen previously when mapping a function to a tkinter button we need to mit the () otherwise python will run the function when executin the script.  This means that if we want to pss parameters we cant do it directlt therefore we need to create wrapper functions that will be mapped to the command= in the tkinter button and will call the functions defined in our backend scrpit.  The funtion below does just that
def view_command():
#the line below is used to clear the listbox before displaying the results
    lb1.delete(0,END)
    for row in backend4.read_data():
       lb1.insert(END,row)

#this is a good example of the wrapper fubction where you need to pass arguments to the backend function.  As you can see we use the get() method to grab the StringVar value of what we are passing into any of the 4 boxes.
def search_command():
    lb1.delete(0,END)
    for row in backend4.search_data(title_value.get(),author_value.get(),year_value.get(),(isbn_value.get())):
        lb1.insert(END,row)

#here we make an entry in the db and then show the entry on the listbox for the user
def add_command():
    backend4.add_data(title_value.get(),author_value.get(),year_value.get(),(isbn_value.get()))
    lb1.delete(0,END)
    lb1.insert(END,backend4.search_data(title_value.get(),author_value.get(),year_value.get(),(isbn_value.get()))[-1])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def delete_command():
#this is where we make use of the global variable from our click event.
    backend4.delete_data(whole_line[0])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    view_command()

def update_command():
    backend4.update_data(whole_line[0],title_value.get(),author_value.get(),year_value.get(),(isbn_value.get()))
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

#for the delete button we want the user to choose a row from the listbox and delete it via the delete function ehich takes the id as an argument.  Listbox has method within the tkinter library that allows for this to happen - its called bind().  The logic here is to create the bind between the listbox and the action and the create a function that allows us to pull the data out and use it - getselectedrow (which is a cutom function.)
lb1.bind('<<ListboxSelect>>', getselectedrow)


#As stated previously when we attach a function to a button we don't specify the () as otherwise when python reads the script the function would be executed - obviously we dont want that as we only want the function to be executed when the button is pressed.
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
