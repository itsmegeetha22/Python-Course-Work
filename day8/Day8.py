'''
data={
    'geetha@gmail.com':'g@123',
    'hema@gmail.com':'h@123',
    'nithya@gmail':'n@123'
    }
email=input("enter the emai;l:")
password=input("enter the password:")
if data.get(email)==password:
    print("login successful")
else:
    print("login invalid")



hr,min=list(map(int,input("enter the time(HH:MM):").split(':')))
fare=0
price=350
if 0<=hr<=23 and 0<=min<=59:
                          if 8<=hr<16:
                             fare = 40
                          elif 17<=hr<23:
                             fare = 150
                          elif 0<=hr<7:
                             fare = 100
                          print("total fare:",fare+price)
else:
    print("invalid time")
    

data={
    'geetha@gmail.com':'g@123',
    'hema@gmail.com':'h@123',
    'nithya@gmail':'n@123'
    }
email=input("enter the emai;l:")
password=input("enter the password:")
if data.get(email)==password:
    print("login successful")
else:
    print("login invalid")
    

import random
otp=random.randint(1000,9999)
print("OTP:", otp)
entered_otp=int(input("enter the otp:"))
if otp==entered_otp:
    print("verified succesfully")
else:
    print("verification failed")
    



data={
    'geetha':{'status':True,'python':80,'sql':89,'flask':90},
    'hema':{'status':True,'python':65,'sql':79,'flask':50},
    'nithya':{'status':False,'python':78,'sql':87,'flask':70},
    'lakshmi':{'status':True,'python':85,'sql':45,'flask':76},
    'vijaya':{'status':True,'python':83,'sql':79,'flask':92}
    }
name=input("enter the student name:")
if name in data:
    print(name,"'s Report:")
    if data[name]['status']:
        avg=(data[name]['python']+data[name]['sql']+data[name]['flask'])/3
        if avg>90:
            print('congrats,well done')
        elif avg>60:
            print('Good, Improvement needed')
        elif avg>35:
            print('Just Passed, Better luck next time')
        else:
            print("Failed in the exam. Please bring your parents")
    else:
        print("Didn't attempt the exam.")
else:
    print(name,"'s data is not found")
    '''

    
                          
    
    


