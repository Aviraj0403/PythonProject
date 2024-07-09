from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime
import cx_Oracle


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")
        self.root.resizable(False,False)

         #************title*************
        lbl_title=Label(self.root,text="Roombooking Details",font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #*************logo**********
        img2=Image.open("hotel logo.jpeg")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        labling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        labling.place(x=5,y=2,width=100,height=40)



        self.var_Contact=StringVar()
        self.var_Checkindata=StringVar()
        self.var_Checkoutdata=StringVar()
        self.var_Typeofroom=StringVar()
        self.var_roomavailabel=StringVar()
        self.var_Meal=StringVar()
        self.var_nodys=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_total=StringVar()   

        #*********labelframe**************
        label_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("arial",12,"bold"),padx=2)
        label_frame.place(x=5,y=50,width=425,height=490)

        # ------------------- Entery ---------------------------
#contact    
        lbl_contact=Label(label_frame,text="Customer Contact",font=("arial", 12 ,"bold"),padx=2,pady=2)
        lbl_contact.grid(row=0,column=0,sticky=W) 

        cust_ref=ttk.Entry(label_frame,textvariable=self.var_Contact,font=("arial", 12 ,"bold"),width=20)
        cust_ref.grid(row=0,column=1,sticky=W)  

#fetch Data Button
        btn_fetch=Button(label_frame,command=self.fetch_data,text="Fetch Data",font=("arial", 8,"bold"),bd=1,bg="black",width=8,fg="gold") 
        btn_fetch.place(x=347,y=4)     

#----Check in Date
        lbl_check_in_date=Label(label_frame,text="Check-in Date :",font=("arial", 12 ,"bold"),padx=2,pady=6)
        lbl_check_in_date.grid(row=1,column=0,sticky=W) 

        cust_check_in_date=ttk.Entry(label_frame,textvariable=self.var_Checkindata,font=("arial", 12 ,"bold"),width=29)
        cust_check_in_date.grid(row=1,column=1)  

#--------check out Date
        lbl_check_out_date=Label(label_frame,text="Check-out Date :",font=("arial", 12 ,"bold"),padx=2,pady=6)
        lbl_check_out_date.grid(row=2,column=0,sticky=W) 

        cust_check_out_date=ttk.Entry(label_frame,textvariable=self.var_Checkoutdata,font=("arial", 12 ,"bold"),width=29)
        cust_check_out_date.grid(row=2,column=1) 


#------ Type of room
        lbl_room_type=Label(label_frame,text="Room Type :",font=("arial", 12 ,"bold"),padx=2,pady=6)
        lbl_room_type.grid(row=3,column=0,sticky=W)

        # con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
        con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
        my_cursor=con.cursor()
        
        my_cursor.execute("select roomtype from room_details")
        ide=my_cursor.fetchall()



        como_room_type=ttk.Combobox(label_frame,textvariable=self.var_Typeofroom,font=("arial", 12 ,"bold"),width=27,state="readonly")
        como_room_type["value"]=ide
        como_room_type.current(0)
        como_room_type.grid(row=3,column=1)  

        #Available room
        lblavilableroom=Label(label_frame,font=("arial",12,"bold"),text="Available room",padx=2,pady=6)
        lblavilableroom.grid(row=4,column=0,sticky=W)

        # txtroomavailble=ttk.Entry(label_frame,textvariable=self.var_roomavailabel,font=("arial", 12 ,"bold"),width=29)
        # txtroomavailble.grid(row=4,column=1) 


        con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
        my_cursor=con.cursor()
        
        my_cursor.execute("select roomno from room_details")
        rows=my_cursor.fetchall()

        como_room_no=ttk.Combobox(label_frame,textvariable=self.var_roomavailabel,font=("arial", 12 ,"bold"),width=27,state="readonly")
        como_room_no["value"]=rows
        como_room_no.current(0)
        como_room_no.grid(row=4,column=1) 

        
        #------meal

        lblnoofdays=Label(label_frame,text="Meal:",font=("arial", 12 ,"bold"),padx=2,pady=6)
        lblnoofdays.grid(row=5,column=0,sticky=W) 

        txtnoofdays=ttk.Entry(label_frame,textvariable=self.var_Meal,font=("arial",12,"bold"),width=29)
        txtnoofdays.grid(row=5,column=1)





        
        
        #no of days
        lblnoofdays=Label(label_frame,text="No. of dys:",font=("arial", 12 ,"bold"),padx=2,pady=6)
        lblnoofdays.grid(row=6,column=0,sticky=W) 

        txtnoofdays=ttk.Entry(label_frame,textvariable=self.var_nodys,font=("arial",12,"bold"),width=29)
        txtnoofdays.grid(row=6,column=1)


        #----------- paid Tax
        lbl_paid=Label(label_frame,text="Paid Tax :",font=("arial", 12 ,"bold"),padx=2,pady=6)
        lbl_paid.grid(row=7,column=0,sticky=W) 

        cust_paid=ttk.Entry(label_frame,textvariable=self.var_paidtax,font=("arial", 12 ,"bold"),width=29)
        cust_paid.grid(row=7,column=1) 


        #-----------------sub total
        lbl_sub=Label(label_frame,text="Sub Total :",font=("arial", 12 ,"bold"),padx=2,pady=6)
        lbl_sub.grid(row=8,column=0,sticky=W) 

        cust_sub=ttk.Entry(label_frame,textvariable=self.var_subtotal,font=("arial", 12 ,"bold"),width=29)
        cust_sub.grid(row=8,column=1)      

