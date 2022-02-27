"""
    TU856/2 OOP CA2
    Bank Management System
    Created by: Adam O'Shea (C20372181)
                Ignas Prakapas (C20424992)
"""

# imports
import uuid
import numpy
import time
import sys
import os
from datetime import date
from datetime import datetime

"""
    customer class containing the customers login and account details
    startmenu method presents a menu allowing user to login or register
    login method allows user to login
    register method allows user to register
    addCust writes customers details to customers.txt after registration
"""
class customer():
    def __init__(self, username = None, accDetails = None, accID = None, accType = None, accUser = None, accBalance = None):
        self.accID = accID 
        self.accType = accType 
        self.accUser = accUser
        self.accBalance = accBalance
        self.username = username
        self.accDetails = accDetails

    # function for getting the start menu
    def startmenu(self):
        print("---------------------------------------------------------------------------------------------------------------------------")

        option = True
        
        # this is an infinite loop for the reg/login menu, but is stopped by the input
        while option:
            print("\nThis is the login/register menu, please choose an option to either register or login")
            print("Enter (x) to exit")
            print("1. Register")
            print("2. Login\n")

            # user input for option
            option = input("Choose an option from menu: ")

            if option == "1":
                # when this option is selected it brings the user to the register function
                self.Register()
                # this resets the Checking option to none (null value)
                option = None
            elif option == "2":
                # when the option is selected it brings the user to the login function
                self.Login()
                # this resets the Checking option to none (null value)
                option = None
            elif option == "x":
                # this is the program exit option
                print("Smell you later!")
                # this resets the Checking option to none (null value)
                option = None
                sys.exit()
            # this is for input validation
            else:
                print("Please enter a valid option")

        print("---------------------------------------------------------------------------------------------------------------------------")

    # this is the login function, from where you can enter by selecting option 2 through the startmenu
    def Login(self):
        print("---------------------------------------------------------------------------------------------------------------------------")

        print("Please enter in your details to login ")
        print()
        # makes a list called userDetails
        userDetails = {}
        # this reads the customer.txt file
        with open('customers.txt', 'r') as file:
            # for each line in file...
            for line in file:
                # split every string in a line if there is whitespace between them
                line = line.split()
                # assigns dictionary of username: password to userDetails from customers file
                userDetails.update({line[1]: line[2]})

        # this is a loop for checking if the username matches up with the one registered into the text file
        while True:
            username = input("Enter your username: ")
            # error checking for if the username does not exist
            if username not in userDetails:
                print("This username does not exist")
                # resets the input for username into an empty string
                username = ''
            else:
                # when the input username is correct, the loop is exited
                break
        # this is a loop for checking if the password matches up with the one registered into the text file
        while True:
            password = input("Enter your password: ")
            # checks if password matches key of username
            if password not in userDetails.get(username):
                print("Incorrect Password")    
                password = ''
            # if input blank
            elif password == '':
                print("Incorrect Password")
                password = ''
            else:
                print("You are now logged in")
                # assign username to username class attribute
                self.username = username
                # call account class usermenu, pass self
                account.usermenu(self)
                break
    # this is the register function, this is activated through selecting option 1 in startmenu
    def Register(self):
        print("---------------------------------------------------------------------------------------------------------------------------")

        print("Please enter in all the necessary details")
        # a loop that does not stop until break is reached...
        while True:
            firstname = input("Enter First name: ")
            # if there are any characters in the input, break the loop
            if firstname != '':
                break
            # else keep looping until there are characters
            else:
                firstname = ''
        # a loop that does not stop until break is reached...        
        while True:
            lastname = input("Enter Last name: ")
            if lastname != '':
                break
            else:
                lastname = ''
        # a loop that does not stop until break is reached...        
        while True:
            age = input("Enter Age: ")
            if age != '':
                break
            else:
                age = ''
        # a loop that does not stop until break is reached...
        while True:
            username = input("Enter Username: ")
            if username != '':
                break
            else:
                username = ''
        # a loop that does not stop until break is reached...
        while True:
            password = input("Enter Password: ")
            if password != '':
                break
        # a loop that does not stop until break is reached...
        while True:
            confirmPassword = input("Confirm password: ")
            # a check to see if the confirm password is equal to the password that was input
            if confirmPassword == password:
                print("\nUser created successfully, proceed to login:")
                # calls addCust function that adds all the details that were input into a text file
                self.addCust([username, password, firstname, lastname, age])
                # a break to stop the loop
                break
            else:
                # passwords didn't match
                print("\nPasswords did not match. Please try again\n")
                # sets the password and confirmPassword to empty strings
                confirmPassword = ''
                password = ''
                # brings the user back to the main menu
                self.startmenu()
                # a break to stop the loop
                break

        print("---------------------------------------------------------------------------------------------------------------------------")
    
    # this is a function to add the userDetails from registration into a text file
    def addCust(self, userDetails: list):
        # open file in append
        with open('customers.txt', 'a') as file:
            # create an random id limited to 8 chars 
            id = str(uuid.uuid4())[:8]
            # write id as first string of line
            file.write(id)
            file.write(' ')
            # for loop that writes all details to file
            for details in userDetails:    
                file.write(details)
                file.write(' ')
            
            file.write('\n')
        self.startmenu()

