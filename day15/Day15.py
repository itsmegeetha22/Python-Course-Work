'''
add=lambda a,b:a+b
print(add(3,4))


add=lambda base,power:base**power
print(add(3,4))


wish=lambda name: f'{name},welcome to the python'
print(wish('geetha'))
print(wish('hema'))
      


check=lambda num:"even" if num%2==0 else "odd"
print(check(19))
print(check(20))


square=lambda num:num**2
print(square(19))
print(square(20))


check=lambda a,b:max(a,b)
print(check(19,13))
print(check(20,30))



check=lambda s:len(s)
print(check('geetha324'))
print(check('nithya345'))


check=lambda s:"starts with vowel" if s[0] in'aeiouAEIOU' else "not starts with vowel"
print(check('ehbsdjb'))
print(check('hudhaud'))



check=lambda email:email.split('@')[-1]
print(check('geetha@gmail.com'))
print(check('nithya@yahoo.com'))


check=lambda year:"leap year" if year%400==0 or (year%400==0 and year%100!=0) else "not leap year"
print(check(2023))
print(check(2022))



check=lambda year:year%10
print(check(2024))
print(check(2025))


l=[1,4,3,6]
res=list(map(lambda i:i**2,l))
print(res)



l=["hello","world","geetha","hema"]
res=list(map(lambda i:i.upper(),l))
print(res)




l={'geetha':45,'hema':56,'nithya':80}
res=dict(sorted(l.items()))
print(res)



l={'geetha':45,'hema':56,'nithya':80}
print(dict(sorted(l.items(),key=lambda i:i[1])))
print(dict(sorted(l.items(),key=lambda i:i[1],reverse=True)))
'''






