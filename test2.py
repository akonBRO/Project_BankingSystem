class Banking_System:
    
    def __init__(self):
        self.balance_dict=0

    def current_balance(self):
        for i in balance_dict.keys():
            if i==self.name:
                print('---------------------------------')
                print(f'Your Current Balance is {balance_dict[i][0]} tk only')
                print('---------------------------------')
                print('Return to main menu==1 or Exit==0')
                print('---------------------------------')
                menu=input('Type--')
                if menu==str(1):
                    self.user_acc()
                if menu==str(0):
                    print('Thank You!')
                    print('---------------------------------')
                else:
                    self.user_acc
        return None

    def add_money(self):
        add= float(input('Amount of money --'))
        for i in balance_dict.keys():
            if i==self.name:
                balance_dict[i][0]+=add
                print('---------------------------------')
                print(f'Money added Successfully.\nYour Current Balance is {balance_dict[i][0]} tk only')
                print('---------------------------------')
                print('Return to main menu==1 or Exit==0')
                print('---------------------------------')
                menu=int(input('Type--'))
                if menu==1:
                    self.user_acc()
                if menu==0:
                    print('Thank You!')
                    print('---------------------------------')
        return None

    def withdraw_money(self):
        withdraw= float(input('Amount of money you want to withdraw --'))
        for i in balance_dict.keys():
            if i==self.name:
                if withdraw>balance_dict[i][0]:
                    print('---------------------------------')
                    print('Sorry, not enough money! Please check your balance.')
                    print('---------------------------------')
                else:
                    balance_dict[i][0]-=withdraw
                    print('---------------------------------')
                    print(f'Money Withdrawn Successfully.\nYour Current Balance is {balance_dict[i][0]} tk only')
                    print('---------------------------------')
                print('Return to main menu==1 or Exit==0')
                print('---------------------------------')
                menu=int(input('Type--'))
                if menu==1:
                    self.user_acc()
                if menu==0:
                    print('Thank You!')
                    print('---------------------------------')
        return None
    
    def send_money(self):
        receiver= input('Enter Receiver Account Name: ')
        flag= False
        for i in balance_dict.keys():
            if i==receiver:
                flag= True
                send_amount= int(input('Enter Amount: '))
                if send_amount<balance_dict[self.name][0] and send_amount>0:
                    balance_dict[self.name][0]-=send_amount
                    balance_dict[i][0]+=send_amount
                    print('---------------------------------')
                    print(f'Send Money Successful!\nYour Current Balance is {balance_dict[self.name][0]} tk only')
                    print('---------------------------------')
                    print('Return to main menu==1 or Exit==0')
                    print('---------------------------------')
                    menu=int(input('Type--'))
                    if menu==1:
                        self.user_acc()
                    if menu==0:
                        print('Thank You!')
                        print('---------------------------------')
                        self.user_login()
                else:
                    print('---------------------------------')
                    print('Not Enough Balance In Your Account')
                    print('---------------------------------')
                    self.send_money
        if flag==False:
            print('---------------------------------')
            print('No account found. Please try again!')
            print('---------------------------------')
            self.send_money
                        
        return None
    
    def user_login(self):
        print('For Login, Type-- 1')
        print('For Registration, Type-- 0')
        print('---------------------------------')
        typ= input('Type: ')
        flag= False
        if typ=='1':
            self.name= input('Your Name: ')
            for i in balance_dict.keys():
                if i==self.name:
                    flag= True
                    self.check_password= int(input('Your Password: '))
                    if self.check_password==balance_dict[i][1]:
                        self.user_acc()
                    else:
                        print('Wrong Password')
                        self.user_login                  
            if flag==False:
                print('No Account Found. Try Again!')
                print('---------------------------------')
                self.user_login()
        if typ=='0':
            self.reg_acc()      
        else:
            print('---------------------------------')
            self.user_login()      
        return None
    
    def reg_acc(self):
        self.name1= str(input('Account Name: '))
        self.password= int(input('Choose Password(must be 4 digit integer): '))
        temp_list= [0]
        temp_list.append(self.password)
        balance_dict[self.name1]=temp_list
        temp_list=[0]
        print('Registration Successful.')
        print('---------------------------------')
        self.user_login()
        return None
    
    def user_acc(self): 
        flag2=False
        for i in balance_dict.keys():
            if i==self.name:
                flag2=True
                print('---------------------------------')
                print(f'Welcome to our Banking System, {i}.')
                print('---------------------------------')
                print('Type numbers accordingly to access')
                print('Current Balance --Press 1--')
                print('Add Money --Press 2--')
                print('Withdraw Money --Press 3--')
                print('Send Money --Press 4--')
                print('---------------------------------')
                user= input('Type Number --')
                if user==str(1):
                    self.current_balance()
                if user==str(2):
                    self.add_money()
                if user==str(3):
                    self.withdraw_money()
                if user==str(4):
                    self.send_money()
                else:
                    print('Wrong Input. Please use any valid numbers')
                    print('---------------------------------')
                    self.user_acc()
        if flag2==False:
            print('No Account Found')
            print('---------------------------------')
        return None
    
balance_dict= {'Sabbir':[0,1234]}    
bank=Banking_System()
bank.user_login()