""" account class allows user to perform actions on their account
    usermenu method presents menu to user
    checkAccount method allows user to check their accounts
    checkSavings method takes user's account details from checkAccount and displays all of their savings accounts
    checkChecking method takes user's account details from checkAccount and displays all of their checking accounts
    createAccount method allows user to create either savings or checking account
    createSavingsAcc creates savings account based on users details
    createCheckingAcc creates checking account based on users details
    deposit allows user to deposit to an account
    withdraw allows user to withdraw from an account
    transfer allows user to transfer money from their account to another
    viewTransactions allows user to view the transactions of any of their accounts
    resetPassword allows a user to reset their login password
    closeAccount allows a user to close one of their accounts
"""
class account(customer):
    def __init__(self, accID = None, accType = None, accUser = None, accBalance = None, target = None, amount = None, targetAccBalance = None):
        self.accID = accID 
        self.accType = accType 
        self.accUser = accUser
        self.accBalance = accBalance
        self.target = target
        self.amount = amount
        self.targetAccBalance = targetAccBalance
    # display main menu to user
    def usermenu(self):
        
        opt = True
        
        while opt:
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("This is the main menu, please choose any of these options with the assigned number")
            print("1. Check your account")
            print("2. Make a new account")
            print("3. Deposit money to an account")
            print("4. Withdraw money from an account")
            print("5. Close an account")
            print("6. Transfer money from one account to another")
            print("7. View an account's transactions")
            print("8. Reset login password")
            print("---------------------------------------------------------------------------------------------------------------------------")
        
            opt = input("Please choose an option. Enter (x) to logout \n")
            # Depending on input, calls a method and passes self, or exits loop
            if opt == "1":
                account.checkAccount(self)
                break
            elif opt == "2":
                account.createAccount(self)
                break
            elif opt == "3":
                account.deposit(self)
                break
            elif opt == "4":
                account.withdraw(self)
                break
            elif opt == "5":
                account.closeAccount(self)
                break
            elif opt == "6":
                account.transfer(self)
                break
            elif opt == "7":
                account.viewTransactions(self)
                break
            elif opt == "8":
                account.resetPassword(self)
            elif opt == "x":
                customer.startmenu(self)
                break
            else:
                print("Please enter a valid option")
        
    # check an account
    def checkAccount(self):
        print("You have selected: Check an account\n")
        print("Select which type of accounts you would like to check: \n")
        
        opt1 = True
        
        while opt1:
            print("1. Savings Account")
            print("2. Checking Account")
            print("Enter (x) to exit\n")
            opt1 = input("Choose an option: ")
            
            # if user chooses savings account
            if opt1 == '1':
                print("Savings Accounts")
                # initialise lists
                accDetails = []
                cAccDetails = []
                # open file in read
                with open('accounts.txt', 'r') as file:
                    #read whole file to cAccDetails
                    cAccDetails = [(line.strip()).split() for line in file]
                    for i in range(len(cAccDetails)):
                        for j in range(len(cAccDetails[i])):
                            # if it reads a savings accounts details...
                            if cAccDetails[i][1] == 'savings':    
                                # and it belongs to the user
                                if cAccDetails[i][j] == self.username:
                                    #add it to addDetails list
                                    accDetails += cAccDetails[i]
                # then pass to checkSavings                   
                account.checkSavings(self, accDetails)
                break
            # if user chooses checking account
            elif opt1 == '2':
                print("Checking Accounts")
                accDetails = []
                cAccDetails = []
                # read whole file to cAccDetails
                with open('accounts.txt', 'r') as file:
                    cAccDetails = [(line.strip()).split() for line in file]
                    for i in range(len(cAccDetails)):
                        for j in range(len(cAccDetails[i])):
                            if cAccDetails[i][1] == 'Checking':    
                                if cAccDetails[i][j] == self.username:
                                    accDetails += cAccDetails[i]
                # pass to checkChecking
                account.checkChecking(self, accDetails)
                break
            #exit menu
            elif opt1 == 'x':
                account.usermenu(self)
                break
            else:
                print("Please enter a valid argument")
    #check savings accounts
    def checkSavings(self, accDetails):
        # if user has no savings accounts, exit
        if accDetails == []:
            print("You do not have any accounts of this type")
            time.sleep(2)
            account.usermenu(self)
        else:
            # if multiple savings accounts, turn list into 2d array for easier access of elements
            a = (len(accDetails) / 5)
            numOfAcc = int(a)
            if numOfAcc > 1:
                # convert to 2d array
                accDetails = numpy.reshape(accDetails, (numOfAcc, 5))
                for i in range (len(accDetails)):
                    for j in range(len(accDetails[i])):
                        # display accounts
                        if j == 0:
                            print("Account ID: "+accDetails[i][j])
                        elif j == 1:
                            print("Account Type: "+accDetails[i][j])
                        elif j == 2:
                            print("Account Holder: "+accDetails[i][j])
                        elif j == 3:
                            print("Account Balance: "+accDetails[i][j])
                        elif j == 4:
                            print("Account Opening Date: "+accDetails[i][j])
                            print()        
            else:
                # if only 1 account, display
                for i in range(len(accDetails)):
                    if i == 0:
                        print("Account ID: "+accDetails[i])
                    elif i == 1:
                        print("Account Type: "+accDetails[i])
                    elif i == 2:
                        print("Account Holder: "+accDetails[i])
                    elif i == 3:
                        print("Account Balance: "+accDetails[i])
                    elif i == 4:
                        print("Account Opening Date: "+accDetails[i])
                        print()        
            time.sleep(3)
            account.usermenu(self)
        
    def checkChecking(self, accDetails):
        # if no checking accounts, exit
        if accDetails == []:
            print("You do not have any accounts of this type")
            time.sleep(2)
            account.usermenu(self)
        else:
            #if multiple, convert to 2d array
            a = (len(accDetails) / 5)
            numOfAcc = int(a)
            if numOfAcc > 1:
                #convert
                accDetails = numpy.reshape(accDetails, (numOfAcc, 5))
                for i in range (len(accDetails)):
                    for j in range(len(accDetails[i])):
                        #display
                        if j == 0:
                            print("Account ID: "+accDetails[i][j])
                        elif j == 1:
                            print("Account Type: "+accDetails[i][j])
                        elif j == 2:
                            print("Account Holder: "+accDetails[i][j])
                        elif j == 3:
                            print("Account Balance: "+accDetails[i][j])
                        elif j == 4:
                            print("Account Opening Date: "+accDetails[i][j])
                            print()        
            else:
                #if only 1 account, display
                for i in range(len(accDetails)):
                    if i == 0:
                        print("Account ID: "+accDetails[i])
                    elif i == 1:
                        print("Account Type: "+accDetails[i])
                    elif i == 2:
                        print("Account Holder: "+accDetails[i])
                    elif i == 3:
                        print("Account Balance: "+accDetails[i])
                    elif i == 4:
                        print("Account Opening Date: "+accDetails[i])
                        print() 
            time.sleep(3)
            account.usermenu(self)
    
    # create an account
    def createAccount(self):
        print("Select type of account to create: \n")
        
        # defining opt1 as true for a loop
        opt1 = True
        
        # since opt1 = True this means that this loops until there is a break
        while opt1:
            print("1. Savings Account")
            print("2. Checking Account")
            print("Enter (x) to exit\n")
            opt1 = input("Choose an option: ")
            
            if opt1 == '1':
                print("Savings Account")
                # if 1 is input, this makes a savings account
                account.createSavingsAcc(self)
                break
            elif opt1 == '2':
                print("Checking Account")
                # if 2 is input, this makes a Checking account
                account.createCheckingAcc(self)
                break
            elif opt1 == 'x':
                #if x is input, then the user is brought back to the main menu
                account.usermenu(self)
                break
            # this is for error checking
            else:
                print("Please enter a valid argument")
    # this is the function for creating a savings account
    def createSavingsAcc(self):
        print("Creating Savings Account")
        print()
        
        # we set both currUser and userDetails to empty lists
        currUser = []
        userDetails = []
        #read file to userDetails
        with open('customers.txt', 'r') as file:
            userDetails = [(line.strip()).split() for line in file]
        
        # if it finds the user's username in userDetails, assigns it to currUser
        for i in range(len(userDetails)):
            for j in range(len(userDetails[i])):
                if userDetails[i][j] == self.username:
                    currUser = userDetails[i]
        
        # Check if user is 14 or over. If not, they cannot create a savings account
        if int(currUser[5]) < 14:
            print("You can't have a savings account, bozo\n")
            account.usermenu(self)
        else:
            #write new accounts details to accounts.txt
            id = str(uuid.uuid4())[:8]
            balance = '0'
            accType = 'savings'
            creationDate = date.today()
            accDetails = [id, accType, currUser[1], balance, str(creationDate)]
            with open('accounts.txt', 'a') as file:
                for i in range(len(accDetails)):
                    file.write(accDetails[i])
                    file.write(' ')
                # new line after account details
                file.write('\n')
            print()
            print("Savings account succesfully created!")
            print("Your account ID is "+id+"\n")
            time.sleep(2)
            #redirect to main menu
            account.usermenu(self)
    # create checking acc
    def createCheckingAcc(self):
        print("Creating Checking Account")
        print()
        # read file
        currUser = []
        userDetails = []
        with open('customers.txt', 'r') as file:
            userDetails = [(line.strip()).split() for line in file]
        
        for i in range(len(userDetails)):
            for j in range(len(userDetails[i])):
                if userDetails[i][j] == self.username:
                    currUser = userDetails[i]
        # check if 18 or over
        if int(currUser[5]) < 18:
            print("You can't have a checking account, bozo\n")
            time.sleep(2)
            account.usermenu(self)
        else:
            # write new account to file
            id = str(uuid.uuid4())[:8]
            balance = '0'
            accType = 'Checking'
            creationDate = date.today()
            accDetails = [id, accType, currUser[1], balance, str(creationDate)]
            with open('accounts.txt', 'a') as file:
                for i in range(len(accDetails)):
                    file.write(accDetails[i])
                    file.write(' ')
                
                
                file.write('\n')
            print()
            print("Checking account succesfully created!")
            print("Your account ID is "+id+"\n")
            time.sleep(2)
            account.usermenu(self)

    # this is the deposit function

    def deposit(self):
        print("Deposit to an account")
        print("Please enter the ID of the account you want to deposit to")
        #prompt user for id
        opt = True
        while opt != 'x':
            print("Enter (x) to exit")
            opt = input("Enter: ")
            #read accounts file
            accDetails = []
            cAccDetails = []
            with open('accounts.txt', 'r') as file:
                cAccDetails = [(line.strip()).split() for line in file]
                for i in range(len(cAccDetails)):
                    for j in range(len(cAccDetails[i])):    
                        if cAccDetails[i][j] == self.username:
                            accDetails += cAccDetails[i]
            check = 0
            #check if user owns the account
            for i in range(len(accDetails)):
                if accDetails[i] == opt:
                    check = 1
            if check == 0:
                print("You do not own this account, please try again")
                time.sleep(2)
                break
            #check if they own any accounts
            if accDetails == []:
                print("You do not have any accounts")
                time.sleep(2)
                account.usermenu(self)
                break
            # assign account details to class attributes
            for i in range(len(accDetails)):
                if opt == accDetails[i]:
                    self.accID = accDetails[i]
                    self.accType = accDetails[i+1]
                    self.accBalance = accDetails[i+3]
                    
                    opt2 = True
                    #prompt for deposit amount
                    while opt2:
                        print("Please enter the amount to deposit")
                        print("Enter (x) to exit")
                        opt2 = input("Enter: ")
                        
                        if opt2 == 'x':
                            account.usermenu(self)
                            break 
                        
                        else:
                            #check for valid amount
                            try:
                                float(opt2)
                            except ValueError:
                                print("You did not enter a valid float, please try again")
                                break
                            #pass to relevent type of account
                            if self.accType == 'savings':
                                self.amount = float(opt2)
                                savingsAccount(self.username).deposit(self.accBalance, self.accID, self.amount)
                                time.sleep(2)
                                account.usermenu(self)
                                break
                            else:
                                self.amount = float(opt2)
                                CheckingAccount(self.username).deposit(self.accBalance, self.accID, self.amount)
                                time.sleep(2)
                                account.usermenu(self)
                                break
    #withdraw func
    def withdraw(self):
        print("Withdraw from an account")
        print("Please enter the ID of the account you want to withdraw from")
        opt = True
        while opt != 'x':
            print("Enter (x) to exit")
            opt = input("Enter: ")
            # read file and look for accounts under current username
            check = 0
            accDetails = []
            cAccDetails = []
            with open('accounts.txt', 'r') as file:
                cAccDetails = [(line.strip()).split() for line in file]
                for i in range(len(cAccDetails)):
                    for j in range(len(cAccDetails[i])):    
                        if cAccDetails[i][j] == self.username:
                            accDetails += cAccDetails[i]
            for i in range(len(accDetails)):
                if accDetails[i] == opt:
                    check = 1
            #check for ownership
            if check == 0:
                print("You do not own this account, please try again")
                time.sleep(2)
                account.usermenu(self)
                break
            if accDetails == []:
                print("You do not have any accounts")
                time.sleep(2)
                account.usermenu(self)
            #if its a savings account, dont allow withdrawal if balance is 0 or under
            for i in range(len(accDetails)):
                if opt == accDetails[i]:
                    self.accID = accDetails[i]
                    self.accType = accDetails[i+1]
                    self.accBalance = accDetails[i+3]
                    if self.accType == 'savings':
                        if float(self.accBalance) < 1:
                            print("Your balance is below 0, therefore you cannot withdraw money from this account")
                            account.usermenu(self)
                            break
                        else:
                            #checks if savings account has any withdrawals or transfers within last 30 days
                            transactions = []
                            with open('accountsTransactions.txt', 'r') as file:
                                transactions = [(line.strip()).split() for line in file]
                            for i in range(len(transactions)):
                                if transactions[i][3] == 'transfer' or transactions[i][3] == 'withdrawal':
                                    lastTran = transactions[i][4]
                                    dt_lastTran = datetime.strptime(lastTran, '%Y-%m-%d')
                                    delta = datetime.today() - dt_lastTran
                                    if (delta.days) < 30:
                                        print("There has been a withdrawal or transfer from this account within the last 30 days, therefore you cannot transfer money")
                                        time.sleep(2)
                                        account.usermenu(self)
                                        break
                                    
                            opt2 = True
                            
                            while opt2:
                                    #prompt for withdrawal amount
                                    print(self.accBalance)
                                    print("Please enter the amount to withdraw")
                                    print("Enter (x) to exit")
                                    opt2 = input("Enter: ")
                                    
                                    if opt2 == 'x':
                                        account.usermenu(self)
                                        break 
                                    #check for valid input
                                    try:
                                        float(opt2)
                                    except ValueError:
                                        print("You did not enter a valid float, please try again")
                                        break
                                    # if amount will take the account balance under 0, dont allow
                                    if float(self.accBalance) < float(opt2):
                                        print("You cannot withdraw this amount as your account will be below 0")
                                        break
                                    else:
                                        #pass details to savingsAccount class withdraw method
                                        self.amount = float(opt2)
                                        savingsAccount(self.username).withdraw(self.accBalance, self.accID, self.amount)
                                        time.sleep(2)
                                        account.usermenu(self)
                                        break
                    else:
                        # if checking account balance under -999 dont allow
                        if float(self.accBalance) < -999:
                            print("Your balance is below -999, therefore you cannot withdraw money from this account")
                            account.usermenu(self)
                            break
                        
                        opt20 = True
                        #prompt for amount
                        while opt20:
                            print("Please enter the amount to withdraw")
                            print("Enter (x) to exit")
                            opt20 = input("Enter: ")
                            
                            if opt20 == 'x':
                               account.usermenu(self)
                               break 
                            #input validation
                            try:
                                float(opt20)
                            except ValueError:
                                print("You did not enter a valid float, please try again")
                                break
                            
                            if (float(self.accBalance) - float(opt20)) < -999:
                                print("You cannot withdraw this amount as your account will be below -999")
                                break
                            else:
                                #pass to checkingAccount withdraw method
                                self.amount = float(opt20)
                                CheckingAccount(self.username).withdraw(self.accBalance, self.accID, self.amount)
                                time.sleep(2)
                                account.usermenu(self)
                                break
                            
     #method for transfers                                                            
    def transfer(self):
        print("Transfer money between accounts:")
        print("Please enter the ID of the account you want to transfer money FROM")
        opt = True
        while opt != 'x':
            print("Enter (x) to exit")
            opt = input("Enter: ")
            # read accounts file
            check = 0
            accDetails = []
            cAccDetails = []
            with open('accounts.txt', 'r') as file:
                cAccDetails = [(line.strip()).split() for line in file]
                for i in range(len(cAccDetails)):
                    for j in range(len(cAccDetails[i])):    
                        if cAccDetails[i][j] == self.username:
                            accDetails += cAccDetails[i]
                #if input matches one of users accounts id
                for i in range(len(accDetails)):
                    if accDetails[i] == opt:
                        check = 1
                if check == 0:
                    print("You do not own this account, please try again")
                    time.sleep(2)
                    account.usermenu(self)
                    break
                if accDetails == []:
                    print("You do not have any accounts")
                    account.usermenu(self)
                    break
                #assign details to attributes
            for i in range(len(accDetails)):
                if opt == accDetails[i]:
                    self.accID = accDetails[i]
                    self.accType = accDetails[i+1]
                    self.accBalance = accDetails[i+3]
                    if self.accType == 'savings':
                        #dont allow transfer for savings account with balance under 1
                        if float(self.accBalance) < 1:
                            print("Your balance is below 0, therefore you cannot transfer money from this account")
                            time.sleep(2)
                            account.usermenu(self)
                            break
                        else:
                            #check for withdrawals or transfer within last 30 days
                            transactions = []
                            with open('accountsTransactions.txt', 'r') as file:
                                transactions = [(line.strip()).split() for line in file]
                            for i in range(len(transactions)):
                                if transactions[i][3] == 'transfer' or transactions[i][3] == 'withdrawal':
                                    lastTran = transactions[i][4]
                                    dt_lastTran = datetime.strptime(lastTran, '%Y-%m-%d')
                                    delta = datetime.today() - dt_lastTran
                                    if (delta.days) < 30:
                                        print("There has been a withdrawal or transfer from this account within the last 30 days, therefore you cannot transfer money")
                                        time.sleep(2)
                                        account.usermenu(self)
                                        break
                            opt1 = True
                            
                            #prompt for account to transfer to
                            while opt1:
                                print("Please enter the ID of account you want to transfer money TO")
                                print("Enter (x) to exit")
                                opt1 = input("Enter: ")
                                
                                accDetails = []
                                cAccDetails = []
                                self.target = ''
                                with open('accounts.txt', 'r') as file:
                                    cAccDetails = [(line.strip()).split() for line in file]
                                    for i in range(len(cAccDetails)):
                                        for j in range(len(cAccDetails[i])):    
                                            if cAccDetails[i][0] == opt1:
                                                self.target = cAccDetails[i][0]
                                                self.targetAccBalance = cAccDetails[i][3]
                                    #input validation
                                    if self.target == '':
                                        print("No accounts with this ID exist, please try again")
                                        time.sleep(2)
                                        account.transfer(self)
                                    
                                    opt2 = True
                                    #prompt for transfer amount
                                    while opt2:
                                        print("Please enter the amount to transfer")
                                        print("Enter (x) to exit")
                                        opt2 = input("Enter: ")
                                        
                                        if opt2 == 'x':
                                            account.usermenu(self)
                                            break
                                        #input validation
                                        try:
                                            float(opt2)
                                        except ValueError:
                                            print("You did not enter a valid float, please try again")
                                            time.sleep(2)
                                            break
                                        
                                        if float(self.accBalance) < float(opt2):
                                            print("You cannot transfer this amount as your account will be below 0")
                                            time.sleep(2)
                                            break
                                        else:
                                            #pass attributes to savingsAccount transfer method
                                            self.amount = float(opt2)
                                            savingsAccount(self.username).transfer(self.accBalance, self.accID, self.target, self.amount, self.targetAccBalance)
                                            time.sleep(2)
                                            account.usermenu(self)
                                            break
                                if opt1 == 'x':
                                   account.usermenu(self)
                                   break
                    
                    else:
                        #dont allow transfer for checking accounts with balance under -999
                        if float(self.accBalance) < -999:
                            print("Your balance is below -999, therefore you cannot transfer money from this account")
                            time.sleep(2)
                            account.usermenu(self)
                            break
                        opt19 = True
                        #prompt for transfer target
                        while opt19:
                            print("Please enter the ID of account you want to transfer money TO")
                            print("Enter (x) to exit")
                            opt19 = input("Enter: ")
                            # read accounts file
                            accDetails = []
                            cAccDetails = []
                            self.target = ''
                            with open('accounts.txt', 'r') as file:
                                cAccDetails = [(line.strip()).split() for line in file]
                                for i in range(len(cAccDetails)):
                                    for j in range(len(cAccDetails[i])):    
                                        if cAccDetails[i][0] == opt19:
                                            self.target = cAccDetails[i][0]
                                            self.targetAccBalance = cAccDetails[i][3]
                                                        
                                if self.target == '':
                                    print("No accounts with this ID exist, please try again")
                                    time.sleep(2)
                                    account.transfer(self)
                                
                                opt20 = True
                                #prompt for transfer amount
                                while opt20:
                                    print("Please enter the amount to transfer")
                                    print("Enter (x) to exit")
                                    opt20 = input("Enter: ")
                                    
                                    if opt20 == 'x':
                                        account.usermenu(self)
                                        break
                                    #input valdiation
                                    try:
                                        float(opt20)
                                    except ValueError:
                                        print("You did not enter a valid float, please try again")
                                        time.sleep(2)
                                        break
                                    
                                    if (float(self.accBalance) - float(opt20)) < -999:
                                        print("You cannot transfer this amount as your account will be below -999")
                                        time.sleep(2)
                                        break
                                    else:
                                        #pass attributes to checkingAccount transfer method
                                        self.amount = float(opt20)
                                        CheckingAccount(self.username).transfer(self.accBalance, self.accID, self.target, self.amount, self.targetAccBalance)
                                        time.sleep(2)
                                        account.usermenu(self)
                                        break
                            if opt19 == 'x':
                               account.usermenu(self)
                               break
            if opt == 'x':
                account.usermenu(self)
                break
        #view accounts transactions
    # method for viewing account transactions
    def viewTransactions(self):
        print("Please enter the ID of an account to view it's transactions")
        opt = True
        while opt != 'x':
            print("Enter (x) to exit")
            opt = input("Enter: ")
            #read accounts file
            accDetails = []
            cAccDetails = []
            with open('accounts.txt', 'r') as file:
                cAccDetails = [(line.strip()).split() for line in file]
                for i in range(len(cAccDetails)):
                    for j in range(len(cAccDetails[i])):    
                        if cAccDetails[i][j] == self.username:
                            accDetails += cAccDetails[i]
                #check if user has any accounts
                if accDetails == '':
                    print("You do not have any accounts")
                    time.sleep(2)
                    account.usermenu(self)
            for i in range(len(accDetails)):
                if opt == accDetails[i]:
                    self.accID = accDetails[i]
                    self.accType = accDetails[i+1]
                    #pass account details to respective account type class viewTransactions function
                    if self.accType == 'savings':
                        savingsAccount(self.username).viewTransactions(self.accID)
                        time.sleep(4)
                        account.usermenu(self)
                        break
                    else:
                        CheckingAccount(self.username).viewTransactions(self.accID)
                        time.sleep(4)
                        account.usermenu(self)
                        break
                     
    def resetPassword(self):
        opt = True
        #confirm desire to reset password
        while opt:
            print("Are you sure you want to reset your password?")
            opt = input("Enter Y/N: ")
            
            newPass = ''
            cPass = ''
            cNewPass = ''
            #prompt for current password
            if opt == 'Y':
                print("Please enter your current password")
                cPass = input("Enter: ")
                #input validation
                if cPass == '':
                    print("Input empty, try again")
                    account.resetPassword(self)
                    break
                #read customers files and check for correct input
                with open('customers.txt', 'r') as file:
                    accDetails = [(line.strip()).split() for line in file]
                    for i in range(len(accDetails)):
                        for j in range(len(accDetails[i])):
                            if accDetails[i][j] == self.username:
                                if accDetails[i][2] == cPass:
                                    #prompt for new password
                                    print("Please enter a new password for your account")
                                    newPass = input("Enter: ")
                                    #input validation
                                    if newPass == '':
                                        print("Your password cannot be empty")
                                        account.resetPassword(self)
                                        break
                                    else:
                                        #prompt for repeat of new password
                                        print("Please repeat your new password")
                                        cNewPass = input("Enter: ")
                                        #input validation
                                        if cNewPass == '':
                                            print("Input empty, try again")
                                            account.resetPassword(self)
                                            break
                                        #check in repeat password matches new password
                                        if cNewPass != newPass:
                                            print("Passwords don't match, please try again")
                                            account.resetPassword(self)
                                            break
                                else:
                                    print("This is not your current password, try again")
                                    time.sleep(2)
                                    account.resetPassword(self)
                                    break
                #read customers file
                with open('customers.txt', 'r') as file:
                    for i in range(len(accDetails)):
                        for j in range(len(accDetails[i])):
                            if accDetails[i][j] == self.username:
                                accDetails[i][2] = newPass
                #overwrite customers file with changed password
                with open('customers.txt', 'w') as file:
                    for i in range(len(accDetails)):
                        for j in range(len(accDetails[i])):
                            file.write(accDetails[i][j])
                            file.write(' ')
                            if j == 5:
                                file.write("\n")
                print("Password Changed Successfully")
                time.sleep(2)
                account.usermenu(self)
                break
            elif opt == 'N':
                account.usermenu(self)
                break
            else:
                print("Enter a valid argument")
                time.sleep(2)
                account.resetPassword(self)
                
                
    def closeAccount(self):
        print("Close an account:")
        print("Please enter the ID of the account you would like to close")
        opt10 = True
        #prompt for account to close
        while opt10:
            
            print("Enter (x) to exit")
            opt10 = input("Choose: ")
            #read file and check if user owns account
            accDetails = []
            cAccDetails = []
            with open('accounts.txt', 'r') as file:
                cAccDetails = [(line.strip()).split() for line in file]
                for i in range(len(cAccDetails)):
                    for j in range(len(cAccDetails[i])):    
                        if cAccDetails[i][j] == self.username:
                            accDetails += cAccDetails[i]
            for i in range(len(accDetails)):
                if opt10 == accDetails[i]:
                    self.accID = accDetails[i]
                    self.accType = accDetails[i+1]
                    #pass details to respective account type class close method
                    if self.accType == 'savings':
                        savingsAccount(self.username).close(self.accID)
                        break
                    else:
                        CheckingAccount(self.username).close(self.accID)
                        break
                    

            if opt10 == 'x':
                account.usermenu(self)
                break

