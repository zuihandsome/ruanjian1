from tkinter import *
from thread import *
import time


def update():
    while (1):
        if e1.status == 2:
            if e1.pNum != 0:
                fm13.pack(fill=BOTH)
                e1.status = 1
            else:
                fm11.pack(fill=BOTH)
                e1.status = 1
        if e2.status == 2:
            if e2.pNum != 0:
                fm23.pack(fill=BOTH)
                e2.status = 1
            else:
                fm21.pack(fill=BOTH)
                e2.status = 1
        if e3.status == 2:
            if e3.pNum != 0:
                fm33.pack(fill=BOTH)
                e3.status = 1
            else:
                fm31.pack(fill=BOTH)
                e3.status = 1
        if e4.status == 2:
            if e4.pNum != 0:
                fm43.pack(fill=BOTH)
                e4.status = 1
            else:
                fm41.pack(fill=BOTH)
                e4.status = 1
        time.sleep(2)
        canvas1.delete(ALL)
        canvas1.create_rectangle(20, -int(e1.floor) * 20 + 500, 120, -(int(e1.floor) * 20 + 20) + 500, fill='black')
        canvas1.create_rectangle(140, -int(e2.floor) * 20 + 500, 240, -(int(e2.floor) * 20 + 20) + 500, fill='black')
        canvas1.create_rectangle(260, -int(e3.floor) * 20 + 500, 360, -(int(e3.floor) * 20 + 20) + 500, fill='black')
        canvas1.create_rectangle(380, -int(e4.floor) * 20 + 500, 480, -(int(e4.floor) * 20 + 20) + 500, fill='black')


def w(num, direction):
    wList = {1: e1.weighT(num, direction), 2: e2.weighT(num, direction),
             3: e3.weighT(num, direction), 4: e4.weighT(num, direction)}
    print(wList)
    eNum = sorted(zip(wList.values(), wList.keys()))[0]
    if eNum[0] != 999:
        if eNum[1] == 1:
            e = e1
        elif eNum[1] == 2:
            e = e2
        elif eNum[1] == 3:
            e = e3
        else:
            e = e4
        e.pickUp(num,direction)
    else:
        print("暂无电梯可用，请稍后重试")


def up():
    num = I1.get()
    print(num)
    direction = 1
    w(int(num), int(direction))


def down():
    num = I1.get()
    direction = 0
    w(int(num), int(direction))


# 电梯1
def e1Leave():
    num = I16.get()
    e1.leave(int(num))
    fm13.forget()
    fm11.pack(fill=BOTH)


def e1ComeIn():
    num = I12.get()
    e1.comeIn(int(num))
    fm11.forget()
    if e1.pNum != 0:
        fm12.pack(fill=BOTH)
    else:
        e1.signal = 1


def e1Send():
    num = I14.get()
    e1.send(int(num))
    e1.signal = 1
    fm12.forget()


# 电梯2
def e2Leave():
    num = I26.get()
    e2.leave(int(num))
    fm23.forget()
    fm21.pack(fill=BOTH)


def e2ComeIn():
    num = I22.get()
    e2.comeIn(int(num))
    fm21.forget()
    if e2.pNum != 0:
        fm22.pack(fill=BOTH)
    else:
        e2.signal = 1

def e2Send():
    num = I24.get()
    e2.send(int(num))
    e2.signal = 1
    fm22.forget()


# 电梯3
def e3Leave():
    num = I36.get()
    e3.leave(int(num))
    fm33.forget()
    fm31.pack(fill=BOTH)


def e3ComeIn():
    num = I32.get()
    e3.comeIn(int(num))
    fm31.forget()
    if e3.pNum != 0:
        fm32.pack(fill=BOTH)
    else:
        e3.signal = 1

def e3Send():
    num = I34.get()
    e3.send(int(num))
    e3.signal = 1
    fm32.forget()


# 电梯4
def e4Leave():
    num = I46.get()
    e4.leave(int(num))
    fm43.forget()
    fm41.pack(fill=BOTH)


def e4ComeIn():
    num = I42.get()
    e4.comeIn(int(num))
    fm41.forget()
    if e4.pNum != 0:
        fm42.pack(fill=BOTH)
    else:
        e4.signal = 1

def e4Send():
    num = I44.get()
    e4.send(int(num))
    e4.signal = 1
    fm42.forget()

win = Tk()
win.geometry("1000x800") #设置窗口大小
win.title("电梯算法")
# Canvas
canvas1 = Canvas(win, bg='blue', height=500, width=500)
canvas1.create_rectangle(20,-int(e1.floor)*20+500,120,-(int(e1.floor)*20+20)+500,fill='black')
canvas1.create_rectangle(140,-int(e2.floor)*20+500,240,-(int(e2.floor)*20+20)+500,fill='black')
canvas1.create_rectangle(260,-int(e3.floor)*20+500,360,-(int(e3.floor)*20+20)+500,fill='black')
canvas1.create_rectangle(380,-int(e4.floor)*20+500,480,-(int(e4.floor)*20+20)+500,fill='black')
canvas1.pack(side="left")

