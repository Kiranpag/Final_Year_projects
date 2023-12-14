from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from sub_attendance import Student1
import os
from time import strftime
from datetime import datetime
import tkinter
from train1 import Train1
from face_recognition1 import Face_Recognition1
from showAttendance import Attendance1
from chatbot import ChatBot
from Devloper import Devloper


class Face_Recognition_System1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #First IMG
        img=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\Stanford.jpg")
        img=img.resize((350,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=130)

        #Second IMG
        img1=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\facialrecognition.png")
        img1=img1.resize((350,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=350,y=0,width=350,height=130)

        #Third IMG
        img2=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\u.jpg")
        img2=img2.resize((350,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=700,y=0,width=310,height=130)


        #BG IMG
        img3=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\background.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",22,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1000,height=45)


        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time) 

        lbl=Label(title_lbl,font=('times new roman',12,'bold'),bg='white',fg='blue')
        lbl.place(x=0,y=0,width=100,height=50)
        time()       

        
        #Student button
        img4=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\student.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details1,cursor="hand2")
        b1.place(x=150,y=100,width=150,height=150)



        b1_1=Button(bg_img,text="Subject Details",command=self.student_details1,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=250,width=150,height=40)



        #Student detection button
        img5=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\face_detector.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data1)
        b1.place(x=350,y=100,width=150,height=150)



        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data1,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=350,y=250,width=150,height=40)



        #Student Attendance button
        img6=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\attendance.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data1)
        b1.place(x=550,y=100,width=150,height=150)



        b1_1=Button(bg_img,text="Sub Attendance",cursor="hand2",command=self.attendance_data1,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=550,y=250,width=150,height=40)
        


        #Student Chatbot button
        img7=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\chat.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatbot)
        b1.place(x=750,y=100,width=150,height=150)



        b1_1=Button(bg_img,text="ChatBot",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=250,width=150,height=40)



        #Student Train button
        img8=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\Train.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data1)
        b1.place(x=150,y=350,width=150,height=150)



        b1_1=Button(bg_img,text="Train data2",cursor="hand2",command=self.train_data1,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=500,width=150,height=40)



         #Student Photos button
        img9=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\photos.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=350,y=350,width=150,height=150)



        b1_1=Button(bg_img,text="Photos1",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=350,y=500,width=150,height=40)
        


        #Student Devloper button
        img10=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\Devloper.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.devloper_data)
        b1.place(x=550,y=350,width=150,height=150)



        b1_1=Button(bg_img,text="Devloper",cursor="hand2",command=self.devloper_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=550,y=500,width=150,height=40)



        #Student Exit button
        img11=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\exit.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.IExit)
        b1.place(x=750,y=350,width=150,height=150)



        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.IExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=500,width=150,height=40)
        

        
    def open_img(self):
        os.startfile("data1")
  
    def IExit(self):
        self.IExit=messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.IExit >0:
            self.root.destroy()
        else:
            return      


        #    ==========================Function buttons================
        
       
    def student_details1(self):
        self.new_window=Toplevel(self.root)
        self.app=Student1(self.new_window) 


    def train_data1(self):
        self.new_window=Toplevel(self.root)
        self.app=Train1(self.new_window)


    def face_data1(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition1(self.new_window)  

    def attendance_data1(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance1(self.new_window)

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)  

    def devloper_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Devloper(self.new_window)            
                    
                      
                    
        












if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System1(root)
    root.mainloop()
