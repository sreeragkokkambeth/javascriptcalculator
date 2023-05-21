from tkinter import *
from tkinter import Button
root=Tk()
root.geometry('600x700')
root.title('calculator')
scvalue=StringVar()
def click(num):
    scvalue.set(scvalue.get()+str(num))
    screen.update()
    print(num)
def cal():
    try:
        rslt=eval(scvalue.get())
        scvalue.set(rslt)
        screen.update()
        print(rslt)
    except ZeroDivisionError:
        scvalue.set('cant divide by zero')
        screen.update()
def backspace():
    ge=scvalue.get()
    rslt=ge[:(len(ge))-1]
    scvalue.set(rslt)
    screen.update()
    print(rslt)
def clear():
    scvalue.set('')
    screen.update()
def square():
    a=float(scvalue.get())
    rslt=a*a
    scvalue.set(rslt)
    screen.update()
def sr():
    a=float(scvalue.get())
    rslt=a**.5
    scvalue.set(rslt)
    screen.update()

screen=Entry(root,width=80,background='ivory',text=scvalue,font='luicida 30 bold')
screen.pack(padx=5,pady=2)

f=Frame(root,background='skyblue')
f.pack(padx=5)
b=Button(f,text='7',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(7))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='8',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(8))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='9',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(9))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='+',fg='black',background='red' ,font='luicida 30 bold',command=lambda:click('+'))
b.pack(side=LEFT, padx=6,pady=5)

f=Frame(root,background='skyblue')
f.pack(padx=5)
b=Button(f,text='4',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(4))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='5',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(5))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='6',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(6))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='-',fg='black',background='red' ,font='luicida 30 bold',command=lambda:click('-'))
b.pack(side=LEFT, padx=6,pady=5)

f=Frame(root,background='skyblue')
f.pack(padx=5)
b=Button(f,text='1',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(1))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='2',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(2))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='3',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(3))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='*',fg='black',background='red' ,font='luicida 30 bold',command=lambda:click('*'))
b.pack(side=LEFT, padx=6,pady=5)

f=Frame(root,background='skyblue')
f.pack(padx=5)
b=Button(f,text='0',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click(0))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='.',fg='black',background='blue' ,font='luicida 30 bold',command=lambda:click('.'))
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='=',fg='black',background='red' ,font='luicida 30 bold',command=lambda:cal())
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='/',fg='black',background='red' ,font='luicida 30 bold',command=lambda:click('/'))
b.pack(side=LEFT, padx=6,pady=5)

f=Frame(root,background='skyblue')
f.pack(padx=5)
b=Button(f,text='C',fg='black',background='red' ,font='luicida 25 bold',command=lambda:clear())
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='B',fg='black',background='red' ,font='luicida 25 bold',command=lambda:backspace())
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='S',fg='black',background='red' ,font='luicida 25 bold',command=lambda:square())
b.pack(side=LEFT, padx=6,pady=5)
b=Button(f,text='Sr',fg='black',background='red' ,font='luicida 25 bold',command=lambda:sr())
b.pack(side=LEFT, padx=6,pady=5)
root.mainloop()