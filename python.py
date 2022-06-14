from cProfile import label
from pydoc import classname
from tkinter import*
from turtle import title
from PIL import ImageTk
from django.shortcuts import redirect
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root= root
        self.root.title ("Login System")
        self.root.geometry("1199x600+100+75")
        self.root.resizable(False, False)


        # Frame_login= Frame(self.root, bg="lightyellow")
        # Frame_login.place(x=330, y=150, width=500, height=400)
    #background  image
        self.bg = ImageTk.PhotoImage(file="images/bg.jpg")
        self.bg_Image=Label(self.root, image=self.bg).place(x=0 ,y=0, relwidth=1, relheight=1)

    # Login Frame
        Frame_login= Frame(self.root, bg = "white" )
        Frame_login.place(x=330, y=150, width=500, height=400)


    # title & subtitle
        title=Label(Frame_login, text="Login Here",font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90, y=30)
        subtitle=Label(Frame_login, text="Members Login Area",font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90, y=100)

    # username

        lbl_user =Label(Frame_login, text="UserName", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(x=90, y=140)
        self.username =Entry(Frame_login, font=("Goudy old style", 15),  bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)

    #Password

        lbl_passwod =Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(x=90, y=210)
        self.password =Entry(Frame_login, font=("Goudy old style", 15),  bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

    # #Confrom Password

    #     lab_confrompassword =Label(Frame_login, text="Confrom Password", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(x=90, y=280)
    #     self.confrompassword =Entry(Frame_login, font=("Goudy old style", 15),  bg="#E7E6E6")
    #     self.confrompassword.place(x=90, y=310, width=320, height=35)
    #Button
        forget =Button(Frame_login, text="Forget Password?",bd=0,cursor="hand2", font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=90, y=280)
        Submit =Button(Frame_login, command=self.check_funcation, cursor="hand2", text="Login?", font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=320, width=140, height=40)

    def check_funcation(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All Fildes Are Required", parent=self.root)

        elif self.username.get()!="Chbabulal" or self.password.get()!="8886576149":
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Wlcome {self.username.get()}")



root = Tk()
obj=Login(root)
root.mainloop()