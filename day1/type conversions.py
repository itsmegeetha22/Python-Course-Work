Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
float(a)
10.0
set(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
b=1.23
int(b)
1
str(a)
'10'
complex(b)
(1.23+0j)
list(b)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
str(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    str(c)
NameError: name 'c' is not defined
list(c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(c)
NameError: name 'c' is not defined
bool(c)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    bool(c)
NameError: name 'c' is not defined
c=19
ste(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ste(c)
NameError: name 'ste' is not defined. Did you mean: 'str'?
set(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    set(c)
TypeError: 'int' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dict(c)
TypeError: 'int' object is not iterable
bool(c)
True
c=19
int(c)
19
float(c)
19.0
str(c)
'19'
s='pyhton'
s = 'python'
complex(s)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['p', 'y', 't', 'h', 'o', 'n']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
dict(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
set(s)
{'t', 'o', 'n', 'y', 'p', 'h'}
bool(s)
True
s='10'
int(s)
10
float(s)
10.0
complex(s)
(10+0j)
l=[1,2,3,4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
'[1, 2, 3, 4, 5]'
bool(l)
True
complex(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
t=(1,2,3,4,5)
\
int(t)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(t)
'(1, 2, 3, 4, 5)'
complex(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
set(t)
{1, 2, 3, 4, 5}
dict(t)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
list(t)
[1, 2, 3, 4, 5]
bool(t)
True
s={1,2,3,4,5}
int(s)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not set
str(s)
'{1, 2, 3, 4, 5}'
list(s)
[1, 2, 3, 4, 5]
dict(s)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
tuple(s)
(1, 2, 3, 4, 5)
bool(s)
True
d=[1,2,3,4,5]
int(d)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(d)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'list'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not list
>>> str(d)
'[1, 2, 3, 4, 5]'
>>> set(D)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    set(D)
NameError: name 'D' is not defined. Did you mean: 'd'?
>>> set(d)
{1, 2, 3, 4, 5}
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    dict(d)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> tuple(d)
(1, 2, 3, 4, 5)
>>> list(d)
[1, 2, 3, 4, 5]
>>> bool(D)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    bool(D)
NameError: name 'D' is not defined. Did you mean: 'd'?
>>> bool(d)
True
>>> complex(D)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    complex(D)
NameError: name 'D' is not defined. Did you mean: 'd'?
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not list
>>> a=10
>>> b=12.4
>>> c='python'
>>> print(a,b,c)
10 12.4 python
print('a=',a,'b=',b,'c=',c)
a= 10 b= 12.4 c= python
print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
12.4
c=
python
print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	12.4	c=	python
print('a=',a,'b=',b,'c=',c,sep='\n',end='\n\n')
a=
10
b=
12.4
c=
python

print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n')
a=	10	b=	12.4	c=	python

print('a=',a,'b=',b,'c=',c,sep='\t',end='@@@')
a=	10	b=	12.4	c=	python@@@
print(f'a: {a},b: {b},c: {c}')
a: 10,b: 12.4,c: python
print(f'a: {a}b: {b}c: {c}')
a: 10b: 12.4c: python
print('a= %d b= %f c= %s'(a,b,c))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print('a= %d b= %f c= %s'(a,b,c))
TypeError: 'str' object is not callable
print('a= %d b= %f c= %s'%(a,b,c))
a= 10 b= 12.400000 c= python
print('a= %d b= %.2f c= %s'(a,b,c))
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print('a= %d b= %.2f c= %s'(a,b,c))
TypeError: 'str' object is not callable
print('a= %d b= %.2f c= %s'%(a,b,c))
a= 10 b= 12.40 c= python
print('a= {} b= {} c= {}'.format(a,b,c))
a= 10 b= 12.4 c= python
print('a= {2} b= {0} c= {1}'.format(a,b,c))
a= python b= 10 c= 12.4
name = input()
geetha
name
'geetha'
name = input("enter the name: ")
enter the name: geetha
name
'geetha'
type(name)
<class 'str'>
age = input("enter the age")
enter the age:20
age
':20'
type(age)
<class 'str'>
age = int(input("enter the age"))
enter the age20
age
20
type(ag)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    type(ag)
NameError: name 'ag' is not defined. Did you mean: 'a'?
type(age)
<class 'int'>
gpa=float(input("enter the gpa:"))
enter the gpa:5.6
gpa
5.6
type(gpa)
<class 'float'>
'geetha mouni lakshmi nithya'.split()
['geetha', 'mouni', 'lakshmi', 'nithya']
names = input("enter the names:").split()
enter the names:geetha mouni lakshmi nithya
names
['geetha', 'mouni', 'lakshmi', 'nithya']
age = input("enter the age:").split()
enter the age:2122 23 24
age
['2122', '23', '24']
map(int,input("enter the ages: ").split())
enter the ages: 21 22 23  24
<map object at 0x000001F8B8525640>
age
['2122', '23', '24']
age=list(map(int,input("enter the age: ").split()))
enter the age: 2121 23 24
age
[2121, 23, 24]
age=list(map(float,input("enter the age: ").split()))
enter the age: 2122 23 24
age
[2122.0, 23.0, 24.0]
names=tuple(input("enter the names: ").split()))
SyntaxError: unmatched ')'
names=tuple(input("enter the names: ").split())
enter the names: geetha mouni
names
('geetha', 'mouni')
age=tuple(map(int,input("enter the ages: ").split())
