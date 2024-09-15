import numpy
ans=[]
ending="1229"
while True:
    data=numpy.random.randint(1,10000000000,1)
    data=str(data[0])
    res=data.endswith(ending)
    if res==True:
        ans.append(int(data))
    if len(ans)==10:
        break
print(list(ans))
