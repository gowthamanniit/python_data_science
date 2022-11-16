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
def showchart():
    k1=[]
    k2=[]
    srun=int(over1tb.get())
    erun=int(over2tb.get())
    dbcon()
    cur.execute("select * from score where over between %d and %d"%(srun,erun))
    alldata=cur.fetchall()
    for i in alldata:
        #print(i[0],i[1])
        k1.append(i[0])
        k2.append(i[1])
    plt.bar(k1,k2)
    plt.show()

over1lbl=tkinter.Label(window,text="Enter starting Over Number:")
over1tb=tkinter.Entry(window)

over2lbl=tkinter.Label(window,text="Enter ending Over Number:")
over2tb=tkinter.Entry(window)

but1=tkinter.Button(window,text="show graph",command=showchart)
over1lbl.place(x=100,y=100)
over2lbl.place(x=100,y=200)
over1tb.place(x=300,y=100)
over2tb.place(x=300,y=200)
but1.place(x=300,y=300)
window.mainloop()
