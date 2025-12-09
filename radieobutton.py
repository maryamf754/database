from tkinter import *
from tkinter import messagebox
win=Tk()
win.geometry("500x500")
win.config(bg="#b8c8b8")
win.title(" گروه بندی رایودتن ها")

#........function
def show_choice():
    lb1_reuslt.config(text="you are select:"+lang.get())
    lb1_reuslt1.config(text="os :"+os_var.get())



#........fram_lang
lang=StringVar()
lang.set("python")

frame_lang=LabelFrame(win, text=" انتخاب زبان ",padx=20,pady=20)
frame_lang.pack(padx=20,pady=20,fill="both")

r1=Radiobutton(win,text=" python ",variable=lang,value=" python",anchor="sw",font="arial10")
r2=Radiobutton(frame_lang, text=" java ", variable=lang,value="java",anchor="center",font="arial10",padx=1,pady=1)
r3=Radiobutton(win,text="c++",variable=lang,value=" c++ ",anchor="ne",font="arial10")

r1.place(x=20,y=100,anchor="sw")
r2.pack(anchor="n",padx=10,pady=10)
r3.place(x=370,y=86,anchor="w")
#........frame os
os_var=StringVar()
os_var.set("x")

frame_os=LabelFrame(win,text="انتخاب سیتم عامل",padx=30,pady=30)
frame_os.pack(padx=30,pady=30,fill="both")
r4=Radiobutton(win,text=" windeows",variable=os_var,value="windows",font="arial10")
r5=Radiobutton(frame_os,text="lunx",variable=os_var,value="lunx",font="arial10")
r6=Radiobutton(win,text="mac os",variable=os_var,value="mac",font="arial10")

r4.place(x=50,y=250,anchor="sw")
r5.pack(anchor="center")
r6.place(x=340,y=240,anchor="w")
#......buttton
bt_show=Button(win,text=" show", font=" arial 20", command=show_choice,bg="#b8c8b8")
bt_show.place(x=180,y=300)

lb1_reuslt=Label(win,text=" ",font="arial 20",anchor="s",fg="#b8c8b8")
lb1_reuslt.place(x=100,y=370)

lb1_reuslt1=Label(win, text=" ",font="arial 20",anchor="s",fg="#b8c8b8")
lb1_reuslt1.place(x=100,y=420)


win.mainloop()
