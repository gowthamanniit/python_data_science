import matplotlib.pyplot as plt
import numpy
import mysql.connector
k1=[]
k2=[]

con=mysql.connector.connect(host="localhost",user="root",password="12345",database="ds")
cur=con.cursor()
cur.execute("select * from score")
alldata=cur.fetchall()
for i in alldata:
    #print(i[0],i[1])
    k1.append(i[0])
    k2.append(i[1])

plt.bar(k1,k2)
plt.show()

