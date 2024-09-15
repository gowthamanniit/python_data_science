import mysql.connector
import matplotlib.pyplot as plt
o=[]
r=[]
con=mysql.connector.connect(host="localhost",user="root",password="12345",database="india")
print("connection success")

cur=con.cursor()
cur.execute("select * from scoce")
alldata=cur.fetchall()
for data in alldata:
    print(data,type(data))
    o.append(data[0])
    r.append(data[1])
plt.bar(o,r)
plt.title("Runs per Over")
plt.xlabel("overs")
plt.ylabel("runs")
plt.show()
cur.close()
con.commit()
          
