'''
class Flipkart:
    products={'laptop':73819,
              'phone':198233,
              'earphones':435,
              'bags':311}
    @classmethod
    def showProducts(cls):
        print(cls.products)
geetha=Flipkart()
geetha.



class Flipkart:
    products={'laptop':73819,
              'phone':198233,
              'earphones':435,
              'bags':311}
    @classmethod
    def showProducts(cls):
        print(cls.products)
   
    def register(self,name,phno):
        self.username = name
        self.phonenumber = phno
        print(f'Welcome to flipkart {self.username},shop now!!!')
    @staticmethod
    def discount():
        print("Hey all,10% discount is going on,shop now!!!!")
              
        
geetha=Flipkart()
geetha.register('geetha','989473871')
geetha.discount()
geetha.showProducts()




class Flipkart:
    def __intit__(self,name,phno):
        self.username = name
        self.phonenumber = phno
        print(f'welcome to flipkart {self.username},shop now!!!1')
geetha = Flipkart('geetha','13456256')



class Instagram:
    def __intit__(self,username):
        self.username = name
        self.bio=''
        self.fullname=''
        self.followers=set()
        self.following=set()
        print(f"welcome to the instagram {self.username}")
        print(f'Followers:{len(self.followers)}Following:{len(self.following)}')
        
       
        
geetha = Instagram('geetha')

'''

