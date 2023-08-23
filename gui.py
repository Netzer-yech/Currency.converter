import os
from tkinter import *
from coins import USD, ILS, EUR
from documents import LIST, Result
import atexit

root = Tk()
root.geometry("360x300")
root.title('Currency Converter')
root.iconbitmap("C:\\automation course\\icons\\exchange.ico")

currency_list = LIST()
currency_list.create_file()
currency_list = []

def exit_func():
    with open('C:\\automation course\\Currency_Results.txt', 'r') as file:
        os.startfile('C:\\automation course\\Currency_Results.txt')
def clear():
    e.delete(0, END)
    result_label.config(text='')

def usd_ils():
    try:
        current = float(e.get())
        usd = USD()
        result = usd.calculate(current)
        result_label.config(text=f"{round(result, 2)} ILS")
        currency_list.append(result)
        currency_file = open('C:\\automation course\\Currency_Results.txt', 'a')
        currency_file.write(str(f"{round(result, 2)} USD to ILS"))
        currency_file.write(' \n')
        currency_file.close()
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        error = "Invalid value"
        result_label.config(text=f"{error}")


def ils_usd():
    try:
        current = float(e.get())
        ils = ILS()
        result = ils.calculate(int(current))
        result_label.config(text=f"{round(result, 2)} USD")
        currency_list.append(result)
        currency_file = open('C:\\automation course\\Currency_Results.txt', 'a')
        currency_file.write(str(f"{round(result, 2)} ILS to USD"))
        currency_file.write(' \n')
        currency_file.close()
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        error = "Invalid value"
        result_label.config(text=f"{error}")


def ils_eur():
    try:
        current = float(e.get())
        eur = EUR()
        result = eur.calculate(int(current))
        result_label.config(text=f"{round(result, 2)} EUR")
        currency_list.append(result)
        currency_file = open('C:\\automation course\\Currency_Results.txt', 'a')
        currency_file.write(str(f"{round(result, 2)} ILS to EUR"))
        currency_file.write(' \n')
        currency_file.close()
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        error = "Invalid value"
        result_label.config(text=f"{error}")






welcome_label = Label(root, text='Welcome to Currency Converter!', width=30, height=2)
welcome_label.grid(row=0, column=1)

space_label = Label(root, text='', width=8, height=1)
space_label.grid(row=0, column=0)

enter_label = Label(root, text='Please enter an amount to convert', width=30, height=1)
enter_label.grid(row=1, column=1)


e = Entry(root, width=30)
e.insert(0, '')
e.grid(row=2, column=1)

space_label_1 = Label(root, text='', width=30, height=1)
space_label_1.grid(row=3, column=1)


button_frame = Frame(root)
button_frame.grid(row=4, column=1)

clear_button = Button(button_frame, text="Clear", width=8, height=1, command=clear, borderwidth=2)
clear_button.grid(row=2, column=1)

space_label_2 = Label(button_frame, text='', width=9, height=1)
space_label_2.grid(row=1, column=0)

usd_ils_button = Button(button_frame, text="USD to ILS", width=9, height=1, command=usd_ils, borderwidth=2)
ils_usd_button = Button(button_frame, text="ILS to USD", width=9, height=1, command=ils_usd, borderwidth=2)
ils_eur_button = Button(button_frame, text="ILS to EUR", width=9, height=1, command=ils_eur, borderwidth=2)

usd_ils_button.grid(row=0, column=0)
ils_usd_button.grid(row=0, column=1)
ils_eur_button.grid(row=0, column=2)

result_frame = Frame(root, width=40, height=20)
result_frame.grid(row=5, column=1, columnspan=1)

result_space = Label(result_frame, text='', font=2)
result_space.grid(row=0, column=0)

result_label_1 = Label(result_frame, text='Result:')
result_label_1.grid(row=1, column=0)

result_label = Label(result_frame, text='')
result_label.grid(row=1, column=1)

atexit.register(exit_func)

root.mainloop()