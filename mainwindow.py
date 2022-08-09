from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageGrab
import qrcode
import random
from email.message import EmailMessage
import smtplib
import os
import sqlite3
from tkinter import filedialog
#main front page :
root=Tk()
root.title('TT ID_Generator')
#root.geometry('900x400')
window_heightt = 400
window_widthh = 900
root.resizable(False, False)
screen_widthh = root.winfo_screenwidth()
screen_heightt = root.winfo_screenheight()
x_cordinatee = int((screen_widthh/2) - (window_widthh/2))
y_cordinatee = int((screen_heightt/2) - (window_heightt/2))
root.geometry("{}x{}+{}+{}".format(window_widthh, window_heightt, x_cordinatee, y_cordinatee))
root.iconbitmap('C:/Users/User/Desktop/mainproject/image.ico')
imgquit=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/quit.jpg'))
img1=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/admin.jpg'))
imggue=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/guest.png'))
#this is adminloginpage code
def adminpage():
    win1=Toplevel()
    win1.title('admin_login page')
    #win1.geometry("900x400")
    window_heighttt = 400
    window_widthhh = 900
    win1.resizable(False, False)
    screen_widthhh = win1.winfo_screenwidth()
    screen_heighttt = win1.winfo_screenheight()
    x_cordinateee = int((screen_widthhh/2) - (window_widthhh/2))
    y_cordinateee = int((screen_heighttt/2) - (window_heighttt/2))
    win1.geometry("{}x{}+{}+{}".format(window_widthh, window_heightt, x_cordinateee, y_cordinateee))
    win1.iconbitmap('C:/Users/User/Desktop/mainproject/image.ico')
    global img,img2,imagee
    mainlist=[]
    def my_upd(*args):
        if(len(t1.get())>4):
            butt.config(state='normal')
    def checkbutt_fonc(r1):
        if r1=='1':
            f=open('C:/Users/User/Desktop/mainproject/previous.txt','w+')
            f.write(t1.get()+' '+t2.get()+'\n')

    def listfromtext():
        f=open("C:/Users/User/Desktop/mainproject/admin.txt",'r')
        for x in f:
            l=x.split()
            mainlist.append(l)
        f.close()
        return mainlist

    def advance():
        win1.destroy()
        functionalities()
    def verify(mainlist):
        global index
        result =False
        pos=0
        counterror=0
        while pos< len(mainlist) and not result :
            if mainlist[pos][0]==t1.get() and mainlist[pos][1]==t2.get() :
                result=True

            pos+=1
        if result:
            bout=Button(win1,text="welcome admin ---->",bd=5,command=lambda:advance(),bg='light grey',fg='green',font=('times','14','bold')).place(x=710,y=190)
            index=1
        else : 
            messagebox.showerror(message="wrong infos try again!")
    global list
    list=[]
    def rememberme():
        f=open('C:/Users/User/Desktop/mainproject/previous.txt','r') 
        for i in f:
            l=i.split()
            list.append(l)
        t1.set(list[0][0])
        f.close()
        return True
       # os.remove('C:/Users/User/Desktop/mainproject/previous.txt')  
    def validation(event):
        n=t1.get()
        n1=t2.get()
        if len(n)==0 or len(n1)==0:
            msg.config(text='empty field! ')
        else:
            try:
                if (ch==' ' for ch in n or ch==' ' for ch in n1):
                    msg.config(text='no spaces allwoed ')
            except Exception as ep :
                messagebox.showerror('error',ep)

    def previous2():
            win1.destroy()
            root.deiconify()



#bg image:
    img2=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/login.jpg'))
    img=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/adminimg.jpg'))
    lab0=Label(win1,image=img).grid(row=0,column=0)
    #entries:
    t1=StringVar(win1)
    t2=StringVar()
    u_entry=Entry(win1,width=30,font=("times","19"),textvariable=t1).place(x=300,y=150)
    pass_entry=Entry(win1,show="*",width=30,font=("times","19"),textvariable=t2).place(x=300,y=219)
    r1=StringVar()
    r1.set(None)
    c1=Checkbutton(win1,variable=r1,onvalue='1',bg='grey').place(x=550,y=260)
    c2=Checkbutton(win1,variable=r1,onvalue='0',bg='grey').place(x=550,y=280)
    butt=Button(win1,image=img2,compound=TOP,padx=10,pady=10,command=lambda:verify(mainlist))
    butt.place(x=300,y=300)
    butt2=Button(win1,text='save infos',bg='grey',command=lambda:checkbutt_fonc(r1.get())).place(x=550,y=310)
    imagee=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/quitte.jpg'))
    butt3=Button(win1,border=5,image=imagee,compound=TOP,command=lambda:previous2()).place(x=850,y=350)

    listfromtext()
    rememberme()

