from tkinter import *

geometry_main_screen = "500x500"

simple_screen_3 = Tk()

simple_screen_3.title("This is a Messaged Screen")
simple_screen_3.geometry(geometry_main_screen)

T = Text(simple_screen_3, height = 5, width = 52)
l = Label(simple_screen_3, text = "Fact of the Day")
Fact = """Harry Potter is the best movie ever!!
There is no movie like Harry Potter <3"""
l.pack()
T.pack()

T.insert(END, Fact)   #textin içine fact'i aldığımız için text kısmını oluşturmamız şart.
simple_screen_3.mainloop()