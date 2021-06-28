from tkinter import *

window=Tk()

def kg_converter():
    grams = float(input_kg.get()) * 1000
    pounds = float(input_kg.get()) * 2.20
    ounces = float(input_kg.get()) * 35.24
    output_grams.delete("1.0", END)
    output_grams.insert(END,grams)
    output_pounds.delete("1.0", END)
    output_pounds.insert(END,pounds)
    output_ounces.delete("1.0", END)
    output_ounces.insert(END,ounces)        

calc_button=Button(window,text="calculate",command=kg_converter)
calc_button.grid(column=2,row=0)

input_kg=StringVar()
input_kg=Entry(window, textvariable=input_kg)
input_kg.grid(column=1,row=0)

output_grams=Text(window, height=1, width=30)
output_grams.grid(column=0,row=1)

output_pounds=Text(window, height=1, width=30)
output_pounds.grid(column=1,row=1)

output_ounces=Text(window, height=1, width=30)
output_ounces.grid(column=2,row=1)

window.mainloop()
