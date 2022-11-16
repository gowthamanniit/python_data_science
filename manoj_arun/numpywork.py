
import numpy

n=int(input("enter number  10 to 40 "))
c=0
if n>=10 and n<=40:
    while True:
        c=c+1
        ans=numpy.random.randint(10,41,1)
        if n==ans[0]:
            print("success after",c,"tries")
            break
else:
    print("wrong number:")
'''
print("numpy package accepted")
mylist=[]
while True:
    ch=input("do you want to append data(y/n)?")
    if ch=="y" or ch=="Y":
        data=int(input("Enter integer data:"))
        mylist.append(data)
    else:
        break
print("list data:",mylist)
print("sum of list:",numpy.sum(mylist))
print("count of list:",numpy.count_nonzero(mylist))
'''

        
