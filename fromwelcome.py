from tkinter import *
root=Tk()
root.geometry('300x300')
root.config(bg="#c9b5c3")
#root.iconbitmap("home.ico")
def open_second():
    root.withdraw()
    #مخفی کردن پنجره 
    win=Toplevel(root)
    #پنجره جدید(فرزند  پنجره اصلی)  یا ساختن پنجره جدا
    win.title("new window")
    win.geometry("300x200")
    win.config(bg="#a8c8b9")
    #win.iconbitmap("accept.ico")

    #تلاش می کنه ایکون پنجره جدید  را با فایل تنظیم کنه 
    #حتما ایکون دانلود می کنیم و توی عکس  برنامه  تو فایل پروزه قرار می دهیم
    Label(win,text=" خوش امدید", font=("arial",16)).pack(pady=20)
    #دکمه بازگشت به پنجره اصلی 
    def back_to_main():
        win.destroy()
        #بستن پنجره دوم 
        root.deiconify()
        #نمایش پنجره اول 
    Button(win,text="بازگشت", command=back_to_main ,font=("arial",12)).pack()

Button(root,text="بازکردن پنجره خوش امدید", command=open_second ,font=("arial",12)).pack(pady=50)

root.mainloop()
