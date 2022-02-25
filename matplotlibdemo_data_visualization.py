#import matplotlib.pyplot as plt
'''
score=[10,20,30,40,40,45,70,89,110,110,110,110,140]
plt.xlabel("overs")
plt.ylabel("runs")
plt.title("India vs Australia")
plt.plot(score)
plt.show()
'''
'''
plt.xlabel("overs")
plt.ylabel("runs")
plt.title("India vs Australia")
plt.plot([10,22,33,45])
plt.plot([10,20,30,40])
plt.plot([5,6,9,100])
plt.show()
'''
'''
v=[1,2,3,4,5,6]
k=[1,2,3,44,12,-10]

#s=[i**2 for i in k]
#print(type(s))
#or
s=[]
for i in k:
    s.append(i**2)
plt.plot(s,v)
plt.show()
'''
'''
k=['Abi','aRUN','AraVIND','BaNu','chitrA']
s=[]
for i in k:
    s.append(i.upper())
#print(s)

name=input("Enter Name:")
if name.upper() in s:
    print("valid person")
else:
    print("invalid person")
'''
'''
k=[1,2,3,44,12,-10]
plt.plot([i**2 for i in k])
plt.show()
'''
'''
s=['aaa','bbb','ccc','ddd','eee','fff']
k=[1,2,3,4,2,10]
#plt.plot([1,2,3,4,5],[11,22,33,44,55],'rs') # ro - red oval  bs-blue square
#plt.plot([1,2,3,4,5],[11,22,33,44,55],'r--') # r-- red dash dash
#plt.plot([1,2,3,4,5],[11,22,33,44,55],'g--') # r-- red dash dash
#plt.plot([1,2,3,4,5],[11,22,33,44,55],'g^',label="india") # g^ -- green triangle
plt.plot([1,2,3,4,5],[11,22,33,44,55],'g-',label="india") # g- green line
plt.plot([1,2,3,4,5],[3,29,39,59,65],'r^',label="corona") # r^ --red triangle
plt.legend()
#plt.plot(s,[i**2 for i in k])
#plt.plot([i**2 for i in k],s)
plt.xlabel("names")
plt.ylabel("scores")
#plt.axis([0,5,0,200])
plt.ylim([0,150])
plt.grid(True)
plt.savefig("d:/images/1.jpg")
plt.show()
'''
'''
import numpy
data=numpy.random.randn(10,20)
print (data)
'''
'''
k=[]
for i in range(5):
    data=numpy.random.randint(10,10)
    print(data)    
    k.append(data)
'''
#plt.ylim(0,20)
#plt.xlim(10,20)
#plt.hist(k)
#plt.hist(data)
#----------------------
#plt.bar([11,22,33,44],[11,33,44,55])
#plt.show()
#-------------------
'''
import numpy
k1=[]
k2=[]
for i in range(5):
    data1=numpy.random.randint(10,50)
    data2=numpy.random.randint(10,50)
    k1.append(data1)
    k2.append(data2)
print(k1)
print(k2)
plt.bar(k1,k2)
plt.show()
plt.show()
'''
'''
my_dict = {'A':30, 'B':65, 'C': 50, 'D': 80,'E':90}
for i, key in enumerate(my_dict):
    print(i,key,my_dict[key])
    plt.bar(i, my_dict[key])
plt.legend(['a','b','c','d','e'])
#plt.xticks([0, 1, 2, 3,4],  my_dict.keys())
#plt.yticks([30,65,50,80,90],my_dict.values())
    
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.figure(figsize=(14,14)) # size of the plot
x = [60000, 200000, 300000, 70000, 30000] # proportion of sectors
my_labels = ['DMK', 'Cars', 'Super-cars', 'bicyle', 'planes']
plt.pie(x, labels=my_labels)
plt.show()
'''
'''
import matplotlib.pyplot as plt
names = ['aa', 'bb', 'cc', 'dd']
f,ax1 = plt.subplots()
ax1.pie([30, 35, 10, 25],labels=names,autopct='%1.2f%%')
plt.show()

'''
import matplotlib.pyplot as plt
names = ['aa', 'bb', 'cc', 'dd']
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
#print(type(fig1))
#print(type(ax1))
ax1.pie([30, 25, 40, 35],
        explode=(0.2, 0, 0, 0), # it would separate 'bb'
        labels=names,
        autopct='%1.1f%%'        
)
ax2.pie([130, 125, 140, 35],
        explode=(0.2, 0, 0, 0), # it would separate 'bb'
        labels=names,
        autopct='%1.1f%%'        
)

ax1.axis('equal')
ax2.axis()

plt.show()
