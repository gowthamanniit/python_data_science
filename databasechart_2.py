import matplotlib.pyplot as plt
import mysql.connector
import tkinter
from tkinter import messagebox
window=tkinter.Tk()
wi=window.winfo_screenwidth()
he=window.winfo_screenheight()
window.configure(width=wi,height=he,bg="green")
def dbcon():
    global con
    global cur        
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="ds")
    cur=con.cursor()    
def clearbox():
    overtb.delete(0,"end")
    runstb.delete(0,"end")
    overtb.focus()
def insertfun():
    over=int(overtb.get())
    runs=int(runstb.get())
    #print(over,runs)
    dbcon()
    cur.execute("insert into score values(%d,%d)"%(over,runs))
    con.commit()
    messagebox.showinfo("Success","Inserted")
    clearbox()
    showchart()
def showchart():
    k1=[]
    k2=[]
    dbcon()
    cur.execute("select * from score")
    alldata=cur.fetchall()
    for i in alldata:
        #print(i[0],i[1])
        k1.append(i[0])
        k2.append(i[1])
    plt.bar(k1,k2)
    plt.show()
overlbl=tkinter.Label(window,text="Enter Over Number:")
overtb=tkinter.Entry(window)

runslbl=tkinter.Label(window,text="Enter Runs:")
runstb=tkinter.Entry(window)

but1=tkinter.Button(window,text="show graph",command=showchart)
but2=tkinter.Button(window,text="Insert",command=insertfun)

overlbl.place(x=50,y=100)
overtb.place(x=200,y=100)

runslbl.place(x=50,y=200)
runstb.place(x=200,y=200)

but1.place(x=300,y=300)
but2.place(x=200,y=300)

window.mainloop()
