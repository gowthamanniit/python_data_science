import matplotlib.pyplot as plt
label=["dmk","admk","bjp","others"]
values=[50,25,15,10]
mycolor=["red","green","blue","yellow"]
exp=[0,0.1,0,0]
plt.pie(values,explode=exp,labels=label,colors=mycolor,shadow=True,autopct="%1.1f%%",startangle=45)
plt.axis('equal')
plt.show()
