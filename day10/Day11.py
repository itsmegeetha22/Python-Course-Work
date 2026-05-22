Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
n=int(input("enter the size:"))
enter the size:4
for row in range(n):
    for col in range(n):
        print('*',end=' ')
    print()

    
* * * * 
* * * * 
* * * * 
* * * * 






n=int(input("enter the size:"))
enter the size:5
for i in range(n):
    for j in range(n):
        print('*',end=' ')

        
* * * * * * * * * * * * * * * * * * * * * * * * * 



n=int(input("enter the size:"))
enter the size:5
for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
        
SyntaxError: multiple statements found while compiling a single statement
n=int(input("enter the size:"))
enter the size:5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

    
* 
* * 
* * * 
* * * * 
* * * * * 

n=int(input("enter the size:"))
enter the size:10
for i in range(5):
    for j in range(n-i):
        print('*',end=' ')
    print()

    
* * * * * * * * * * 
* * * * * * * * * 
* * * * * * * * 
* * * * * * * 
* * * * * * 



n=int(input("enter the size:"))
enter the size:10
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()
    
SyntaxError: multiple statements found while compiling a single statement
n=int(input("enter the size:"))
enter the size:10
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()
    
SyntaxError: multiple statements found while compiling a single statement
n=int(input("enter the size:"))
enter the size:5
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()

    
* * * * * 
* * * * 
* * * 
* * 
* 







n=int(input("enter the size:"))
enter the size:6
for i in range(n):
    for j in range(i-n):
        print('*',end=' ')
    print()

    











n=int(input("enter tne size:"))
enter tne size:6
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
        for j in range(i+1)
            print('*',end=' ')
            
SyntaxError: expected ':'
n=int(input("enter the size:"))
enter the size:6
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
     print()
     
SyntaxError: unindent does not match any outer indentation level
n=int(input("enter the size:"))
enter the size:6
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')print()
        
SyntaxError: invalid syntax
n=int(input("enter the sizez:"))
enter the sizez:6
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')print()
        
SyntaxError: invalid syntax
n=int(input("enter the sizez:"))
enter the sizez:6
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

    
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * * 








n=int(input("enter the size:"))
enter the size:4
for i in range(n):
    for sp in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()

    
* * * * 
  * * * 
    * * 
      * 






n=int(input("enter the size:"))
enter the size:7
for i in range(n):
    for j in range(n):
        print(int(j%2==0),end=' ')
    print()

    
1 0 1 0 1 0 1 
1 0 1 0 1 0 1 
1 0 1 0 1 0 1 
1 0 1 0 1 0 1 
1 0 1 0 1 0 1 
1 0 1 0 1 0 1 
1 0 1 0 1 0 1 







n=int(input("enter the size:"))
enter the size:6
for i in range(n):
    for j in range(n):
        print(int(j%2!=0),end=' ')
    print()

    
0 1 0 1 0 1 
0 1 0 1 0 1 
0 1 0 1 0 1 
0 1 0 1 0 1 
0 1 0 1 0 1 
0 1 0 1 0 1 

... 
... 
... 
... 
... 
>>> KeyboardInterrupt
>>> n=int(input("enter the size:"))
enter the size:5
>>> for i in range(n):
...     for j in range(n):
...         print(int( not j%2==0),end=' ')
...     print()
... 
...     
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
>>> n=int(input("enter the size:"))
enter the size:5
>>> for i in range(n):
...     for j in range(n):
...         print(int(i+j)%2==0),end=' ')
...         
SyntaxError: unmatched ')'
>>> n=int(input("enter the size:"))
enter the size:6
>>> for i in range(n):
...     for j in range(n):
...         print(int(i+j)%2==0),end=' ')
...         
SyntaxError: unmatched ')'
>>> n=int(input("enter the size:"))
enter the size:6
>>> for i in range(n):
...     for j in range(n):
...         print((int(i+j)%2==0),end=' ')
...     print()
... 
...     
True False
 True False True False
 
False True 
False True False True 

True False True False 
True False 
False
 True False True False True
 
True False 
True False True False 
False True False True False True 
