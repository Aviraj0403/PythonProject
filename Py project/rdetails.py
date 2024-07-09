from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import random 
from time import strftime
from datetime import datetime
import cx_Oracle


class DetailsRoom:
    def __init__(self,root):
       self.root=root
       self.root.title("Hotel Management")
       self.root.geometry("1295x550+230+220")
       self.root.resizable(False,False)

# ---------------- Title ------------------------------
       tit=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=SUNKEN)
       tit.place(x=0,y=0,width=1295,height=50)

#*************logo**********
       img2=Image.open("hotel logo.jpeg")
       img2=img2.resize((100,40),Image.LANCZOS)
       self.photoimg2=ImageTk.PhotoImage(img2)


       labling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
       labling.place(x=5,y=2,width=100,height=40)

        #*********labelframe**************
       labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2)
       labelframeleft.place(x=5,y=50,width=540,height=350)

#Floor    
       lbl_floor=Label(labelframeleft,text="Floor",font=("arial", 12 ,"bold"),padx=10,pady=6)
       lbl_floor.grid(row=0,column=0,sticky=W,padx=20) 

       self.var_floor=StringVar()
       
       cust_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("times new roman", 12 ,"bold"),width=20)
       cust_floor.grid(row=0,column=1,sticky=W) 


# #----Room No
       lbl_room_no=Label(labelframeleft,text="Room No :",font=("arial", 12 ,"bold"),padx=2,pady=6)
       lbl_room_no.grid(row=1,column=0,sticky=W,padx=20)

       self.var_roomno=StringVar()

       

       cust_room_no=ttk.Entry(labelframeleft,textvariable=self.var_roomno,font=("arial", 12 ,"bold"),width=20)
       cust_room_no.grid(row=1,column=1,sticky=W) 

# #--------Room Type
       lbl_room_type=Label(labelframeleft,text=" Room Type:",font=("arial", 12 ,"bold"),padx=2,pady=6)
       lbl_room_type.grid(row=2,column=0,sticky=W,padx=20) 

       self.var_roomtype=StringVar() 


       # como_room_type=ttk.Combobox(label_frame,textvariable=self.var_roomtype,font=("times new roman", 12 ,"bold"),width=16,state="readonly")
       # como_room_type["value"]=("Single","Double","Laxary")
       # como_room_type.current(0)
       # como_room_type.grid(row=2,column=1,padx=1,pady=1)  

       cust_room_type=ttk.Entry(labelframeleft,textvariable= self.var_roomtype,font=("arial", 12 ,"bold"),width=20)
       cust_room_type.grid(row=2,column=1,sticky=W)   



# # ---------------btn----------
       btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
       btn_frame.place(x=0,y=200,width=412,height=40)
       
       btn_add=Button(btn_frame,text="ADD",command=self.add,font=("arial", 11 ,"bold"),bg="black",width=10,fg="gold") 
       btn_add.grid(row=0,column=0,padx=1)

       btn_save=Button(btn_frame,text="UPDATE",command=self.update_data,font=("arial", 11 ,"bold"),bg="black",width=10,fg="gold") 
       btn_save.grid(row=0,column=1,padx=1)

       btn_delete=Button(btn_frame,text="DELETE",command=self.delet_data,font=("arial", 11 ,"bold"),bg="black",width=10,fg="gold") 
       btn_delete.grid(row=0,column=2,padx=1)

       btn_update=Button(btn_frame,text="RESET",command=self.reset_data,font=("arial", 11 ,"bold"),bg="black",width=10,fg="gold") 
       btn_update.grid(row=0,column=3,padx=1)  



