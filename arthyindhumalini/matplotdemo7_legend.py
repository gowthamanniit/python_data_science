# to set user defined x & y axis values
import matplotlib.pyplot as plt
overs=[1,2,3,4,5,6,7,8,9,10]
indiaruns=[10,20,22,27,30,40,44,70,75,100]
ausruns=[10,14,22,33,44,55,66,70,72,79]

plt.title("INDIA VS AUSTRALIA")
plt.grid(True)
plt.xlabel("Overs")
plt.ylabel("runs")
plt.axis([-1,12,-10,110])
#========== assign label and legend======
plt.plot(overs,indiaruns,label="INDIA")
plt.plot(overs,ausruns,label="AUSTRALIA")
plt.legend()
plt.show()
