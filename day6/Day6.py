Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4]
sum(l)
10
#0 0.0 '' [] () {} False
any([1,0.0,'',[],(),set(),{},False])
True
all([1,0.0,'',[],(),set(),{},False])
False
all([1,0.0,'geetha',[],(),set(),{},False])
False
all([1,1.1,3,'geetha',[1,2,3]])
True
T=()
t=()
t=tuple()
t=(1,2,3,4,5,6)
t
(1, 2, 3, 4, 5, 6)
t.add(1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.add(1)
AttributeError: 'tuple' object has no attribute 'add'
t.append(1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t.append(1)
AttributeError: 'tuple' object has no attribute 'append'
t=(1,1,1,1)
t
(1, 1, 1, 1)
t=(1,1.1,'python',[1,2,3,4],(1,2,3,4),{1,2,3,4},(1:1,2:2)
   
SyntaxError: invalid syntax
t=(1,1.1,'python',[1,2,3,4],(1,2,3,4),{1,2,3,4},{1:1,2:2})
   
t
   
(1, 1.1, 'python', [1, 2, 3, 4], (1, 2, 3, 4), {1, 2, 3, 4}, {1: 1, 2: 2})
t[3]
   
[1, 2, 3, 4]
t[3].append(15)
   
t
   
(1, 1.1, 'python', [1, 2, 3, 4, 15], (1, 2, 3, 4), {1, 2, 3, 4}, {1: 1, 2: 2})
a=(1,2,3,4)
   
x,y,z=a
   
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    x,y,z=a
ValueError: too many values to unpack (expected 3, got 4)
a=(1,2,3)
   
x,y,z=a
   
x
   
1
y
   
2
z
   
3
t=(1,2,3,4)
   
id(t)
   
2543697666800
t=t+(5,6)
   
t
   
(1, 2, 3, 4, 5, 6)
id(t)
   
2543697217856
t=('geetha', 'hema', 'sree', 'swapna')
   
t
   
('geetha', 'hema', 'sree', 'swapna')
t+10
   
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t+10
TypeError: can only concatenate tuple (not "int") to tuple
t+('geetha','hema')
   
('geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema')
t*10
   
('geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema', 'sree', 'swapna', 'geetha', 'hema', 'sree', 'swapna')
t(3)
   
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t(3)
TypeError: 'tuple' object is not callable
t[3]
   
'swapna'
t[5]
   
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t[5]
IndexError: tuple index out of range
t[4]
   
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t[4]
IndexError: tuple index out of range
t
   
('geetha', 'hema', 'sree', 'swapna')
t[0]
   
'geetha'
t[1]
   
'hema'
t[3]
   
'swapna'
t[4]
   
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    t[4]
IndexError: tuple index out of range
t[-1]
   
'swapna'
t[-2]
   
'sree'
t[:3]
   
('geetha', 'hema', 'sree')
t[2:]
   
('sree', 'swapna')
t[::2]
   
('geetha', 'sree')
t[-1:3:-1]
   
()
t[1:2:-1]
   
()
'geetha' in 't'
   
False
'geetha' not in 't'
   
True
t
   
('geetha', 'hema', 'sree', 'swapna')
'hema' in 't'
   
False
t[::2]
   
('geetha', 'sree')
t[1::2]
   
('hema', 'swapna')
t[::-1]
   
('swapna', 'sree', 'hema', 'geetha')
t[-2::]
   
('sree', 'swapna')
'geetha' in t
   
True
'hema' in t
   
True
'sree' not in t
   
False
t[-1:-3:-1]
   
('swapna', 'sree')
t
   
('geetha', 'hema', 'sree', 'swapna')
t[-1:-3:-1]
   
('swapna', 'sree')
t=(1,1,1,1,1,2,2,2,3,4,5)
   
t.count(1)
   
5
t.count(2)
   
3
t.count(3)
   
1
t.count(4)
   
1
t.count(10)
   
0
max(t)
   
5
min(t)
   
1
sorted(t)
   
[1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 5]
sum(t)
   
23
t.index(2)
   
5
len(t)
   
11
DATA=
   
SyntaxError: invalid syntax
data={}
   
type(data)
   
<class 'dict'>
data
   
{}
data={'userid':102,'username':'geetha','skills':['python','java','sql'],'gpa':8.9}
   
d={}
   
d[1]='int'
   
d[1.1]='float'
   
d
   
{1: 'int', 1.1: 'float'}
d['string']='str'
   
d[(2+3j)]='complex'
   
d[[1,2,3,4]]='list'4
   
SyntaxError: invalid syntax
d[[1,2,3,4]]='list'
   
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    d[[1,2,3,4]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[(1,2,3,4)]='tuple'
   
d[{1,2,3,4}]='list'
   
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    d[{1,2,3,4}]='list'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{1,2,3,4}]='set'
   
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    d[{1,2,3,4}]='set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{1:1,2:2}]='dict'
   
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    d[{1:1,2:2}]='dict'
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
d
   
{1: 'int', 1.1: 'float', 'string': 'str', (2+3j): 'complex', (1, 2, 3, 4): 'tuple'}
d[Flase]='bool'
   
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    d[Flase]='bool'
NameError: name 'Flase' is not defined. Did you mean: 'False'?
d[False]='bool'
   
d
   
{1: 'int', 1.1: 'float', 'string': 'str', (2+3j): 'complex', (1, 2, 3, 4): 'tuple', False: 'bool'}
data
   
{'userid': 102, 'username': 'geetha', 'skills': ['python', 'java', 'sql'], 'gpa': 8.9}
data['userid']=102
   
data
   
{'userid': 102, 'username': 'geetha', 'skills': ['python', 'java', 'sql'], 'gpa': 8.9}
data['userid']=103
   
data
   
{'userid': 103, 'username': 'geetha', 'skills': ['python', 'java', 'sql'], 'gpa': 8.9}
data['userid']
   
103
data['username']
   
'geetha'
data['skills']
   
['python', 'java', 'sql']
data['gpa']
   
8.9
data.get('username')
   
'geetha'
data.get('age')
   
data.get('age','age is not there')
   
'age is not there'
'userid' in data
   
True
'gpa' not in 'data'
   
True
'gpa' not in data
   
False
data['username']
   
'geetha'
data['username']='nithya'
   
data['gpa']=5
   
>>> data
...    
{'userid': 103, 'username': 'nithya', 'skills': ['python', 'java', 'sql'], 'gpa': 5}
>>> data['skills'].append['flask']
...    
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    data['skills'].append['flask']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> data['skills'].append('flask')
...    
>>> data
...    
{'userid': 103, 'username': 'nithya', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 5}
>>> data['age']=23
...    
>>> data
...    
{'userid': 103, 'username': 'nithya', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 5, 'age': 23}
>>> data.update({'phone numnber':9390062539,'passedout':2026})
...    
>>> data
...    
{'userid': 103, 'username': 'nithya', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 5, 'age': 23, 'phone numnber': 9390062539, 'passedout': 2026}
>>> data.pop('age')
...    
23
>>> data
...    
{'userid': 103, 'username': 'nithya', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 5, 'phone numnber': 9390062539, 'passedout': 2026}
>>> data.popitem()
...    
('passedout', 2026)
>>> data
...    
{'userid': 103, 'username': 'nithya', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 5, 'phone numnber': 9390062539}
>>> del data['skills']
...    
>>> data
...    
{'userid': 103, 'username': 'nithya', 'gpa': 5, 'phone numnber': 9390062539}
>>> data.clear()
...    
>>> data
...    
{}
