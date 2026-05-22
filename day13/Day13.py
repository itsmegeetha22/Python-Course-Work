'''
#int,float,str,bool,tuple(immutable)(pass by values)
#set,dict,list(passing the mutable items)(pass by references)
def display(n):
   n=n+[5,6]
   print("inside n:",n)
n=[1,2,3,4]
display(n)
print("outside n:",n)



def display():
    global num
    num+=10
    print("inside num:",num)
num=10
display()
print("outside num:",num)




def display(num):
    num+=10
    print("inside num:",num)
num=10
display(num)
print("outside num:",num)


def display(num):
    num+=10
    print("inside num:",num)
num=10.7
display(num)
print("outside num:",num)

def display(num):
    num=num+[5,6]
    print("inside num:",num)
num=[1,2,3,4]
display(num)
print("outside num:",num)




def courses():
    course="java"
    print("in the start:",course)
    def change():
        nonlocal course
        course="python"
        print("changed:",course)
    change()
    print("final:",course)
    
courses()


def courses():
    course="java"
    print("in the start:",course)
    def change():
        course="python"
        print("changed:",course)
    change()
    print("final:",course)
    
courses()

#example
s="python"
print(len(s))


s="python"
len=5
print(len(s))#we can't use itis as a variable bcz it looses its property

#recursion
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)



def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)


s="python"
def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
display(s,0)



s="python"
def display(s,ind):
    if ind==len(s):
        return
    display(s,ind+1)
    print(s[ind])
display(s,0)


s="python"
def display(s,ind):
    if ind==len(s)+1:
        return
    display(s,ind+1)
    print(s[:ind])
display(s,1)

s="python"
def display(s,ind):
    if ind==len(s)+1:
        return
    print(s[:ind])
    display(s,ind+1)
    
display(s,1)


def display(s,ind,w):
    if ind==len(s)-w+1:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)
s="python programming"
display(s,0,10)
'''


def display(n):
    if n==11:
        sum+=n+1
        print(sum)
        return
    

    
        

