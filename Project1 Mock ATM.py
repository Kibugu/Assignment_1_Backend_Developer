import datetime
now = datetime.datetime.now()
date = now.strftime('%x')

print('Current date and time :')
print(now.strftime("%d-%m-%y %H:%M:%M:%S:"))
name = input("What is your name? \n")
allowedUsers = ['James', 'Esther', 'Hellen', 'Susan']               
allowedPassword = ['passwordJames','passwordEsther','passwordHellen','passwordSusan']

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome %s' % name)
        print("These are the available options:")
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))
        
        
        if (selectedOption == 1):
            print('you selected %s' %selectedOption)
            selectwithdrawalAmount = int(input('How much would you like to withdraw? \n'))
            print('Take you cash')
        elif(selectedOption == 2):
            print('you selected %s' %selectedOption)
            selectdepositAmount = int(input('How much would you like to Deposit? \n'))
            print('Your Current Balance is: 100,000 naira')
        elif(selectedOption == 3):
            print('you selected %s' %selectedOption)
            selectdepositAmount = input('What issue will you like to report? \n')
            print('Thank you for contacting us')   
    else:
        print('Password Incorrect, Please try again')
else:

    print("Name not found, please try again")



