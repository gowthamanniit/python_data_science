'''
import matplotlib.pyplot as plt
k=[100,120,310,440]
plt.xlabel("India")
plt.ylabel("PAKISTAN")
plt.plot(k)
plt.show()
'''
'''
import matplotlib.pyplot as plt
k1=[10,20,30,40,50,60,70,80,90,100]
k2=[100,120,310,445,510,620,780,880,930,1000]
plt.xlabel("India")
plt.ylabel("PAKISTAN")
plt.plot(k1,k2)
plt.show()
'''
'''
k=[2,3,4,5,6,7]
#res=[ i*i for i in k]
#or
res=[]
for i in k:
    res.append(i*i) 
print(res)
'''
'''
import matplotlib.pyplot as plt
k1=[1,2,3,4,5,6,7]
k2=[i*i for i in k1]
plt.xlabel(" x axis ")
plt.ylabel(" y axis ")
plt.plot(k1,k2)
plt.show()
'''
'''
import matplotlib.pyplot as plt
k1=["Trichy","Chennai","Karur"]
k2=[103.34,104.4,107.4]
plt.xlabel(" weather Report - city wise ")
plt.ylabel(" Range ")
plt.plot(k1,k2)
plt.show()
'''
'''
import matplotlib.pyplot as plt
overs=[1,2,3,4,5,6,7,8,9,10]
indruns=[10,20,24,32,44,55,60,71,89,100]
pakruns=[6,12,14,19,24,40,51,66,73,80]
plt.xlabel(" Overs ")
plt.ylabel(" Runs ")
plt.plot(overs,indruns)
plt.plot(overs,pakruns)
plt.show()
'''
'''
import matplotlib.pyplot as plt
overs=[1,2,3,4,5,6,7,8,9,10]
plt.xlabel(" Overs ")
plt.ylabel(" Runs ")
plt.ylim(0,150)
plt.xlim(0,15)
plt.plot([i*i for i in overs])
plt.show()
'''
'''
import matplotlib.pyplot as plt
overs=[1,2,3,4,5,6,7,8,9,10]
indruns=[10,20,24,32,44,55,60,71,89,100]
pakruns=[6,12,14,19,24,40,51,66,73,80]
plt.xlabel(" Overs ")
plt.ylabel(" Runs ")
plt.xlim(0,15)
plt.ylim(0,150)
plt.grid(True)
plt.plot(overs,indruns)
plt.plot(overs,pakruns)
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.xlabel("india")
plt.ylabel("runs")
plt.plot([1,2,3,4],[10,22,33,40],"ro")
plt.plot([1,2,3,4],[10,22,33,40])
plt.axis([0,10,0,100]) # or plt.xlim(0,10)  plt.ylim(0,100)
plt.grid(True)
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
k=np.arange(0,50,10)
#plt.plot(k,"r+")
#plt.plot(k,"r*")
#plt.plot(k,"r--")
#plt.plot(k,"g--")
#plt.plot(k**2,'bs')  # bs - blue square  # r - red # g-green
#plt.plot(k**2,'g^')  # b^ blue triangle
#plt.plot(k**2)
plt.plot([1,13,24,37,49],"bs",label="pakistan")
plt.plot([4,23,34,47,59],"g^",label="India")
plt.plot([1,13,24,37,49])
plt.plot([4,23,34,47,59])
plt.legend()

plt.grid(True)
plt.title("This is Title")
plt.xlabel("x axis data")
plt.ylabel("y axis data")

plt.show()
'''
# histogram chart
# no. of occurances based
'''
#import numpy as np
import matplotlib.pyplot as plt
#k=np.random.randn(2,4)
#print(k)
plt.xlim(0,80)
plt.hist([[10,10,10,10,20,20,20,50,50,60]])
plt.show()
#print(k)
'''
# bar chart  or column chart
# basic
'''
import matplotlib.pyplot as plt
plt.bar([1,2,3,4,5],[10,3,25,12,5])
plt.savefig("mypic.jpg") # jpeg: join photograph expert group
plt.savefig("mypic1")  # it will save on .png format : portable network grapics
                        # gif: graphical interchange format.
plt.show()
'''
'''
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9]
y=[10,12,13,4,5,0,9,23,22]
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.bar(x,y,label="Runs")
plt.grid(True)
plt.legend()
plt.show()
'''
# bar chart using dictionary
'''
import matplotlib.pyplot as plt
d={"a":10,"b":49,"c":55,"d":76}
x=d.keys()
y=d.values()
plt.bar(x,y)
plt.show()
'''
'''
import matplotlib.pyplot as plt
d={"a":10,"b":49,"c":55,"d":76}
ans=[]
for i,k in enumerate(d):
    print("index:",i,"key:",k,"value:",d[k])
    ans.append(d[k])
    plt.bar(i+1,d[k])
#plt.bar([1,2,3,4],ans)
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.xticks([1,2,3,4],[110,22,323,44])
plt.yticks([1,2,3,4,7,8],[100,200,400,300,500,"gowtham"])
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
vote=[10000,20000,3000,2000]
team=["ADMk","DMK","mDmk","others"]
plt.pie(vote,labels=team)

plt.title("TN Election Result: 2020")
plt.show()
'''
# percentage : autopct
'''
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
vote=[10000,20000,30000,40000]
team=["ADMk","DMK","mDmk","others"]
plt.pie(vote,labels=team,autopct='%1.2f%%')

plt.title("TN Election Result: 2020")
plt.show()
'''
#explode : use: to show separate part.
'''
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
vote=[10000,20000,30000,40000]
team=["ADMk","DMK","mDmk","others"]
plt.pie(vote,explode=(.2,.5,0,-0.2), labels=team,autopct='%1.2f%%')
                    # distance(admk), dis(dmk),dis(mdmk),dis(others)

plt.title("TN Election Result: 2020")
plt.show()

'''






