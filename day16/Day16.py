'''
l=[2,3,4,5,65,67,89]
res=list(filter(lambda i:i%2==0,l))
print(res)


l=[2,3,4,5,65,67,89]
res=list(filter(lambda i:i%2!=0,l))
print(res)



l="python programming"
res=list(filter(lambda i:i in 'aeiouAEIOU',l))
print(res)


l="python programming"
res=list(filter(lambda i:i not in 'aeiouAEIOU',l))
print(res)

 
l=["opearors","consonants","conditional","exeptional"]
res=list(filter(lambda i:  i[0] not in 'aeiouAEIOU',l))
print(res)

l=["opearors","consonants","conditional","exeptional"]
res=list(filter(lambda i:  i[0]  in 'aeiouAEIOU',l))
print(res)


data={
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':5500},
    'hp':{'stock':13,'price':6500},
    'mac':{'stock':67,'price':87000}
    }
res=list(filter(lambda i:data[i]['stock']==0,data))
print(res)

data={
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':5500},
    'hp':{'stock':13,'price':6500},
    'mac':{'stock':67,'price':87000}
    }
res=list(filter(lambda i:data[i]['price']>50000,data))
print(res)



data={
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':5500},
    'hp':{'stock':13,'price':6500},
    'mac':{'stock':67,'price':87000}
    }
res={ i:data[i]['price'] for i in data}
r=dict(sorted(res.items(),key=lambda i:i[1]))
r1=dict(sorted(res.items(),key=lambda i:i[1],reverse=True))
print("low to high:")
print(r)
print("high to low:")
print(r1)



from functools import reduce
l=[1,223,3,45,4353,6547,6845]
m=["operators","constants","exeptional","conditional"]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
ms=reduce(lambda sum,i:sum+i,m)
print(s,p,ms)




def reels():
    r=['1..100','101..200','201..300','301..400','401..500']
    for i in r:
        yield i
scroll=reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

def reels():
    yield"1-10 files"
    yield"21-30 files"
    yield"31-40 files"
    yield"41-50 files"
    yield"51-60 files"
scroll=reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
'''
