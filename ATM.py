
class ATM:
    def __init__(self):
        self.adminUsername = 'UZAIR MUSTAFA'
        self.adminPin = '3838'
        self.isloginAdmin = False
        self.accountsInfo = {}
        self.balance = 0
        self.islogin = False
        self.menu()
        

    def authentication(self):
        i=3
        
        self.accNumber = int(input('enter your account number\n'))
        self.pin = input('enter four digit pin\n')
        flag = False
        while(i>=0):
            
            if self.accNumber in self.accountsInfo.keys() and self.pin ==self.accountsInfo[self.accNumber]['PIN']:
                print('Success...!\n')
                flag = True
                break
            elif self.accNumber in self.accountsInfo.keys() and self.pin !=self.accountsInfo[self.accNumber]['PIN']:
                print(f'You have entered wrong pin\nre-enter the pin\n{i} try/tries left\n')
                pin = input()
                if i ==1 and self.pin !=self.accountsInfo[self.accNumber]['PIN']:
                    print('You have entered wrong pin four times\n...EXITING...')
                    self.exit()
                    break
            elif self.accNumber not in self.accountsInfo.keys():
                print(f'You have entered wrong account number\nre-enter the account numnber\n{i} try/tries left\n')
                self.accNumber = input()
                if i ==1 and self.accNumber not in self.accountsInfo.keys():
                    print('You have entered wrong account number four times\n...EXITING...')
                    self.exit()
                    break
            else:
                print(f'Invalid entries\n{i} try/tries left\n')
                self.accNumber = int(input('Enter the account number\n'))
                self.pin = input('Enter the pin\n')
                if i ==1 and id not in self.accountsInfo.keys():
                    print('You have entered wrong information four times\n...EXITING...')
                    self.exit()
                    break
            i-=1
        if flag:
            self.islogin = True
        return flag


    def optSelection(self):
        opt = int(input('''
        Choose an Option From Following
        1.Goto Menu
        2.Goto Login
        3.Make Deposite
        4.Balance Inquiry
        5.Withraw Money
        6.Change Pin
        7.Log Out
        or press any other button to Exit
        '''))
        if opt == 1:
            self.menu()
        elif opt == 2:
            self.login()
        elif opt == 3:
            self.deposit()
        elif opt == 4:
            self.balanceInquiry()
        elif opt == 5:
            self.withdraw()
        elif opt == 6:
            self.changePin()
        elif opt == 7:
            self.logout()
        else:
            self.exit()


    def menu(self):
        print('...MENU...\n')
        userInput =int(input( '''
        choose from following options
        0.Log in as admin
        1.Create new Account
        2.Login To Existing Account
        3.Exit
        '''))
        if userInput ==0:
            self.admin()
        elif userInput ==1:
            self.createAccount()
        elif userInput ==2:
            if len(self.accountsInfo)==0:
                print('No account exists\nDo you want to create a new account\npress 1 to create account and 2 to exit the system\n')
                opt = int(input())
                if opt ==1:
                    self.createAccount()
                else:
                    self.exit()
            else:
                self.login()
        else:
            self.exit()

    def admin(self):
        print('......ADMIN LOGIN......')
        if self.isloginAdmin:
            print('You are already logged in as admin\n')
            self.adminOpt()
        elif self.islogin:
            print('Already one account is logged in\nLog out first\n')
            self.optSelection()
        else:
            username = input('Enter the Admin username\n')
            pin = input('Enter the Admin pin\n')
            if username == self.adminUsername and pin == self.adminPin:
                self.isloginAdmin = True
                print('Admin logged in...\n')
                self.adminOpt()
                

    def adminOpt(self):
        temp = int(input('''
                Choose operation you want to perform
                1.See registered accounts 
                2.Remove an account
                3.Add an account
                4.Log out
                '''))
        if temp == 1:
            if len(self.accountsInfo)==0:
                print('No registered accounts to show\n')

            else:
                print(f'Following are the details of registered accounts\n{self.accountsInfo}')
            self.adminOpt()
        elif temp ==2:
            if len(self.accountsInfo)==0:
                print('No accounts exist\n')
            else:
                accNumber = int(input('Enter the account number of the customer of which you want to remove account\n'))
                del self.accountsInfo[accNumber]
                print('Account removed successfully\n')
            self.adminOpt()
        elif temp  == 3:
            self.accNumber = int(input('Enter the account number\n'))
            self.username = input('Enter the account holder name\n')
            self.pin = input('enter a four digit pin\n')
            while True:
                if len(self.pin)==4:
                    #print('Pin created successfully\n')
                    break
                else:
                    if len(self.pin)>4:
                        print('length of pin exceeded\nre-enter a four digit pin\n')
                        self.pin = input()
                    else:
                        print('length of pin is less than 4\nre-enter a four digit pin\n')
                        self.pin = input()
            self.accountsInfo[self.accNumber] = {'Name':self.username,'PIN':self.pin,'Balance':0} 
            print('Congrats! Account Created Sucessfully\n')
            self.adminOpt()
            
        else:
            self.isloginAdmin = False
            print('Logged out seccessfully...\nReturning to menu\n')
            self.menu()
        

    def createAccount(self):
        print('...NEW ACCOUNT...\n')
        self.accNumber = int(input('Enter the account number\n'))
        self.username = input('Enter the account holder name\n')
        self.pin = input('enter a four digit pin\n')
        while True:
            if len(self.pin)==4:
                #print('Pin created successfully\n')
                break
            else:
                if len(self.pin)>4:
                    print('length of pin exceeded\nre-enter a four digit pin\n')
                    self.pin = input()
                else:
                    print('length of pin is less than 4\nre-enter a four digit pin\n')
                    self.pin = input()
        self.accountsInfo[self.accNumber] = {'Name':self.username,'PIN':self.pin,'Balance':0} 
        print('Congrats! Account Created Sucessfully\n')
        opt = int(input('''
        choose option among following
        1.Goto Login
        2.Goto Menu\n'''))
        while True:
            if opt ==1:
                self.login()
                break
            elif opt == 2:    
                self.menu()
                break
            else:
                print('Wrong Input\nSelect from given options\nre-enter your choice\n1.Goto Login\n2.Goto Menu\n')
                opt = int(input())

    def login(self):
        print('...LOGIN...\n')
        if self.islogin:
            print('Already one account is logged in\nLog out first\n')
            self.optSelection()
        else:
            flag = self.authentication()
            if flag :
                print('Logged in...\n')
                self.optSelection()
            else:
                print('Authentication Failed...\nReturning to menu\n')
                self.menu()

    def changePin(self):
        print('...CHANGE PIN...\n')
        print('Enter your account number and old pin\nEnter the new pin after successful authentication\n')
        flag = self.authentication()
        if flag:
            pin = input('Enter a new 4 digit pin\n')
            while True:
                if len(pin)==4:
                    self.accountsInfo[self.accNumber]['PIN'] =pin
                    print('Pin changed successfully\n')
                    self.islogin = False
                    break
                else:
                    if len(pin)>4:
                        print('length of pin exceeded\nre-enter a four digit pin\n')
                        pin = input()
                    else:
                        print('length of pin is less than 4\nre-enter a four digit pin\n')
                        pin = input()
             
        self.optSelection()

    def balanceInquiry(self):
         
        print('...BALANCE INQUIRY...\n')
        balance = self.accountsInfo[self.accNumber]['Balance']
        if self.islogin:
            
             print(f'Your current balance is {balance}\n')
             self.optSelection()
        else:
            flag = self.authentication()
            if flag:
                print(f'Your current balance is {balance}\n')
                self.optSelection()
            else:
                self.exit()

    def deposit(self):
        print('...DEPOSITE SECTION...\n')
        balance = self.accountsInfo[self.accNumber]['Balance']
        if self.islogin:
            amount = int(input(f'Your current balance is {balance}\nEnter the amount you want to deposit\n'))
            self.accountsInfo[self.accNumber]['Balance']+=amount
            balance = self.accountsInfo[self.accNumber]['Balance']
            print(f'Deposite successful\nNew balance is {balance}\n')
            self.optSelection()
        else:
            flag = self.authentication()
            if flag:
                amount = int(input(f'Your current balance is {balance}\nEnter the amount you want to deposit\n'))
                self.accountsInfo[self.accNumber]['Balance']+=amount
                balance = self.accountsInfo[self.accNumber]['Balance']
                print(f'Deposite successful\nNew balance is {balance}\n')
                self.optSelection()
            else:
                print('Authentication Failed...\nReturning to menu\n')
                self.menu()

    def withdraw(self):
        print('...WITHDRAW MONEY...\n')
        balance = self.accountsInfo[self.accNumber]['Balance']
        if self.islogin:
            amount = int(input('Enter the amount you want to withdraw\n'))
            while True:
                
                if amount<self.accountsInfo[self.accNumber]['Balance']:
                    self.accountsInfo[self.accNumber]['Balance']-=amount
                    balance = self.accountsInfo[self.accNumber]['Balance']
                    print(f'Withdrawl successful...\nAmount withdrawn:\n{amount}\nRemaining Balance:\n{balance}\n')
                    break
                else:
                    print(f'Insufficient Balance\nYour current balance is {balance}\nYour amount must be less than this balance\nEnter the amount again or press 0 to exit system\n')
                    amount = int(input())
                    if amount == 0:
                        self.exit()
                        break
                    else:
                        pass
            self.optSelection()
        else:
            flag = self.authentication()
            if flag:
                amount = int(input('Enter the amount you want to withdraw\n'))
                while True:
                    
                    if amount<self.accountsInfo[self.accNumber]['Balance']:
                        self.accountsInfo[self.accNumber]['Balance']-=amount
                        balance = self.accountsInfo[self.accNumber]['Balance']
                        print(f'Withdrawl successful...\nAmount withdrawn:\n{amount}\nRemaining Balance:\n{balance}\n')
                        break
                    else:
                        print(f'Insufficient Balance\nYour current balance is {balance}\nYour amount must be less than this balance\nEnter the amount again or press 0 to exit system\n')
                        amount = int(input())
                        if amount == 0:
                            self.exit()
                            break
                        else:
                            pass
            
            else:
                print('Authentication Failed...\nReturning to menu\n')
                self.menu()

            self.optSelection()

    def logout(self):
        if self.islogin:
            self.islogin = False
            print('Logged Out successfullly...\n')
        else:
            print('No account is logged in\n')
            self.menu()
        self.optSelection()

    
    def exit(self):
        print('Program Exited')
                
atm = ATM()
