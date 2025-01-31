from tkinter import *

def click(event):
    global num
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if num.get().isdigit():
            value=int(num.get())
        else:
            try:
                value=eval(front.get())

            except Exception as e:
                print(e)
                value="Error"


        num.set(value)
        front.update()
    elif text=="c":
        num.set("")
        front.update()
    else:
        num.set(num.get()+text)
        front.update()
window=Tk()
window.geometry("325x544")
window.title("Calculator Using GUI by grp 7")
num= StringVar()
num.set("")
front=Entry(window,textvar=num,font="lucida 40 bold")
front.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(window,bg="red")
b=Button(f,text="c",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=12)
b.bind("<Button-1>", click)
b=Button(f,text="()",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=12)
b.bind("<Button-1>", click)
b=Button(f,text="%",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=12)
b.bind("<Button-1>", click)
b=Button(f,text="/",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=12)
b.bind("<Button-1>", click)

f.pack()


f=Frame(window,bg="red")
b=Button(f,text="7",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="8",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="9",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="*",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=12)
b.bind("<Button-1>", click)
f.pack()


f=Frame(window,bg="red")
b=Button(f,text="4",padx=10,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="5",padx=11,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="6",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="-",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=12)
b.bind("<Button-1>", click)
f.pack()


f=Frame(window,bg="red")
b=Button(f,text="1",padx=9,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="2",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="3",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="+",padx=8,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=12)
b.bind("<Button-1>", click)
f.pack()


f=Frame(window,bg="red")
b=Button(f,text="//",padx=9,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="0",padx=9,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text=".",padx=9,pady=5,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>", click)
b=Button(f,text="=",padx=11,pady=7,font="lucida 25 bold")
b.pack(side=LEFT,padx=8,pady=12)
b.bind("<Button-1>", click)
f.pack()



window.mainloop()
print()
