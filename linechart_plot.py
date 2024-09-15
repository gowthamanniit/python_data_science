import matplotlib.pyplot as plt
def assigntext():
    for i in xaxisdata:
        plt.text(i, yaxisdata[i-1],yaxisdata[i-1])        
xaxisdata=[1,2,3,4,5,6,7,8,9,10,11,12,13]
yaxisdata=[10,15,20,20,26,48,67,67,89,90,99,110,125]
plt.grid(True)
plt.xlabel("OVERS")
plt.ylabel("RUNS")
plt.title("Line Chart Demo")
plt.axis([-1,max(xaxisdata)+1,1,max(yaxisdata)+10])
plt.plot(xaxisdata,yaxisdata,"r^",label="INDIA")
plt.plot(xaxisdata,yaxisdata)
plt.bar(xaxisdata,yaxisdata)
assigntext()
plt.legend()
plt.savefig("arikrishnan.jpg")
plt.show()
