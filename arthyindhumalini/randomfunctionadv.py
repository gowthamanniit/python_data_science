import numpy
n=int(input("enter number range:100-200"))
if n>=101 and n<=200:
    c=0
    while True:
        c+=1
        ans=numpy.random.randint(100,200) # otp, online game,
        if n==ans:
            print("success after ",c,"tries")
            break
else:
    print(" not in range")
print("game end")

