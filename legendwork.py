import matplotlib.pyplot as plt
my_dict = {'A':30, 'B':65, 'C': 50, 'D': 80,'E':90}
#for i, key in enumerate(my_dict):
 #   print(i,key,my_dict[key])
p1=plt
p1.plot([10,20,30,40,50])
p2=plt
p2.plot([16,26,36,42,59])

plt.legend(['india','aus'])
#p2.legend(['a','b','c','aaaaa'])
#plt.xticks([0, 1, 2, 3,4],  my_dict.keys())
#plt.yticks([30,65,50,80,90],my_dict.values())
    
plt.show()
