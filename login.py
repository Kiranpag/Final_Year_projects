from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import mysql.connector
from chatbot import ChatBot
from main2 import Face_Recognition_System1

def main():
    win=Tk()
    app=Login_windows(win)
    win.mainloop()


class Login_windows:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


         #First IMG
        img=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\attendance.jpg")
        img=img.resize((350,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=100)

        #Second IMG
        img1=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\facialrecognition.png")
        img1=img1.resize((350,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=350,y=0,width=350,height=100)

        #Third IMG
        img2=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\student1.jpg")
        img2=img2.resize((350,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=700,y=0,width=310,height=100)

         #BG IMG
        img3=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\bgg.jpeg")
        img3=img3.resize((1100,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1100,height=710)


        title_lbl=Label(bg_img,text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",22,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1100,height=45)



       
       
       
        #self.bg=ImageTk.PhotoImage(file=r"college_images\un.jpg")
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=350,y=170,width=340,height=450)

        img1=Image.open(r"college_images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimage1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimage1.place(x=470,y=175,width=100,height=100)

        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=98,y=100)

        #label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)



        #==========Icon image===========
        img2=Image.open(r"college_images\LoginIconAppl.png")
        img2=img2.resize((30,30),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimage1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimage1.place(x=390,y=320,width=30,height=30)

        img3=Image.open(r"college_images\lock-512.png")
        img3=img3.resize((30,30),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimage1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimage1.place(x=390,y=390,width=30,height=30)

        #login
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register
        register=Button(frame,text="New User Register",command=self.register_windows,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        register.place(x=15,y=350,width=160)

        
        #forget
        forgetbtn=Button(frame,command=self.forget_password_windows,text="Forget Password",font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=6,y=370,width=160)
    
    
    
    
    def register_windows(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

  
  
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kiran" and self.txtpass.get()=="pagar":
            messagebox.showinfo("Sucess","Welcome Login")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                         self.txtuser.get(),
                                                                                         self.txtpass.get()

                                                                                     ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root) 
                    self.app=Face_Recognition_System(self.new_window) 
                else:
                    if not open_main:
                        return 
            conn.commit()
            conn.close() 

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Questions",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value) 

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,please login new password",parent=self.root2)    
                self.root2.destroy()



    def forget_password_windows(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please Enter the valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+350+180")


                l=Label(self.root2,text="Forget Password",font=("times new roman",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1) 
                
                security_Q=Label(self.root2,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your petname","Your place name")
                self.combo_security_Q.place(x=50,y=115,width=200)
                self.combo_security_Q.current(0)




                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=160)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))     
                self.txt_security.place(x=50,y=195,width=200) 


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=235)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"),show="*")     
                self.txt_new_password.place(x=50,y=270,width=200)


                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman",18,"bold"),fg="white",bg="green")
                btn.place(x=110,y=320) 


   



                
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")


        #variable
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()





        self.bg=ImageTk.PhotoImage(file=r"college_images\background.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        self.bg1=ImageTk.PhotoImage(file=r"college_images\LoveSove.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=400,height=550)
        
        
        #===========main frame====================
        frame=Frame(self.root,bg="white")
        frame.place(x=451,y=100,width=550,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white") 
        register_lbl.place(x=20,y=20) 



        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)


        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))     
        fname_entry.place(x=50,y=130,width=200) 

        #last name
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=300,y=100)


        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))     
        self.txt_lname.place(x=300,y=130,width=200) 

        #contact
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)


        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))     
        self.txt_contact.place(x=50,y=200,width=200) 

        #Email
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=300,y=170)


        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))     
        self.txt_email.place(x=300,y=200,width=200) 

        # Security questions
        security_Q=Label(frame,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your petname","Your place name")
        self.combo_security_Q.place(x=50,y=270,width=200)
        self.combo_security_Q.current(0)




        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=300,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))     
        self.txt_security.place(x=300,y=270,width=200) 


        #password
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))     
        self.txt_pswd.place(x=50,y=340,width=200) 


        #conform password

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=300,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))     
        self.txt_confirm_pswd.place(x=300,y=340,width=200)


        #========checkbutton==============
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",10,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380) 


        #============buttons============
        img=Image.open(r"college_images\register-now-button1.jpg")
        img=img.resize((150,60),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=15,y=420,width=150)




        img1=Image.open(r"college_images\loginl.png")
        img1=img1.resize((150,45),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=290,y=430,width=150)




        #==============function declaration=========
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),          
                                                                                        self.var_contact.get(), 
                                                                                        self.var_email.get(),    
                                                                                        self.var_securityQ.get(), 
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()      
                                                                                        
                                                                                     )) 
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully") 


    def return_login(self):
        self.root.destroy()

class Face_Recognition_System:
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

        
        #Student button
        img4=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\student.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=150,height=150)



        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=250,width=150,height=40)



        #Student detection button
        img5=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\face_detector.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=350,y=100,width=150,height=150)



        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=350,y=250,width=150,height=40)



        #Student Attendance button
        img6=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\attendance.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=550,y=100,width=150,height=150)



        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
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

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=350,width=150,height=150)



        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=500,width=150,height=40)



         #Student Photos button
        img9=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\photos.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=350,y=350,width=150,height=150)



        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=350,y=500,width=150,height=40)
        


         #Student Devloper button
        img10=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\Devloper.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.sub_attendance)
        b1.place(x=550,y=350,width=150,height=150)



        b1_1=Button(bg_img,text="Sub Attendance",cursor="hand2",command=self.sub_attendance,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
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
        os.startfile("data")

    def IExit(self):
        self.IExit=messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.IExit >0:
            self.root.destroy()
        else:
            return        


        #    ==========================Function buttons================
        
       
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window) 


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)  

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)  

    def sub_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System1(self.new_window)            
                                  
                    
        










if __name__== "__main__":
    main()
    
    