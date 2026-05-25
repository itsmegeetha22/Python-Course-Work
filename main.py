'''
import sys
print(sys.argv)
print()
print(sys.path)
print()
print(sys.version)
print()
sys.exit()
print("end")


import platform
print(platform.system)
print(platform.release)
print(platform.processor)


import math
print(math.pi)
print(math.e)
print(math.sqrt(16))
print(math.pow(2,3))
print(math.floor(-12.00001))
print(math.floor(-12.3))
print(math.floor(-12.999))
print(math.ceil(-12.00001))
print(math.ceil(-12.3))
print(math.ceil(-12.999))
print(math.floor(12.00001))
print(math.floor(12.3))
print(math.floor(12.999))
print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.999))




import math
print(math.fabs(-123))
print(math.factorial(5))
print(math.gcd(44,12))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(190))
print(math.radians(190))



import random
print(random.random())#0-1
print(random.randint(1,3))#rnge
print(random.uniform(1,3))#float
l=['geetha','hema','nithya','lakshmi']
print(random.choice(l))#out of choice
print(random.choices(l,k=2))#specific choice
print("before:",l)
random.shuffle(l)
print("after:",l)




import collections
#s='pyhton programming'
s=[1,2,3,44,54,5,6,7,5,7,8]
print(collections.Counter(s))#key values in dict frmat 
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)



import collections
s='pyhton programming'
#s=[1,2,3,44,54,5,6,7,5,7,8]
 
d=collections.defaultdict(str)
for i in s:
    d[i]+=i
print(d)



import collections
d=collections.deque([])
d.append(10)
d.append(20)
d.popleft()
d.append(30)
d.popleft()
d.popleft()
d.append(40)
d.append(50)
print(d)


import collections
d=collections.deque([])
d.appendleft(10)
d.appendleft(20)
d.pop()
d.appendleft(30)
d.pop()
d.pop()
d.appendleft(40)
d.appendleft(50)
print(d)




from itertools import combinations,permutations
print(list(combinations('ABCD',3)))
print(list(permutations('ABCD',3)))






from datetime import date,time,datetime,timedelta
t=date.today()
print(t)
print(t.year)
print(t.month)
print(t.day)
print(t.weekday())
print(t.isoweekday())







from datetime import date,time,datetime,timedelta
print(date(2026,22,31))


from datetime import date,time,datetime,timedelta
print(date(2026,13,31))



from datetime import date,time,datetime,timedelta
print(date(2026,2,1))


from datetime import date,time,datetime,timedelta
dob=list(map(input("enter the dob[YYYY-MM-DD]:").split('-')))
print(date(year,month,day))



from datetime import date,time,datetime,timedelta
print(time(21,59,50))


from datetime import date,time,datetime,timedelta
print(time(21,59,54))



from datetime import date,time,datetime,timedelta
n=datetime.now()
print(n)



from datetime import date,time,datetime,timedelta
n=datetime.now()
print(n.year)
print(n.month)
print(n.day)
print(n.hour)
print(n.minute)
print(n.second)


from datetime import date,time,datetime,timedelta
n=datetime.now()
print(n.strftime('%Y/%m/%d'))
print(n.strftime('%y/%m/%d'))
print(n.strftime('%y/%m/%d/%H:%M:%S'))
print(n.strftime('%a %y/%m/%d:%I:%M:%S %p'))
print(n.strftime('%A,%d %b %Y %I:%M:%S %P'))
print(n.strftime('%A,%d %B %Y %I:%M:%S %P'))


from datetime import date,time,datetime,timedelta
n=datetime.now()
d=date.today()
a7=d-timedelta(days=20)
a15=n+timedelta(minutes=15)
print(a15)
'''
import random

def dice():
    return random.randint(1,6)
    
player1_name = input("Enter the player-1 name: ")
player2_name = input("Entere the player-2 name: ")

player1_score = 0
player2_score = 0


snake = {29:15,35:21,42:12,56:22,74:39,87:3,92:64,99:44}
ladder = {5:17,19:43,36:67,45:93,51:77,61:85,83:95}

winning_point = 100

while player1_score < winning_point and player2_score < winning_point:

    player1_status = input(f"{player1_name} - [P]lay or [Q]uit: ").upper()
    if player1_status == 'P':
        d=dice()
        print("Dice score:",d)
        if player1_score+d <= winning_point:
            player1_score+=d
        if player1_score in snake:
            player1_score = snake[player1_score]
            print(f"{player1_name}'s score: {player1_score} after snake----------")

        elif player1_score in ladder:
            player1_score = ladder[player1_score]
            print(f"{player1_name}'s score: {player1_score} after ladder+++++++++")

        elif player1_score == winning_point:
            print(f"{player1_name}'s score: {player1_score}")
            break
            
        else:
            print(f"{player1_name}'s score: {player1_score}")
    else:
        print(f"Congrats!! {player2_name}, you won the game")
        break


    player2_status = input(f"{player2_name} - [P]lay or [Q]uit: ").upper()
    if player2_status == 'P':
        d=dice()
        print("Dice score:",d)
        if player2_score+d <= winning_point:
            player2_score+=d
        if player2_score in snake:
            player2_score = snake[player2_score]
            print(f"{player2_name}'s score: {player2_score} after snake----------")

        elif player2_score in ladder:
            player2_score = ladder[player2_score]
            print(f"{player2_name}'s score: {player2_score} after ladder+++++++++")

        elif player2_score == winning_point:
            print(f"{player2_name}'s score: {player2_score}")
            break
        else:
            print(f"{player2_name}'s score: {player2_score}")
    else:
        print(f"Congrats!! {player1_name}, you won the game")
        break
    


if player1_score > player2_score:
    print(f"Congrats!! {player1_name}, you won the game")
else:
    print(f"Congrats!! {player2_name}, you won the game")
    





