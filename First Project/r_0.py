#C:\Users\aletr\Desktop\python projects\restaurant software
#constants
FILE_NAMES = 'names.txt'
#
with open(FILE_NAMES, 'r+') as f:
    valid_user = f.read().splitlines()
print("Welcome to NAME.app")
##############
# USER LOGIN #
##############
while True:
    user_input = input("""
    \n - Insert user name to logg in
    \n - ADD to save new user
    \n - LIST to see saved users
    \n - REMOVE to delete a user
    \n - EXIT to finish
    \n - ...""")

    user_input_lower = user_input.lower()

    if user_input_lower == "add":
        print('''- Please...
        \n - Simplify the user name.
        \n - Do not use NUMBERS or SIGNS \n''')
        user_name = input("Name:")
        if user_name.isdigit():
            print('Please try again.')
            continue
        with open(FILE_NAMES, 'a') as f:
            f.write(user_name + '\n')

    elif user_input_lower == "list":
        with open(FILE_NAMES, 'r') as f:
            print(f.read().splitlines())
            f.close()

    elif user_input in valid_user:
        print("Logged as", user_input.upper())
        user = user_input
        input('Welcome, press enter to continue \n')
        break

    elif user_input_lower == 'remove':
        remove = input("Insert user name to remove \n ...")
        with open(FILE_NAMES, 'r') as f:
            lines = f.readlines()
            lines = [line for line in lines if remove not in line]
        with open(FILE_NAMES, 'w') as f:
            f.writelines(lines)

    elif user_input_lower == "exit":
        exit()
####################
# TABLE MANAGEMENT #
####################
#C:\Users\aletr\Desktop\python projects\restaurant software
while True:
    user_action = input ('''
 - NEW table
    \n - ADD table
    \n - BILL
    \n - CLOSING
    \n - EXIT
    \n - ... ''')

    menu = {'(1) chburger': 19,'(2) bncburger': 23,'(3) plpasta': 6}

    if user_action == 'new':
            try:
                table_number = int(input('Insert table number \n - ...'))
            except ValueError:
                print('Invalid input')
                continue
            name = 'T' + str(table_number)
            open(name + '.txt', 'w+')
            print('Done')

    elif user_action.lower() == 'add':
            try:
                table = input ('Select desired table number: \n - ...')
            except ValueError:
                print('Invalid input')
                continue
            fulltab = 'T' + table
            with open(fulltab + '.txt', 'w+') as f:
# Order list and add Orde
                while True:
                    for k, v in menu.items():
                        print(k, v)
                    add_order = input('Insert order. \n - ...')
                    for k, v in menu.items():
                        if add_order == k[1]:
                            f.write(str(v) + '\n')
#Option to continue.
                    break_continue = input('Add more? y/n \n -...')
                    if break_continue.lower() == 'y': continue
                    if break_continue.lower() == 'n': break

 #File as F

    elif user_action.lower() == 'bill':
        try:
            table_number = input('Please insert number of table. \n -... ')
        except ValueError:
            print('Invalid Input')
            continue
        with open (('T' + table_number)+ '.txt', 'r') as f:
            total_bill = 0
            for line in f : total_bill = int(total_bill) + int(line)

            service_charge = input('Group table (+10 ppl)? y/n: \n')
            if service_charge == 'y' :
                total_bill = total_bill + (total_bill/100)*10
                print('SERVICE CHARGE ADDED.')

            elif service_charge == 'n' : print ('Processing bill...')
            print('Total to pay:', total_bill)
            print('Serviced by', user)

            #### Closing added part to bill.
            with open('closing.txt', 'a+') as f:
                f.write(str(total_bill) + '\n')

# Closing days balance.
    elif user_action.lower() == 'closing':
        date = input('Please enter DATE. ')
        with open('closing.txt', 'r+') as f:
            result = 0
            for line in f : result = int(result) + int(line)
            print('Closing is...')
            print(result)
            print('Today tips', (result / 100 * 10))
        current_closing = 'C:\\Users\\aletr\\Desktop\\python projects\\restaurant software\\closing.txt'
        old_closing = 'C:\\Users\\aletr\\Desktop\\python projects\\restaurant software\\' + date + '.txt'
        import os
        os.rename(current_closing, old_closing)
        print('Day closed, find the closing balance in the specific dated document.')
# Exit command.
    elif user_action.lower() == 'exit':
        exit()
