import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
mylabels=[2019,2020,2021,2022,2023]
values=[75,10,5,5,5]
colors=["red","green","blue","yellow","pink"]
plt.pie(values,labels=mylabels,colors=colors,shadow=True,autopct="%1.2f%%",pctdistance=.6)
plt.pie(values,labels=values,labeldistance=.95,shadow=True)
plt.title("year wise income")
plt.show()
           
