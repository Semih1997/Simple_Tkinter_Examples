from tkinter import *

start_python_tk = Tk()
start_python_tk.geometry("600x300")
start_python_tk.title("Python Öğrencisi")

start_python_tk.configure(bg="Black")
label_text = Label(start_python_tk,text="Python'a Başlıyorum",
                   font=("Times New Roman",35),fg="Orange",
                   bg="Black").place(x=100,y=50)
label_text_2 = Label(start_python_tk,text="Python Öğrencisi",
                     font=("Times New Roman",20),fg="Purple",
                     bg="Black").place(x=170,y=120)
label_text_2 = Label(start_python_tk,text="(Son Fotoğrafta Bu Ekranın Tkinter Kodlarını Görebilirsin)",
                     font=("Times New Roman",15),fg="Purple",bg="Black").place(x=50,y=170)

start_python_tk.resizable(False,False)
start_python_tk.mainloop()