def guestpage():
    global img2,img3,img4,imgqui
    win2=Toplevel()
    win2.title('guest page')
    #win2.geometry('900x400')
    window_height = 400
    window_width = 900
    win2.resizable(False, False)
    screen_width = win2.winfo_screenwidth()
    screen_height = win2.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win2.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    win2.iconbitmap('C:/Users/User/Desktop/mainproject/image.ico')
    img2=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/explore.jpg'))
    img3=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/exp.png'))
    img4=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/exp1.png'))
    lab1=Label(win2,image=img2).place(x=0,y=0)
    def app():
        guest_text.delete('1.0',END)
        f=open('C:/Users/User/Desktop/mainproject/app.txt','r')
        guest_text.insert(END,f.read())
        f.close()
    def telinfo():
        guest_text.delete('1.0',END)
        f=open('C:/Users/User/Desktop/mainproject/telinfo.txt','r')
        guest_text.insert(END,f.read())
        f.close()
    def previous1():
        win2.destroy()
        root.deiconify()
    guest_text= Text(win2,width=50,height=13,bd=10,bg='grey',font=("Helvetica",16))
    guest_text.place(x=140,y=10)
    guest_text.insert(END,"""  
    HI i am so glad you decided to try out this APPLICATION.
     here are few TIPS to get you up and running fast:


    1- click on explore this application for further informations about this application
    2- click on 'TUNISIE TELECOM' to know more about the entreprise background and adopted values.
 

    I HOPE YOU LIKE THE CONTENT AND THANK YOU FOR YOUR TIME DEAR USER """)
    imgqui=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/quit.jpg'))
    butt1=Button(win2,text='EXPLORE THE APPLICATION',image=img3,compound=RIGHT,padx=10,pady=2,bd=4,anchor='e',font=('times',12,'bold'),command=lambda:app()).place(x=140,y=348)
    butt2=Button(win2,text="    TUNISIE TELECOM     " ,padx=10,pady=2,image=img4,compound=RIGHT,bd=4,anchor='e',font=('times',12,'bold'),command=lambda:telinfo()).place(x=485,y=347)
    butt3=Button(win2,image=imgqui,compound=TOP,padx=10,pady=10,bd=4,command=lambda:previous1(),font=('times',12,'bold')).place(x=860,y=360)
#functionalities page code:
def functionalities():
        global add_img,modif_img,bg_img,imgquitt
        win4=Toplevel()
        win4.title('directing page')
        #win4.geometry('900x400')
        window_heightttt = 400
        window_widthhhh = 900
        win4.resizable(False, False)
        screen_widthhhh = win4.winfo_screenwidth()
        screen_heightttt = win4.winfo_screenheight()
        x_cordinateeee = int((screen_widthhhh/2) - (window_widthhhh/2))
        y_cordinateeee = int((screen_heightttt/2) - (window_heightttt/2))
        win4.geometry("{}x{}+{}+{}".format(window_widthhhh, window_heightttt, x_cordinateeee, y_cordinateeee))
        win4.iconbitmap('C:/Users/User/Desktop/mainproject/image.ico')
        def back():
            win4.destroy()
            adminpage()
        def register1():
            win4.destroy()
            register()
        def editt1():
            win4.destroy()
            editt()
        bg_img=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/path.jpg'))
        add_img=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/adduser.png'))
        modif_img=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/modif.png'))
        imgquitt=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/quit.jpg'))
        lab1=Label(win4,image=bg_img).grid(row=0,column=0)
        but1=Button(win4,text='ADD USER',font=('times',14,'bold'),image=add_img,compound=TOP,command=lambda:register1()).place(x=100,y=120)
        but2=Button(win4,text='EDIT USER',font=('times',14,'bold'),image=modif_img,compound=TOP,command=lambda:editt1()).place(x=700,y=120)
        butt3=Button(win4,image=imgquitt,compound=TOP,padx=10,pady=10,bd=4,font=('times',12,'bold'),command=lambda:back()).place(x=850,y=355)
