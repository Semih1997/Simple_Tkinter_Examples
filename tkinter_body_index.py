from tkinter import *

labels_height = 50
labels_width = 200

body_index_screen = Tk()

def body_index_calculate():
    height = height_entry.get()
    height = float(height) / 100
    kilogram = kilogram_entry.get()
    kilogram = float(kilogram)
    body_index = kilogram / (height ** 2)
    calculated_label = Label(body_index_screen,text=str(body_index)).place(x=150,y=125)
    calculated_text = Label(body_index_screen,text="Your body index =").place(x=40,y=125)

body_index_screen.geometry("300x200")
body_index_screen.title("Body Index Calculator")

kilogram_label = Label(body_index_screen,text="Kilogram =").place(x=10,y=10)
kilogram_entry = Entry(body_index_screen,width=20)
kilogram_entry.place(x=150,y=10)

height_label = Label(body_index_screen,text="Height(santimeter) =").place(x=10,y=40)
height_entry = Entry(body_index_screen,width=20)
height_entry.place(x=150,y=40)

calculate_button = Button(body_index_screen,text="CALCULATE",command=lambda :body_index_calculate()).place(x=100,y=85)
# calculated_label = Label(body_index_screen,text="").place(x=150,y=125)
# calculated_text = Label(body_index_screen,text="").place(x=30,y=125)

body_index_screen.resizable(False,False)
body_index_screen.mainloop()