from tkinter import *
from tkinter import messagebox
import random
win=Tk()
win.geometry("500x500")
win.title(" بازی رنگ")
win.config(bg="#c8b8b8")
win.resizable(0,0)
color=['blue','green','white','yellow','red','orange','brown']
score=0
timeleft=60

#....funtion
def startgame(event):
            if timeleft==60:
                  countdown() 
            nextcolor()

def nextcolor():
      global score
      global timeleft
      if timeleft>0:
            e.focus_set()
            if e.get().lower()==color[1].lower():
              score +=1
            e.delete(0,END)
            random.shuffle(color)
            lb2.config(fg=str(color[1]),text=str(color[0]))
            score_lb2.config(text=" امتیاز "+str(score), font=" arial 12 bold")
def countdown():
      global timeleft
      if timeleft>0:
        timeleft -=1
        time_lb1.config(text=str(timeleft),font="arial 12")
        time_lb1.after(1000,countdown)
    
      
      
            

#label
lb1=Label(win,text=" رنگ هرکلمه را با انگلیسی وارد کنید",font="arial 18")
lb1.place(x=70,y=50)

score_lb1=Label(win, text="  enter شروع" ,font="arial 18")
score_lb1.place(x=150,y=100)


score_lb2=Label(win, text=" " ,font="arial 18")
score_lb2.place(x=50,y=300)

time_lb1=Label(win, text=str(timeleft),font="arial 12")
time_lb1.place(x=350,y=300)
lb2=Label(win ,font=('comice ms',30))
lb2.place(x=150,y=220)
#enble
e=Entry(win, width=30)
e.place(x=150,y=300)
win.bind('<Return>',startgame)
e.focus_set()


win.mainloop()