from tkinter import *
val = []

def histry():
    with open(r"C:\Users\anilv\PycharmProjects\all projects\his.txt", "r+") as f1:
        line=f1.readlines()
        for line in line[::-1]:
            print(line)

def remove():
    val.pop()


def insert(a):
    val.append(a)


def final():
    fval = "".join(val)
    print(fval, end=" ")
    print(eval(fval))
    ans = eval(fval)
    with open("his.txt", "a") as f1:
        fval = "".join(val)
        f1.write(fval + " = " + str(ans) + "\n")


window = Tk()
window.geometry('900x550')
window.title("   CALCULATOR   ")
frame1 = Frame(window, bd=10).grid(padx=45, pady=35)
inpt = Entry(window,width=50, bg="#87CEEB")
inpt.place(x=0,y=90)
b1 = Button(frame1, text="1", font=("Helvetica", 16, "bold"), padx=14, command=lambda: insert("1")).grid(row=1, column=1, sticky=W)
b2 = Button(frame1, text="2", font=("Helvetica", 16, "bold"), padx=14, command=lambda: insert("2")).grid(row=1, column=2, sticky=W)
b3 = Button(frame1, text="3", font=("Helvetica", 16, "bold"), padx=22, command=lambda: insert("3")).grid(row=1, column=3, sticky=W)
b4 = Button(frame1, text="4", font=("Helvetica", 16, "bold"), padx=14, command=lambda: insert("4")).grid(row=2, column=1, sticky=W)
b5 = Button(frame1, text="5", font=("Helvetica", 16, "bold"), padx=14, command=lambda: insert("5")).grid(row=2, column=2, sticky=W)
b6 = Button(frame1, text="6", font=("Helvetica", 16, "bold"), padx=22, command=lambda: insert("6")).grid(row=2, column=3, sticky=W)
b7 = Button(frame1, text="7", font=("Helvetica", 16, "bold"), padx=14, command=lambda: insert("7")).grid(row=3, column=1, sticky=W)
b8 = Button(frame1, text="8", font=("Helvetica", 16, "bold"), padx=14, command=lambda: insert("8")).grid(row=3, column=2, sticky=W)
b9 = Button(frame1, text="9", font=("Helvetica", 16, "bold"), padx=22, command=lambda: insert("9")).grid(row=3, column=3, sticky=W)
b0 = Button(frame1, text="0", font=("Helvetica", 16, "bold"), padx=14, command=lambda: insert("0")).grid(row=4, column=1, sticky=W)
plus = Button(frame1, text="+", font=("Helvetica", 16, "bold"), padx=15, command=lambda: insert('+')).grid(row=1, column=5, sticky=W)
minus = Button(frame1, text="-", font=("Helvetica", 16, "bold"), padx=17.5, command=lambda: insert('-')).grid(row=2, column=5, sticky=W)
div = Button(frame1, text="/", font=("Helvetica", 16, "bold"), padx=18, command=lambda: insert('/')).grid(row=3, column=5, sticky=W)
multi = Button(frame1, text="*", font=("Helvetica", 16, "bold"), padx=17, command=lambda: insert('*')).grid(row=4, column=5, sticky=W)
mod = Button(frame1, text="%", font=("Helvetica", 16, "bold"), padx=37, command=lambda: insert('%')).grid(row=1, column=6, sticky=W)
equal = Button(frame1, text="=", font=("Helvetica", 16, "bold"), padx=40, command=final).grid(row=2, column=6, sticky=W)
sq = Button(frame1, text="x2", font=("Helvetica", 16, "bold"), padx=8, command=lambda: insert('**')).grid(row=4, column=2, sticky=W)
sq = Button(frame1, text="sqrt", font=("Helvetica", 16, "bold"), padx=8, command=lambda: insert('**(1/2)')).grid(row=4, column=3, sticky=W)
c = Button(frame1, text="C", font=("Helvetica", 16, "bold"), padx=38, command=remove).grid(row=3, column=6, sticky=W)
history = Button(frame1, text="HISTORY", font=("Helvetica", 16, "bold"), command=histry).grid(row=4, column=6, sticky=W)

cnt = 0
with open(r"C:\Users\anilv\PycharmProjects\all projects\his.txt", "r") as f:
    for line in f.readlines():
        cnt += 1
    p = f.readline(cnt-1)
    print(p)
inpt.grid(row=0, column=2, sticky=W)
inpt.insert(0, p)
inpt.delete(0, "end")
window.mainloop()