import numpy
print("module accepted")
k=[[11,22,None],[1,2,3],[44,535,66],[77,88,99],[10,20,30]]
print("normal list:",k)
arr=numpy.array(k)
print("array list:\n",arr)
#==============
totlen=len(k)
print(totlen)
s=0
for i in range(totlen):
    print("[",end="")
    for j in range(len(k[i])):
        if k[i][j]!=None:
            s+=k[i][j]
            print("%4d"%k[i][j],end=" ")
        else:
            print("%4s"%"None",end=" ")
    print("] = ",s)
    s=0    
