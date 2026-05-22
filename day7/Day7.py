Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={1:1,2:4,3::5,4:6,5:6,6:7}
SyntaxError: invalid syntax
d={1:1,2:4,3:5,4:6,5:6,6:7}
d.keys()
dict_keys([1, 2, 3, 4, 5, 6])
d.values()
dict_values([1, 4, 5, 6, 6, 7])
d.items()
dict_items([(1, 1), (2, 4), (3, 5), (4, 6), (5, 6), (6, 7)])
len(d)
6
sorted(d)
[1, 2, 3, 4, 5, 6]
max(d)
6
min(d)
1
d.get(6)
7
d.setdefault(8:0)
SyntaxError: invalid syntax
d.setdefault(8,0)
0
d.keys()
dict_keys([1, 2, 3, 4, 5, 6, 8])
d
{1: 1, 2: 4, 3: 5, 4: 6, 5: 6, 6: 7, 8: 0}
s=set()
s={9,2,3,4,5,34,2,5,67,98,2,9,99}
s
{2, 3, 4, 5, 34, 67, 98, 9, 99}
s=set()
s.add(1)
s
{1}
s.add(1.1)
s.add("string")
s.add((2+3j))
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.add(1,2,3,4)
TypeError: set.add() takes exactly one argument (4 given)
s
{(2+3j), 1, 'string', 1.1}
s.add((1,2,3,4))
s
{1, 1.1, (2+3j), (1, 2, 3, 4), 'string'}
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add(False)
s
{False, 1, 1.1, (2+3j), (1, 2, 3, 4), 'string'}
{1,2}+{3,4}
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    {1,2}+{3,4}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
{1,2}]*10
SyntaxError: unmatched ']'
{1,2}*10
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    {1,2}*10
TypeError: unsupported operand type(s) for *: 'set' and 'int'
S[2]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    S[2]
NameError: name 'S' is not defined. Did you mean: 's'?
S[::2]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    S[::2]
NameError: name 'S' is not defined. Did you mean: 's'?
1 in s
True
1.1 not in s
False
a={1,2,3,4,5}
b-{2,3,4,7,8}
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b-{2,3,4,7,8}
NameError: name 'b' is not defined
b={2,3,7,8,9}
a|b
{1, 2, 3, 4, 5, 7, 8, 9}
a&b
{2, 3}
a-b
{1, 4, 5}
b-a
{8, 9, 7}
a^b
{1, 4, 5, 7, 8, 9}
{1,2}<a
True
{1,2}>a
False
a={1,2}
b={3,4}
x.isdisjoint(y)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x.isdisjoint(y)
NameError: name 'x' is not defined
a.isdisjoint(b)
True
a.union
<built-in method union of set object at 0x0000020EC61D2960>
a.union(b)
{1, 2, 3, 4}
a.imtersection(b)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.imtersection(b)
AttributeError: 'set' object has no attribute 'imtersection'. Did you mean: 'intersection'?
a.intersection(b)
set()
a={1,2,3,4,5}
b-{2,3,4,7,8}
SyntaxError: multiple statements found while compiling a single statement
a.union(b)
{1, 2, 3, 4}
a.intersection(b)
set()
a.difference(b)
{1, 2}
a.issubset(b)
False
a.issuperscript(b)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.issuperscript(b)
AttributeError: 'set' object has no attribute 'issuperscript'. Did you mean: 'issuperset'?
a.issuperset(b)
False
sorted(a)
[1, 2]
max(a)
2
min(a)
1
len(a)
2
sum(a)
3
a.count()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
a
{1, 2}
a={1,2,3,4,5}
a.add(9)
a.update({67,89,70})
a
{1, 2, 3, 4, 5, 67, 70, 9, 89}
a.pop(6)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.pop(6)
TypeError: set.pop() takes no arguments (1 given)
a.pop()
1
a.popitem()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.popitem()
AttributeError: 'set' object has no attribute 'popitem'
>>> a.clear()
>>> a
set()
>>> a.remove(2)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.remove(2)
KeyError: 2
>>> a={1,2,3,4,5}
>>> a.remove(2)
>>> a
{1, 3, 4, 5}
>>> a.discard(89)
>>> a
{1, 3, 4, 5}
>>> a={1,2,3,4,5}
>>> b={2,3,7,8,9}
>>> a.intersection_update(b)
>>> a
{2, 3}
>>> b
{2, 3, 7, 8, 9}
>>> a.copy(b)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.copy(b)
TypeError: set.copy() takes no arguments (1 given)
>>> a.add(45)
>>> a
{2, 3, 45}
>>> c=b
>>> b
{2, 3, 7, 8, 9}
>>> c
{2, 3, 7, 8, 9}
>>> c.add(100)
>>> c
{2, 3, 100, 7, 8, 9}
>>> b
{2, 3, 100, 7, 8, 9}
>>> d=b.copy()
>>> d
{2, 3, 100, 7, 8, 9}
>>> b
{2, 3, 100, 7, 8, 9}
