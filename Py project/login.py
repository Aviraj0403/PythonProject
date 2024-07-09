from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from home import hotelmanagementsystem
import cx_Oracle


def main():
    win=Tk()
    app=login_win(win)
    win.mainloop()
    
class login_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #**********background image*****
        img1=Image.open("frame.jpg")
        img1=img1.resize((1550,800),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labl=Label(self.root,image=self.photoimg1)
        labl.place(x=0,y=0,relwidth=1,relheight=1)

        #frame
        frame=Frame(self.root,bg="skyblue")
        frame.place(x=610,y=170,width=340,height=450)

        #frame logo image
        img2=Image.open("login_logo.jpg")
        img2=img2.resize((100,100),Image.BICUBIC)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl=Label(image=self.photoimg2,bg="skyblue",borderwidth=0)
        lbl.place(x=730,y=175,width=100,height=100)

        lbl=Label(frame,text="Hotel Management System",bg="skyblue",fg="Black",font=("times new roman",20,"bold"))
        lbl.place(x=20,y=100)
        
     
    
      #starting entry fill
        #username
        userlabel=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        userlabel.place(x=60,y=155)

        self.textuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textuser.place(x=40,y=180,width=270)
        
        '''
        #PASSWORD PHOTO
        img4=Image.open("images2.png")
        img4=img4.resize((30,30),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbl=Label(frame,image=self.photoimg4,bg="black",borderwidth=0)
        lbl.place(x=2,y=36,relx=0.1,rely=0.42)

        self.ep=StringVar()
'''
        #password
        userpass=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        userpass.place(x=60,y=225)

        self.textpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.textpass.place(x=40,y=250,width=270)

        #login button
        loginbutton=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbutton.place(x=110,y=300,width=120,height=35)

       #new user
        loginnew=Button(frame,text="New user Register",command=self.new_register,font=("times new roman",15,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="skyblue",activeforeground="white",activebackground="black")
        loginnew.place(x=13,y=350,width=160)

         #forget  passowrd
        loginforget=Button(frame,text="Forget password",command=self.forget_password,font=("times new roman",15,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="skyblue",activeforeground="white",activebackground="black")
        loginforget.place(x=5,y=380,width=160)
    
    
    #****NEW REGISTER
    def new_register(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
           
             messagebox.showerror("error","all field are required")
               
             self.user.set("")              
             self.password.set("")
               
               
        elif self.textuser.get()=="avi" and self.textpass.get()=="avi@123":
            
                messagebox.showinfo("success","successfully login")
                self.avi=hotelmanagementsystem(self.root)
        elif self.textuser.get()=="hritik" and self.textpass.get()=="hritik@123":
            
                messagebox.showinfo("success","successfully login")
                self.hritik=hotelmanagementsystem(self.root)
        else:
                con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
                my_cursor=con.cursor()
                query = "SELECT email, password FROM register WHERE email = :email"
                my_cursor.execute(query, {'email': self.textuser.get()})
                result = my_cursor.fetchone()

            # check if the email exists and the password matches
                if result and result[1] == self.textpass.get():
            # login successful
                    messagebox.showinfo("success","succesfully")
                    self.avi=hotelmanagementsystem(self.root)
                else:
             # login failed
                   messagebox.showerror("error","invalid user or password")
                   self.user.set("")              
                   self.password.set("")
               

    #---------reset password
    def reset_pass(self):
        if self.combo_security_Q.get()=="select":
            messagebox.showerror("error","select the secuirty question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("error","please enter the answer",parent=self.root2) 
        elif self.txt_new_pass.get()=="":
            messagebox.showerror("erorr","please enter the new passwod",parent=self.root2)
        else:
            con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
            my_cursor=con.cursor() 
            query="select * from register where email=:email and security_Q=:security_Q and security_A=:security_A "
            value=(self.textuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value) 

            row=my_cursor.fetchone() 
            if row==None:
                messagebox.showerror("error","please enter the correct answer",parent=self.root2) 
            else:
                query="update register set password=:password where email=:email" 
                value=(self.txt_new_pass.get(),self.textuser.get())  
                my_cursor.execute(query,value) 
                con.commit() 
                con.close()
                messagebox.showinfo("info","your password has been reset,please log in new password")      

  
    def forget_password(self):
        if self.textuser.get()=="":
            messagebox.showerror("error","please enter the email to reset password")
        else:
            con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
            my_cursor=con.cursor()
            query = "SELECT * FROM register WHERE email = :email" 
            value=(self.textuser.get(),)
            my_cursor.execute(query,value) 
            row=my_cursor.fetchone() 
            # print(row)   
            if row==None:
                messagebox.showerror("error","please enter the valid user name") 
            else:
                con.close()
                self.root2=Toplevel()
                self.root2.title("forget password")  
                self.root2.geometry("340x450+610+170") 

                l=Label(self.root2,text="Forget Password",font=("times new roman",10,"bold"),fg="red",bg="white") 
                l.place(x=0,y=10,relwidth=1)  

                #***secirity question**

                lbl_scqest=Label(self.root2,text="Select Security Questions",bg="white",font=("times new roman",15,"bold"))
                lbl_scqest.place(x=50,y=80)

                # self.var_combo_security=StringVar()
                # self.var_txt_security=StringVar()

                self.combo_security_Q=ttk.Combobox(self.root2,font=("arial",12,"bold"),state="readonly")
                self.combo_security_Q["value"]=("select","DOB","favourite Game","Nick name")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=250)



                lbl_secuirity=Label(self.root2,text="Security Answer",bg="white",font=("times new roman",15,"bold"))
                lbl_secuirity.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)  


                
                new_password=Label(self.root2,text="New password",bg="white",font=("times new roman",15,"bold"))
                new_password.place(x=50,y=220)

                self.txt_new_pass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_pass.place(x=50,y=250,width=250)  

                
                btnreset=Button(self.root2,text="RESET",command=self.reset_pass,font=("arial",11,"bold"),bg="green",fg="white")
                btnreset.place(x=100,y=290)
              


# ************************ register*****************
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("register")
        self.root.geometry("1600x900+0+0")

        #*** variable***
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_A=StringVar()
        self.var_pass=StringVar()
        self.var_confirm_pass=StringVar()
        self.var_check=IntVar()


        #background image

        img1=Image.open("frame.jpg")
        img1=img1.resize((1590,850),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        

        bg_label=Label(self.root,image=self.photoimg1)
        bg_label.place(x=0,y=0,relheight=1,relwidth=1)

        #left image
        img2=Image.open("eat2.jpg")
        img2=img2.resize((800,600),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        

        img2_label=Label(self.root,image=self.photoimg2)
        img2_label.place(x=50,y=100,height=550,width=470)

        #***frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        lbl_register=Label(frame,text="REGISTER HERE",bg="white",fg="darkgreen",font=("times new roman",20,"bold"))
        lbl_register.place(x=20,y=20)

        #***label for fname
        lbl_fname=Label(frame,text="First Name",bg="white",font=("times new roman",15,"bold"))
        lbl_fname.place(x=50,y=100)

        self.fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname.place(x=50,y=130,width=250)

        #**label entry lname***
        lbl_lname=Label(frame,text="Last Name",bg="white",font=("times new roman",15,"bold"))
        lbl_lname.place(x=370,y=100)

        self.lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname.place(x=370,y=130,width=250)

        #***lbl and entry for contact**
        lbl_contact=Label(frame,text="Contact No",bg="white",font=("times new roman",15,"bold"))
        lbl_contact.place(x=50,y=170)

        self.contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact.place(x=50,y=200,width=250)

        #*** lbl and entry of email**
        lbl_email=Label(frame,text="Email",bg="white",font=("times new roman",15,"bold"))
        lbl_email.place(x=370,y=170)

        self.email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email.place(x=370,y=200,width=250)

        #***secirity question**

        lbl_scqest=Label(frame,text="Select Security Questions",bg="white",font=("times new roman",15,"bold"))
        lbl_scqest.place(x=50,y=240)

        combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("arial",12,"bold"),state="readonly")
        combo_security_Q["value"]=("select","DOB","Nickname","Favourite Game")
        combo_security_Q.current(0)
        combo_security_Q.place(x=50,y=270,width=250)



        lbl_secuirity=Label(frame,text="Security Answer",bg="white",font=("times new roman",15,"bold"))
        lbl_secuirity.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        #***passwordr
        lbl_pass=Label(frame,text="Password",bg="white",font=("times new roman",15,"bold"))
        lbl_pass.place(x=50,y=310)

        self.password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.password.place(x=50,y=340,width=250)

        lbl_confirm=Label(frame,text="confirm Password",bg="white",font=("times new roman",15,"bold"))
        lbl_confirm.place(x=370,y=310)

        self.confirm=ttk.Entry(frame,textvariable=self.var_confirm_pass,font=("times new roman",15,"bold"))
        self.confirm.place(x=370,y=340,width=250)

        #***checkbutton**
        chechbtn=Checkbutton(frame,variable=self.var_check,text="I agree The Terms & Condition",font=("times new roman",15,"bold"),bg="white",onvalue=1,offvalue=0)
        chechbtn.place(x=50,y=380)
        

        #****buttons**
     
       
      

        #*** login now button**
        img4=Image.open("loginnow.jpg")
        img4=img4.resize((200,100),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)  
        b2=Button(frame,command=self.return_login,image=self.photoimg4,borderwidth=0,cursor="hand2",bg="white")
        b2.place(x=330,y=470,width=200)



# """        #***function declarion
    def register_data(self):
        
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="select":
            messagebox.showerror("error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confirm_pass.get():
            messagebox.showerror("error","password & confirm password must be same",parent=self.root)  
        elif self.var_check.get()==0:
            messagebox.showerror("error","Please agrre terms and conditions",parent=self.root) 
        else:
            fname=self.var_fname.get()
            lname=self.var_lname.get()
            contact=self.var_contact.get()
            email=self.var_email.get()
            security_Q=self.var_security_Q.get()
            security_A=self.var_security_A.get()
            password=self.var_pass.get()
            
            con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
            my_cursor=con.cursor()
            # create an INSERT statement
            insert_statement = "INSERT INTO Register (fname, lname, contact,email,security_Q,security_A,password) VALUES (:fname,:lname,:contact,:email,:security_Q,:security_A,:password)"

            # execute the INSERT statement
            my_cursor.execute(insert_statement, {'fname':fname, 'lname': lname, 'contact': contact,'email': email,'security_Q':security_Q,'security_A': security_A,'password': password})

            con.commit() 
            
            my_cursor.close()
            con.close()
            messagebox.showinfo("success","register succesfully") 

    def return_login(self):
        self.root.destroy()  

   

if __name__=="__main__":
   main()

