from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import cx_Oracle
from tkinter import messagebox


class cust_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1395x550+230+210")
    
    
    #************** variable***************
        self.var_ref=StringVar() 
        x=random.randint(10000,999999)
        self.var_ref.set(str(x))


        self.var_cutname=StringVar()
        self.var_fname=StringVar()
        self.var_mname=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_pin=StringVar()
        self.var_nation=StringVar()
        self.var_id=StringVar()
        self.var_idnumber=StringVar()
        self.var_gen=StringVar()
        #************title*************
        lbl_title=Label(self.root,text="Add Customer Details",font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        #************bg image at details*******
        img1=Image.open("frame.jpg")
        img1=img1.resize((1550,800),Image.BICUBIC)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labl=Label(self.root,image=self.photoimg1)
        labl.place(x=0,y=0,relwidth=1,relheight=1)

        #*************logo**********
        img2=Image.open("hotel logo.jpeg")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        labling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE,bg="skyblue",fg="red")
        labling.place(x=5,y=2,width=100,height=40)

         #*********labelframe**************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #*************label and enrty*************
        #cust_ref
        lbl_cust_ref=Label(labelframeleft,text="Customer ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"))
        entry_ref.grid(row=0,column=1)

         #*************cust_name*************
        lbl_cust_name=Label(labelframeleft,text="Customer name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        entry_name=ttk.Entry(labelframeleft,textvariable=self.var_cutname,width=29,font=("arial",13,"bold"))
        entry_name.grid(row=1,column=1)

         #*************cust_father_name*************
        lbl_cust_father=Label(labelframeleft,text="Customer father",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_father.grid(row=2,column=0,sticky=W)

        entry_f=ttk.Entry(labelframeleft,textvariable=self.var_fname,width=29,font=("arial",12,"bold"))
        entry_f.grid(row=2,column=1)

         #*************cust_mothers_name*************
        lbl_cust_m=Label(labelframeleft,text="Customer mother",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_m.grid(row=3,column=0,sticky=W)

        entry_m=ttk.Entry(labelframeleft,textvariable=self.var_mname,width=29,font=("arial",12,"bold"))
        entry_m.grid(row=3,column=1)

         #*************cust_gender*************
        lbl_cust_g=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_g.grid(row=4,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gen,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("male","female","other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)

       

         #*************pincode*************
        lbl_cust_pin=Label(labelframeleft,text="pincode",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_pin.grid(row=5,column=0,sticky=W)

        entry_pin=ttk.Entry(labelframeleft,textvariable=self.var_pin,width=29,font=("arial",12,"bold"))
        entry_pin.grid(row=5,column=1)


         #*************cust_mob*************
        lbl_cust_mob=Label(labelframeleft,text="mobile no",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_mob.grid(row=6,column=0,sticky=W)

        entry_mob=ttk.Entry(labelframeleft,textvariable=self.var_phone,width=29,font=("arial",12,"bold"))
        entry_mob.grid(row=6,column=1)

         #*************cust_email*************
        lbl_cust_email=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=7,column=0,sticky=W)

        entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",12,"bold"))
        entry_email.grid(row=7,column=1)

         #*************nationality*************
        lbl_cust_n=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_n.grid(row=8,column=0,sticky=W)
        combo_nation=ttk.Combobox(labelframeleft,textvariable=self.var_nation,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nation["value"]=("Indian","Nepal","America","Russia")
        combo_nation.current(0)
        combo_nation.grid(row=8,column=1)



         #*************Id  proof type*************
        lbl_cust_id=Label(labelframeleft,text="Id proof type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_id.grid(row=9,column=0,sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Aadharcard","pancard","passport","drivinglicense")
        combo_id.current(0)
        combo_id.grid(row=9,column=1)



         #*************Id number*************
        lbl_cust_idn=Label(labelframeleft,text="id no",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_idn.grid(row=10,column=0,sticky=W)

        entry_idn=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=29,font=("arial",12,"bold"))
        entry_idn.grid(row=10,column=1)

        #********Address************8
        lbl_cust_adr=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_adr.grid(row=11,column=0,sticky=W)

        entry_adr=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",12,"bold"))
        entry_adr.grid(row=11,column=1)

        #******btns FRAME***
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=425,width=412,height=40)


        #button in frame***
        btn=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",command=self.update_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="DELETE",command=self.delete_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=3,padx=1)

        #******table frame search****
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and search system",font=("arial",12,"bold"),padx=2)
        tableframe.place(x=435,y=50,width=860,height=490)

        lblsearch=Label(tableframe,font=("arial",11,"bold"),text="Search BY:",bg="red",fg="white")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        #***combo box
        self.search_var=StringVar()
        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Refernce")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        #***entery fill
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        #*** button search**
        btnsearch=Button(tableframe,text="Search",command=self.search_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        #search show all***
        btnsearch_showall=Button(tableframe,text="Show all",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnsearch_showall.grid(row=0,column=4,padx=1)

        #*** show data table**
        table_details=Frame(tableframe,bd=2,relief=RIDGE)
        table_details.place(x=0,y=50,width=860,height=350)


        #*** scroll bar**
        scrol_x=Scrollbar(table_details,orient=HORIZONTAL)
        scrol_y=Scrollbar(table_details,orient=VERTICAL)

        self.cust_details_Table=ttk.Treeview(table_details,column=("ref","name","father","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM,fill=X)  
        scrol_y.pack(side=RIGHT,fill=Y) 

        scrol_x.config(command=self.cust_details_Table.xview)
        scrol_y.config(command=self.cust_details_Table.yview)

        self.cust_details_Table.heading("ref",text="Refer No ")
        self.cust_details_Table.heading("name",text="Customer Name ")
        self.cust_details_Table.heading("father",text="Father Name ")
        self.cust_details_Table.heading("mother",text="Mother Name ")
        self.cust_details_Table.heading("gender",text="Gender ")
        self.cust_details_Table.heading("post",text="PinCode")
        self.cust_details_Table.heading("mobile",text="Contact Number")
        self.cust_details_Table.heading("email",text="E-mail Id")
        
       
        
        self.cust_details_Table.heading("nationality",text="Nationality")
        self.cust_details_Table.heading("idproof",text="Id Proof")
        self.cust_details_Table.heading("idnumber",text="Id Number")
        self.cust_details_Table.heading("address",text="Address")

        self.cust_details_Table["show"]="headings"

        self.cust_details_Table.column("ref",width=100)
        self.cust_details_Table.column("name",width=100)
        self.cust_details_Table.column("father",width=100)
        self.cust_details_Table.column("mother",width=100)
        self.cust_details_Table.column("gender",width=100)
        self.cust_details_Table.column("post",width=100)
        self.cust_details_Table.column("mobile",width=100)
       
        self.cust_details_Table.column("email",width=100)
        self.cust_details_Table.column("nationality",width=100)
       
        
        
        
        self.cust_details_Table.column("idproof",width=100)
        self.cust_details_Table.column("idnumber",width=100)
        self.cust_details_Table.column("address",width=100)

        self.cust_details_Table.pack(fill=BOTH,expand=1)
        self.cust_details_Table.bind("<ButtonRelease-1>",self.get_cur)
        self.fetch_data() 

    def add_data(self):
          if self.var_phone.get()=="" or self.var_address.get()=="" or self.var_cutname.get()=="" or self.var_fname.get()=="" :
            messagebox.showerror("Error","Fill All Requirement")
          else:
            
            cust_ref=self.var_ref.get()
            cust_name=self.var_cutname.get()
            cust_fname=self.var_fname.get()
            cust_mname=self.var_mname.get()
            cust_email=self.var_email.get()
            cust_phone=self.var_phone.get()
            cust_address=self.var_address.get()
            cust_pin=self.var_pin.get()
            cust_nation=self.var_nation.get()
            cust_id=self.var_id.get()
            cust_id_number=self.var_idnumber.get()
            cust_gender=self.var_gen.get()
            
            con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
            my_cursor=con.cursor()
            # create an INSERT statement
            insert_statement = "INSERT INTO cust_data (ref, name,father, mother,gender,post,mobile,email,nationality,idproof,idnumber,address) VALUES (:ref,:name,:father,:mother,:gender,:post,:mobile,:email,:nationality,:idproof,:idnumber,:address)"

            # execute the INSERT statement
            my_cursor.execute(insert_statement, {'ref':cust_ref, 'name': cust_name, 'father': cust_fname,'mother': cust_mname,'gender':cust_gender,'post': cust_pin,'mobile': cust_phone,'email':cust_email,'nationality':cust_nation,'idproof':cust_id,'idnumber':cust_id_number,'address':cust_address})

            con.commit() 
            self.fetch_data()
            
            my_cursor.close()
            con.close()
            messagebox.showinfo("success","register succesfully",parent=self.root) 
    def fetch_data(self):
        con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
       
        my_cur=con.cursor()
        my_cur.execute("select * from cust_data")
        data=my_cur.fetchall()
        if len(data)!=0:
           self.cust_details_Table.delete(*self.cust_details_Table.get_children())
           for i in  data:
               self.cust_details_Table.insert("",END,values=i) 
        con.commit() 
        con.close()    
    # def get_curser(self)   


    def get_cur(self,event=""):
        cur_row=self.cust_details_Table.focus()
        content=self.cust_details_Table.item(cur_row)
        rows=content["values"]

        self.var_ref.set(rows[0]),
        self.var_cutname.set(rows[1]),
        self.var_fname.set(rows[2]),
        self.var_mname.set(rows[3])
        self.var_gen.set(rows[4]),
        self.var_pin.set(rows[5]),
        self.var_phone.set(rows[6]),
        self.var_email.set(rows[7]),
        self.var_nation.set(rows[8]),
       
        
        self.var_id.set(rows[9]),
        self.var_idnumber.set(rows[10])
        self.var_address.set(rows[11]),


        #update botton        
    def update_data(self):
        cust_ref=self.var_ref.get()
        cust_name=self.var_cutname.get()
        cust_fname=self.var_fname.get()
        cust_mname=self.var_mname.get()
        cust_email=self.var_email.get()
        cust_phone=self.var_phone.get()
        cust_address=self.var_address.get()
        cust_pin=self.var_pin.get()
        cust_nation=self.var_nation.get()
        cust_id=self.var_id.get()
        cust_id_number=self.var_idnumber.get()
        cust_gender=self.var_gen.get()
        if self.var_phone.get()=="" or self.var_address.get()=="" or self.var_cutname.get()==""  or self.var_fname.get()=="" :
             messagebox.showerror("Error","Fill All Requirement")
        else: 
             con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
       
             my_cur=con.cursor()
             my_cur.execute( "UPDATE cust_data SET name=:name, father=:father,mother=:mother,gender=:gender,post=:post,mobile=:mobile,email=:email,nationality=:nationality,idproof=:idproof,idnumber=:idnumber,address=:address WHERE ref=:ref", { 'name': cust_name, 'father': cust_fname,'mother': cust_mname,'gender':cust_gender,'post': cust_pin,'mobile': cust_phone,'email':cust_email,'nationality':cust_nation,'idproof':cust_id,'idnumber':cust_id_number,'address':cust_address,'ref':cust_ref})
             con.commit()
             self.fetch_data()
             con.close()
             messagebox.showinfo("update","customer details has been updated successfuly",parent=self.root)


    #delete function
    def delete_data(self):
      delete_data=messagebox.askyesno("Hotel Management System","Do You Want To Delete This Customer",parent=self.root)  
      if delete_data>0:
         con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
       
         my_cur=con.cursor()
         query="delete from cust_data where ref=:ref"
         value=(self.var_ref.get(),)
         my_cur.execute(query,value)
      else:
        if not delete_data:
          return
      con.commit()
      self.fetch_data()
      con.close()   
    def reset_data(self):
        #self.var_ref.set(""),
        self.var_cutname.set(""),
        self.var_fname.set(""),
        self.var_mname.set("")
        #self.var_gen.set(""),
        self.var_pin.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        #self.var_nation.set(""),
       
        
        #self.var_id.set(""),
        self.var_idnumber.set("")
        self.var_address.set(""),

        x=random.randint(10000,999999)
        self.var_ref.set(str(x))

   # Secrh Data 
    def search_data(self):
       con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
       
       my_cur=con.cursor()
       print(str(self.search_var.get()))
       my_cur.execute("select * from cust_data where ref like '%"+str(self.txt_search.get())+"%'") 
       data=my_cur.fetchall()
       if len(data)!=0:
              self.cust_details_Table.delete(*self.cust_details_Table.get_children())
              for i in data:
                     self.cust_details_Table.insert("",END,values=i)  
              con.commit()
       con.close()                











if __name__=="__main__":
    root=Tk()
    obj=cust_window(root) 
    root.mainloop()         