'''->1.keyword arguments:
def display(name,email,phonenumber):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'phone number: {phonenumber}')
display(name='geetha',email='geetha@gmail.com',phonenumber='9390876253')
display(email='geetha@gmail.com',name='geetha',phonenumber='924698310')
display(phonenumber='089347812',name='geetha',email='geetha@gmail.com')
'''

'''->2.default arguments(must be write at end of the parameters and also at right side)
def display(name,email,phonenumber,cgpa=None):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'phone number: {phonenumber}')
    print(f'CGPA:{cgpa}')
display(name='geetha',email='geetha@gmail.com',phonenumber='9390876253')
display(email='geetha@gmail.com',name='geetha',phonenumber='924698310')
display(phonenumber='089347812',name='geetha',email='geetha@gmail.com')
'''

'''->3.varaible length(tuple):

def display(*names):
    print(names)
display('geetha')
display('hema','gowwri','nithya')
display('lakshmi','vijaya')
'''


'''->4.variable length(dict):
def display(**names):
    print(names)
display(n1='geetha')
display(n2='hema',n3='gowwri',n4='nithya')
display(n5='lakshmi',n6='vijaya')
'''


'''

n=int(input("enter the  number:"))
c=0
for i in range(2,n):
    if n%i==0:
       c+=1
print("prime number" if c==2 else "not prime number")
'''

'''
n=int(input("enter the  number:"))
c=0
for i in range(2,n//2+1):
    if n%i==0:
       c+=1
print("prime number" if c==0 else "not prime number")


n=int(input("enter the  number:"))
c=0
for i in range(1,n+1):
    if n%i==0:
       c+=1
print("prime number" if c==2 else "not prime number")

'''

'''
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input("enter the  number:"))
print("prime number" if isprime(n) else "not prime number")

'''

def check(s):
    vc=cc=dc=sc=0
    wc=1
    vol='aeiouAEIOU'
    for i in s:
        if i.isalpha():
            if i in vol():
                vc+=1
            else:
                cc+=1
        elif i.isdigit():
             dc+=1
        elif i.isspace():
            wc+=1
        else:
            sc+=1
            
    print(f"vol count: {vc}")
    print(f"con count: {cc}")
    print(f"dig count: {dc}")
    print(f"word count: {wc}")
    print(f"scount: {sc}")
    
check("python programming language:3.14")
                





