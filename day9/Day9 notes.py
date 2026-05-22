Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python'
for i in s:
    print(s)

    
python
python
python
python
python
python

for i in enumerate (s):
    print(i[0],i[1])

    
0 p
1 y
2 t
3 h
4 o
5 n
l=[123,345,567]
for i in enumerate (l):
    print(i[0],i[1],i)

    
0 123 (0, 123)
1 345 (1, 345)
2 567 (2, 567)
t=(1,2,3,4,5,)
for i in enumerate(t):
    print(i[0],i[1],i)

    
0 1 (0, 1)
1 2 (1, 2)
2 3 (2, 3)
3 4 (3, 4)
4 5 (4, 5)
s={12,23,34}
for i in enumerate (s):
    print(i[0],i[1],i)

    
0 34 (0, 34)
1 12 (1, 12)
2 23 (2, 23)
d={'k1':'g1','k2':'g2','k3':'g3'}
for i in enumerate (d):
    print(i[0],i[1],d(i[1]))

    
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    print(i[0],i[1],d(i[1]))
TypeError: 'dict' object is not callable



d={'k1':'g1','k2':'g2','k3':'g3'}
d
{'k1': 'g1', 'k2': 'g2', 'k3': 'g3'}
for i in enumerate (d):
    print(i[0],i[1],d(i[1]))

    
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    print(i[0],i[1],d(i[1]))
TypeError: 'dict' object is not callable
for i in range(1,100,2)
SyntaxError: expected ':'
print
<built-in function print>
for i in range(1,100,2):
    print(i)

    
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
pin=1234
'''
for i in range(5):
    entered_pin=int(input("enter the pin:"))
    if entered_pin==pin:
        print("unlock the pin")
        break
    else:
        print("invalid pin")
else:
    print("try after 60 seconds")
    

    

















    








    








    

