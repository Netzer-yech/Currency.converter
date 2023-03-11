import os
from coins import USD
from coins import ILS
from coins import EUR
from documents import LIST
from documents import Result
# import the classes that relevant for this code

currency_list = LIST()
# defined the list as an object using class
currency_list.create_file()
# creating the results file
currency_list = []
# creating the list structure

def get_user_choice():
    user_choice = input('Please enter your choice (1/2/3):')
    if user_choice == '1':
        try:
            value_to_convert = float(input('Please enter an amount to convert:'))
        # casting input to float number
        except ValueError:
            print('Invalid Choice, please try again')
            return main()
        if value_to_convert < 0:
            print('Invalid Choice, please try again')
            return get_user_choice()
        # Preventing the program from crashing from an error using try-except
        # let user know that choice is invalid
        usd = USD()
        # defined an object using class
        result = Result(usd.calculate(value_to_convert), 'USD to ILS')
        # defined an object using class
        print(result.result)
        currency_list.append((result.result, result.conversion))
        # append result and conversion to the list
        write_result(str(result.result))
        return start_over()
        # calling start_over function if needed

    elif user_choice == '2':
        try:
            value_to_convert = float(input('Please enter an amount to convert:'))
        except ValueError:
            print('Invalid Choice, please try again')
            return main()
        if value_to_convert < 0:
            print('Invalid Choice, please try again')
            return get_user_choice()
        ils = ILS()
        result = Result(ils.calculate(value_to_convert), 'ILS to USD')
        print(result.result)
        currency_list.append((result.result, result.conversion))
        write_result(str(result.result))
        return start_over()

    elif user_choice == '3':
        try:
            value_to_convert = float(input('Please enter an amount to convert:'))
        except ValueError:
            print('Invalid Choice, please try again')
            return main()
        if value_to_convert < 0:
            print('Invalid Choice, please try again')
            return get_user_choice()
        eur = EUR()
        result = Result(eur.calculate(value_to_convert), 'EUR to ILS')
        print(result.result)
        currency_list.append((result.result, result.conversion))
        write_result(str(result.result))
        return start_over()

    else:
        while user_choice != '1' or user_choice != '2' or user_choice != '3':
            print('Invalid Choice, please try again')
            return get_user_choice()
        # make sure user's choice is valid

# generally this function get the user's choice and amount to convert,
# check if inputs are valid, calculate and document the result using if/else statements


def start_over():
    user_choice_2 = input('Would you like to start over Y / N ?')
    if user_choice_2.upper() == 'Y':
        # upper function is allowing non-case-sensitive
        get_user_choice()
        # calling get_user_choice again
    elif user_choice_2.upper() == 'N':
        print('Thanks for using our currency converter')
        print(currency_list)
        with open('C:\\automation course\\results.txt', 'r') as file:
            os.startfile('C:\\automation course\\results.txt')
            # open the results file automatically
    else:
        print('Invalid Choice, please try again')
        return start_over()
# this function is looping the process if user is decided Y/y, or end it if user decided n/N using if/else statements

def write_result(result):
    append_result = open('C:\\automation course\\results.txt', 'a')
    append_result.write(result)
    append_result.write(' \n')
    # write every result in a new line at text file
    append_result.close()
# this function append all results to a file that created before using i/o

def main():
    print('Please choose option (1/2/3):')
    print('1. Dollars to Shekels')
    print('2. Shekels to Dollars')
    print('3. Shekels to Euros')
    get_user_choice()
# this function print first screen and start the process calling "get_user_choice" function

print('Welcome to currency converter')
# first print separately because it is not needed in the rest of the program

main()
# execute main function for first screen