""" savingsAccount class allows user to perform actions on one of their savings accounts
    deposit allows user to deposit to a savings account
    withdraw allows user to withdraw from a savings account
    transfer allows user to transfer money from their savings account to another account
    viewTransactions allows user to view the transactions of any of their savings accounts
    close allows a user to close one of their savings accounts
"""

class savingsAccount(account):
    # __init__ username again to avoid errors after multiple passes
    def __init__(self, username):
        self.username = username
    
    #use passed attributes to deposit money in savings account
    def deposit(self, accBalance, accID, amount):
        print("Depositing money")
        accDetails = []
        #calculate new balance
        newAccBalance = float(accBalance) + float(amount)
        #read file and edit balance
        with open('accounts.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == accID:
                        accDetails[i][3] = str(newAccBalance)
        #overwrite file with edited balance
        with open('accounts.txt', 'w') as file:
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    file.write(str(accDetails[i][j]))
                    file.write(' ')
                    if j == 4:
                        file.write("\n") 
        #record transaction by writing details to accountsTransactions file
        target = accID             
        action = 'deposit'
        tranDate = date.today()
        tranDetails = [str(accID), str(target), str(amount), action, str(tranDate)]
        with open('accountsTransactions.txt', 'a') as file:
            for i in range(len(tranDetails)):
                file.write(tranDetails[i])
                file.write(' ')
            file.write('\n')
            print("Money has been deposited! Your new balance is: "+str(newAccBalance))
    #use passed attributes to withdraw money from savings account
    def withdraw(self, accBalance, accID, amount):
        print("Withdrawing money")
        accDetails = []
        #calculate new balance
        newAccBalance = float(accBalance) - float(amount)
        #read file and edit balance
        with open('accounts.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == accID:
                        accDetails[i][3] = str(newAccBalance)
        #overwrite file with edited balance
        with open('accounts.txt', 'w') as file:
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    file.write(str(accDetails[i][j]))
                    file.write(' ')
                    if j == 4:
                        file.write("\n") 
        #record transaction to accountsTransactions file
        target = accID             
        action = 'withdrawal'
        tranDate = date.today()
        tranDetails = [str(accID), str(target), str(amount), action, str(tranDate)]
        with open('accountsTransactions.txt', 'a') as file:
            for i in range(len(tranDetails)):
                file.write(tranDetails[i])
                file.write(' ')
            file.write('\n')
            print("Money has been withdrawn! Your new balance is: "+str(newAccBalance))
          
    #use passed attributes to transfer money from a savings account to another account
    def transfer(self, accBalance, accID, target, amount, targetAccBalance):
        print("Transferring money")
        accDetails = []
        #calculate new balance
        newAccBalance = float(accBalance) - float(amount)
        #read file and edit user's account balance
        with open('accounts.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == accID:
                        accDetails[i][3] = str(newAccBalance)
                        
        #overwrite file with edited balance 
        with open('accounts.txt', 'w') as file:
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    file.write(accDetails[i][j])
                    file.write(' ')
                    if j == 4:
                        file.write("\n")         
        #calculate transfer targets new balance     
        newTargetBalance = float(targetAccBalance) + float(amount)
        #read file and edit target's balance
        with open('accounts.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == target:
                        accDetails[i][3] = str(newTargetBalance)
        #overwrite file with edited balance
        with open('accounts.txt', 'w') as file:
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    file.write(accDetails[i][j])
                    file.write(' ')
                    if j == 4:
                        file.write("\n")
            
        #record transaction in accountsTransactions
        action = 'transfer'
        tranDate = date.today()
        tranDetails = [str(accID), str(target), str(amount), action, str(tranDate)]
        with open('accountsTransactions.txt', 'a') as file:
            for i in range(len(tranDetails)):
                file.write(tranDetails[i])
                file.write(' ')
            file.write('\n')
            print("Money has been transferred! Your new balance is: "+str(newAccBalance))
    
    #use passed attributes to display account Transactions
    def viewTransactions(self, accID):
        print("Displaying Transactions")
        print("FROM:\t\tTO:\t\t:AMOUNT:\t\tTYPE:\t\tDATE:")
        accDetails = []
        #read transactions file and display relevent transactions
        with open('accountsTransactions.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == accID:
                        print(accDetails[i][0]+'\t'+accDetails[i][1]+'\t'+accDetails[i][2]+'\t\t'+accDetails[i][3]+'\t\t'+accDetails[i][4]+'\n')
           
    #use passed attributes to delete an account from accounts file             
    def close(self, accID):
            print("Are you sure you want to close this account? If you have any remaining balance, we will steal it.")
            opt4 = True
            while opt4:
                #confirm
                opt4 = input("Enter Y/N: ")
                if opt4 == 'Y':
                    #read accounts file and write every line excluding the closing accounts to tempFile
                    with open('accounts.txt', 'r') as file:
                       with open('tempFile.txt', "w") as temp:
                           for line in file:
                               if not line.strip("\n").startswith(accID):
                                   temp.write(line)
                    #rename tempFile to accounts.txt
                    os.replace('tempFile.txt', 'accounts.txt')
                    
                    print("Account deleted")
                    time.sleep(3)
                    account.usermenu(self)
                    break
                elif opt4 == 'N':
                    account.closeAccount(self)
                    break
                else:
                    print("Please enter a valid argument")

""" CheckingAccount class allows user to perform actions on one of their checking accounts
    deposit allows user to deposit to a checking account
    withdraw allows user to withdraw from a checking account
    transfer allows user to transfer money from their checking accounts to another account
    viewTransactions allows user to view the transactions of any of their checking accounts
    close allows a user to close one of their checking accounts
"""

class CheckingAccount(account):
    # __init__ username again to avoid errors after multiple passes
    def __init__(self, username):
        self.username = username 
        
    #use passed attributes to deposit money in checking account
    def deposit(self, accBalance, accID, amount):
        print("Depositing money")
        accDetails = []
        #calculate new balance
        newAccBalance = float(accBalance) + float(amount)
        #read file and edit balance
        with open('accounts.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == accID:
                        accDetails[i][3] = str(newAccBalance)
        #overwrite file with edited balance
        with open('accounts.txt', 'w') as file:
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    file.write(str(accDetails[i][j]))
                    file.write(' ')
                    if j == 4:
                        file.write("\n") 
        #record transaction by writing details to accountsTransactions file
        target = accID             
        action = 'deposit'
        tranDate = date.today()
        tranDetails = [str(accID), str(target), str(amount), action, str(tranDate)]
        with open('accountsTransactions.txt', 'a') as file:
            for i in range(len(tranDetails)):
                file.write(tranDetails[i])
                file.write(' ')
            file.write('\n')
            print("Money has been deposited! Your new balance is: "+str(newAccBalance))
    #use passed attributes to withdraw money from savings account
    def withdraw(self, accBalance, accID, amount):
        print("Withdrawing money")
        accDetails = []
        #calculate new balance
        newAccBalance = float(accBalance) - float(amount)
        #read file and edit balance
        with open('accounts.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == accID:
                        accDetails[i][3] = str(newAccBalance)
        #overwrite file with edited balance
        with open('accounts.txt', 'w') as file:
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    file.write(str(accDetails[i][j]))
                    file.write(' ')
                    if j == 4:
                        file.write("\n") 
        #record transaction to accountsTransactions file
        target = accID             
        action = 'withdrawal'
        tranDate = date.today()
        tranDetails = [str(accID), str(target), str(amount), action, str(tranDate)]
        with open('accountsTransactions.txt', 'a') as file:
            for i in range(len(tranDetails)):
                file.write(tranDetails[i])
                file.write(' ')
            file.write('\n')
            print("Money has been withdrawn! Your new balance is: "+str(newAccBalance))
            
            
    #use passed attributes to transfer money from a savings account to another account
    def transfer(self, accBalance, accID, target, amount, targetAccBalance):
        print("Transferring money")
        accDetails = []
        #calculate new balance
        newAccBalance = float(accBalance) - float(amount)
        #read file and edit user's account balance
        with open('accounts.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == accID:
                        accDetails[i][3] = str(newAccBalance)
        #overwrite file with edited balance 
        with open('accounts.txt', 'w') as file:
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    file.write(accDetails[i][j])
                    file.write(' ')
                    if j == 4:
                        file.write("\n")       
         #calculate transfer targets new balance        
        newTargetBalance = float(targetAccBalance) + float(amount)
        #read file and edit target's balance
        with open('accounts.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == target:
                        accDetails[i][3] = str(newTargetBalance)
        #overwrite file with edited balance
        with open('accounts.txt', 'w') as file:
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    file.write(accDetails[i][j])
                    file.write(' ')
                    if j == 4:
                        file.write("\n")
            
        #record transaction in accountsTransactions
        action = 'transfer'
        tranDate = date.today()
        tranDetails = [str(accID), str(target), str(amount), action, str(tranDate)]
        with open('accountsTransactions.txt', 'a') as file:
            for i in range(len(tranDetails)):
                file.write(tranDetails[i])
                file.write(' ')
            file.write('\n')
            print("Money has been transferred! Your new balance is: "+str(newAccBalance))
    
    #use passed attributes to display account Transactions
    def viewTransactions(self, accID):
        print("Displaying Transactions")
        print("FROM:\t\tTO:\t\t:AMOUNT:\t\tTYPE:\t\tDATE:")
        accDetails = []
        #read transactions file and display relevent transactions
        with open('accountsTransactions.txt', 'r') as file:
            accDetails = [(line.strip()).split() for line in file]
            for i in range(len(accDetails)):
                for j in range(len(accDetails[i])):
                    if accDetails[i][j] == accID:
                        print(accDetails[i][0]+'\t'+accDetails[i][1]+'\t'+accDetails[i][2]+'\t\t'+accDetails[i][3]+'\t\t'+accDetails[i][4]+'\n')
    
    #use passed attributes to delete an account from accounts file 
    def close(self, accID):
            print("Are you sure you want to close this account? If you have any remaining balance, we will steal it.")
            opt9 = True
            while opt9:
                #confirm
                opt9 = input("Enter Y/N: ")
                if opt9 == 'Y':
                    #read accounts file and write every line excluding the closing accounts to tempFile
                    with open('accounts.txt', 'r') as file:
                       with open("tempFile.txt", "w") as temp:
                           for line in file:
                               if not line.strip("\n").startswith(accID):
                                   temp.write(line)
                    #rename tempFile to accounts.txt
                    os.replace('tempFile.txt', 'accounts.txt')
                    
                    print("Account deleted")
                    time.sleep(3)
                    account.usermenu(self)
                    break
                elif opt9 == 'N':
                    account.closeAccount(self)
                    break
                else:
                    print("Please enter a valid argument")

# display user menu at program start
customer().startmenu()