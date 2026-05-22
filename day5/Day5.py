Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
names='geetha sree swapna hema'
names.split()
['geetha', 'sree', 'swapna', 'hema']
names.split('a')
['geeth', ' sree sw', 'pn', ' hem', '']
names.split(' ',2)
['geetha', 'sree', 'swapna hema']
names.rsplit(' ',2)
['geetha sree', 'swapna', 'hema']
names.partition('')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    names.partition('')
ValueError: empty separator
names.partition(' ')
('geetha', ' ', 'sree swapna hema')
'1.python.png'.partition('.')
('1', '.', 'python.png')
'1.python.png'.rpartition('.')
('1.python', '.', 'png')
names.split()
['geetha', 'sree', 'swapna', 'hema']
l=['geetha', 'sree', 'swapna', 'hema']
''.join(1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
''.join(1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
''.join(l)
'geethasreeswapnahema'
'-'joint(l)
SyntaxError: invalid syntax
'-'.join(l)
'geetha-sree-swapna-hema'
','.join(l)
'geetha,sree,swapna,hema'
h='    yyyYY  YYYyyy  '

h.strip()
'yyyYY  YYYyyy'
h.lstrip()
'yyyYY  YYYyyy  '
h.rstrip()
'    yyyYY  YYYyyy'
\
'heeelo'.encode()
b'heeelo'
b'heeelo'.decode()
'heeelo'
text="Hello @"
text.encode()
b'Hello @'
b'Hello @'.decode
<built-in method decode of bytes object at 0x000002859E662BB0>
b'Hello @'.decode()
'Hello @'
'python'.startswith('p')
True
'python.py'.endswith('.py')
True
'sdfg'.isalpha()
True
'1234fght'.isalnum()
True
'1234'.isalnum()
True
'hgty'.isalnum()
True
'9876  hty'.isalnum()
False
'ryui'.islower()
True
'Rtyui'.islower()
False
'RTYH'.isupper()
True
'tYUUI'.isupper()
False
'     '.isspace()
True
'  k  '.isspace()
False
'tyui iopk yuio'.istitle()
False
'Ftyu Htyu Koiu'.istitle()
True
'myvar'.isidentifier()
True
'my@@var'.isidentifier()
False
'3678'.isdecimal()
True
'34569'.isdigit()
True
'4563'.isnumeric()
True

l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
l=['fdgh',1,12.3,[8,9],[6.7],[8.9],true,{1:1},{1,2,3},none]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    l=['fdgh',1,12.3,[8,9],[6.7],[8.9],true,{1:1},{1,2,3},none]
NameError: name 'true' is not defined. Did you mean: 'True'?
l=['fdgh',1,12.3,[8,9],[6.7],[8.9],True,{1:1},{1,2,3},none]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    l=['fdgh',1,12.3,[8,9],[6.7],[8.9],True,{1:1},{1,2,3},none]
NameError: name 'none' is not defined. Did you mean: 'None'?
l=['fdgh',1,12.3,[8,9],[6.7],[8.9],True,{1:1},{1,2,3},None]
L
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    L
NameError: name 'L' is not defined. Did you mean: 'l'?
l
['fdgh', 1, 12.3, [8, 9], [6.7], [8.9], True, {1: 1}, {1, 2, 3}, None]
l=[1,1,1,1,1]
l
[1, 1, 1, 1, 1]
a=[l]
a=[1,2,3,4]
b=[5,6,7,8]
a+b
[1, 2, 3, 4, 5, 6, 7, 8]
a*10
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l=['geetha','sree','swapna','hema']
l
['geetha', 'sree', 'swapna', 'hema']
l[0]
'geetha'
l[1]
'sree'
l[2]
'swapna'
l[3]
'hema'
l[4]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    l[4]
IndexError: list index out of range
l[:;3]
SyntaxError: invalid syntax
l[::3]
['geetha', 'hema']
l[3:]
['hema']
l[:3]
['geetha', 'sree', 'swapna']
l[:;-1]
SyntaxError: invalid syntax
l[::-1]
['hema', 'swapna', 'sree', 'geetha']
l[-4:-2]
['geetha', 'sree']
l[:;2]
SyntaxError: invalid syntax
l[::2]
['geetha', 'swapna']
l[1::2]
['sree', 'hema']
'geetha'in l
True
'sree' not in l
False
l=[]
l=list()
l=['geetha','sree','swapna','hema']
l
['geetha', 'sree', 'swapna', 'hema']
l[0]
'geetha'
l[0]='niharika'
l
['niharika', 'sree', 'swapna', 'hema']
id[l]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    id[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
id[l]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    id[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
l
['niharika', 'sree', 'swapna', 'hema']
id[l]
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    id[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
l.append['sravani')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
l.append['sravani']
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    l.append['sravani']
TypeError: 'builtin_function_or_method' object is not subscriptable
l.append('sravani')
l
['niharika', 'sree', 'swapna', 'hema', 'sravani']
l.insert(1,'nithya')
l
['niharika', 'nithya', 'sree', 'swapna', 'hema', 'sravani']
l.extend('lakshmi','gowri','vijaya')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    l.extend('lakshmi','gowri','vijaya')
TypeError: list.extend() takes exactly one argument (3 given)
l.extend['lakshmi','gowri','vijaya']
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    l.extend['lakshmi','gowri','vijaya']
TypeError: 'builtin_function_or_method' object is not subscriptable
l.extend(['lakshmi','gowri','vijaya'])
l
['niharika', 'nithya', 'sree', 'swapna', 'hema', 'sravani', 'lakshmi', 'gowri', 'vijaya']
>>> l.remove('sree')
>>> l
['niharika', 'nithya', 'swapna', 'hema', 'sravani', 'lakshmi', 'gowri', 'vijaya']
>>> l.remove('hema')
>>> l
['niharika', 'nithya', 'swapna', 'sravani', 'lakshmi', 'gowri', 'vijaya']
>>> l.pop(0)
'niharika'
>>> del[0]
SyntaxError: cannot delete literal
>>> sorted(l)
['gowri', 'lakshmi', 'nithya', 'sravani', 'swapna', 'vijaya']
>>> max(l)
'vijaya'
>>> min(l)
'gowri'
>>> len(l)
6
>>> l.index('swapna')
1
>>> l.index('geetha')
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    l.index('geetha')
ValueError: list.index(x): x not in list
>>> l.count('swapna')
1
>>> l.sort()
>>> l
['gowri', 'lakshmi', 'nithya', 'sravani', 'swapna', 'vijaya']
>>> l.reverse()
>>> l
['vijaya', 'swapna', 'sravani', 'nithya', 'lakshmi', 'gowri']
>>> l=[2,3,4]
>>> l
[2, 3, 4]
>>> m=l
>>> m
[2, 3, 4]
>>> n=l.copy()
>>> n.append(10)
>>> n
[2, 3, 4, 10]
>>> l
[2, 3, 4]
