from tkinter import *
import math

first_element = ""
second_element = ""
calculated_tuple = (first_element,second_element)

gas_calculator = Tk()
gas_calculator.geometry("600x100")

def parametre(para):
    if para == "Dollar":
        calculated_label_2["text"] = "Dollar"
    elif para == "Euro":
        calculated_label_2["text"] = "Euro"
    else:
        calculated_label_2["text"] = "TL"
def gas_calculate():
    a = hundred_km_entry.get()
    a = float(a)
    b = gas_price_entry.get()
    b = float(b)
    price = (a/100) * b
    price = round(price,3)
    calculated_label["text"] = str(price)

hundred_km_label = Label(gas_calculator,text="L/100 ",font=("Times New Roman",12))
hundred_km_label.place(x=10,y=10)
hundred_km_entry = Entry(gas_calculator)
hundred_km_entry.place(x=100,y=13)

gas_price_label = Label(gas_calculator,text="Gas Price ",font=("Times New Roman",12))
gas_price_label.place(x=10,y=50)
gas_price_entry = Entry(gas_calculator)
gas_price_entry.place(x=100,y=53)

calculate_button = Button(gas_calculator,text="CALCULATE",command =lambda: gas_calculate())
calculate_button.place(x=350,y=33)

dollar_button = Button(gas_calculator,text="Dollar",height=1,width=10, command= lambda: parametre(dollar_button.cget("text")))
dollar_button.place(x=250,y=5)
euro_button = Button(gas_calculator,text="Euro",height=1,width=10, command= lambda: parametre(euro_button.cget("text")))
euro_button.place(x=250,y=35)
tl_button = Button(gas_calculator,text="TL",height=1,width=10, command= lambda: parametre(tl_button.cget("text")))
tl_button.place(x=250,y=65)

calculated_label = Label(gas_calculator, text="", font=("Times New Roman",15))
calculated_label.place(x=450,y=33)
calculated_label_2 = Label(gas_calculator, text="", font=("Times New Roman",15))
calculated_label_2.place(x=510,y=33)

gas_calculator.resizable(False,False)
gas_calculator.mainloop()