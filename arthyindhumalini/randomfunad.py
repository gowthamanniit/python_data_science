import numpy
ans=numpy.random.power(2,5)  # only decimal place 0.any15
print(ans)
ans=ans*1000
print(ans)
for a in ans:
    print(round(a,0))
