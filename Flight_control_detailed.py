#UNFINISH (fact is not the best way to give warning)
#Messagebox is more efficient for just giving information.
#In this file i am going to try to give more inputs if the passenger in the legal limit or not! 

from tkinter import *
from tkinter import messagebox

first = (range(1,21))
bussinnes = (range(21,51))
economy = (range(51,101))

simple_screen_4 = Tk()

def limit_texts():
    message_screen = Tk()
    ticket_number = ticket_number_entry.get()
    ticket_number = int(ticket_number)  
    message_screen.geometry("300x130")
    message_screen.title("YOUR LİMİTS")
    text = Text(message_screen, height=5, width=52)
    if ticket_number in first:
        Fact = """
        Handbag Limit = 20 KG
        Liquid Limit = 4 L
        """
    elif ticket_number in bussinnes:
        Fact = """
        Handbag Limit = 15 KG
        Liquid Limit = 2 L
        """
    elif ticket_number in bussinnes:
        Fact = """
        Handbag Limit = 5 KG
        Liquid Limit = 1 L
        """
    else:
        Fact = """
        Please write a valid 
        ticket number!
        """
    text.pack()
    text.insert(END,Fact)
    ok_button = Button(message_screen, text= "QUIT", command= quit)
    ok_button.pack()
    message_screen.mainloop()
simple_screen_4.geometry("500x100")

message_label_1 = Label(simple_screen_4, text= "Give your ticket number:", )
message_label_1.place(rely= 0.1, relx= 0.2)

ticket_number_entry = Entry(simple_screen_4, width=20)
ticket_number_entry.place(relx=0.5, rely=0.1)

enter_button = Button(simple_screen_4, text="Enter",command= lambda :limit_texts())
enter_button.place(rely=0.4, relx=0.35, height=30, width=100)

simple_screen_4.resizable(False,False)
simple_screen_4.mainloop()