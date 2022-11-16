import sys
try:
    f=open("d:/123test1.txt","x")
    data=input("enter your data:")
    f.write("\n"+data)    
    f.close()
except:
    print("Error Name:",sys.exc_info()[0])
    print("Error Name:",sys.exc_info()[1])
finally:
    print("program end")
