from tkinter import*
from PIL import Image,ImageTk
import xlwt
import bs4
import openpyxl as xl
import csv
def enterval():
    n1=nvalue.get()
    p1=pvalue.get()
    r1=rvalue.get()
    g1=gvalue.get()
    res1=int(res.get())
    s1=int(s.get())
    with open("newfile.csv","a")as csvfile:
        writer.csv.writer(csvfile)
        writer.writerow((n1,p1,r1,g1,res1,s1))
root=Tk()
root.config(background="light blue")
root.geometry("655x320")
Label(text="operation",font="Crysis 20 bold",bg='green',fg='blue').grid(row=0,column=4)
name=Label(root,text="Username")
pwd=Label(root,text="Password")
rg=Label(root,text="RegNumber")
g=Label(root,text="gender")
name.grid()
pwd.grid()
rg.grid()
g.grid()
#var classes in tkinter
#booleanvAR,doublevar,stringvar,intvar
nvalue=StringVar()
pvalue=StringVar()
rvalue=StringVar()
gvalue=StringVar()
res=IntVar()
s=IntVar()
nentry=Entry(root,textvariable=nvalue,width=10,bg="yellow")
pentry=Entry(root,textvariable=pvalue)
rentry=Entry(root,textvariable=rvalue)
gentry=Entry(root,textvariable=gvalue)
nentry.grid(row=1,column=1)
pentry.grid(row=2,column=1)
rentry.grid(row=3,column=1)
gentry.grid(row=4,column=1)
result=Checkbutton(text="Mark here",variable=res)
result.grid(row=5,column=3)
rb=Radiobutton(root,text="Indian",variable=s,value=1).grid()#value must be different
rb1=Radiobutton(root,text="Foreign",variable=s,value=2).grid()
ci=StringVar()
city=['Delhi','Ghaziabad','Allahabad','Hyderabad']
droplist=OptionMenu(root,ci,*city)
droplist.config(bg="orange")
ci.set('Allahabad')
droplist.grid(row=7,column=2)

Button(text="submit",command=enterval).grid()














root.mainloop()