#  # --------------- table Frame Serch  -------------------------
       tabel_frame=LabelFrame(self.root,bd=2,relief=RIDGE,font=("arial", 12 ,"bold"),text="Show Room Details",padx=1)
       tabel_frame.place(x=600,y=55,width=600,height=350)     

       scrol_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
       scrol_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)


       self.room_table=ttk.Treeview(tabel_frame,column=("Floor","Room_No","Room_Type"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
       
       scrol_x.pack(side=BOTTOM,fill=X)
       scrol_y.pack(side=RIGHT,fill=Y)
       scrol_x.config(command=self.room_table.xview)
       scrol_y.config(command=self.room_table.yview)  


       self.room_table.heading("Floor",text="Floor")
       self.room_table.heading("Room_No",text="Room-Number")
       self.room_table.heading("Room_Type",text="Room-Type")

       self.room_table["show"]="headings"

       self.room_table.column("Floor",width=100)
       self.room_table.column("Room_No",width=100)
       self.room_table.column("Room_Type",width=100)

       
       self.room_table.pack(fill=BOTH,expand=1)  
       self.room_table.bind("<ButtonRelease-1>",self.get_cur)
       self.fetch_data()


#  #--------------- Add Function ------------------------                 

    def add(self):
        if self.var_floor.get()=="" and self.var_roomno.get()=="":
            messagebox.showerror("Error","Fill All Requirement",parent=self.root)
        else :
              try:
                     con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
                     my_cursor=con.cursor()
                     # create an INSERT statement
                     insert_statement = "INSERT INTO room_details  (floor, roomno,roomtype) VALUES (:floor,:roomno,:roomtype)"

                     # execute the INSERT statement
                     my_cursor.execute(insert_statement, {'floor':self.var_floor.get(), 'roomno': self.var_roomno.get(), 'roomtype': self.var_roomtype.get()})

                     con.commit() 
                     self.fetch_data()
                     my_cursor.close()
                     
                     
                     con.close()
                     messagebox.showinfo("success","room details register succesfully",parent=self.root)  
              except Exception as ex:
                  messagebox.showwarning("Warning",f"Something Went Wrong : {str(ex)}",parent=self.root)  



    def fetch_data(self):
        con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
        my_cursor=con.cursor()
        
        my_cursor.execute("select * from room_details")
        data=my_cursor.fetchall()
        if len(data)!=0:
           self.room_table.delete(*self.room_table.get_children())
           for i in  data:
               self.room_table.insert("",END,values=i) 
        con.commit() 
        con.close()   



    def get_cur(self,event=""):
              cur_row=self.room_table.focus()
              content=self.room_table.item(cur_row)
              row=content["values"]

              self.var_floor.set(row[0]),
              self.var_roomno.set(row[1]),
              self.var_roomtype.set(row[2]),      


#-----------------update---------------------
    def update_data(self):
        if self.var_floor.get()=="":
             messagebox.showerror("Error","Fill All Requirement",parent=self.root)
        else:
              try:    
                     con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
                     my_cursor=con.cursor()
                     my_cursor.execute( "UPDATE room_details SET roomno=:roomno,roomtype=:roomtype WHERE floor=:floor", {'roomno':self.var_roomno.get() , 'roomtype': self.var_roomtype.get(),'floor': self.var_floor.get()})
                     con.commit() 
                     self.fetch_data() 
                     my_cursor.close()
                     messagebox.showinfo("Success","Room Details Update Successsfully",parent=self.root) 
              except Exception as ex:
                  messagebox.showwarning("Warning",f"Something Went Wrong : {str(ex)}",parent=self.root)  
    
          

                                                                                                                                            
             

#----------------delete Function---------------
    def delet_data(self):
       delet_data=messagebox.askyesno("Hotel Management System","Do You Want To Delete This Room",parent=self.root)
       if delet_data>0:
              con=cx_Oracle.connect(user="system",password='834',dsn=cx_Oracle.makedsn('LAPTOP-5L4CGTPT','1521')) 
              my_cursor=con.cursor()
           
              query="delete from room_details where roomno=:roomno"   
              value=(self.var_roomno.get(),)    
              my_cursor.execute(query,value)  
       else:
            if not delet_data:
              return
       con.commit() 
       self.fetch_data()
       con.close()     



#--------- reset Function ---------------
    def reset_data(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")
                                                            





if __name__=="__main__":
   root=Tk()
   ob=DetailsRoom(root)
   root.mainloop()               