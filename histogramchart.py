#histogram chart
import matplotlib.pyplot as plt
plt.title("Histogram Chart")
plt.grid(True)
plt.xlabel("---")
plt.ylabel("----")
#plt.axis([0,190,0,2])
#========== assign label and legend======

data1=[90,100,105,110,119,118,160,161,117,163,167,250,255,300]

   


plt.hist(data1,label="difference")

plt.legend()
plt.show()
