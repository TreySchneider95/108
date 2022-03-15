from email import message


def print_menu():
    print('======================')
    print('PyCalc')
    print('======================')
    print('[1] Sum')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')
    print('[5] Repeat message')

print_menu()
option = input('\n\nPlease select an option: \n')

if option == '1':
    num_1 = input('Enter your first number: \n')
    num_2 = input('Enter your second number: \n')
    try:
        print(f'\n\nTotal: {float(num_1) + float(num_2)}')
    except:
        print('You must enter numbers')
elif option == '2':
    num_1 = input('Enter your first number: \n')
    num_2 = input('Enter your second number: \n')
    try:
        print(f'\n\nTotal: {float(num_1) - float(num_2)}')
    except:
        print('You must enter numbers')
elif option == '3':
    num_1 = input('Enter your first number: \n')
    num_2 = input('Enter your second number: \n')
    try:
        print(f'\n\nTotal: {float(num_1) * float(num_2)}')
    except:
        print('You must enter numbers')
elif option == '4':
    num_1 = input('Enter your first number: \n')
    num_2 = input('Enter your second number: \n')
    if num_2 != '0':
        try:
            print(f'\n\nTotal: {float(num_1) / float(num_2)}')
        except:
            print('You must enter numbers: \n')
    else:
        print('wrong')
elif option == '5':
    the_message = input('Enter you message: \n')
    num = input('Enter the number of times to say it: \n')
    print(f'{the_message} \n' * int(num))
else:
    'Not a correct input'

