#histogram chart
import matplotlib.pyplot as plt

plt.title("Bar/Column Chart - INIDA Score")
plt.grid(True)
plt.xlabel("Overs")
plt.ylabel("Runs")

#========== assign label and legend======
data1=[1,2,3,4,5,6,7,8,9,10]
data2=[10,7,3,4,1,2,9,10,10,13]
plt.axis([0,10,0,max(data2)+3])
plt.bar(data1,data2)
#plt.legend()
plt.show()
