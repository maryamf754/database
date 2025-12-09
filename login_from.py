from tkinter import *
from tkinter import messagebox
import mymodule
win=Tk()
win.geometry("500x500")
win.title("login_local")
win.config(bg="#b7b6c5")

db=mymodule.Database('h:/m/mydata1.db')
win.iconbitmap("h:/m/accept.ico")
#clear
def clear():
     fname=ent_fname.delete(0,END)
     lname=ent_lname.delete(0,END)
     email=ent_email.delete(0,END)
     password=ent_pass.delete(0,END)
     ent_fname.focus_set()
#insert 
def insert():
      fname=ent_fname.get()
      lname=ent_lname.get()
      email=ent_email.get()
      password=ent_pass.get()
      if email=="" or password=="":
            messagebox.showerror("error"," email , password not empty!")
            return
      db.insert_record(fname,lname,email,password)
      ruslt=messagebox.showinfo("insert"," record sabt shad")
      clear()
      ####search
def search(self,email,password):
      search=ent_search.get()
      email=ent_email.get()
      password=ent_pass.get()
      record=db.search_record(search)
      if email=="" or password=="":
            messagebox.showinfo("welcome"f'{email}')
      else:

       messagebox.showinfo("login eror"," place ")
      clear()
      
#
def back_to_main():
        root.destroy()
        win.deiconify()
    
#رفتن به یک فرم دیگه
def open_second():
    global root
    win.withdraw()
    root=Toplevel(win)
    root.geometry("500x300")
    root.title("from 2")
    root.config(bg="#b8c9a7")
    root.iconbitmap("h:/m/home.ico")
    Label(root,text=" فرم دوم ", font=("arial",16)).pack(pady=20)
    Button(root,text="بازگشت", command=back_to_main ,font=("arial",12)).pack()

#Button(win,text=" ورود به فرم دوم ",command=open_second,font=("arial",12)).pack(pady=10)
#lable
lb1_fname=Label(win,text=" fname : ", font=" arial 15")
lb1_fname.place(x=60,y=60)

lb1_lname=Label(win,text=" lname : ", font=" arial 15")
lb1_lname.place(x=60,y=120)

lb1_Email=Label(win,text="  Email : ", font=" arial 15")
lb1_Email.place(x=60,y=180)

lb1_e=Label(win,text="*", font=" arial 15")
lb1_e.place(x=40,y=180)

lb1_Password=Label(win,text="pasword:", font=" arial 15")
lb1_Password.place(x=60,y=240)

lb1_p=Label(win,text="*", font=" arial 15")
lb1_p.place(x=40,y=240)

lb1_search=Label(win,text="search", font=" arial 15")
lb1_search.place(x=60,y=300)
#entry
ent_fname=Entry(win,font="arial 14")
ent_fname.place(x=150,y=60)

ent_lname=Entry(win,font="arial 14")
ent_lname.place(x=150,y=120)

ent_email=Entry(win,font="arial 14")
ent_email.place(x=150,y=180)

ent_pass=Entry(win,font="arial 14",show="*")
ent_pass.place(x=150,y=240)
ent_search=Entry(win,font="arial 14")
ent_search.place(x=150,y=300)
#button
btn_sigin=Button(win,text=" sign in ", font="arial 18",command=open_second)
btn_sigin.place(x=220,y=390)
btn_sigup=Button(win,text=" sign up", font="arial 18",command=insert)
btn_sigup.place(x=80,y=390)
btn_search=Button(win,text=" search", font="arial 18",command=search)
btn_search.place(x=340,y=390)
win.mainloop()