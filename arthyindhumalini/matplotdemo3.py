import matplotlib.pyplot as plt
print("ok")
ind=[1,17,30,34,49,67]
aus=[10,12,24,30,44,55]
xlabel=[1,2,3,4,5,6]
plt.title("INDIA VS AUSTRALIA")
plt.xlabel("overs")
plt.ylabel("runs")
plt.plot(xlabel,ind)
plt.plot(xlabel,aus)
plt.show()
