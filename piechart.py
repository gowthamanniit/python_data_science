import matplotlib.pyplot as plt
label=["dmk","admk","bjp","others"]
values=[50,25,15,10]
mycolor=["red","green","blue","yellow"]
exp=[0,0.1,0,0]
plt.pie(values,explode=exp,labels=label,colors=mycolor,shadow=True,autopct="%1.1f%%",startangle=45)
plt.axis('equal')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
data={"chennai":90000,"covai":80000,"madurai":75000,"salem":86000,"ooty":10000}
keyvalue=[]
for v in data.keys():
    keyvalue.append(str(v)+"   "+str(data[v]))

plt.pie(data.values(),labels=keyvalue)
plt.title("CIty wise Sales report")
#plt.xlabel("city")
#plt.ylabel("sales")
plt.show()
