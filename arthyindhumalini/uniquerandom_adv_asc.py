import numpy

st=11
ed=30
cou=10
data=numpy.random.randint(st,ed,cou)
print(list(data))

ans=list(set(data))
ans.sort()
print(ans)
asclen=len(ans)  # 9    11 20 21 22 23 24 25 27 28
ln=ans[-1]
balasc=cou-asclen

if (balasc+ans[-1])>ed:
    print("we can't update")
else:
    while True:
        if len(ans)==10:
            print(ans)
            break
        else:
            ins=numpy.random.randint(st,ed,1)
            res=ins not in ans
            if res==True:
                if ans[-1]<ins:
                    ans.extend(ins)
        


