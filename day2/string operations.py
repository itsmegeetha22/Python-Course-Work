Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='pyhton'
type(S)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined. Did you mean: 's'?
type(s)
<class 'str'>
s=''
s
''
a='python'
id(a)
1967975874208
a=a+' lang'
a
'python lang'
id(a)
1968018448048
fname='abc'
lname='xyz'
fname+lname
'abcxyz'
fname*10
'abcabcabcabcabcabcabcabcabcabc'
'*'*30
'******************************'
'-*-'*10
'-*--*--*--*--*--*--*--*--*--*-'
names='niharika geethanjali sravani pavitra'
names[1]
'i'
names[8]
' '
names[10]
'e'
names[-1]
'a'
names
'niharika geethanjali sravani pavitra'
names[0;8:1]
SyntaxError: invalid syntax
names[0:8:1]
'niharika'
names[:8]
'niharika'
names[:19]
'niharika geethanjal'
names[9:19]
'geethanjal'
names[-7]
'p'
names[-7:]
'pavitra'
names[-9;]
SyntaxError: invalid syntax
names[-9]
'i'
names[-9:]
'i pavitra'
names[-8;]
SyntaxError: invalid syntax
names[-8:]
' pavitra'
names[::]
'niharika geethanjali sravani pavitra'
names[-1:-8:-1]
'artivap'
names[::2]
'nhrk etajl rvn air'
l=['niharika geethanjali sravani pavitra']
l
['niharika geethanjali sravani pavitra']
l[::-1]
['niharika geethanjali sravani pavitra']
l=l[::-1]
l
['niharika geethanjali sravani pavitra']
l=['niharika geethanjali sravani pavitra'].split()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l=['niharika geethanjali sravani pavitra'].split()
AttributeError: 'list' object has no attribute 'split'
'geethanjali' in names
True
'sravani' in names
True
'jyoshna' not in names
True
'niharika' not in names
False
len(names)
36
sorted(names)
[' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'e', 'e', 'g', 'h', 'h', 'i', 'i', 'i', 'i', 'i', 'j', 'k', 'l', 'n', 'n', 'n', 'p', 'r', 'r', 'r', 's', 't', 't', 'v', 'v']
ord('a')
97
ord('g')
103
ord('0')
48
ord('890')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    ord('890')
TypeError: ord() expected a character, but string of length 3 found
ord('90')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    ord('90')
TypeError: ord() expected a character, but string of length 2 found
chr('890')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    chr('890')
TypeError: 'str' object cannot be interpreted as an integer
chr(890)
'ͺ'
chr(56)
'8'
char(678)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    char(678)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(897)
'\u0381'
chr(99)
'c'
max(names)
'v'
min(names)
' '
names=''niharika geethanjali sravani pavitra'
SyntaxError: unterminated string literal (detected at line 1)
names='niharika geethanjali sravani pavitra'
names.upper()
'NIHARIKA GEETHANJALI SRAVANI PAVITRA'
names.lower()
'niharika geethanjali sravani pavitra'
l.capitalize()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    l.capitalize()
AttributeError: 'list' object has no attribute 'capitalize'
l='niharika geethanjali sravani pavitra'
l=capitalize()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    l=capitalize()
NameError: name 'capitalize' is not defined
l.capitalize()
'Niharika geethanjali sravani pavitra'
l.title()
'Niharika Geethanjali Sravani Pavitra'
names.swapcase()
'NIHARIKA GEETHANJALI SRAVANI PAVITRA'
"stghdaiierfnkjnkl".casefold()
'stghdaiierfnkjnkl'
names.center(40,'-')
'--niharika geethanjali sravani pavitra--'
names.center(20,'*')
'niharika geethanjali sravani pavitra'
names.center(50,'*')
'*******niharika geethanjali sravani pavitra*******'
names.ljust(30,'-)
            
SyntaxError: unterminated string literal (detected at line 1)
names.ljust(30,'-')
            
'niharika geethanjali sravani pavitra'
names.ljust(60,'-')
            
'niharika geethanjali sravani pavitra------------------------'
names.rjust(70,'*')
            
'**********************************niharika geethanjali sravani pavitra'
'5'.zfill(5)
            
'00005'
'45'.zfill(5)
            
'00045'
'456'.zfill(5)
            
'00456'
'4567'.zfill(5)
            
'04567'
'456778'.zfill(5)
            
'456778'
names='sree geetha swapna'
            
names.find('s')
            
0
names.find('g')
            
5
names.rfind('a')
            
17
names.find('y')
            
-1
names.index('a')#left to right
...             
10
>>> names.rindex('g')#right to left
...             
5
>>> names.index('z')
...             
Traceback (most recent call last):\
  File "<pyshell#92>", line 1, in <module>
    names.index('z')
ValueError: substring not found
>>> names.count('a')
...             
3
>>> names.count(' ')
...             
2
>>> names.count('x')
...             
0
>>> names='sree swapna geetha'
...             
>>> names.replace('a','1')
...             
'sree sw1pn1 geeth1'
>>> names.replace('i',' ')
...             
'sree swapna geetha'
>>> names.replace('e',' ')
...             
'sr   swapna g  tha'
>>> names.replace('geetha','sree')
...             
'sree swapna sree'
>>> names.replace('sree','hema')
...             
'hema swapna geetha'
>>> names.replace('geetha',' ')
...             
'sree swapna  '
>>> names.maketrans('aeiou','12345')
...             
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
>>> names.translate(names.maketrans('aeiou','12345'))
...             
'sr22 sw1pn1 g22th1'
