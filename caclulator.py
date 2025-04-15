from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())


            scvalue.set(value)
            screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else: 
        scvalue.set(scvalue.get()+ text)
        screen.update()

root = Tk()
root.geometry("350x500")
root.title("CALCULATOR BY PHANTOM")
root.resizable(False,False)
root.configure(bg="black")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font= "lucida 40 bold")
screen.pack(fill = X, ipadx=8,padx = 10,pady=10)



f = Frame(root, bg= "black")

b = Button(f, text= "9", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "8", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "7", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "+", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

f.pack()



f = Frame(root, bg= "black")

b = Button(f, text= "6", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "5", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "4", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "-", font = "pasti 36 bold")
b.pack(side=LEFT,ipadx=1)
b.bind("<Button-1>", click)
b.configure(bg="grey")

f.pack()



f = Frame(root, bg= "black")

b = Button(f, text= "3", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "2", font = "pasti 36 bold")
b.pack(side=LEFT, ipadx=1)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "1", font = "pasti 36 bold")
b.pack(side=LEFT, ipadx=5,)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "*", font = "pasti 36 bold")
b.pack(side=LEFT, ipadx=3)
b.bind("<Button-1>", click)
b.configure(bg="grey")

f.pack()



f = Frame(root, bg= "black")

b = Button(f, text= "c", font = "pasti 36 ")
b.pack(side=LEFT, ipadx=1)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "0", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "=", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

b = Button(f, text= "/", font = "pasti 36 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b.configure(bg="grey")

f.pack()




root.mainloop()