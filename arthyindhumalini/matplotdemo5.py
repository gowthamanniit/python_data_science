# to set user defined x & y axis values
import matplotlib.pyplot as plt
avg=[99.3,88.4,77.4,79.9,87.9,88.6,90.9]
rno=[1001,1002,1003,1004,1005,1006,1007]
plt.title("Student Avg List")
plt.grid(True)
plt.xlabel("Roll Numbers")
plt.ylabel("Percentages")
plt.plot(rno,avg)
plt.plot(rno,avg,'r*')
plt.axis([997,1010,-10,110])
plt.show()
