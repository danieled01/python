from tkinter import *
import backend
#from tkinter import ttk

appgui=Tk()
appgui.title("IP address checkout")
#themes=ttk.Style()
#print(themes.theme_names())

def getselectedrow(evt):
    try:
        global whole_line
        index=lb1.curselection()[0]
        whole_line=lb1.get(index)
        e1.delete(0,END)
        e1.insert(END,whole_line[0])
        e2.delete(0,END)
        e2.insert(END,whole_line[1])
    except IndexError:
        pass

def add_command():
    backend.add_data(e1_text.get(),e2_text.get())
    lb1.delete(0,END)
#    lb1.insert(END,backend4.search_data(title_value.get(),author_value.get(),year_value.get(),(isbn_value.get()))[-1])
    e1.delete(0,END)
    e2.delete(0,END)

def view_command():
#the line below is used to clear the listbox before displaying the results
    lb1.delete(0,END)
    for row in backend.read_data():
       lb1.insert(END,row)

def delete_command():
    backend.delete_data(whole_line[0])
    e1.delete(0,END)
    e2.delete(0,END)
    view_command()

lb1=Listbox(appgui,height=4,width=50)
lb1.grid(column=0,row=0,rowspan=2,columnspan=2)
lb1.bind('<<ListboxSelect>>', getselectedrow)

e1_text=StringVar(appgui,value="ip")
e1=Entry(appgui,textvariable=e1_text)
e1.grid(column=0,row=2)

e2_text=StringVar(appgui,value="hostname")
e2=Entry(appgui,textvariable=e2_text)
e2.grid(column=1,row=2)

b1=Button(appgui,text='ADD',width=15,command=add_command)
b1.grid(column=0,row=3)

b2=Button(appgui,text='DELETE',width=15,command=delete_command)
b2.grid(column=1,row=3)

b3=Button(appgui,text='LIST',width=15,command=view_command)
b3.grid(column=0,row=4)

b4=Button(appgui,text='CLOSE',width=15)
b4.grid(column=1,row=4)

appgui.mainloop()