#registration page code :
def register():
    global image1,image2,bg_img3,bg_img1,imgvb,imagnext,cpy
    win3=Toplevel()
    win3.title('Registration page')
    #win3.geometry('910x450')
    window_height = 450
    window_width = 910
    win3.resizable(False, False)
    screen_width = win3.winfo_screenwidth()
    screen_height = win3.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win3.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    win3.iconbitmap('C:/Users/User/Desktop/mainproject/image.ico')
    conn=sqlite3.connect("users.db")
    cur=conn.cursor()
    def cincheck(*args):
        for i in v1.get():
            if i not in ['0','1','2','3','4','5','6','7','8','9']:
                messagebox.showerror(message='cin accepts only digital')
                e1.delete(0,'end')
            elif len(v1.get())>8:
                messagebox.showerror(message='cin is only 8 digits long! !')
                e1.delete(0,'end')
    
    def namecheck(*args):
        for i in v2.get():

            if i  in ['0','1','2','3','4','5','6','7','8','9','"','é','&','(',')','-','_','@','ç','^','|','{}','+','*','/','-']:
                messagebox.showwarning(message='please verify your name')
    def poscheck(*args):
        for i in v4.get():

            if i  in ['0','1','2','3','4','5','6','7','8','9','"','é','&','(',')','-','_','@','ç','^','|','{}','+','*','/','-']:
                messagebox.showerror(message='POSITION cant hold digits')   
                e4.delete(0,'end')
    cpy = ''

    def sendcode():
        otp_no = ''
        for _ in range(4):
            r = random.randint(0, 9)
            otp_no += str(r)  
    
        global cpy 
        cpy += otp_no
        sender = "karam.fayek@esprit.tn"
        reciever = e3.get()
        password = "213JMT7417"
        msg_body = f'verification code is {cpy}'
        msg = EmailMessage()
        msg['subject'] = 'OTP'   
        msg['from'] = sender
        msg['to'] = reciever
        msg.set_content(msg_body)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender,password)
        
            smtp.send_message(msg)
    
        print(cpy)
        return cpy  
    def callback():
        value=v3.get()
        exist=0
        for i in value:
            if i =='@':
                exist+=1
        if exist!=1:
            messagebox.showerror(message='email syntax requires @')
        else:
            sendcode()  
    def add_one(id,fname,lname,number,pos):
        conn1=sqlite3.connect('users.db')
        cur=conn1.cursor()
        cur.execute("INSERT INTO users values(?,?,?,?,?)",(id,fname,lname,number,pos))
        conn1.commit()
        conn1.close()           
    def submit():
        expectedcode=cpy
        enteredcode=v5.get()
        cin=v1.get()
        firstlastname=v2.get()
        email=v3.get()
        position=v4.get()
        gender=var.get()
        checkcount=0
        if cin=="":
            messagebox.showwarning(message="cin cant be empty")
        else : checkcount+=1
        if firstlastname=="":
            messagebox.showwarning(message="firstlastname cant be empty")
        else : checkcount+=1
        if email=="":
            messagebox.showwarning(message="email cant be empty")
        else : checkcount+=1
        if position=="":
            messagebox.showwarning(message="position cant be empty")
        else : checkcount+=1
        if gender=="unspecified":
            messagebox.showwarning(message="gender cant be unspecified")
        else : checkcount+=1
        if checkcount==5:
            if(expectedcode==enteredcode):
                add_one(cin,firstlastname,email,position,gender)
            else: messagebox.showerror(message='incorrect verification code')   


    def callback1(*args):
        if r.get()==1 and len(str(v5.get()))==4:
            butt.config(state='normal')
        else :butt.config(state='disabled')
    def import_img():
        f_types=[('jpg files','*.jpg'),('png files','*.png')]
        filename=filedialog.askopenfilename(title='choose an image(.jpg/.png)',initialdir='C:/Users/User/Desktop',filetypes=f_types)
        image_selected=ImageTk.PhotoImage(file=filename)
        lab7=Label(win3,image=image_selected,bg='white',fg='grey')
        lab7.place(x=670,y=297)
        lab7['image']=image_selected

    bg_img3=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/id_card.jpg'))
    lab=Label(win3,image=bg_img3).place(x=0,y=0)
    bg_img1=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/azerty.jpg'))
    lab=Label(win3,image=bg_img1).place(x=50,y=150)
    #labels
    lab1=Label(win3,text='REGISTER HERE:',font=('metalica','14','bold'),bg='white' ).place(x=590,y=90)
    lab2=Label(win3,text='CIN',font=("times new roman",11,"bold"),bg='white',fg='grey').place(x=400,y=150)
    lab3=Label(win3,text='FIRST & LAST NAME',font=("times new roman",11,"bold"),bg='white',fg='grey').place(x=590,y=150)
    lab4=Label(win3,text='EMAIL ADDRESS',font=("times new roman",11,"bold"),bg='white',fg='grey').place(x=400,y=200)
    lab5=Label(win3,text='POSITION',font=("times new roman",11,"bold"),bg='white',fg='grey').place(x=400,y=250)
    lab6=Label(win3,text='GENDER',font=("times new roman",11,"bold"),bg='white',fg='grey').place(x=660,y=250)

    lab8=Label(win3,text='',bg='white',fg='grey').place(x=700,y=400)
    #entries:
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    v4=StringVar()
    v5=StringVar()
    e1=Entry(win3,width=23,bd=2,bg='light grey',textvariable=v1)
    e1.place(x=445,y=152)

    e2=Entry(win3,width=22,bd=2,bg='light grey',textvariable=v2)
    e2.place(x=760,y=152)

    e3=Entry(win3,width=50,bd=2,bg='light grey',textvariable=v3,validate='focusout',validatecommand=callback)
    e3.place(x=550,y=200)
    e4=Entry(win3,width=23,bd=2,bg='light grey',textvariable=v4)
    e4.place(x=511,y=250)
    def nextt():
        win3.destroy()
        dataextraction1()
    def previous():
        win3.destroy()
        functionalities()
    image1=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/image1.png'))
    image2=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/regg.png'))
    imgvb=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/quit.jpg'))            
    butt3=Button(win3,border=5,image=imgvb,compound=TOP,command=previous).place(x=800,y=390)
    imagnext=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/next.png'))
    butt4=butt3=Button(win3,border=3,image=imagnext,compound=TOP,command=lambda:nextt())
    butt4.place(x=850,y=390)
    var=StringVar()
    var.set('unspecified')
    r=IntVar()
    gender=OptionMenu(win3,var,'MALE','FEMALE','OTHER')
    gender.place(x=743,y=245)
    agree=Checkbutton(win3,text='I AGREE TO THE TERMS & CONDITIONS',bg='white',variable=r,onvalue=1,offvalue=0,command=callback1)
    agree.place(x=400,y=350)
    butt=Button(win3,image=image2,bg='light pink',compound=TOP,state='disabled',command=lambda:submit())
    butt.place(x=400,y=385)
    label=Label(win3,text='VERIFICATION CODE',bg='white').place(x=670,y=350)
    verif_entry=Entry(win3,width=15,bd=2,bg='light grey',textvariable=v5)
    verif_entry.place(x=800,y=350)
    v1.trace('w',cincheck)
    v2.trace('w',namecheck)
    v4.trace('w',poscheck)
    v5.trace('w',callback1)
    r.trace('w',callback1)

    conn.commit()
    conn.close()
