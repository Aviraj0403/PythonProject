from tkinter import *
from PIL import Image,ImageTk
from data import cust_window
# from login import login
from room import Roombooking
from rdetails import DetailsRoom


class hotelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management project")
        self.root.geometry("1550x800+0+0")


        #******************1st image*********
        img1=Image.open("front.jpg")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        labling.place(x=0,y=0,width=1550,height=140)

        #*************logo**********
        img2=Image.open("hotel logo.jpeg")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        labling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        labling.place(x=0,y=0,width=230,height=140)

        #************title*************
        lbl_title=Label(self.root,text="Hotel Management System",font=("times new roman",40,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #*************mainfrmae************
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #***************menu***************
        lbl_menu=Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #**************btnframe**********
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="Customer",command=self.cust_details,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        cust_btn=Button(btn_frame,text="Room",command=self.roombooking,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)

        cust_btn=Button(btn_frame,text="Details",command=self.detailsroom,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=2,column=0,pady=1)

        cust_btn=Button(btn_frame,text="Report",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=3,column=0,pady=1)

        cust_btn=Button(btn_frame,text="Logout",command=self.logout,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=4,column=0,pady=1)

        #*************rightside image************
        img3=Image.open("frame.jpg")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        labling1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        labling1.place(x=225,y=0,width=1310,height=590)

        #*************downimage***********
        img4=Image.open("eat.jpg")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        labling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        labling1.place(x=0,y=225,width=230,height=210)
        
        img5=Image.open("lhom.jpg")
        img5=img5.resize((230,190),Image.BICUBIC)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        labling1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        labling1.place(x=0,y=420,width=230,height=210)
        # img5=Image.open("eat2.jpg")
        # img5=img5.resize((230,190),Image.LANCZOS)
        # self.photoimg5=ImageTk.PhotoImage(img5)

        # labling1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        # labling1.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        # self.ap=login(self.new_window)
        self.app=cust_window(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        # self.ap=login_win(self.new_window)
        self.app=Roombooking(self.new_window)
    def detailsroom(self):
        self.new_window=Toplevel(self.root)
        # self.ap=login_win(self.new_window)
        self.app=DetailsRoom(self.new_window) 
    def logout(self):
        self.root.destroy() 








if __name__=="__main__":
    root=Tk()
    obj=hotelmanagementsystem(root) 
    root.mainloop()       


