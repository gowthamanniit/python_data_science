import matplotlib.pyplot as plt
names = ['aa', 'bb', 'cc', 'dd']
#plt.pie([40, 35, 10, 25],explode=(0,0.4,0,0),labels=names,autopct='%1.2f%%',shadow=True)
plt.pie([40, 35, 10, 25],explode=(0,0.3,0,0),labels=[40, 35, 10, 25],autopct='%1.2f%%',labeldistance=1.2,shadow=True)
plt.show()