#editing window code :
def editt():
    global image2,cpy,imag,imagnext1
    win5=Toplevel()
    win5.title('modification page')
    #win5.geometry('900x400')
    window_height = 400
    window_width = 900
    win5.resizable(False, False)
    screen_width = win5.winfo_screenwidth()
    screen_height = win5.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win5.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    win5.iconbitmap('C:/Users/User/Desktop/mainproject/image.ico')
    def val(*args):
        if len(v4.get())==4:
            butt_modif.config(state='normal')
        else:
                    butt_modif.config(state='disabled')


    cpy=''
    def nextt():
        win5.destroy()
        dataextraction1()
    def sendcode1():
        otp_no = ''
        for _ in range(4):
            r = random.randint(0, 9)
            otp_no += str(r)  
    
        global cpy 
        cpy += otp_no
        sender = "karam.fayek@esprit.tn"
        reciever = e3.get()
        password = "213JMT7417"
        msg_body = f'verification code is {cpy}'
        msg = EmailMessage()
        msg['subject'] = 'OTP'   
        msg['from'] = sender
        msg['to'] = reciever
        msg.set_content(msg_body)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender,password)
        
            smtp.send_message(msg)
    
        print(cpy)
        return cpy  

    def checkmail():
        result=0
        for i in v3.get():
            if i =='@':
                result+=1
        if result!=1:
            messagebox.showwarning("email address must have 1 '@'")
        else: 
            sendcode1()
    def pos(*args):
        for i in v1.get():
            if i in ['0','1','2','3','4','5','6','7','8','9','"','é','&','(',')','-','_','@','ç','^','|','{}','+','*','/','-']:
                messagebox.showwarning(message="position can't hold digits or symbols ")
    def pos1(*args):
        for i in v2.get():
            if i in ['0','1','2','3','4','5','6','7','8','9','"','é','&','(',')','-','_','@','ç','^','|','{}','+','*','/','-']:
                messagebox.showwarning(message="first and lastname can't hold digits or symbols ")

    def filterTreeview(*args):
        itemsontreeview=my_tree.get_children()
        search=entry_search.get()
        for eachitem in itemsontreeview:
            if search in my_tree.item(eachitem)['values'][1]:
                search_res=my_tree.item(eachitem)['values']
                my_tree.delete(eachitem)
                my_tree.insert("",0,values=search_res)

    def selectItem():
        curItem = my_tree.focus()
        print (my_tree.item(curItem))           
    
    def del_rec(idd ):
        conn2=sqlite3.connect('users.db')
        c1=conn2.cursor()
        c1.execute("DELETE FROM users where CIN=(?)",(idd,))
        conn2.commit()
        conn2.close()
        x=my_tree.selection()
        for i in x:
            y=messagebox.askokcancel(message="confirm deletion")
            if y==1:
                 my_tree.delete(i)
        e_delete.delete(0,'end')
    def update_rec():

        selected=my_tree.focus()
        values=my_tree.item(selected,'values')
        my_tree.item(selected,text='',values=(values[0],e2.get(),e3.get(),e1.get(),r.get())) 
    
        conn=sqlite3.connect('users.db')
        c=conn.cursor()

        expectedcode=cpy
        enteredcode=v4.get()
        firstlastname=v2.get()
        email=v3.get()
        position=v1.get()
        gender=r.get()
        checkcount=0
        if firstlastname=="":
            messagebox.showwarning(message="firstlastname cant be empty")
        else : checkcount+=1
        if email=="":
            messagebox.showwarning(message="email cant be empty")
        else : checkcount+=1
        if position=="":
            messagebox.showwarning(message="position cant be empty")
        else : checkcount+=1
        if gender=="unspecified":
            messagebox.showwarning(message="gender cant be unspecified")
        else : checkcount+=1
        if checkcount==4:
            if(expectedcode==enteredcode):
                c.execute("""UPDATE users SET 
                    POSITION=:pos,
                    FIRSTandLASTNAME=:fl_name,
                    EMAIL=:mail
                    WHERE CIN=:cin""",
                    {
                         'pos':e1.get(),
                        'fl_name':e2.get(),
                         'mail':e3.get(),
                         'cin':values[0]   
                     }


                    )
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
           
            else: messagebox.showerror(message='incorrect verification code')
        conn.commit()
        conn.close()
    def addfromdb():
        conn2=sqlite3.connect('users.db')
        cur1=conn2.cursor()
        cur1.execute('SELECT * FROM users')
        list=cur1.fetchall()
        for item in list:
                my_tree.insert(parent="",index='end',values=(item[0],item[1],item[2],item[3],item[4]))
    img10=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/quit.jpg'))            
    butt7=Button(win5,border=5,image=img10,compound=TOP,command=lambda:previous())
    butt7.place(x=800,y=300)         
    image2=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/office.jpg'))
    lab_bg=Label(win5,image=image2).grid(row=0,column=0)
    #add some style:
    style=ttk.Style()
    #pick a theme:
    style.theme_use("clam")
    style.configure("Treeview",
        background="silver",
        foreground="black",
        rowheight=25,
        fieldbackground="silver"
        )
    style.map('Treeview',background=[('selected','green')])
    #creating tree
    my_tree =ttk.Treeview(win5,height =6)
    # creating columns:
    my_tree['columns']=("CIN","FIRST&LASTNAME","EMAIL","POSITION","GENDER")
    #format our columns:
    my_tree.column("#0",width=0,stretch=NO)
    my_tree.column("CIN",anchor=CENTER,width=100)
    my_tree.column("FIRST&LASTNAME",anchor=W,width=120)
    my_tree.column("EMAIL",anchor=W,width=180)
    my_tree.column("POSITION",anchor=W,width=100)
    my_tree.column("GENDER",anchor=W,width=70)

