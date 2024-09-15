import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
mylabels=[2019,2020,2021,2022,2023]
values=[50,10,5,15,20]
colors=["red","green","blue","yellow","pink"]
plt.pie(values,labels=mylabels,colors=colors)
plt.show()
           
