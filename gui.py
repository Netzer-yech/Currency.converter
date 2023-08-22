from tkinter import *
from coins import USD
from coins import ILS
from coins import EUR

def clear():
    e.delete(0, END)
def usd_ils():
    try:
        current = float(e.get())
        usd = USD()
        e.insert(0, usd.calculate(float(current)))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid value")
def ils_usd():
    try:
        current = float(e.get())
        ils = ILS()
        e.insert(0, ils.calculate(float(current)))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid value")
def ils_eur():
    try:
        current = float(e.get())
        eur = EUR()
        e.insert(0, eur.calculate(float(current)))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid value")


root = Tk()
root.geometry("360x250")
root.title('Currency Converter')
root.iconbitmap("C:\\automation course\icons\exchange.ico")

welcome_label = Label(root, text='Welcome to Currency Converter!', width=30, height=2)
welcome_label.grid(row=0, column=1)
enter_label = Label(root, text='Please enter an amount to convert', width=30, height=1)
enter_label.grid(row=1, column=1)

e = Entry(root, width=30)
e.insert(0, '')
e.grid(row=2, column=1)

space_label = Label(root, text='    ', width=30, height=1)
space_label.grid(row=3, column=1)
space_label_1 = Label(root, text='    ', width=9, height=1)
space_label_1.grid(row=0, column=0)

button_frame = Frame(root)
button_frame.grid(row=4, column=1)

usd_ils_button = Button(button_frame, text="USD to ILS", width=9, height=1, command=usd_ils)
ils_usd_button = Button(button_frame, text="ILS to USD", width=9, height=1, command=ils_eur)
ils_eur_button = Button(button_frame, text="ILS to EUR", width=9, height=1, command=ils_eur)

usd_ils_button.grid(row=2, column=0)
ils_usd_button.grid(row=2, column=1)
ils_eur_button.grid(row=2, column=2)

clear_button = Button(button_frame, text="Clear", width=9, height=1, command=clear)
clear_button.grid(row=0, column=1)

space_label = Label(button_frame, text='    ', width=9, height=1)
space_label.grid(row=1, column=0)



root.mainloop()