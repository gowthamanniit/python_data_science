# to set user defined x & y axis values
import matplotlib.pyplot as plt
overs=[1,2,3,4,5,6,7,8,9,10,11]
indiaruns=[10,20,22,27,30,40,44,70,75,100,101]
ausruns=[10,14,22,33,44,55,66,70,72,79,81]
southafricaruns=[12,13,22,31,40,50,62,72,79,87,90]
def addlabelsindia():
    for i in range(len(overs)):
        plt.text(overs[i],indiaruns[i],indiaruns[i])
def addlabelsaustralia():
    for i in range(len(overs)):
        plt.text(overs[i],ausruns[i],ausruns[i])
def addlabelssouthafrica():
    for i in range(len(overs)):
        plt.text(overs[i],southafricaruns[i],southafricaruns[i])

plt.title("INDIA VS AUSTRALIA")
plt.grid(True)
plt.xlabel("Overs")
plt.ylabel("runs")
plt.axis([0,12,-5,110])
#========== assign label and legend======
plt.plot(overs,indiaruns)
plt.plot(overs,ausruns)
plt.plot(overs,southafricaruns)
plt.plot(overs,indiaruns,"b^",label="INDIA")
plt.plot(overs,ausruns,"y*",label="AUSTRALIA")
plt.plot(overs,southafricaruns,"r+",label="SOUTH AFRICA")
# syntax: adding lables 
#=========
#plt.text(2,20,30)
addlabelsindia()
addlabelsaustralia()
addlabelssouthafrica()
#========x, y, printvalue
plt.legend()
plt.savefig("mylabels.jpg")
plt.show()
