from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry("600x650")
root.title("Game")
root.configure(bg="skyblue")
#root.resizable(False, False)
ls = []
cl = []
wk = []
hs1 = []
hs2 = []
hs3 = []
hs4 = []
hs5 = []
hs6 = []
val = IntVar()
ad = StringVar()
v = 5


def apl():
    global v
    clo = val.get()
    if clo in (5, 10, 15, 20, 25, 30):
        v = clo
    else:
        v = 5
        by.current(0)


def hsc():
    h = 0
    if v == 5:
        for sr in hs1:
            if sr > h:
                h = sr
        sbx.delete(0, 'end')
        sbx.insert('end', h)
        sby.delete(0, 'end')
        sby.insert('end', 5)
    if v == 10:
        for sr in hs2:
            if sr > h:
                h = sr
        sbx.delete(0, 'end')
        sbx.insert('end', h)
        sby.delete(0, 'end')
        sby.insert('end', 10)
    if v == 15:
        for sr in hs3:
            if sr > h:
                h = sr
        sbx.delete(0, 'end')
        sbx.insert('end', h)
        sby.delete(0, 'end')
        sby.insert('end', 15)
    if v == 20:
        for sr in hs4:
            if sr > h:
                h = sr
        sbx.delete(0, 'end')
        sbx.insert('end', h)
        sby.delete(0, 'end')
        sby.insert('end', 20)
    if v == 25:
        for sr in hs5:
            if sr > h:
                h = sr
        sbx.delete(0, 'end')
        sbx.insert('end', h)
        sby.delete(0, 'end')
        sby.insert('end', 25)
    if v == 30:
        for sr in hs6:
            if sr > h:
                h = sr
        sbx.delete(0, 'end')
        sbx.insert('end', h)
        sby.delete(0, 'end')
        sby.insert('end', 30)


def spkf():
    au = ad.get()
    if au == "Male" or au == "Female":
        if au == 'Male':
            spkmale('You selected male voice')
        else:
            speak('You selected female voice')
    else:
        suo.current(0)
        speak('Select in the two options that are provided')


def spkm(audio):
    au = ad.get()
    if au == "Male" or au == "Female":
        if au == "Male":
            spkmale(audio)
        else:
            speak(audio)
    else:
        return


def speak(audio):
    import pyttsx3
    eng = pyttsx3.init()
    sound = eng.getProperty("voices")
    eng.setProperty("voice", sound[1].id)
    eng.say(audio)
    eng.runAndWait()


def spkmale(audio):
    import pyttsx3
    eng = pyttsx3.init()
    eng.say(audio)
    eng.runAndWait()


def sd():
    fp['state'] = NORMAL
    global s
    wk.append(0)
    s = len(wk)
    if s > v:
        score1 = 0
        for i in ls:
            score1 = score1 + i
        lr.delete(0, 'end')
        lr.insert('end', score1)
        score2 = 0
        for i in cl:
            score2 = score2 + i
        sr.delete(0, 'end')
        sr.insert('end', score2)
        if score1 > score2:
            cls('green', 'You Win')
            spkm('Impressively You win')
        elif score1 == score2:
            cls('yellow', 'Match Tied')
            spkm('Ohh The match is tied')
        else:
            cls('red', 'You Lose')
            spkm('I am Sorry You lose')
        wk.clear()
        if v == 5:
            hs1.append(score1)
        if v == 10:
            hs2.append(score1)
        if v == 15:
            hs3.append(score1)
        if v == 20:
            hs4.append(score1)
        if v == 25:
            hs5.append(score1)
        if v == 30:
            hs6.append(score1)
        hsc()
    else:
        ok()


def ok():
    global o, render, load, z, wn
    st.destroy()
    wn = Label(p, font=15, fg='white', width=8)
    wn.grid(row=0, column=2, padx=65)
    o = ["stone.png", "paper.png", "Scissors.png"]
    z = random.choice(o)
    load = Image.open(z)
    render = ImageTk.PhotoImage(load)
    mn = Label(f, image=render)
    mn.grid(row=0, column=0)
    try:
        sp.destroy()
    except:
        return


def tie():
    ls.append(1)
    cl.append(1)
    wn.config(bg='yellow', text="Tie", fg='black')


def los():
    ls.append(0)
    cl.append(2)
    wn.config(bg='red', text="Lose")


def wiin():
    ls.append(2)
    cl.append(0)
    wn.config(bg='green', text="Win")


def ch1():
    if s > v:
        return
    else:
        if z == "stone.png":
            tie()
        if z == "paper.png":
            los()
        if z == "Scissors.png":
            wiin()
        scr()


