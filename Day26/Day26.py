'''
#REGULAR EXPRESSIONS:
import re
pattern=r'[A-Z]'
text='Pyhton version 3.13.1.3'
res=re.match(pattern,text)
print("match found " if res else"not matched")



import re
pattern=r''
text='Pyhton version 3.13.1.3'
res=re.match(pattern,text)
print("match found " if res else"not matched")




import re
pattern=r'[a-z]'
text='Pyhton version 3.13.1.3'
res=re.match(pattern,text)
print("match found " if res else"not matched")






import re
pattern=r''
text='Pyhton version 3.13.1.3'
res=re.search(pattern,text)
print(res.group() if res else"not matched")




import re
pattern=r'[A-Z]'
text='Pyhton version 3.13.1.3'
res=re.search(pattern,text)
print(res.group() if res else"not matched")




import re
pattern=r'[a-z]{3}'
text='Pyhton version 3.13.1.3'
res=re.findall(pattern,text)
print(res)
#print(res.group() if res else"not matched")




import re
pattern=r'[0-9]{2}'
text='Pyhton version 3.13.1.3'
res=re.findall(pattern,text)
print(res)



import re
pattern=r'[0-9]{2}'
text='Pyhton version 3.13.1.3'
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())



import re
pattern=r'[0-9]{10}'
text='1235637642'
res=re.fullmatch(pattern,text)
print(res.group() if res else"not matched")



import re
pattern=r'[0-9]{10}'
text='phone no:1235637642'
res=re.sub(pattern,'**********',text)
print(res)


import re
pattern=r'[aeiouAEIOU]'
text='pythhon programming langugaage'
res=re.sub(pattern,'*',text)
print(res)




import re
pattern=r'[,-:]'
text='pyt,hho-npro:gram,ming-lang:uga,age'
res=re.split(pattern,text)
print(res)
'''

import re
pattern=r'(h.t)'
text='hut','hit','hat'
res=re.findall(pattern,text)
print(res)























































































































































































