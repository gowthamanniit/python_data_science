#assigning user defined x-axis label
#===================================
import matplotlib.pyplot as plt
print("ok")
score=[1,17,30,34,49,67]
xlabel=[1,2,3,4,5,6]
plt.xlabel("overs")
plt.ylabel("runs")
plt.plot(xlabel,score)
plt.plot([10,20,30,40,50,60])
plt.show()
