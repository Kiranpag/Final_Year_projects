from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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





        # self.bg=ImageTk.PhotoImage(file=r"college_images\employee_img2.jpg")
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        img3=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\employee_img2.jpg")
        img3=img3.resize((1100,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1000,height=710)




       


        # self.bg1=ImageTk.PhotoImage(file=r"college_images\LoveSove.jpg")
        # left_lbl=Label(self.root,image=self.bg1)
        # left_lbl.place(x=50,y=100,width=400,height=550)

        img2=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\LoveSove.jpg")
        img2=img2.resize((400,550),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=50,y=100,width=400,height=550)
        
        
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
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
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
            messagebox.showinfo("Success","Register Successfully",parent=self.root)                                                                            
          


       
if __name__== "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()  