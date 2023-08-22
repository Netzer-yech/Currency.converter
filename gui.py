
from tkinter import *
from coins import USD
from coins import ILS
from coins import EUR


root = Tk()
root.geometry("360x300")
root.title('Currency Converter')
root.iconbitmap("C:\\automation course\icons\exchange.ico")

def clear():
    e.delete(0, END)
    result_label.config(text='')
def usd_ils():
    try:
        current = int(e.get())
        usd = USD()
        result = usd.calculate(int(current))
        result_label.config(text=f"{round(result, 2)} USD to ILS")
    except ValueError:
        e.delete(0, END)
        error = "Invalid value"
        result_label.config(text=f"{error}")


def ils_usd():
    try:
        current = int(e.get())
        ils = ILS()
        result = ils.calculate(int(current))
        result_label.config(text=f"{round(result, 2)} ILS to USD")
    except ValueError:
        e.delete(0, END)
        error = "Invalid value"
        result_label.config(text=f"{error}")


def ils_eur():
    try:
        current = int(e.get())
        eur = EUR()
        result = eur.calculate(int(current))
        result_label.config(text=f"{round(result, 2)} ILS to EUR")
    except ValueError:
        e.delete(0, END)
        error = "Invalid value"
        result_label.config(text=f"{error}")






welcome_label = Label(root, text='Welcome to Currency Converter!', width=30, height=2)
welcome_label.grid(row=0, column=1)

space_label = Label(root, text=' ', width=8, height=1)
space_label.grid(row=0, column=0)

enter_label = Label(root, text='Please enter an amount to convert', width=30, height=1)
enter_label.grid(row=1, column=1)


e = Entry(root, width=30)
e.insert(0, '')
e.grid(row=2, column=1)

space_label_1 = Label(root, text='    ', width=30, height=1)
space_label_1.grid(row=3, column=1)


button_frame = Frame(root)
button_frame.grid(row=4, column=1)

clear_button = Button(button_frame, text="Clear", width=8, height=1, command=clear)
clear_button.grid(row=0, column=1)

space_label_2 = Label(button_frame, text=' ', width=9, height=1)
space_label_2.grid(row=1, column=0)

usd_ils_button = Button(button_frame, text="USD to ILS", width=9, height=1, command=usd_ils)
ils_usd_button = Button(button_frame, text="ILS to USD", width=9, height=1, command=ils_usd)
ils_eur_button = Button(button_frame, text="ILS to EUR", width=9, height=1, command=ils_eur)

usd_ils_button.grid(row=2, column=0)
ils_usd_button.grid(row=2, column=1)
ils_eur_button.grid(row=2, column=2)

result_frame = Frame(root, width=40, height=20)
result_frame.grid(row=5, column=1, columnspan=1)

result_space = Label(result_frame, text='   ', font=2)
result_space.grid(row=0, column=0)

result_label_1 = Label(result_frame, text='Result:', font=2)
result_label_1.grid(row=1, column=0)

result_label = Label(result_frame, text=' ', font=2)
result_label.grid(row=1, column=1)





root.mainloop()