# create headings :
    my_tree.heading("#0",text="",anchor=W)
    my_tree.heading("CIN",text="CIN",anchor=W)
    my_tree.heading("FIRST&LASTNAME",text="FIRST&LASTNAME",anchor=W)
    my_tree.heading("EMAIL",text="EMAIL",anchor=W)
    my_tree.heading("POSITION",text='POSITION',anchor=W)
    my_tree.heading("GENDER",text='GENDER',anchor=W)

# add data :
    my_tree.place(x=170,y=190)
#searching:
    entry_search=StringVar()
    del_entry=StringVar()
    label_search=Label(win5,text="SEARCH USER",font=("times new roman",11,"bold"),bg='light grey',fg='black').place(x=600,y=50)
    e_search=Entry(win5,width=15,bg='light grey',font=('times',13),textvariable=entry_search)
    e_search.place(x=720,y=53)  
    e_delete=Entry(win5,width=15,bg='light grey',font=('times',13),textvariable=del_entry)
    e_delete.place(x=720,y=110)

#deleting:
    butt_delete=Button(win5,text="DELETE USER  ",bg='light grey',bd=5,padx=5,pady=5,command=lambda:del_rec(del_entry.get())).place(x=600,y=100)
    lab=Label(win5,text='(select user and type his CIN)',bg='light grey',bd=5,font=('times',9)).place(x=600,y=150)
