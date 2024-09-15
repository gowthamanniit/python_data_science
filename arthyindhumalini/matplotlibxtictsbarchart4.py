import matplotlib.pyplot as plt
my_dict = {'A':30, 'B':65, 'C': 50, 'D': 80,'E':90}
for i, key in enumerate(my_dict):
    print(i,key,my_dict[key])
    plt.bar(i, my_dict[key])
plt.legend(['a','b','c','d','e'])
plt.xticks([0, 3, 2, 1,4], my_dict.keys())
plt.yticks([30,70,50,65,90],my_dict.values())    
plt.show()
