from scipy import stats
print("module accepted")
#k=[11,22,33,44,55,22,22,22,22,33,11,66,77,88,99,11,24,11,11,11,99,11]
k=[11,22,33,44,55,22,22,22,22,33,66,77,88,99,24,11,99,11,33,33,33]
print("mode:",stats.mode(k))

#mode: maximum no. of occurances same value.

#=====================


d={}

for i in range(len(k)):
    c=1
    for j in range(i+1,len(k)):
        if k[i]==k[j]:
           c+=1
           k[j]=None
    d[k[i]]=c
print(d)


print(d.values())
mv=max(d.values())
print(mv)

for s in d.keys():
    if d[s]==mv:
        print("max no. of occurances:",s," -->",mv," times ")
#========================================

