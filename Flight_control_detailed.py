#UNFINISH (fact is not the best way to give warning)
#Messagebox is more efficient for just giving information.
#In this file i am going to try to give more inputs if the passenger in the legal limit or not! 

from tkinter import *
from tkinter import messagebox

first = (range(1,21))
bussinnes = (range(21,51))
economy = (range(51,101))

labels_x = 100
enterys_x = 300
simple_screen_4 = Tk()


def limit_texts():
    ticket_number = ticket_number_entry.get()
    ticket_number = int(ticket_number)
    hand_bag = hand_bag_entry.get()
    hand_bag = int(hand_bag)
    liquid = liquid_entry.get()
    liquid = int(liquid)
    if (ticket_number in first) and (hand_bag <= 20) and (liquid <= 4):
        messagebox.showinfo("Safe Travels!","Your limits in range. Enjoy the flight.")
    elif (ticket_number in bussinnes) and (hand_bag <= 10) and (liquid <= 2):
        messagebox.showinfo("Safe Travels!","Your limits in range. Enjoy the flight.")
    elif (ticket_number in economy) and (hand_bag <= 5) and (liquid <= 1):
        messagebox.showinfo("Safe Travels!","Your limits in range. Enjoy the flight.")
    else:
        if ticket_number in first:
            messagebox.showinfo("Limits","Handbag Limit = 20 KG Liquid Limit = 4 L")
        elif ticket_number in bussinnes:
            messagebox.showinfo("Limits","Handbag Limit = 15 KG Liquid Limit = 2 L")
        elif ticket_number in economy:
            messagebox.showinfo("Limits","Handbag Limit = 5 KG Liquid Limit = 1 L")
        else:
            messagebox.showerror("Error!", "Please write valid ticket number!")
    
ws = simple_screen_4.winfo_screenwidth()
hs = simple_screen_4.winfo_screenheight()
x = (ws/2) - (500/2)
y = (hs/2) - (300/2)
simple_screen_4.geometry('%dx%d+%d+%d' % (500, 200, x, y))

message_label_1 = Label(simple_screen_4, text= "Give your ticket number:", )
message_label_1.place(x=labels_x,y=10)
ticket_number_entry = Entry(simple_screen_4, width=20)
ticket_number_entry.place(x=enterys_x, y=10)

hand_bag_label = Label(simple_screen_4, text= "Enter your handbag weight in KG:")
hand_bag_label.place(x=labels_x,y=60)
hand_bag_entry = Entry(simple_screen_4,width=20)
hand_bag_entry.place(x=enterys_x, y=60)

liquid_label = Label(simple_screen_4, text= "Enter your liquid quantity in L:")
liquid_label.place(x=labels_x,y=110)
liquid_entry = Entry(simple_screen_4,width=20)
liquid_entry.place(x=enterys_x, y=110)

enter_button = Button(simple_screen_4, text="Enter",command= lambda :limit_texts())
enter_button.place(x= 200 , y=150, height=30, width=100)

simple_screen_4.resizable(False,False)
simple_screen_4.mainloop()