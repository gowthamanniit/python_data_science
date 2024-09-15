import numpy
k=[81,49,36,89,90,16]   
print(numpy.sqrt(k))

s=numpy.random.randint(0,100,10)
print(s)
fans=numpy.sqrt(s)
print(fans)

ans=[]
for i in range(len(fans)):
    ans.append(round(fans[i],2))
print(ans)
