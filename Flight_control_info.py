from tkinter import *
from tkinter import messagebox

first = (range(1,21))
bussinnes = (range(21,51))
economy = (range(51,101))

Flight_control_info = Tk()

Flight_control_info.configure(bg='purple')
def limit_texts():
    ticket_number = ticket_number_entry.get()
    ticket_number = int(ticket_number)
    if ticket_number in first:
        messagebox.showinfo("Limits","Handbag Limit = 20 KG Liquid Limit = 4 L")
    elif ticket_number in bussinnes:
        messagebox.showinfo("Limits","Handbag Limit = 15 KG Liquid Limit = 2 L")
    elif ticket_number in economy:
        messagebox.showinfo("Limits","Handbag Limit = 5 KG Liquid Limit = 1 L")
    else:
        messagebox.showerror("Error!", "Please write valid ticket number!")

#This is for place our screen in the middle.
ws = Flight_control_info.winfo_screenwidth() # width of the screen
hs = Flight_control_info.winfo_screenheight() # height of the screen
x = (ws/2) - (500/2) # calculate x and y coordinates for the Tk root window
y = (hs/2) - (100/2)
Flight_control_info.geometry('%dx%d+%d+%d' % (500, 100, x, y)) # set the dimensions of the screen and where it is placed.

Flight_control_info.title("Flight Control Center")

message_label_1 = Label(Flight_control_info, text= "Give your ticket number:")
message_label_1.place(rely= 0.1, relx= 0.2)
message_label_1.configure(bg='purple')

ticket_number_entry = Entry(Flight_control_info, width=20)
ticket_number_entry.place(relx=0.5, rely=0.1)

enter_button = Button(Flight_control_info, text="Enter",command= lambda :limit_texts())
enter_button.place(rely=0.4, relx=0.35, height=30, width=100)
enter_button.configure(bg="blue")

Flight_control_info.mainloop()