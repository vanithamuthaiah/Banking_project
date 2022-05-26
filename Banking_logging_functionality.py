import sqlite3 as sl
import sys

con=sl.connect('usersarchive3.db')
cur = con.cursor()
'''
#with cur:
cur.execute("""
    CREATE TABLE USER (
        Account_num INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Username TEXT,
        Balance INTEGER,
        Address TEXT,
        Phone_num INTEGER,
        Password TEXT        
        
    );
""")


sql = 'INSERT INTO USER (Account_num, Username, Balance, Address,Phone_num,Password) values(?,?,?,?,?,?)'
data=[(100,'Vani',1000,'xyz',123456,'123'),
          (101,'Mani',2000,'xyk',123456,'1234')]
#with cur:
cur.executemany(sql, data)
con.close

#with cur:
with con:
    con.execute("""
        CREATE TABLE Admins7_Info ( 
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Username TEXT,
            Password TEXT        
        
        );
    """)


sql1 = 'INSERT INTO Admins7_Info (ID, Username,Password) values(?,?,?)'
data1=[(22001,'Janu','123'),
          (22002,'Manu','1234'),
          (22003,'Aishu','456')]
with con:
    con.executemany(sql1, data1)
#cu.close
'''
class Logging:

    def __init__(self):
        self.user = self.get_user_type()

    def get_user_type(self):
        print('Welcome to XYZ Bank\n 1.Customer 2.Admin 3.Exit')
        user = input('\n Who are you? Please enter the number: ')
        return user

    def welcome_page(self):
        if self.user == '1':
            print('\n ***welcome to customer area*** \n')
            return self.customer_area()
        elif self.user == '2': 
            data1=Admin()
            print('\n ***Welcome to Admin area*** \n')         
            return data1.admin_area()
        elif self.user == '3':
            SystemExit

    def customer_area(self):
        entry = input('Please choose from the option \n 1.Login \n 2.Sign up \n 3.Previous Menu \n 4.Exit \n')
        data = Customer()
        if entry == '1':
            return data.login()
        elif entry=='2':
            data.sign_up()
        elif entry=='3':
            return self.get_user_type()
        else:
            SystemExit


class Customer:

    def __init__(self):
        self.user_name = ''

    def login(self):
        self.user_name = input('\n Username:  ')
        with con:
            db_userlist = cur.execute("SELECT Username FROM USER")
            user_found=False
            for db_user in db_userlist:
                if  db_user[0] == self.user_name:
                    user_found=True
                    counter=0
                    while True:
                        if counter==3:
                            print('Done with your password attempt')
                            break
                        password=input('Please enter the password: ')
                        db_password=cur.execute(f"SELECT Password FROM USER WHERE Username = '{self.user_name}'")
                        for db_pw in db_password:
                            if db_pw[0] == password:
                                print('welcome!!!')
                                return self.mainmenu()
                            else:
                                print('Wrong Password!!')
                                counter+=1
            if user_found==False:
                print('Username is unavailable')

    def mainmenu(self):
        print('\n******Welcome ' + self.user_name + '******\n')
        process = input('Please choose the number \n 1.Withdrawal \n 2.Deposit \n 3.Show balance \n')

        if process == '1':
            print(f'Your current balance is: {self.withdrawal()}')
        elif process == '2':
            print(f'Your current balance is {self.deposit()}')
        elif process=='3':
            print(f'Your Account balance is {self.get_db_balance()}')

    def withdrawal(self):
        withdrawal_amount = int(input('Please enter the amount to be withdraw: '))
        balance=self.get_db_balance()
        if withdrawal_amount > balance:
                print(f'Please enter the amount lesser than {balance}')
        else:
            balance = balance - withdrawal_amount
            self.update_db_balance(balance)
            return balance

    def deposit(self):
        deposit_amount = int(input('Please enter the amount to be deposit: '))
        balance=self.get_db_balance()
        balance = balance + deposit_amount
        self.update_db_balance(balance)
        return balance

    def get_db_balance(self):
        with con:
            cur.execute(f"SELECT Balance[0] FROM USER WHERE Username='{self.user_name}'")
            balance1 = [int(balance1[0]) for balance1 in cur.fetchall()]
            return balance1[0]

    def update_db_balance(self,balance):
        with con:
            db_balance = cur.execute(f"UPDATE USER SET Balance= {balance} WHERE Username  = '{self.user_name}'")
    
    def sign_up(self):

        Username = input('enter your Username: ')
        Balance = int(input('enter your balance: '))
        Address=input('Enter your address: ')
        Phone_num=int(input('Enter your Phone Number: '))
        Password=input('Enter your Password: ')
        cur.execute("""
        INSERT INTO USER(Username, Balance, Address, Phone_num, Password )
        VALUES (?,?,?,?,?)
        """, (Username, Balance, Address, Phone_num, Password ))
        con.commit ()
        print ( '****Data Signed up successfully!!!Login with your Username and password**** ' )
       # con . close ()
        self.login()

class Admin:
        def __init__(self):
            self.admin_username=''

        def admin_area(self):
            entry= input('Please choose from the option \n 1.Login \n 2.Previous Menu \n 3.Exit \n')
            if entry == '1':
                self.admin_username=input('Please enter your Username: \n')
                with con:
                    db_adminlist = cur.execute("SELECT Username FROM Admins7_Info")
                    user_found=False
                    for db_admin in db_adminlist:
                        if  db_admin[0] == self.admin_username:
                            user_found=True
                            counter=0
                            while True:
                                if counter==3:
                                    print('Done with your password attempt')
                                    break
                                password=input('Please enter the password: ')
                                db_password=cur.execute(f"SELECT Password FROM Admins7_Info WHERE Username = '{self.admin_username}'")
                                for db_pw in db_password:
                                    if db_pw[0] == password:
                                        print('welcome!!!')
                                        return self.admin_main_menu()
                                    else:
                                        print('Wrong Password!!Please try again')
                                        counter+=1
            if user_found==False:
                print('Username is unavailable')

                #self.admin_main_menu()

            elif entry== '2':
                return self.user_type()
            else:
                systemExist

        def admin_main_menu(self):
            print(f'*****Welcome  { self.admin_username} *****')
            process = input('Please choose the number \n 1.Customer Details \n 2.Delete The Customer Details \n 3.Add The New Customer Details \n')
            
            if process =='1':
                #my_conn = my_connect.cursor()
                users=cur.execute("SELECT Username, Address, Phone_num FROM USER ")
                #columns = cur.fetchall()
                #print(users)

                i=0
                for user in users:
                    for j in range(len(user)):
                        print(user[j],end=' ')
                    i=i+1
                    print()
            
            elif process == '3' :
                Username = input('enter your Username: ')
                Balance = int(input('enter your balance: '))
                Address=input('Enter your address: ')
                Phone_num=int(input('Enter your Phone Number: '))
                Password=input('Enter your Password: ')
                cur.execute("""
                INSERT INTO USER(Username, Balance, Address, Phone_num, Password )
                VALUES (?,?,?,?,?)
                """, (Username, Balance, Address, Phone_num, Password ))
                con.commit ()
                print ( '****Data Signed up successfully!!!**** ' )                
  
d = Logging()
d.welcome_page()

''' elif process == '2':
                username_delete=(input('Enter the username to delete: '))
                columns = cur.fetchall()
                delete_box=cur.execute(f"DELETE from USER WHERE Username = {username_delete}" )
                delete_box.delete(0, END)
'''