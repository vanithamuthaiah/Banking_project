import sys

class Logging:

    def __init__(self):
        self.user = self.user_type()

    def user_type(self):
        print('Welcome to XYZ Bank\n 1.Customer 2.Admin 3.Exit')
        user = input('\n Who are you? Please enter the number: ')
        return user

    def site(self):
        if self.user == '1':
            print('\n ***welcome to customer area*** \n')
            return self.customer_area()
        elif self.user == '2':
            print('\n ***Welcome to Admin area*** \n')
            return self.admin_area()
        elif self.user == '3':
            return sys.exit()

    def customer_area(self):
        entry = input('Please choose from the option \n 1.Login \n 2.Sign up \n 3.Previous Menu \n 4.Exit \n')
        data = Customer()

        if entry == '1':
            return data.login()


        elif entry == '2':
            return data.sign_up()


        elif entry == '3':
            return self.user_type()
        else:
            SystemExit

    def admin_area(self):
        entry= input('Please choose from the option \n 1.Login \n 2.Previous Menu \n 3.Exit \n')
        if entry == '1':
            username=input('Please enter your Username: \n')
            password=input('Please enter your Password: \n')

        elif entry== '2':
            return self.user_type()
        else:
            systemExist



class Customer:
    users = {'Vyshu': 9000, 'Mani': 1000, 'Vani': 2000, 'Jani': 6000}

    def __init__(self):
        self.user_name = ''
        self.__balance = 0

    def login(self):

        self.user_name = input('\n Username:  ')
        self.__balance = self.users.get(self.user_name)
        print(self.__balance)

        if self.user_name in self.users:
            input('\n password:  ')
            return self.mainmenu()

        else:
            print('Please enter the valid username!!')

    def sign_up(self):
        new_user = input('enter your name: ')
        bal = int(input('enter your balance: '))
        input('Enter your address: ')
        input('Enter your Phone Number: ')
        input('Enter your Username: ')
        input('Enter your Password: ')
        self.users[new_user] = bal
        print('Account created successfully!! \n Please exit and login')

    def mainmenu(self):

        print('\n******Welcome ' + self.user_name + '******\n')
        process = input('Please choose the number \n 1.Withdrawal \n 2.Deposit \n 3.Show balance \n')

        if process == '1':
            print(f'Your current balance is: {self.withdrawal()}')
        elif process == '2':
            print(f'Your current balance is {self.deposit()}')
        else:
            print(f'Your Account balance is {self.__balance}')

    def withdrawal(self):
        withdrawal_amount = int(input('Please enter the amount to be withdraw: '))
        if withdrawal_amount > self.__balance:
            print(f'Please enter the amount lesser than {self.__balance}')
        else:
            self.__balance = self.__balance - withdrawal_amount

            self.users.update({self.user_name:self.__balance})
            print(self.users)

            return self.__balance

    def deposit(self):
        deposit_amount = int(input('Please enter the amount to be deposit: '))
        self.__balance = self.__balance + deposit_amount
        self.users[self.user_name] = self.__balance
        return self.__balance





d = Logging()
# print(d.user_type())
print(d.site())

# call from another class
# dic update