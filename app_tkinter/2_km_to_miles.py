from tkinter import *

window=Tk()

#function declared that will be assigned to button1 below.  This function will use the number specified in our entry widget and calculate it into miles.  The number is referenced using e1_value.get().  In this script we map the input placed into the entry widget to the text widget by using the insert() function.  So by decalring t1.insert(END.e1_value.get()) we are saying that whatever we insert into the entry widget it needs to be displayed into the text widget - END is used for positional purpose, as if you add more text into the entry widget it is displayed after the current text on the text widget.
def km_to_miles():
#    t1.insert(END.e1_value.get())
#The 2 lines below calculate the KM into Miles and print the output onto the text window.
    miles = float(e1_value.get()) * 1.6
    t1.insert(END,e1_value.get()+' KM ' + 'equals to ' + str(miles) +' miles.')

#In order for a button to carry out some tasks you need to point it to a function.  Below we use command= and point it to our km_to_miles function we have built above.  Please note that when calling the function you need to omit () - so the command would be command=km_to_miles.
b1=Button(window,text="test", command=km_to_miles)
b1.grid(column=0,row=0)

#Here we declare what the user will input as a value to feed into our funtion stated above.  In our case this will be the KM that we want to turn into miles. So we use the textvariable= parameter in our Entry widget and map that to a variable that calls the StringVar() function.  This is in turn used in our custom function above km_to_miles().  Our custom function grabs that variable by using the variable name along with the .get() function.
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(column=0,row=1)

t1=Text(window, height=2, width=20)
t1.grid(column=1,row=0,rowspan=2)

window.mainloop()
