#import mymodule as mm
#from mymodule import addition,subtraction,multiplication
#from mymodule import *

from mymodule import addition as a,subtraction as s,multiplication as m
n1=int(input("enter no.1:"))
n2=int(input("enter no.2:"))
print(a(n1,n2))

ans=s(n1,n2)
print("answer : ",ans)

ans=m(n1,n2)
print("answer : ",ans)

#ans=division(n1,n2)
#print("answer : ",ans)
