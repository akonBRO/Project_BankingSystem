
class Banking_System:
    def __init__(self):
        self.balance_dict= {'Sabbir':0}

    def current_balance(self):
        for i in self.balance_dict.keys():
            if i==self.name:
                print(f'Your Current Balance is {self.balance_dict[i]} tk only')
                print('Return to main menu==1 or Exit==0')
                menu=int(input('Type--'))
                if menu==1:
                    self.user_acc()
                if menu==0:
                    print('Thank You!')
            
        return None

    def add_money(self):
        add= float(input('Amount of money --'))
        for i in self.balance_dict.keys():
            if i==self.name:
                self.balance_dict[i]+=add
                print(f'Money added Successfully.\nYour Current Balance is {self.balance_dict[i]} tk only')
                print('Return to main menu==1 or Exit==0')
                menu=int(input('Type--'))
                if menu==1:
                    self.user_acc()
                if menu==0:
                    print('Thank You!')
        return None

    def withdraw_money(self):
        withdraw= float(input('Amount of money you want to withdraw --'))
        for i in self.balance_dict.keys():
            if i==self.name:
                if withdraw>self.balance_dict[i]:
                    print('Sorry, not enough money! Please check your balance.')
                else:
                    self.balance_dict[i]-=withdraw
                    print(f'Money Withdrawn Successfully.\nYour Current Balance is {self.balance_dict[i]} tk only')
                print('Return to main menu==1 or Exit==0')
                menu=int(input('Type--'))
                if menu==1:
                    self.user_acc()
                if menu==0:
                    print('Thank You!')
        return None
    
    def user_name(self):
        print('For Login, Type-- 1')
        print('For Registration, Type-- 0')
        typ= int(input('Type: '))
        if typ==1:
            self.name= input('Your Name:')
            for i in self.balance_dict.keys():
                if i==self.name:
                    self.user_acc()
                else:
                    print('No Account Found. Try Again!')
                    self.user_name()
        if typ==0:
            self.reg_acc()      
        else:
            print('Wrong Input! Please try again.')
            self.user_name()      
        return None
    
    def reg_acc(self):
        self.data= str(input('Account Name:'))
        self.balance_dict[self.data]=0
        print('Registration Successful.')
        self.user_name()
        return None
    
    def user_acc(self): 
        for i in self.balance_dict.keys():
            if i==self.name:
                print(f'Welcome to our Banking System, {i}')
                print('Type numbers accordingly to access')
                print('Current Balance --Press 1--')
                print('Add Money --Press 2--')
                print('Withdraw Money --Press 3--')
                user= int(input('Type Number --'))
                if user==1:
                    self.current_balance()
                if user==2:
                    self.add_money()
                if user==3:
                    self.withdraw_money()
                if user<0 or 3<user:
                    print('Wrong Input. Please use any valid numbers')
                    self.user_acc()
            else:
                print('No Account Found')
        return None
    
bank=Banking_System()
bank.user_name()