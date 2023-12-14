from cProfile import label
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
 

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("650x620+0+0")
        self.root.bind('<Return>',self.enter_fuc)


        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()


        img_chat=Image.open(r"college_images\chat.jpg")
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor="nw",width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',20,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)


        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=2,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()



        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=38,font=('times new roman',14,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)


        self.send=Button(btn_frame,command=self.send,text="Send>>",font=('times new roman',14,'bold'),width=6,bg='green',)
        self.send.grid(row=0,column=2,padx=5,stick=W)


        self.clear=Button(btn_frame,command=self.clear,text="Clear Data",font=('times new roman',14,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,stick=W)

        self.msg=''
        self.label1_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label1_11.grid(row=1,column=1,padx=5,sticky=W)

       

    def enter_fuc(self,event):
        self.send.invoke()
        #self.entry.set('')
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')   

    
    
    
    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==""):
            self.msg='Please enter some input' 
            self.label1_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label1_11.config(text=self.msg,fg='red')


        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi\n'+'How can i help you')
        elif (self.entry.get()=="hi"):
            self.text.insert(END,"\n\n"+"Bot: Hello")
        
        elif (self.entry.get()=="how are you"):
            self.text.insert(END,"\n\n"+"Bot: fine and you")
        
        elif (self.entry.get()=="fantastic"):
            self.text.insert(END,"\n\n"+"Bot: Nice To Hear")

        elif (self.entry.get()=="who created you"):
            self.text.insert(END,"\n\n"+"Bot: Mr.Kiran Pagar(Pk)")

        elif (self.entry.get()=="What is your name?"):
            self.text.insert(END,"\n\n"+"Bot: My name is Mr. Hacker")

        elif (self.entry.get()=="can you speak Marathi"):
            self.text.insert(END,"\n\n"+"Bot: I'm still learning it.")
                       
        elif (self.entry.get()=="what is machine learning"):
            self.text.insert(END,"\n\n"+"Bot: machine Learning is a branch\nof artificial intelligence (AI) focused\non building applications that learn\nfrom data and improve their accuracy\nover time without being programming\nto do so. ")

        elif (self.entry.get()=="how does face recognition work"):
            self.text.insert(END,"\n\n"+"Bot: Facial recognition is a way of\nrecognizing a human face through\ntechnology. A facial recognition\nsystem uses biometrics to map\nfacial features from a photograph\nor video. It compares the information.")

        elif (self.entry.get()=="How does facial recognition work step by step?"):
            self.text.insert(END,"\n\n"+"Bot: Step1: Face detection. The camera\ndetects and locates the image of a face,\neither alone or in crowd. ...\nStep 2: Face analysis. Next, an image of\n the face is captured and analyzed. ...\nStep 3:  ")
       
        elif (self.entry.get()=="what is chatbot"):
            self.text.insert(END,"\n\n"+"Bot: A chatbot is a computer\nprograme that's designed to\nsimulate human convarsion.")
        
        elif (self.entry.get()=="bye"):
            self.text.insert(END,"\n\n"+"Bot: Thank You for chatting")

        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I did't get it")


                       

      




if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()       