#modifying:
    image1=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/image1.png'))

    lab2=Label(win5,text='POSITON',font=("times new roman",11,"bold"),bg='light grey',fg='black').place(x=30,y=30)
    lab3=Label(win5,text='FIRST&LASTNAME',font=("times new roman",11,"bold"),bg='light grey',fg='black').place(x=230,y=30)
    lab4=Label(win5,text='EMAIL ADDRESS',font=("times new roman",11,"bold"),bg='light grey',fg='black').place(x=30,y=70)
    lab6=Label(win5,text='GENDER',font=("times new roman",11,"bold"),bg='light grey',fg='black').place(x=30,y=110)
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    v4=StringVar()
    e1=Entry(win5,width=17,bd=2,bg='light grey',textvariable=v1)
    e1.place(x=110,y=30)
    e2=Entry(win5,width=25,bd=2,bg='light grey',textvariable=v2)
    e2.place(x=400,y=30)
    e3=Entry(win5,width=50,bd=2,bg='light grey',textvariable=v3,validate='focusout',validatecommand=checkmail)
    e3.place(x=170,y=70)
    r=StringVar()
    def select_rec():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        selected= my_tree.focus()
        values= my_tree.item(selected,'values')
        e1.insert(0,values[3])
        e2.insert(0,values[1])
        e3.insert(0,values[2])
        e3.focus()
        r.set(values[4])
    def previous3():
        win5.destroy()
        functionalities()
    r.set(None)
    c1=Radiobutton(win5,text='male',variable=r,value="male",bg='light grey',font=('times',11,'bold'))
    c1.place(x=110,y=110)
    c2=Radiobutton(win5,text='female',variable=r,value="female",bg='light grey',font=('times',11,'bold'))
    c2.place(x=170,y=110)
    c3=Radiobutton(win5,text='other',variable=r,value="other",bg='light grey',font=('times',11,'bold'))
    c3.place(x=240,y=110)
    lab=Label(win5,text='VERIFICATION CODE',font=("times new roman",9,"bold"),bg='light grey',fg='black').place(x=320,y=110)
    e4=Entry(win5,width=20,bd=2,bg='light grey',textvariable=v4)
    e4.place(x=460,y=110)



    butt_modif=Button(win5,text='MODIFY USER',bg='light grey',padx=8,pady=8,bd=5,state='disabled',command=update_rec)
    butt_modif.place(x=30,y=260)
    butt_SELECT=Button(win5,text='SELECT USER  ',bg='light grey',padx=8,pady=8,bd=5,command=lambda:select_rec())
    butt_SELECT.place(x=30,y=210)
    imag=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/quittee.jpg'))
    butt30=Button(win5,border=5,image=imag,compound=TOP,command=lambda:previous3())
    butt30.place(x=800,y=350)
    imagnext1=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/next.png'))
    butt43=Button(win5,border=3,image=imagnext1,compound=TOP,command=lambda:nextt())
    butt43.place(x=850,y=350)
