from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cx_Oracle
   
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
            insert_statement = "INSERT INTO register (fname, lname, contact,email,security_Q,security_A,password) VALUES (:fname,:lname,:contact,:email,:security_Q,:security_A,:password)"

            # execute the INSERT statement
            my_cursor.execute(insert_statement, {'fname':fname, 'lname': lname, 'contact': contact,'email': email,'security_Q':security_Q,'security_A': security_A,'password': password})

            con.commit() 
            
            my_cursor.close()
            con.close()
            messagebox.showinfo("success","register succesfully") 

    def return_login(self):
        self.root.destroy()        
        













    



        



        










if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()        