def ch2():
    if s > v:
        return
    else:
        if z == "stone.png":
            wiin()
        if z == "paper.png":
            tie()
        if z == "Scissors.png":
            los()
        scr()


def ch3():
    if s > v:
        return
    else:
        if z == "stone.png":
            los()
        if z == "paper.png":
            wiin()
        if z == "Scissors.png":
            tie()
        scr()


def scr():
    score1 = 0
    for i in ls:
        score1 = score1 + i
    lr.delete(0, 'end')
    lr.insert('end', score1)
    score2 = 0
    for i in cl:
        score2 = score2 + i
    sr.delete(0, 'end')
    sr.insert('end', score2)


def nml():
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL


def xml():
    global sp
    sp = Label(p, bg="blue", text="Start The Game", font=15, fg='white', width=20)
    sp.grid(row=0, column=2)
    mn = Label(f, text="Select an Option", width=25, height=12)
    mn.grid(row=0, column=0)
    ls.clear()
    cl.clear()
    wk.clear()
    sr.delete(0, 'end')
    lr.delete(0, 'end')
    nml()


def nrml():
    win.destroy()
    fp['state'] = NORMAL


def ext():
    ans = messagebox.askquestion('Confirm Exit', 'Do you want to exit Game?')
    if ans == 'yes':
        root.destroy()
    else:
        fp['state'] = NORMAL


def cls(i, j):
    global win
    win = Toplevel()
    win.geometry("200x150")
    win.resizable(False, False)
    win.configure(bg=i)
    lb = Label(win, text=j)
    lb.pack(pady=10)
    lf = Label(win, text="Do you want to replay or exit")
    lf.pack()
    lfc = Frame(win, bg=i)
    lfc.pack(pady=10)
    r = Button(lfc, text="Replay", command=lambda: [xml(), win.destroy()])
    r.grid(row=2, column=1, padx=5)
    e = Button(lfc, text="Exit", command=ext)
    e.grid(row=2, column=2)
    et = Button(lfc, text='Close', command=nrml)
    et.grid(row=3, columnspan=3, pady=10)
    b1['state'] = DISABLED
    b2['state'] = DISABLED
    b3['state'] = DISABLED
    fp['state'] = DISABLED
    win.protocol("WM_DELETE_WINDOW", ext)


col = StringVar()


def app():
    c = col.get()
    try:
        root.config(bg=c)
        so.config(bg=c)
        p1.config(bg=c)
        fd.config(bg=c)
        bf.config(bg=c)
        ss.config(bg=c)
    except:
        bx.current(0)
        root.config(bg='skyblue')
        so.config(bg='skyblue')
        p1.config(bg='skyblue')
        fd.config(bg='skyblue')
        bf.config(bg='skyblue')
        ss.config(bg='skyblue')
        return


def srsn():
    srs['state'] = NORMAL
    srw.destroy()


def scrs():
    global srw
    c = col.get()
    srw = Toplevel()
    srw.title("Scores")
    srw.geometry("200x250")
    srw.configure(bg=c)
    srw.resizable(False, False)
    score = Frame(srw, bg=c)
    score.pack()
    lb1 = Label(score, text="In 5 Selections", width=12)
    lb1.grid(row=0, column=0, pady=10, padx=20)
    sc1 = Listbox(score, height=1, width=5, justify=CENTER)
    sc1.grid(row=0, column=1)
    lb2 = Label(score, text="In 10 Selections", width=12)
    lb2.grid(row=1, column=0)
    sc2 = Listbox(score, height=1, width=5, justify=CENTER)
    sc2.grid(row=1, column=1)
    lb3 = Label(score, text="In 15 Selections", width=12)
    lb3.grid(row=2, column=0, pady=10)
    sc3 = Listbox(score, height=1, width=5, justify=CENTER)
    sc3.grid(row=2, column=1)
    lb4 = Label(score, text="In 20 Selections", width=12)
    lb4.grid(row=3, column=0)
    sc4 = Listbox(score, height=1, width=5, justify=CENTER)
    sc4.grid(row=3, column=1)
    lb5 = Label(score, text="In 25 Selections", width=12)
    lb5.grid(row=4, column=0, pady=10)
    sc5 = Listbox(score, height=1, width=5, justify=CENTER)
    sc5.grid(row=4, column=1)
    lb6 = Label(score, text="In 30 Selections", width=12)
    lb6.grid(row=5, column=0)
    sc6 = Listbox(score, height=1, width=5, justify=CENTER)
    sc6.grid(row=5, column=1)
    okb = Button(srw, text="Ok", command=srsn)
    okb.pack(pady=20)
    srw.protocol("WM_DELETE_WINDOW", srsn)
    s1 = 0
    for h1 in hs1:
        if h1 > s1:
            s1 = h1
    sc1.insert('end', s1)
    s2 = 0
    for h2 in hs2:
        if h2 > s2:
            s2 = h2
    sc2.insert('end', s2)
    s3 = 0
    for h3 in hs3:
        if h3 > s3:
            s3 = h3
    sc3.insert('end', s3)
    s4 = 0
    for h4 in hs4:
        if h4 > s4:
            s4 = h4
    sc4.insert('end', s4)
    s5 = 0
    for h5 in hs5:
        if h5 > s5:
            s5 = h5
    sc5.insert('end', s5)
    s6 = 0
    for h6 in hs6:
        if h6 > s6:
            s6 = h6
    sc6.insert('end', s6)


