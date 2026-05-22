
'''
products={
    'salt':{'stock':20,'discount':10,'price':50},
    'sugar':{'stock':60,'discount':40,'price':90},
    'bread':{'stock':80,'discount':20,'price':70}
 }
for i in products:
    if products[i]['stock']:
        print(i)

products={
    'salt':{'stock':20,'discount':10,'price':50},
    'sugar':{'stock':60,'discount':40,'price':90},
    'bread':{'stock':80,'discount':20,'price':70}
 }
for i in products:
    if products[i]['stock']:
        print(i,products[i]['price'])
      

products={
    'salt':{'stock':20,'discount':10,'price':50},
    'sugar':{'stock':60,'discount':40,'price':90},
    'bread':{'stock':80,'discount':20,'price':70}
 }
for i in products:
    if products[i]['stock']:
        price=products[i]['price']
        print(i,price-(price*products[i]['discount']/100))

        '''



        

