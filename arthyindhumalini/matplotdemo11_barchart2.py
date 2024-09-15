#Bar chart
import matplotlib.pyplot as plt

plt.title("Bar/Column Chart - Student MarkList")
plt.grid(True)
plt.xlabel("Subjects",size="15", weight="bold")
plt.ylabel("Marks",rotation="horizontal",size="10",weight="bold")
plt.axis([-1,6,0,110])
#========== assign label and legend======
data1=("tamil","english","maths","science","social")
data2=[99,77,88,100,88]
def addmarktext():
    k=0
    for i in data2:
        plt.text(k,i-15,i,color="yellow",rotation="vertical",weight="bold")
        k=k+1

colorapply=plt.bar(data1,data2,label="marks")
colorapply[0].set_color("g")
colorapply[1].set_color("r")
colorapply[2].set_color("b")
colorapply[3].set_color("y")
colorapply[4].set_color("c")

plt.legend()
addmarktext()
plt.show()
