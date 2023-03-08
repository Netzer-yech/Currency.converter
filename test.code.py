user_choice = int(input('Please enter your choice 1/2:'))
if user_choice == 1:
    value_to_convert = float(input('Please enter an amount to convert:'))
    usd = USD()
    result = usd.calculate(value_to_convert)
    print(result)
    return result

elif user_choice == 2:
    value_to_convert = float(input('Please enter an amount to convert:'))
    ils = ILS()
    result = ils.calculate(value_to_convert)
    print(result)
    return result
else:
    while user_choice != 1 or user_choice != 2:
        try:
            get_user_choice()
        except ValueError:
            print('Invalid Choice, please try again')
        if user_choice == 1 or user_choice == 2:
            break