#thsi button will be used to pull data from db to treeview
    v1.trace('w',pos)
    v2.trace('w',pos1)
    v4.trace('w',val)

    entry_search.trace('w',filterTreeview)
    addfromdb()

#data extraction code:
def dataextraction1():
    win6=Toplevel()
    win6.title('data extraction page')
    #win6.geometry('900x400')
    window_height = 400
    window_width = 900
    win6.resizable(False, False)
    screen_width = win6.winfo_screenwidth()
    screen_height = win6.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    win6.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    win6.iconbitmap('C:/Users/User/Desktop/mainproject/image.ico')
    global img,image,image1,imags
    def gen_qr():
        global imgqr
        qr=qrcode.QRCode(
        version=1,
        box_size=3,
        border=1
        )
        data=values[1]+ ' ' +values[3]
        qr.add_data(data)
        qr.make(fit=True)
        img=qr.make_image(fill_color='black',back_color='#208d99')
        img.save('id_qr.png')
        imgqr=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/id_qr.png'))
        labqr=Label(top,image=imgqr,highlightthickness=0)
        labqr.place(x=0,y=115)
    def downloadid():
        f_types=[('jpg files','*.jpg'),('png files','*.png')]
        x=filedialog.asksaveasfilename(initialdir='C:/Users/User/Desktop',filetypes=f_types)
        x=x+".png"
        ImageGrab.grab().crop((633,353,981,563)).save(x)
    def data_extraction():
        global top
        global values,imageqot
        top=Toplevel()
        #top.geometry('350x200')
        top.title('id card ')
        top.iconbitmap('C:/Users/User/Desktop/mainproject/image.ico')
        lab=Label(top,image=img1).grid(row=0,column=0)
        window_height = 250
        window_width = 350
        top.resizable(False, False)
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        def returnback():
            top.destroy()
            win6.deiconify()
        butt=Button(top,image=image1,bg='light grey',compound=TOP,command=select_img)
        butt.place(x=10,y=35)
        lab1=Label(top,text='F&LNAME : ',bg='#0270ab',font=('times',11,'bold')).place(x=90,y=30)
        lab2=Label(top,text='GENDER : ',bg='#0270ab',font=('times',11,'bold')).place(x=90,y=60)
        lab3=Label(top,text='POSITION : ',bg='#0270ab',font=('times',11,'bold')).place(x=90,y=90)
        lab4=Label(top,text='EMAIL : ',bg='#0270ab',font=('times',11,'bold')).place(x=110,y=140)
        selected= my_tree.focus()
        values= my_tree.item(selected,'values')
        lab5=Label(top,text=values[1],bg="#0270ab",font=('times',10,'bold')).place(x=180,y=30)
        lab6=Label(top,text=values[4],bg="#0270ab",font=('times',10,'bold')).place(x=170,y=60)
        lab7=Label(top,text=values[3],bg="#0270ab",font=('times',10,'bold')).place(x=170,y=90)
        lab8=Label(top,text=values[2],bg="#0270ab",font=('times',10,'bold')).place(x=190,y=140)
        butt_validate=Button(top,text='DOWNLOAD ID_CARD',bg='light grey',font=('times',9,'bold'),padx=10,pady=11,command=lambda:downloadid())
        butt_validate.place(x=0,y=205)
        imageqot=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/quitte.jpg'))
        butt_quiitt=Button(top,bd=5,bg='light grey',image=imageqot,command=lambda:returnback())
        butt_quiitt.place(x=157,y=207)
        butt_qr=Button(top,text='GENERATE QR CODE',bg='light grey',padx=9,pady=11,font=('times',9,'bold'),command=lambda:gen_qr())
        butt_qr.place(x=199,y=205)
        top.mainloop()
    def addfromdb():
        conn2=sqlite3.connect('users.db')
        cur1=conn2.cursor()
        cur1.execute('SELECT * FROM users')
        list=cur1.fetchall()
        for item in list:
                 my_tree.insert(parent="",index='end',values=(item[0],item[1],item[2],item[3],item[4]))
    def select_img():
        global img
        f_types=[('jpg files','*.jpg'),('png files','*.png')]
        filename=filedialog.askopenfilename(initialdir='C:/Users/User/Desktop',filetypes=f_types)
        img=ImageTk.PhotoImage(file=filename)
        lab=Label(top,image=img)
        lab.place(x=5,y=5)
        lab['image']=img
    def data_extraction1():
        win6.withdraw()
        data_extraction()
    def previous4():
        win6.destroy()
        functionalities()
    style=ttk.Style()
