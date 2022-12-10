from tkinter import *
ar=Tk()
def click(event):
    global ecv
    text = event.widget.cget("text")
    if text == "=":
        if ecv.get().isdigit():
            value = ecv.get()
        else:
            try:
                value = eval(ecve.get())
            except Exception as e:
                value = "Error"

        ecv.set(value)
        ecve.update()
    elif text=="<x|":
        value=ecv.get()
        l=len(value)
        value=value[:l-1]
        ecv.set(value)
        ecve.update()

    elif text == "C":
        ecv.set("")
        ecve.update()

    else:
        ecv.set(ecv.get() + text)
        ecve.update()
ar.geometry("400x600")
ar.title("Calculator-Done By VSHarshaS")
ar.minsize(width=400,height=600)
ar.maxsize(width=400,height=600)
ecv=StringVar()
ecv.set('')
ecve=Entry(ar,textvariable=ecv,font="lucida 40",bg="orange")
ecve.pack(padx=10,pady=20,ipadx=10,ipady=10)
f1=Frame(ar,bg="grey")

f=Frame(f1,bg="grey",pady=10)
b=Button(f,text="7",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>", click)
b=Button(f,text="8",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b=Button(f,text="9",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
b=Button(f,text="<x|",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)
f.pack()


f=Frame(f1,bg="grey")
b=Button(f,text="4",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="6",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="+",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()


f=Frame(f1,bg="grey")
b=Button(f,text="1",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="3",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(f1,bg="grey")
b=Button(f,text="*",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="/",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="C",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=30,pady=30,bg="black",fg="white",font="lucida 10")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f1.pack()
ar.mainloop()