from tkinter import *

#assign a blank tkinter window to window variable
window=Tk()

#Button is defined via Button funtion, assigned to window with some text - b1.grid() allows you to select the position of the button.
b1=Button(window,text="test")
b1.grid(column=0,row=0)

#entry widget works in same manner as Button().
e1=Entry(window)
e1.grid(column=0,row=1)

#text widget works in same manner as Button().
t1=Text(window, height=2, width=20)
t1.grid(column=1,row=0,rowspan=2)

#close the window mainloop - all window config goes between window=Tk() and window.mainloop()
window.mainloop()
