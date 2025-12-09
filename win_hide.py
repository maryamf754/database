from tkinter import *
root=Tk()
root.title(" پنجره اصلی ")
root.geometry("400x500")
def open_second():
    #مخفی  کردن پنجره اصلی 
    root.withdraw()
    #ساخت پنجره دوم 
    win=Toplevel(root)
    win.title(" پنجره خوش اومدید")
    win.geometry("300x400")
    Label(win,text=" خوش امدید",font=("arial",16)).pack(pady=30)
    #دکمه بازگشت به پنجره  اصلی 
    def back_to_main():
        win.destroy()
        #بستن  پنجره دوم 
        root.deiconify()
        #نمایش دوباره پنجره اول 
        Button(win, text=" بازگشت",command=back_to_main,font=("arial",14) ).pack(pady=50)
    Button(win, text=" بازکردن پنجره خوش امد ",command=open_second,font=("arial",12) ).pack(pady=50)
    root.mainloop()