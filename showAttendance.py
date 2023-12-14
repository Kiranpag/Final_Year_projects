from cgitb import text
from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #====================variables==============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_subject=StringVar()

        self.var_atten_attendance=StringVar()







        #First IMG
        img=Image.open(r"college_images\student1.jpg")
        img=img.resize((520,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=520,height=150)

        #Second IMG
        img1=Image.open(r"college_images\student2.jpg")
        img1=img1.resize((520,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=520,y=0,width=500,height=150)

        #bgimage

        img3=Image.open(r"college_images\background.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",22,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1100,height=45)



        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1000,height=600)


        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=0,width=530,height=580)


        


        img_left=Image.open(r"C:\Users\kiran\Desktop\face Recognition System\college_images\image.jpeg")
        img_left=img_left.resize((525,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=525,height=100)



        Left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        Left_inside_frame.place(x=0,y=105,width=520,height=370)





        #student id
        studentId_label=Label(Left_inside_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,pady=5,sticky=W)

        studentID_entry=ttk.Entry(Left_inside_frame,width=11,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,pady=5,sticky=W)

        #Roll
        roll_label=Label(Left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,pady=5,sticky=W)

        roll_entry=ttk.Entry(Left_inside_frame,width=11,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,pady=5,sticky=W)
      
      
        #Name
        name_label=Label(Left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,pady=5,sticky=W)

        name_entry=ttk.Entry(Left_inside_frame,width=11,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,pady=5,sticky=W)


        # Department student 
        deplabel=Label(Left_inside_frame,text="Department:",bg="white",font="conicsansns 11 bold")
        deplabel.grid(row=1,column=2,pady=5,sticky=W)

        atten_dep=ttk.Entry(Left_inside_frame,width=11,textvariable=self.var_atten_dep,font="conicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=5,sticky=W)

        sublabel=Label(Left_inside_frame,text="Time:",bg="white",font="conicsansns 11 bold")
        sublabel.grid(row=2,column=0,pady=5,sticky=W)

        atten_sub=ttk.Entry(Left_inside_frame,width=11,textvariable=self.var_atten_subject,font="conicsansns 11 bold")
        atten_sub.grid(row=2,column=1,pady=5,sticky=W)
         
         
         # date
        datelabel=Label(Left_inside_frame,text="Date:",bg="white",font="conicsansns 11 bold")
        datelabel.grid(row=2,column=2,pady=5,sticky=W)

        atten_date=ttk.Entry(Left_inside_frame,width=11,textvariable=self.var_atten_date,font="conicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=5,sticky=W)

         # Time
        time_label=Label(Left_inside_frame,text="Subject:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=3,column=0,pady=5,sticky=W)

        time_entry=ttk.Entry(Left_inside_frame,width=11,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=3,column=1,pady=5,sticky=W)




        





         # Attendance 
        attendancelabel=Label(Left_inside_frame,text="Attendance Status:",bg="white",font="conicsansns 11 bold")
        attendancelabel.grid(row=4,column=0,pady=5)

        self.atten_status=ttk.Combobox(Left_inside_frame,width=15,textvariable=self.var_atten_attendance,font="conicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=4,column=1,pady=15)
        self.atten_status.current(0)


        #Button Frame
        btn_frame=Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=525,height=40)



        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)


        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Delete",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



        #Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=545,y=0,width=480,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=440,height=455)



        #================scroll bar==============

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","subject","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)




        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("subject",text="Subject")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("time",text="Time")

        self.AttendanceReportTable.heading("attendance",text="SubAttendance")
        

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("subject",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("attendance",width=100)






        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #======================fetch data===================
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata) 


    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showerror("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)              

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values'] 
        self.var_atten_id.set(rows[0])   
        self.var_atten_roll.set(rows[1])           
        self.var_atten_name.set(rows[2])           
        self.var_atten_dep.set(rows[3])           
        self.var_atten_time.set(rows[4])           
        self.var_atten_date.set(rows[5]) 
        self.var_atten_subject.set(rows[5])           
          
        self.var_atten_attendance.set(rows[6]) 


    def reset_data(self):
        self.var_atten_id.set("")   
        self.var_atten_roll.set("")           
        self.var_atten_name.set("")           
        self.var_atten_dep.set("")           
        self.var_atten_time.set("")           
        self.var_atten_date.set("") 
        self.var_atten_subject.set("")   
  
                
        self.var_atten_attendance.set("") 




        

         




if __name__ == "__main__":
    root=Tk()
    obj=Attendance1(root)
    root.mainloop()
