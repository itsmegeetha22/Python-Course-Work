Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026-05-25

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026-05-25
2026
5
25
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 135, in <module>
    print(t.weekend())
AttributeError: 'datetime.date' object has no attribute 'weekend'

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026-05-25
2026
5
25
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 135, in <module>
    print(t.weekdY())
AttributeError: 'datetime.date' object has no attribute 'weekdY'. Did you mean: 'weekday'?

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026-05-25
2026
5
25
0
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 136, in <module>
    print(t.isoweekend())
AttributeError: 'datetime.date' object has no attribute 'isoweekend'. Did you mean: 'isoweekday'?

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026-05-25
2026
5
25
0
1

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 145, in <module>
    print(date(2026,22,31))
ValueError: month must be in 1..12, not 22

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 148, in <module>
    print(date(2026,13,31))
ValueError: month must be in 1..12, not 13

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026-02-01

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
enter the dob[YYYY-MM-DD]:2026-22-23
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 158, in <module>
    dob=list(map(input("enter the dob[YYYY-MM-DD]:").split('-')))
TypeError: map() must have at least two arguments.

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 165, in <module>
    print(time(24,24,24))
ValueError: hour must be in 0..23, not 24

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 165, in <module>
    print(time(24,240,24))
ValueError: hour must be in 0..23, not 24

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 165, in <module>
    print(time(21,29,60))
ValueError: second must be in 0..59, not 60

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
21:59:50

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
21:59:54

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026-05-25 11:53:27.607475

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026
5
25
11
56
31

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 191, in <module>
    print(strftime('%Y/%m/%d'))
NameError: name 'strftime' is not defined

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026/05/25
26/05/25
26/05/25/12:10:10
Mon 26/05/2512:10:10 PM
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 195, in <module>
    print(n.strftime('%A %d %b %y %I:%M:%S %P'))
ValueError: Invalid format string

================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026/05/25
26/05/25
26/05/25/12:10:25
Mon 26/05/2512:10:25 PM
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 195, in <module>
    print(n.strftime('%A, %d %b %y %I:%M:%S %P'))
ValueError: Invalid format string
>>> 
================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026/05/25
26/05/25
26/05/25/12:10:59
Mon 26/05/2512:10:59 PM
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 195, in <module>
    print(n.strftime('%A,%d %b %y %I:%M:%S %P'))
ValueError: Invalid format string
>>> 
================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026/05/25
26/05/25
26/05/25/12:11:12
Mon 26/05/2512:11:12 PM
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 195, in <module>
    print(n.strftime('%A,%d %b %y %I:%M:%S %P'))
ValueError: Invalid format string
>>> 
================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026/05/25
26/05/25
26/05/25/12:11:34
Mon 26/05/2512:11:34 PM
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 195, in <module>
    print(n.strftime('%A,%d %b %Y %I:%M:%S %P'))
ValueError: Invalid format string
>>> 
================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
Traceback (most recent call last):
  File "C:\Users\geeth\OneDrive\Desktop\ATM\main.py", line 201, in <module>
    d=date.time()
AttributeError: type object 'datetime.date' has no attribute 'time'. Did you mean: 'ctime'?
>>> 
================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
2026-05-25 12:33:20.311805
>>> 
================================================================= RESTART: C:\Users\geeth\OneDrive\Desktop\ATM\main.py =================================================================
