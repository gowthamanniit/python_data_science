import numpy
data=numpy.random.randint(11,30,10)
print(list(data))

ans=list(set(data))
ans.sort()
print(ans)

while True:
    if len(ans)==10:
        print(ans)
        break
    else:
        ins=numpy.random.randint(10,30,1)
        res=ins not in ans
        if res==True:
            ans.extend(ins)
        


