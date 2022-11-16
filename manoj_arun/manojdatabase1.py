import tkinter
import matplotlib.pyplot as plt
import mysql.connector
from tkinter import messagebox
win=tkinter.Tk()
win.configure(width="800",height="500",bg="yellow")
def fun():
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="manoj")
    cur=con.cursor()
    cur.execute("select * from india")
    alldata=cur.fetchall()
    overs=[]
    runs=[]
    
    for i in alldata:        
        print(i[1])
        overs.append(i[0])
        runs.append(i[1])
    plt.bar(overs,runs)
    plt.show()
def insertfun():
    o=int(t1.get())
    r=int(t2.get())
    #print(o,r)    
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="manoj")
    cur=con.cursor()
    cur.execute("insert into india values(%d,%d)"%(o,r))
    con.commit()
    clearfun()
    messagebox.showinfo("insert","success")
def clearfun():
    t1.delete(0,"end")
    t2.delete(0,"end")
    t2.focus()
    
    
    
tit=tkinter.Label(win,text="Bar Chart Demo",font=('Times',44,'bold italic underline'),fg="red",bg="white")
tit.place(x=300,y=100)
l1=tkinter.Label(text="Enter over no.")
l2=tkinter.Label(text="Enter runs:")
t1=tkinter.Entry()
t2=tkinter.Entry()
l1.place(x=100,y=200)
l2.place(x=100,y=250)
t1.place(x=210,y=200)
t2.place(x=210,y=250)

but1=tkinter.Button(text="Insert",command=insertfun)
but1.place(x=210,y=300)

but2=tkinter.Button(text="Show Graph",command=fun)
but2.place(x=300,y=300)

win.mainloop()
