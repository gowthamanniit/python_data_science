#histogram chart
import matplotlib.pyplot as plt

plt.title("Histogram Chart")
plt.grid(True)
plt.xlabel("---")
plt.ylabel("----")
plt.axis([0,100,0,2])
#========== assign label and legend======
data=[7,68,29,92,49]
plt.hist(data,label="differences")
plt.legend()
plt.show()