#------------------Total cost
        lbl_total=Label(label_frame,text="Total cost :",font=("arial", 12 ,"bold"),padx=2,pady=6)
        lbl_total.grid(row=9,column=0,sticky=W) 

        cust_total=ttk.Entry(label_frame,textvariable=self.var_total,font=("arial", 12 ,"bold"),width=29)
        cust_total.grid(row=9,column=1)    




                   

#----------- Room Number
        # lbl_tax=Label(label_frame,text="Room Number :",font=("times new roman", 12 ,"bold"),padx=2,pady=2)
        # lbl_tax.grid(row=6,column=0,sticky=W) 

       # cust_tax=Entry(label_frame,textvariable=self.var_roomavailabel,font=("times new roman", 12 ,"bold"),width=29,bd=2,bg="silver",fg="black")
       # cust_tax.grid(row=6,column=1,padx=1,pady=1)

        #******btns FRAME***
        btn_frame=Frame(label_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        #bill gen Button
        btn_bill=Button(label_frame,text="Bill",command=self.total,font=("arial", 11 ,"bold"),bg="black",width=10,fg="gold") 
        btn_bill.grid(row=10,column=0,padx=1,sticky=W)   



       #button in frame***
        btn=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btn.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",command=self.update_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="DELETE",command=self.delete_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=3,padx=1)
        #-------rightside image
        img3=Image.open("roomp1.jpg")
        img3=img3.resize((520,300),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        labling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        labling.place(x=760,y=55,width=520,height=200)


        img4=Image.open("roomp2.jpg")
        img4=img4.resize((520,300),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)


        labling=Label(self.root,image=self.photoimg4,bd=0,relief=RIDGE)
        labling.place(x=430,y=55,width=320,height=200)

        


               #******table frame search****
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and search system",font=("arial",12,"bold"),padx=2)
        tableframe.place(x=435,y=280,width=860,height=260)

        lblsearch=Label(tableframe,font=("arial",11,"bold"),text="Search BY:",bg="red",fg="white")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        #***combo box
        self.search_var=StringVar()
        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        #***entery fill
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        #*** button search**
        btnsearch=Button(tableframe,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        #search show all***
        btnsearch_showall=Button(tableframe,text="Show all",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnsearch_showall.grid(row=0,column=4,padx=1)


        #*** show data table**
        table_details=Frame(tableframe,bd=2,relief=RIDGE)
        table_details.place(x=0,y=50,width=860,height=180)


        #*** scroll bar**
        scrol_x=Scrollbar(table_details,orient=HORIZONTAL)
        scrol_y=Scrollbar(table_details,orient=VERTICAL)

        self.room_Table=ttk.Treeview(table_details,column=("contact","checkin date","checkout date","roomtype","room available","meal","nodys",),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM,fill=X)  
        scrol_y.pack(side=RIGHT,fill=Y) 

        scrol_x.config(command=self.room_Table.xview)
        scrol_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact",text="contact ")
        self.room_Table.heading("checkin date",text="check-in")
        self.room_Table.heading("checkout date",text="check-out ")
        self.room_Table.heading("roomtype",text="room type ")
        self.room_Table.heading("room available",text="room available ")
        self.room_Table.heading("meal",text="meal")
        self.room_Table.heading("nodys",text="no of days")
        

        self.room_Table["show"]="headings"

        self.room_Table.column("contact",width=100)
        self.room_Table.column("checkin date",width=100)
        self.room_Table.column("checkout date",width=100)
        self.room_Table.column("roomtype",width=100)
        self.room_Table.column("room available",width=100)
        self.room_Table.column("meal",width=100)
        self.room_Table.column("nodys",width=100)
       
        
        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cur)

        ### caling 
        self.fetch_data_room()


    def add_data(self):
          if self.var_Contact.get()=="" or self.var_Checkindata.get()=="":
            messagebox.showerror("Error","Fill All Requirement")
          else:
       
            
            
            con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
            my_cursor=con.cursor()
            # create an INSERT statement
            insert_statement = "INSERT INTO room (contact, check_in, check_out,roomtype,roomavailable,meal,nodys) VALUES (:contact,:check_in,:check_out,:roomtype,:roomavailable,:meal,:nodys)"

            # execute the INSERT statement
            my_cursor.execute(insert_statement, {'contact':self.var_Contact.get(), 'check_in':self.var_Checkindata.get() , 'check_out': self.var_Checkoutdata.get(),'roomtype':self.var_Typeofroom.get(),'roomavailable':self.var_roomavailabel.get(),'meal': self.var_Meal.get(),'nodys':self.var_nodys.get()})

            con.commit() 
            self.fetch_data_room()
            
            my_cursor.close()
            con.close()
            messagebox.showinfo("success","room booking succesfully",parent=self.root) 


    def fetch_data_room(self):
        con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
       
        my_cur=con.cursor()
        my_cur.execute("select * from room")
        data=my_cur.fetchall()
        if len(data)!=0:
           self.room_Table.delete(*self.room_Table.get_children())
           for i in  data:
               self.room_Table.insert("",END,values=i) 
        con.commit() 
        con.close() 

        #-----get cursor

    def get_cur(self,event=""):
        cur_row=self.room_Table.focus()
        content=self.room_Table.item(cur_row)
        rows=content["values"]

        self.var_Contact.set(rows[0]),
        self.var_Checkindata.set(rows[1]),
        self.var_Checkoutdata.set(rows[2]),
        self.var_Typeofroom.set(rows[3])
        self.var_roomavailabel.set(rows[4]),
        self.var_Meal.set(rows[5]),
        self.var_nodys.set(rows[6]),

        ##------update room dta


    def update_data(self):
         #      self.var_Contact=StringVar()
        #     self.var_Checkindata=StringVar()
        #                 self.var_Checkoutdata=StringVar()
        #                 self.var_Typeofroom=StringVar()
        #                 self.var_roomavailabel=StringVar()
        #                 self.var_Meal=StringVar()
        #                 self.var_noofday=StringVar()
        #                 self.var_paidtax=StringVar()
        #                 self.var_subtotal=StringVar()
        #                 self.var_total=StringVar()   
                
        
        if self.var_Contact.get()=="":
             messagebox.showerror("Error","please enter mobile no",parent=self.root)
        else: 
             con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
       
             my_cur=con.cursor()
             my_cur.execute( "UPDATE room SET check_in=:check_in,check_out=:check_out,roomtype=:roomtype,roomavailable=:roomavailable,meal=:meal,nodys=:nodys WHERE contact=:contact", { 'check_in': self.var_Checkindata.get(), 'check_out': self.var_Checkoutdata.get(),'roomtype': self.var_Typeofroom.get(),'roomavailable':self.var_roomavailabel.get(),'meal': self.var_Meal.get(),'nodys': self.var_nodys.get(),'contact':self.var_Contact.get()})
             con.commit()
             self.fetch_data_room()
             con.close()
             messagebox.showinfo("update","room details has been updated successfuly",parent=self.root)

             ##----delete room data

    def delete_data(self):
      delete_data=messagebox.askyesno("Hotel Management System","Do You Want To Delete This Customer",parent=self.root)  
      if delete_data>0:
         con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521'))
       
         my_cur=con.cursor()
         query="delete from room where contact=:contact"
         value=(self.var_Contact.get(),)
         my_cur.execute(query,value)
      else:
        if not delete_data:
          return
      con.commit()
      self.fetch_data_room()
      con.close()  


    def reset_data(self):
        self.var_Contact.set(""),
        self.var_Checkindata.set(""),
        self.var_Checkoutdata.set(""),
        self.var_Typeofroom.set("")
        self.var_roomavailabel.set(""),
        self.var_Meal.set(""),
        self.var_nodys.set(""),
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

    

        
       
       
       
        
        



     
   #----------------fetch data-------------------------
    def fetch_data(self):
        if self.var_Contact.get()=="":
                messagebox.showerror("Error","Enter The Contact Number",parent=self.root)
        else:
                 con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
                 my_cursor=con.cursor()
                 query="select name from cust_data where mobile=:mobile"
                 value=(self.var_Contact.get(),)
                 my_cursor.execute(query,value)
                 row=my_cursor.fetchone()

                 if row==None:
                        messagebox.showerror("error","This number is not found",parent=self.root)
                 else:
                        con.commit()
                        con.close() 

                        showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2) 
                        showdataframe.place(x=450,y=55,width=300,height=180)  

                        lblname=Label(showdataframe,text="Name",font=("arial",12,"bold")) 
                        lblname.place(x=0,y=0)  

                        lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                        lbl.place(x=90,y=0)


                        con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
                        my_cursor=con.cursor()
                        query="select gender from cust_data where mobile=:mobile"
                        value=(self.var_Contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lblgender=Label(showdataframe,text="Gender",font=("arial",12,"bold")) 
                        lblgender.place(x=0,y=30)  

                        lbl2=Label(showdataframe,text=row,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=30)

                        #-------------email------
                        con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
                        my_cursor=con.cursor()
                        query="select email from cust_data where mobile=:mobile"
                        value=(self.var_Contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lblemail=Label(showdataframe,text="Email",font=("arial",12,"bold")) 
                        lblemail.place(x=0,y=60)  

                        lbl3=Label(showdataframe,text=row,font=("arial",12,"bold"))
                        lbl3.place(x=90,y=60)

                        #---------nationality---
                        con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
                        my_cursor=con.cursor()
                        query="select nationality from cust_data where mobile=:mobile"
                        value=(self.var_Contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lblnationality=Label(showdataframe,text="Nationality",font=("arial",12,"bold")) 
                        lblnationality.place(x=0,y=90)  

                        lbl4=Label(showdataframe,text=row,font=("arial",12,"bold"))
                        lbl4.place(x=90,y=90)

                        #------address----
                        con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
                        my_cursor=con.cursor()
                        query="select address from cust_data where mobile=:mobile"
                        value=(self.var_Contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        lbladdress=Label(showdataframe,text="Address",font=("arial",12,"bold")) 
                        lbladdress.place(x=0,y=120)  

                        lbl5=Label(showdataframe,text=row,font=("arial",12,"bold"))
                        lbl5.place(x=90,y=120)
    def total(self):

        if self.var_Contact.get()=="":
              messagebox.showerror("Error","Enter The Contact Number",parent=self.root)
        elif(self.var_Checkindata.get()=="" and self.var_Checkoutdata.get()=="") :
              messagebox.showerror("Error","Please Fill The All Requirement",parent=self.root)         
        else:  
               con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
               my_cursor=con.cursor()
              
               query=("select name From cust_data where mobile=:mobile")   
               value=(self.var_Contact.get(),)   
               my_cursor.execute(query,value)  
               rows=my_cursor.fetchone()

               if rows==None:
                   messagebox.showerror("Error","Given Number Is Not Found",parent=self.root)   
               else:                 


                        inDate=self.var_Checkindata.get()
                        outDate=self.var_Checkoutdata.get()
                        inDate=datetime.strptime(inDate,"%d/%m/%Y") 
                        outDate=datetime.strptime(outDate,"%d/%m/%Y") 
                        self.var_nodys.set(abs(outDate-inDate).days) 

                        # if(self.var_Meal.get()=="breakfast" and self.var_Typeofroom.get()=="laxary"):
                        #         q1=float(300)
                        #         q2=float(700)
                        #         q3=float(self.var_noofday.get())
                        #         q4=float(q1+q2)
                        #         q5=float(q3+q4)
                        #         Tax="Rs."+str("%.2f"%((q5)*0.1))
                        #         ST="Rs."+str("%.2f"%((q5)))
                        #         TT="Rs."+str("%.2f"%((q5+((q5)*0.1))))
                        #         self.var_paidtax.set(Tax)
                        #         self.var_subtotal.set(ST)
                        #         self.var_total.set(TT)
                        if (self.var_Meal.get()=="breakfast" and self.var_Typeofroom.get()=="luxary"):
                                        bf=float(200)
                                        rt=float(1500)
                                        t=float(self.var_nodys.get())
                                        tc=float(bf+rt*t)
                                        tax="Rs. "+str("%.2f"%((tc)*0.18))
                                        st="Rs. "+str("%.2f"%((tc)))
                                        tt="Rs. "+str("%.2f"%(tc+(tc)*0.1))
                                        self.var_paidtax.set(tax)
                                        self.var_subtotal.set(st)
                                        self.var_total.set(tt)
                        elif (self.var_Meal.get()=="breakfast" and self.var_Typeofroom.get()=="single"):
                                        bf=float(200)
                                        rt=float(600)
                                        t=float(self.var_nodys.get())
                                        tc=float(bf+rt*t)
                                        tax="Rs. "+str("%.2f"%((tc)*0.18))
                                        st="Rs. "+str("%.2f"%((tc)))
                                        tt="Rs. "+str("%.2f"%(tc+(tc)*0.1))
                                        self.var_paidtax.set(tax)
                                        self.var_subtotal.set(st)
                                        self.var_total.set(tt)
                        elif (self.var_Meal.get()=="breakfast" and self.var_Typeofroom.get()=="double"):
                                        bf=float(200)
                                        rt=float(1000)
                                        t=float(self.var_nodys.get())
                                        tc=float(bf+rt*t)
                                        tax="Rs. "+str("%.2f"%((tc)*0.18))
                                        st="Rs. "+str("%.2f"%((tc)))
                                        tt="Rs. "+str("%.2f"%(tc+(tc)*0.1))
                                        self.var_paidtax.set(tax)
                                        self.var_subtotal.set(st)
                                        self.var_total.set(tt)       
                        elif (self.var_Meal.get()=="lunch" and self.var_Typeofroom.get()=="laxary"):
                                        bf=float(200)
                                        rt=float(1500)
                                        t=float(self.var_nodys.get())
                                        tc=float(bf+rt*t)
                                        tax="Rs. "+str("%.2f"%((tc)*0.18))
                                        st="Rs. "+str("%.2f"%((tc)))
                                        tt="Rs. "+str("%.2f"%(tc+(tc)*0.1))
                                        self.var_paidtax.set(tax)
                                        self.var_subtotal.set(st)
                                        self.var_total.set(tt) 
                        elif (self.var_Meal.get()=="lunch" and self.var_Typeofroom.get()=="double"):
                                        bf=float(200)
                                        rt=float(1000)
                                        t=float(self.var_nodys.get())
                                        tc=float(bf+rt*t)
                                        tax="Rs. "+str("%.2f"%((tc)*0.18))
                                        st="Rs. "+str("%.2f"%((tc)))
                                        tt="Rs. "+str("%.2f"%(tc+(tc)*0.1))
                                        self.var_paidtax.set(tax)
                                        self.var_subtotal.set(st)
                                        self.var_total.set(tt)  
                        elif (self.var_Meal.get()=="lunch" and self.var_Typeofroom.get()=="single"):
                                        bf=float(200)
                                        rt=float(600)
                                        t=float(self.var_nodys.get())
                                        tc=float(bf+rt*t)
                                        tax="Rs. "+str("%.2f"%((tc)*0.18))
                                        st="Rs. "+str("%.2f"%((tc)))
                                        tt="Rs. "+str("%.2f"%(tc+(tc)*0.1))
                                        self.var_paidtax.set(tax)
                                        self.var_subtotal.set(st)
                                        self.var_total.set(tt)   
                        elif (self.var_Meal.get()=="dinner" and self.var_Typeofroom.get()=="laxary"):
                                        bf=float(200)
                                        rt=float(1500)
                                        t=float(self.var_nodys.get())
                                        tc=float(bf+rt*t)
                                        tax="Rs. "+str("%.2f"%((tc)*0.18))
                                        st="Rs. "+str("%.2f"%((tc)))
                                        tt="Rs. "+str("%.2f"%(tc+(tc)*0.1))
                                        self.var_paidtax.set(tax)
                                        self.var_subtotal.set(st)
                                        self.var_total.set(tt) 
                        elif (self.var_Meal.get()=="dinner" and self.var_Typeofroom.get()=="double"):
                                        bf=float(200)
                                        rt=float(1000)
                                        t=float(self.var_nodys.get())
                                        tc=float(bf+rt*t)
                                        tax="Rs. "+str("%.2f"%((tc)*0.18))
                                        st="Rs. "+str("%.2f"%((tc)))
                                        tt="Rs. "+str("%.2f"%(tc+(tc)*0.1))
                                        self.var_paidtax.set(tax)
                                        self.var_subtotal.set(st)
                                        self.var_total.set(tt)  
                        elif (self.var_Meal.get()=="dinner" and self.var_Typeofroom.get()=="single"):
                                        bf=float(200)
                                        rt=float(600)
                                        t=float(self.var_nodys.get())
                                        tc=float(bf+rt*t)
                                        tax="Rs. "+str("%.2f"%((tc)*0.18))
                                        st="Rs. "+str("%.2f"%((tc)))
                                        tt="Rs. "+str("%.2f"%(tc+(tc)*0.1))
                                        self.var_paidtax.set(tax)
                                        self.var_subtotal.set(st)
                                        self.var_total.set(tt)   



     

 








if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root) 
    root.mainloop()                                                        

