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



class Devloper:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="DEVLOPER",font=("times new roman",22,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1100,height=45)
       

        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1050,630),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1050,height=630)





        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=700,y=10,width=300,height=500)


        
        img_top1=Image.open(r"college_images\kiran.jpg")
        img_top1=img_top1.resize((200,160),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=170,y=0,width=200,height=160)



        dev_lbl=Label(main_frame,text="Hello my name,kiran",font=("times new roman",13,"bold"),bg="white",fg="black")
        dev_lbl.place(x=0,y=5)

        dev_lbl=Label(main_frame,text="I am Software engineer",font=("times new roman",13,"bold"),bg="white",fg="black")
        dev_lbl.place(x=0,y=40)

        dev_lbl=Label(main_frame,text="Contact:9518706462",font=("times new roman",13,"bold"),bg="white",fg="black")
        dev_lbl.place(x=0,y=80)

        dev_lbl=Label(main_frame,text="Gmail ID:-",font=("times new roman",13,"bold"),bg="white",fg="black")
        dev_lbl.place(x=0,y=120)

        dev_lbl=Label(main_frame,text="kiranpagar2611@gmail.com",font=("times new roman",13,"bold"),bg="white",fg="black")
        dev_lbl.place(x=0,y=160)



        img2=Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((500,390),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)

        
       







        
















if __name__ == "__main__":
    root=Tk()
    obj=Devloper(root)
    root.mainloop()