# 总输入 楼层 上下
fm1 = Frame(win)
L1 = Label(fm1,text="请输入所在楼层")
I1 = Entry(fm1)
L2 = Label(fm1,text="请选择方向")
B1 = Button(fm1,text="↑",command=up)
B2 = Button(fm1,text="↓",command=down)
L1.pack(side=TOP,fill=Y)
I1.pack(side=TOP,fill=Y)
L2.pack(side=TOP,fill=Y)
B1.pack()
B2.pack()
fm1.pack(fill=BOTH)

# 电梯1输入进入人数
fm11 = Frame(win)
L11 = Label(fm11,text="电梯1 ：请输入进入电梯人数")
I12 = Entry(fm11)
B11 = Button(fm11, text='确认',command=e1ComeIn)
L11.pack(side=TOP,fill=Y)
I12.pack(side=TOP,fill=Y)
B11.pack(side=TOP,fill=Y)


# 电梯1选择楼层
fm12 = Frame(win)
L13 = Label(fm12,text="电梯1 ：请选择去哪楼")
I14 = Entry(fm12)
B12 = Button(fm12, text='确认',command=e1Send)
L13.pack(side=TOP,fill=Y)
I14.pack(side=TOP,fill=Y)
B12.pack(side=TOP,fill=Y)


# 电梯1输入离开人数
fm13 = Frame(win)
L15 = Label(fm13,text="电梯1 ：请输入离开电梯人数")
I16 = Entry(fm13)
B13 = Button(fm13, text='确认',command=e1Leave)
L15.pack(side=TOP,fill=Y)
I16.pack(side=TOP,fill=Y)
B13.pack(side=TOP,fill=Y)


# 电梯2输入进入人数
fm21 = Frame(win)
L21 = Label(fm21,text="电梯2 ：请输入进入电梯人数")
I22 = Entry(fm21)
B21 = Button(fm21, text='确认',command=e2ComeIn)
L21.pack(side=TOP,fill=Y)
I22.pack(side=TOP,fill=Y)
B21.pack(side=TOP,fill=Y)


# 电梯2选择楼层
fm22 = Frame(win)
L23 = Label(fm22,text="电梯2 ：请选择去哪楼")
I24 = Entry(fm22)
B22 = Button(fm22, text='确认',command=e2Send)
L23.pack(side=TOP,fill=Y)
I24.pack(side=TOP,fill=Y)
B22.pack(side=TOP,fill=Y)


# 电梯2输入离开人数
fm23 = Frame(win)
L25 = Label(fm23,text="电梯2 ：请输入离开电梯人数")
I26 = Entry(fm23)
B23 = Button(fm23, text='确认',command=e2Leave)
L25.pack(side=TOP,fill=Y)
I26.pack(side=TOP,fill=Y)
B23.pack(side=TOP,fill=Y)


# 电梯3输入进入人数
fm31 = Frame(win)
L31 = Label(fm31,text="电梯3 ：请输入进入电梯人数")
I32 = Entry(fm31)
B31 = Button(fm31, text='确认',command=e3ComeIn)
L31.pack(side=TOP,fill=Y)
I32.pack(side=TOP,fill=Y)
B31.pack(side=TOP,fill=Y)


# 电梯3选择楼层
fm32 = Frame(win)
L33 = Label(fm32,text="电梯3 ：请选择去哪楼")
I34 = Entry(fm32)
B32 = Button(fm32, text='确认',command=e3Send)
L33.pack(side=TOP,fill=Y)
I34.pack(side=TOP,fill=Y)
B32.pack(side=TOP,fill=Y)


# 电梯3输入离开人数
fm33 = Frame(win)
L35 = Label(fm33,text="电梯3 ：请输入离开电梯人数")
I36 = Entry(fm33)
B33 = Button(fm33, text='确认',command=e3Leave)
L35.pack(side=TOP,fill=Y)
I36.pack(side=TOP,fill=Y)
B33.pack(side=TOP,fill=Y)


# 电梯4输入进入人数
fm41 = Frame(win)
L41 = Label(fm41,text="电梯4 ：请输入进入电梯人数")
I42 = Entry(fm41)
B41 = Button(fm41, text='确认',command=e4ComeIn)
L41.pack(side=TOP,fill=Y)
I42.pack(side=TOP,fill=Y)
B41.pack(side=TOP,fill=Y)


# 电梯4选择楼层
fm42 = Frame(win)
L43 = Label(fm42,text="电梯4 ：请选择去哪楼")
I44 = Entry(fm42)
B42 = Button(fm42, text='确认',command=e4Send)
L43.pack(side=TOP,fill=Y)
I44.pack(side=TOP,fill=Y)
B42.pack(side=TOP,fill=Y)


# 电梯4输入进入人数
fm43 = Frame(win)
L45 = Label(fm43,text="电梯4 ：请输入离开电梯人数")
I46 = Entry(fm43)
B43 = Button(fm43, text='确认',command=e4Leave)
L45.pack(side=TOP,fill=Y)
I46.pack(side=TOP,fill=Y)
B43.pack(side=TOP,fill=Y)

t=threading.Thread(target=update)
t.start()
win.mainloop()