#pick a theme:
    style.theme_use("clam")
    style.configure("Treeview",
        background="silver",
        foreground="black",
        rowheight=25,
        fieldbackground="silver"
        )
    style.map('Treeview',background=[('selected','green')])
    my_tree =ttk.Treeview(win6,height =6)
# creating columns:
    my_tree['columns']=("CIN","FIRST&LASTNAME","EMAIL","POSITION","GENDER")
#format our columns:
    my_tree.column("#0",width=0,stretch=NO)
    my_tree.column("CIN",anchor=CENTER,width=100)
    my_tree.column("FIRST&LASTNAME",anchor=W,width=120)
    my_tree.column("EMAIL",anchor=W,width=180)
    my_tree.column("POSITION",anchor=W,width=100)
    my_tree.column("GENDER",anchor=W,width=70)

# create headings :
    my_tree.heading("#0",text="",anchor=W)
    my_tree.heading("CIN",text="CIN",anchor=W)
    my_tree.heading("FIRST&LASTNAME",text="FIRST&LASTNAME",anchor=W)
    my_tree.heading("EMAIL",text="EMAIL",anchor=W)
    my_tree.heading("POSITION",text='POSITION',anchor=W)
    my_tree.heading("GENDER",text='GENDER',anchor=W)
    img1=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/idbg.png'))
# add data :
    my_tree.place(x=310,y=210)
    image=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/idcard.jpg'))
    lab_bg=Label(win6,image=image).place(x=0,y=0)
    imags=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/quittee.jpg'))
    butt31=Button(win6,border=5,image=imags,compound=TOP,command=lambda:previous4())
    butt31.place(x=850,y=15)
    id_gen=Button(win6,text='GET DATA AND GENERATE ID',bd=5,padx=10,bg='light grey',pady=10,command=lambda:data_extraction1()).place(x=500,y=90)
    image1=ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/mainproject/image1.png'))

    addfromdb()

#this is main window code :
global our_images,count
count=-1
our_images=[
PhotoImage(file='C:/Users/User/Desktop/mainproject/1.png'),
PhotoImage(file='C:/Users/User/Desktop/mainproject/2.png'),
PhotoImage(file='C:/Users/User/Desktop/mainproject/3.png'),
PhotoImage(file='C:/Users/User/Desktop/mainproject/4.png'),
PhotoImage(file='C:/Users/User/Desktop/mainproject/5.png')]
def adminpage1():
    root.withdraw()
    pass
    adminpage()
def guestpage1():
    root.withdraw()
    guestpage()
canva=Canvas(root,width=600,height=400)
canva.pack(fill="both",expand='True')
canva.create_image(0,0,image=our_images[0],anchor='nw')
canvas=Canvas(canva,width=240,height=400,bd=4,bg='white' ).place(x=660,y=0)
label=Label(root,text='WELCOME!',font='helvetica 13 bold',fg='green',bg='white',bd=4,padx=10,pady=5).place(x=710,y=35)
butt1=Button(root,text='Login as ADMINISTRATOR',border=5,image=img1,compound=RIGHT,command=lambda:adminpage1()).place(x=690,y=100)
butt2=Button(root,text='Login as GUEST        ',border=5,image=imggue,compound=RIGHT,command=lambda:guestpage1()).place(x=690,y=150)
butt3=Button(root,border=5,image=imgquit,compound=TOP,command=root.quit).place(x=850,y=350)
""" 
Buut=Button(root,border=5,padx=15,pady=1,image=img1,coompund=TOP,command=go_login).place(x=690,y=50)
butt3=Button(root,border=5,image=img3,compound=TOP,command=root.quit).place(x=720,y=130)
"""

def next():
    global count
    if count==4:
        canva.create_image(0,0,image=our_images[0],anchor='nw')
        count=0
    else:
        canva.create_image(0,0,image=our_images[count+1],anchor='nw')
        count+=1
        root.after(4000,next)
next()
root.mainloop()

