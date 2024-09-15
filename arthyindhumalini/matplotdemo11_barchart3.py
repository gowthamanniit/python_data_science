#Bar chart

import matplotlib.pyplot as plt

plt.title("Bar/Column Chart - Student MarkList")
plt.grid(True)
plt.xlabel("Subjects",size="15", weight="bold")
plt.ylabel("Marks",rotation="horizontal",size="10",weight="bold")
plt.axis([-1,6,0,110])
#========== assign label and legend======
d={"a":97,"b":98,"c":99,"d":100,"e":101,"f":102,"g":103}
co=("r","g","y","y","b","g","c")
marks=["tamil","english","maths","science","social","computer","commerce"]
for i,key in enumerate(d):
    print(i,key,d[key])
    colorapply=plt.bar(i,d[key],label=marks[i])
    colorapply[0].set_color(co[i])
plt.legend()
plt.show()
