import random
from tkinter import *

window = Tk()
site1_var = StringVar()
n1_var = IntVar()
ans_var = IntVar()
window.geometry('500x350')


def passwordf(n, site, lnm):
    password = []
    password.insert(0, site[0].lower())
    for i in range(1, n-1):
        if i % 2 == 0:
            if i <= len(site):
                password.insert(i, site[lnm-1].upper())
                lnm -= 1
            else:
                password.insert(i, chr(random.randrange(97, 122)))
        elif i % 2 != 0 and i <= int(n/2):
            password.insert(i, chr(random.randrange(32, 47)))
        elif i % 2 != 0 and i > int(n/2):
            password.insert(i, str(random.randrange(0, 9)))
    password.append(site[len(site)-1].upper())
    return"".join(password)


def func1():
    ans1 = int(ans_var.get())
    site1 = site1_var.get()
    n1 = int(n1_var.get())
    lnm1 = len(site1)
    if ans1 == 1:
        with open("record.txt", "r") as f:
            for line in f.readlines():
                print("\n", line)
        exit()
    elif ans1 == 0:
        with open("record.txt", "a") as f:
            if ans1 == 0:
                pw = passwordf(n1, site1, lnm1)
                pw = pw.replace(" ", "@")
                f.writelines("site and new password : ")
                f.write(site1 + "  " + pw + "  ")
                f.write("\n")
        with open("record.txt", "r") as f:
            if ans1 == 0:
                for line in f.readlines():
                    print("\n", line)
        exit()


def func():
    site1 = site1_var.get()
    n1 = int(n1_var.get())
    lnm1 = len(site1)
    pw = passwordf(n1, site1, lnm1)
    pw = pw.replace(" ", "@")
    Label(window, text="password :").grid(row=2)
    Label(window, text=pw, font=("Helvetica", 16)).grid(row=2)
    with open("record.txt", "a") as f:
        f.write("site and password :")
        f.write(site1 + "  " + pw + "  ")
        f.write("\n")
    Checkbutton(window, text="accept", variable=ans_var, onvalue=1, offvalue=0).grid(row=3, column=4)
    ans = int(ans_var.get())
    submit1 = Button(window, text="CONFIRM", activebackground="#87CEEB", command=func1).grid(row=5, column=1)
    print("done!!!")


Label(window, text="site name").grid(row=0)
Label(window, text="password lenth").grid(row=1)
site1_ent = Entry(window, textvariable=site1_var).grid(row=0, column=1)
n1_ent = Entry(window, textvariable=n1_var).grid(row=1, column=1)
submit = Button(window, text="SUBMIT", activebackground="#87CEEB", command=func).grid(row=4, column=1)
window.mainloop()