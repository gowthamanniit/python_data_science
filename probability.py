import matplotlib.pyplot as plt
d={"T1":20,"T2":7,"T3":26,"T4":11,"T5":16,"T6":20,"T7":30}

th=0
for k in d.values():
    th=th+k
print("total hours:",th)


pro=[]
for k in d.values():
    v=k/th
    pro.append(v)
print(pro)

v=d.keys()
#print(v,type(v))
v=list(v)
#print(v,type(v))

m=0
for i in v:
    plt.bar(i,pro[m])
    m+=1

#plt.bar(["t1","t2","t3","t4","t5"],pro)
plt.show()

