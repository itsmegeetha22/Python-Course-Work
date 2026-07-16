'''
class Instagram:
    def __init__(self,username,password,cf):
        self.username=username
        self.__password=password
        self._cf=cf

    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.__password=new_password
    @property
    def accesscf(self):
        return self._cf
    @accesscf.setter
    def accesscf(self,new_friend):
        self_cf.append(new_friend)
        




geetha=Instagram('geetha','geetha@123',['hema','nithya','lakshmi'])
print(" before Username:",geetha.username)
geetha.username="hema"
print("after Username:",geetha.username)
print(" before password:",geetha.getpassword())
geetha.setpassword('geetha22')
print("after password:",geetha.getpassword())
print("before close friend:",geetha.accesscf)
geetha.accescf='shiva'
print("after close friend:",geetha.accesscf)


class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_info(self):
        print(f"Tilte:{self.title},Author:{self.author},Price:${self.price}")
book1=Book( "Clean Code","RObert Martin",450)
book1.display_info()




class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def calculate_annual_salary(self):
        return self.base_salary*12
emp=Employee("John",35000)
print("annual salary:",emp.calculate_annual_salary())







class BankAccount:
    def __init__(self,owner):
        self.owner=owner
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
             self.balance-=amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print(f"Balance:{self.balance}")
acc=BankAccount("geetha")
acc.deposit(1000)
acc.withdraw(500)
acc.show_balance()



class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
        self.odometer=0
    def drive(self,km):
        self.odometer+=km
    def show_odometer(self):
        print(f"odometer:{self.odometer}km")
car1=Car("Toyoto","innova")
car1.drive(120)
car1.drive(30)
car1.show_odometer()
'''






