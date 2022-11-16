import pandas as pd
#d={"a":10,"b":20,"c":30}
#d=[11,22,33,44]
#k=pd.Series(d)
'''
d1=["a","b","z"]
d2=[11,33,44]
k=pd.Series(d1,d2)

s=[[11,22,33],["india","pakistan","srilanga"],['a','b','c']]
k=pd.Series(s)
print(k)

k=pd.Series(s[0],s[2]) # (value,key)
print(k)


k=pd.Series([11,55,8,99],["2001","2002","2003","2004"])
print(k)
k1=pd.Series([11,55],["2001","2002"])
print(k1)

print(k+k1)
print(k.index[0])
print(k1.index[1])
'''
'''
data=[11,22,33,44]
k=pd.DataFrame(data)
s=pd.Series(data)
print("----------Data frame-------")
print(k)
print("----------series-------")
print(s)
'''
'''
dic1={'r1':10,'r2':20,'r3':30}
dic2={'r1':20,'r5':55,'r6':84}
dic3={'r7':120,'r8':155,'r2':184}

data={'d1':dic1,'d2':dic2,'d3':dic3}
k=pd.DataFrame(data)
print(k)

list1=[[11,22,33],[10,20,30]]
list2=[[21,32,44],[40,50,60]]

data={'d1':list1,'d2':list2}
k=pd.Series(data)
print(k)
'''
'''
import numpy as np

k=np.random.rand(3,4)
print(k)

r=['row1','row2','row3']
c=['col1','col2','col3','col4']
s=pd.DataFrame(k,r,c)
print(s)
'''
'''
population=[[100,110,120,130],[210,220,230,240],[310,320,330,340]]
row=[2001,2002,2003]
col=['jan','feb','mar','apr']
s=pd.DataFrame(population,row,col)
print(s)
'''
'''
s=0
population=[[100,110,120,130],[210,220,230,240],[310,320,330,340],[11,33,44,55]]
row=[2001,2002,2003,2004]
col=['jan','feb','mar','apr']

# single for loop
rlen=len(row)
print("row length:",rlen)

clen=len(col)
print("col length:",clen)

k=[]

for i in range(rlen):
    s=0
    rt=0
    for j in range(clen):
        s=s+population[i][j]
        rt=rt+population[j][i]
    population[i].append(s)  # 5th col total append
    k.append(rt)             # noral list col wise total
k.append(sum(k))              # final total  last value
population.append(k)          


        
col.append("total")    
row.append("total")




print("================")
s=pd.DataFrame(population,row,col)
print(s)
'''


'''
population=[[100,110,120,130,77],[210,220,230,240,77],[310,320,330,340,77],
            [11,33,44,55,77],
            [10,20,30,40,77],[11,11,11,11,11],[11,12,13,14,15]]
row=[2001,2002,2003,2004,2005,2006,2007]
col=['jan','feb','mar','apr','jun']

# single for loop
rlen=len(row)
print("row length:",rlen)

clen=len(col)
print("col length:",clen)


for i in range(rlen):
    ct=0    
    for j in range(clen):
        ct=ct+population[i][j]
    population[i].append(ct)  # 5th col total append
    


k=[]
for i in range(clen):
    rt=0
    for j in range(rlen):
        rt=rt+population[j][i]
    k.append(rt)             # noral list col wise total
k.append(sum(k))              # final total  last value
population.append(k)
    


        
col.append("total")    
row.append("total")




print("================")
s=pd.DataFrame(population,row,col)
print(s)
'''
"""
# highest month collection

population=[[100,110,120,130,77],[210,220,230,240,77],[310,320,330,340,77],
            [11,133,44,55,77],
            [10,120,30,40,77],[11,111,11,11,11],[11,112,13,14,15]]
row=[2001,2002,2003,2004,2005,2006,2007]
col=['jan','feb','mar','apr','jun']

# single for loop
rlen=len(row)
print("row length:",rlen)

clen=len(col)
print("col length:",clen)


for i in range(rlen):
    ct=0    
    for j in range(clen):
        ct=ct+population[i][j]
    population[i].append(ct)  # 5th col total append
    


k=[]
for i in range(clen):
    rt=0
    for j in range(rlen):
        rt=rt+population[j][i]
    k.append(rt)             # noral list col wise total
k.append(sum(k))              # final total  last value
population.append(k)
        
col.append("total")    
row.append("total")


print("================")
s=pd.DataFrame(population,row,col)
print(s)

#-----------find max total month wise
print(k)
k1=[]
for data in range(len(k)-1):
    print(k[data])
    k1.append(k[data])
k1.sort()
bigcol=max(k1)
print("max collection :",bigcol)

#----------find month--------------------
dic={}
for i in range(len(col)-1):
    dic.update({col[i]:k[i]})
print(dic)

for i in range(len(col)-1):
    if bigcol==dic[col[i]]:
        print("biggest collection month:",col[i])
        break
#-------------------------------------
"""
"""
import numpy as np
import pandas as pd
test=pd.DataFrame(data=np.random.rand(5,4),columns=['W','X','Y','Z'])
print(test)
print(test[['W','Z']])
print(test.shape)
"""

import pandas as pd
data=pd.read_excel("pddemo.xlsx",sheet_name="sheetdata")
print(data)








