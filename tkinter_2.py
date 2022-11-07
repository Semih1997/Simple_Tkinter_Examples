from tkinter import *

main_geometry = "500x500"

simple_screen_2 = Tk()
simple_screen_2.geometry(main_geometry)
simple_screen_2.title("Message")

my_message = Label(simple_screen_2, text="You are gorgeous!")
my_message.place(relx=0.01,rely=0.01)


simple_screen_2.mainloop()