x = 163
y = 163
p = Frame(root)
p.pack()
sc = Label(p, text="Computer Score", width=13, font=10)
sc.grid(row=0, column=0)
sr = Listbox(p, justify='center', height=1, width=3, font=1)
sr.grid(row=0, column=1)
lc = Label(p, text="Your Score", width=13, font=10)
lc.grid(row=0, column=3)
lr = Listbox(p, justify='center', height=1, width=3, font=1)
lr.grid(row=0, column=4)
st = Label(p, bg="blue", text="Start The Game", font=15, fg='white', width=20)
st.grid(row=0, column=2)
so = Frame(root, bg='skyblue')
so.pack()
cs = Label(so, text="Select Color:")
cs.grid(row=0, column=0)
bx = ttk.Combobox(so,
                  values=("skyblue", 'pink', "green", "red", "blue", "yellow", "orange", 'indigo', 'violet', 'grey'),
                  textvariable=col)
bx.current(0)
bx.grid(row=0, column=1, padx=10, pady=10)
co = Button(so, text="OK", command=app)
co.grid(row=0, column=2)
cp = Label(so, text="No of Selections:")
cp.grid(row=0, column=3, padx=10)
by = ttk.Combobox(so, values=('5', '10', '15', '20', '25', '30'), textvariable=val)
by.current(0)
by.grid(row=0, column=4, pady=10)
pc = Button(so, text="OK", command=apl)
pc.grid(row=0, column=5, padx=10)
f = Frame(root)
f.pack(pady=20, padx=15)
mn = Label(f, text="Select an Option", width=25, height=12)
mn.grid(row=0, column=0)
l1 = Image.open('stone.png')
r1 = ImageTk.PhotoImage(l1)
l2 = Image.open('paper.png')
r2 = ImageTk.PhotoImage(l2)
l3 = Image.open('Scissors.png')
r3 = ImageTk.PhotoImage(l3)
p1 = Frame(root, bg="skyblue")
p1.pack()
b1 = Button(p1, image=r1, width=x, height=y, command=lambda: [sd(), ch1()])
b2 = Button(p1, image=r2, width=x, height=y, command=lambda: [sd(), ch2()])
b3 = Button(p1, image=r3, width=x, height=y, command=lambda: [sd(), ch3()])
b1.grid(row=0, column=0, padx=10)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2, padx=10)
fd = Frame(root, bg='skyblue')
fd.pack(pady=10)


def blk():
    fp['state'] = DISABLED


def srsd():
    srs['state'] = DISABLED


fp = Button(fd, text="Replay", command=lambda: [xml(), blk()])
fp.grid(row=0, column=1, padx=10)
fs = Button(fd, text='Exit', command=ext)
fs.grid(row=0, column=2)
srs = Button(root, text="Scores", width=10, font=1, command=lambda: [scrs(), srsd()])
srs.pack(padx=10)
bf = Frame(root, bg="skyblue")
bf.pack(side=BOTTOM, pady=20)
ss = Frame(bf, bg="skyblue")
ss.grid(row=0, column=0, padx=10)
su = Label(ss, text="Select Sound:")
su.grid(row=0, column=0)
suo = ttk.Combobox(ss, values=("Male", "Female"), textvariable=ad)
suo.current(0)
suo.grid(row=0, column=1)
sub = Button(ss, text="Ok", command=spkf)
sub.grid(row=0, column=2, padx=10)
ho = Frame(bf)
ho.grid(row=0, column=1, padx=10)
h = Label(ho, text="High Score:")
h.grid(row=0, column=0)
sbx = Listbox(ho, justify=CENTER, font=1, width=5, height=1)
sbx.grid(row=0, column=1)
hi = Label(ho, text='In selections:')
hi.grid(row=0, column=2)
sby = Listbox(ho, justify=CENTER, font=1, width=5, height=1)
sby.grid(row=0, column=3)
root.protocol("WM_DELETE_WINDOW", ext)
root.mainloop()
