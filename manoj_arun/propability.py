'''
import matplotlib.pyplot as plt
Trainer={"t1":0.25,"T2":0.0875,"t3":0.325,"K4":0.1375,"t5":0.2}
v=Trainer.keys()
v=list(v)
ans=[]
for i,k in enumerate(Trainer):
    print("index:",i,"key:",k,"value:",Trainer[k])
    ans.append(Trainer[k])
    plt.bar(v[i],Trainer[k])
#plt.bar([1,2,3,4,5],ans)
plt.show()
'''
import matplotlib.pyplot as plt
d={"T1":20,"k2":7,"T3":26,"m4":11,"T5":16}

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
v=list(v)
m=0
for i in v:
    plt.bar(i,pro[m])
    m+=1

#plt.bar(["t1","t2","t3","t4","t5"],pro)
plt.show()


