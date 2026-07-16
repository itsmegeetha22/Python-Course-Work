#POLYTMORISM(SAME NAME,DIFFERENT ACTIONS)
#TYPES:METHOD OVERRIDING(SAME METHODS ,SAME PARAMETERS,DIFFERENT ACTIONS BY CHILD CLASS)
      #METHOD OVERLOADING(SAME METHODS,SAME CLASS,PYHTON DOESNOT HAVE ANY OVERLOADING METHOD)
'''
class Hotstar:
    def __init__(self,name):
         self.name=name
         print(f'hello {self.name},welcome to the hotstar--------')
    def login(Self):
        print("you can login ")
    def search(self):
        print("you can search")
    def categories(self):
        print("you can see the divisions")
    def playcontrollers(Self):
        print("you can pause,resume and play")
    def livesports(self):
        print("you can watch the sports")
    def ads(self):
        print("ads will run")
    def movies(self):
        print("limited movies")
    def downloads(self):
        print("cant downlaod")
    def quality(self):
        print("calrity will be limited")
class PremiumUser(Hotstar):
    def __init__(self,name):
        self.name=name
        print(f'hello {self.name},welocme to the hotstar premium---------')
    def login(self):
        print('You can login')
    def search(self):
        print("You can search")
    def categories(self):
        print("You can see the divisions")
    def playcontrollers(self):
        print("You can pause,resume and play")
    def livesports(self):
        print("You can watch live sports")
    def ads(self):
        print("ads will not run")
    def movies(self):
        print("unlimited movies")
    def downloads(self):
        print("can downlaod")
    def quality(self):
        print("calrity will be high")

geetha=Hotstar("geetha")
geetha.login()
geetha.search()
geetha.categories()
geetha.playcontrollers()
geetha.livesports()
geetha.ads()
geetha.movies()
geetha.downloads()
geetha.quality()
print()
hema=PremiumUser("hema")
hema.login()
hema.search()
hema.categories()
hema.playcontrollers()
hema.livesports()
hema.ads()
hema.movies()
hema.downloads()
hema.quality()



#operator method

class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num+other.num
    def __sub__(self,other):
        return self.num-other.num
    def __mul__(self,other):
        return self.num*other.num
    def __eq__(self,other):
        return self.num==other.num
    def __lt__(self,other):
        return self.num<other.num
    def __gt__(self,other):
        return self.num>other.num
a=Number(10)
b=Number(20)
print(a+b)
print(a-b)
print(a*b)
print(a==b)
print(a>b)
print(a<b)




#ABSTRACTION(HIDING COMPLEXITY)
from abc import ABC,abstractmethod
class Phonepay:
    def input(self):
        print("you can scan or enter the number")
    def amount(self):
        print("you enter the amount to pay")
    def pin(self):
        print("you enter the pin")
    @abstractmethod
    def verification(self):
        pass
    def paymentstatus(self):
        print("you enter the amount to transferred successfully/failed")
class HDFC(Phonepay):
    def verification(self):
        print("verification is completed through hdfc")
class SBI(Phonepay):
    def verification(self):
        print("verification is completed through sbi")
class UNION(Phonepay):
    def verification(self):
        print("veirficaation is completed through union")
class AXIS(Phonepay):
    def verification(self):
        print("verification is completed through axis")
geetha=HDFC()
geetha.input()
geetha.amount()
geetha.pin()
geetha.verification()
geetha.paymentstatus()
print()
hema=SBI()
hema.input()
hema.amount()
hema.pin()
hema.verification()
hema.paymentstatus()
print()
nithya=UNION()
nithya.input()
nithya.amount()
nithya.pin()
nithya.verification()
nithya.paymentstatus()
print()
lakshmi=AXIS()
lakshmi.input()
lakshmi.amount()
lakshmi.pin()
lakshmi.verification()
lakshmi.paymentstatus()
print()
 
'''






































        



