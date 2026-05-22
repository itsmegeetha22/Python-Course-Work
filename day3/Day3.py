Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a,b,c=[10,20,30]
a
10
b
20
c
30
a,b,c=list(map(int,input("enter the a b c values:").split()))
enter the a b c values:12 23 45 
a
12
b
23
c
45
email,password=input("enter the email and password:").split()
enter the email and password:22geetha2003@gmail.com
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    email,password=input("enter the email and password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password=input("enter the email and password:").split()
enter the email and password:22geetha2003@gmail 12345
email
'22geetha2003@gmail'
password
'12345'
a,b=list(map(float,input("enter the a,b:").split()))
enter the a,b:23 45 
a
23.0
b
45.0
a=8
b=9
a+b
17
a-b
-1
a*b
72
a/b
0.8888888888888888
a//b
0
a
8
a%b
8
a=8
b=9
a%b
8
a=5
b=10
a%b
5
2**3
8
3**3
27
a
5
b=5
a=10
a==b
False
a!=b
True
a>b
True
a<b
False
a<=b
False
a>=b
True
a=40
a=a+10
a
50
a=a+20
a
70
a+=20
a
90
a-=10
a
80
a*=10
a
800
a/=10
a
80.0
a//=10
a
8.0
a**
SyntaxError: invalid syntax
a**3
512.0
a
8.0
a%=4
a
0.0
a/=2
a
0.0
a=4
a%2==0 and a%3==0 and a%6==0
False
a=12
a%2==0 and a%3==0 and a%6==0
False
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
KeyboardInterrupt
a%2==0 and a%3==0 and a%6==0
True
a=32
a%2==0 or a%3==0 or a%6==0
True
a%2==0
True
not a%2==0
False
#str,list,tuple,dict,set
'p' in'python'
True
'z' in 'python'
False
'i' not in 'python'
True
l=[1,2,3,4]
5 in l
False
3 in l
True
7 not in l
True
t=(80,70,60)
60 in t
True
100 not in t
True
s={2,3,4]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
s={2,4,3,7}
5 in s
False
7 in s
True
9 not in s
True
d={1:2,3:4,4:5,5:6}
6 in d
False
d.keys
<built-in method keys of dict object at 0x000001BF1B899380>
d.keys()
dict_keys([1, 3, 4, 5])
#identical operator
a=[1,2,3,4]
b=[1,2,3,4]
a==b
True
a is b
False
c=a
>>> c
[1, 2, 3, 4]
>>> a==c
True
>>> a is c
True
>>> id(a)
1920312264192
>>> id(b)
1920311045888
>>> id(c)
1920312264192
>>> a is not c
False
>>> a is not b
True
>>> 7&13
5
>>> 7|13
15
>>> 7^13
10
>>> 8<,1
SyntaxError: invalid syntax
>>> 8<<1
16
>>> 16<<1
32
>>> 8>>1
4
>>> 9<<2
36
>>> 9>>2
2
>>> 8<,4
SyntaxError: invalid syntax
>>> 8<<4
128
>>> ~6
-7
>>> ~4
-5
>>> ~7
-8
>>> ~90
-91
