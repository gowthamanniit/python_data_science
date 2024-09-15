import matplotlib.pyplot as plt
print("ok")
ind=[1,17,30,34,49,67]
xlabel=[1,2,3,4,5,6]
plt.title("INDIA SCORE")
plt.xlabel("overs")
plt.ylabel("runs")
plt.plot(xlabel,ind)
plt.plot(xlabel,ind,"bs")
#bs -blue square
#ro -red oval
#go -green oval                            
#plt.plot(xlabel,[i*2 for i in ind],"ro")
plt.show()
