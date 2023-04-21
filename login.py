from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import random
import time
import datetime
from time import strftime
from datetime import datetime
from student import Student
from face_detector import Face_Detector
from train import Train
from tkinter import messagebox
import mysql.connector
from attendance import Attendance
from main import face_recognition_system


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x900+0+0")


        # ===========VARIABLES=====================
        self.fname = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.combo_security_Q = StringVar()
        self.txt_security_A = StringVar()
        self.fname.set("")
        self.email.set("")
        self.password.set("")
        self.combo_security_Q.set("")
        self.txt_security_A.set("")
        img = Image.open(r"ImagesBasics\loginbg.jpg")
        img = img.resize((1540, 780), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_bg=Label(self.root, image=self.photoimg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=500)


        img1=Image.open(r"ImagesBasics\logo.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_img1=Label(self.root,image=self.photoimg1,bg="black",bd=0)
        lbl_img1.place(x=730,y=175,width=100,height=107)



        get_str=Label(frame,text="Get Started",font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95,y=120)

        # label
        username=Label(frame,text="Username",font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=40,y=160)

        self.user=Entry(frame,font=("times new roman", 15, "bold"))
        self.user.place(x=15,y=185,width=270)

        email=Label(frame,text="Email",font=("times new roman", 15, "bold"), fg="white", bg="black")
        email.place(x=40,y=225)

        self.email=Entry(frame,font=("times new roman", 15, "bold"))
        self.email.place(x=15,y=250,width=270)


        password=Label(frame,text="Password",font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=40,y=290)

        self.password=Entry(frame,font=("times new roman", 15, "bold"))
        self.password.place(x=15,y=315,width=270)


# Icon images
        img2=Image.open(r"ImagesBasics\lg.png")
        img2=img2.resize((30,25),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl_img2=Label(self.root,image=self.photoimg2,bg="black",bd=0)
        lbl_img2.place(x=625,y=328,width=28,height=25)


        img3=Image.open(r"ImagesBasics\email.png")
        img3=img3.resize((30,25),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl_img3=Label(self.root,image=self.photoimg3,bg="black",bd=0)
        lbl_img3.place(x=625,y=393,width=28,height=25)


        img4=Image.open(r"ImagesBasics\ps.png")
        img4=img4.resize((30,25),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbl_img4=Label(self.root,image=self.photoimg4,bg="black",bd=0)
        lbl_img4.place(x=625,y=458,width=28,height=25)

        #  Login button
        log_btn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), borderwidth=0, relief=RIDGE, bg="dark green", fg="white", 
                          activebackground="red", activeforeground="white")
        log_btn.place(x=80, y=350, width=120, height=30)

# Register button
        reg = Button(frame, text="Register New User", command=self.Register_Window, font=("times new roman", 15, "bold"), borderwidth=0, relief=RIDGE, bg="black", fg="white", 
                          activebackground="black", activeforeground="white")
        reg.place(x=15, y=390, width=160)


        # forget password
        forget = Button(frame, text="Forget Password", command=self.forget_data, font=("times new roman", 15, "bold"), borderwidth=0, relief=RIDGE, bg="black", fg="white", 
                          activebackground="black", activeforeground="white")
        forget.place(x=10, y=430, width=160)


    def Register_Window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_Windows(self.new_window)

    def main_data(self):
            self.new_window = Toplevel(self.root)
            self.app = face_recognition_system(self.new_window)



    
    def login(self):
            email = self.email.get()
            password = self.password.get()
            if self.email.get() == "" or self.password.get() == "Select":
                messagebox.showerror("Error", "All Fields are Required!", parent=self.root)
            # elif not self.email.get() or not self.confpass.get():
            #     messagebox.showerror("Error", "Email and password are required", parent=self.root)
            else:
                try:
                    con = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
                    cursor = con.cursor()
                    cursor.execute("select * from registers where email=%s and password=%s", 
                                    (self.email.get(), self.password.get()))
                    row = cursor.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Invalid Username or Password!", parent=self.root)
                    else:
                        open_main = messagebox.askyesno("YesNo", "Access only admin", parent=self.root)
                        if open_main:
                            self.new_window = Toplevel(self.root)
                            self.app = face_recognition_system(self.new_window)
                            # self.app.open_mainloop()
                        else:
                            return

                    con.commit()
                    # con.close()

                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)


    def reset(self):
            if self.combo_security_Q.get() == "Select security question":
                # print(self.combo_security_Q)
                messagebox.showerror("Error", "Please select a security question", parent=self.root)

            elif self.txt_security_A.get() == "":
                messagebox.showerror("Error","Please enter the answer to security question",parent=self.root)
            elif self.txt_newpass.get() == "":
                messagebox.showerror("Error","Please enter the new password",parent=self.root)
            else:
                conn = mysql.connector.connect(host="localhost",user="root",password="",database="recognizer")
                my_cursor = conn.cursor()
                query = "SELECT * FROM registers WHERE email=%s AND securityQ=%s AND securityA=%s"
                value = (self.user.get(), self.combo_security_Q.get(), self.txt_security_A.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error","Please enter the correct answer",parent=self.root)
                else:
                    query = "UPDATE registers SET password=%s WHERE email=%s"
                    value = (self.txt_newpass.get(), self.user.get())
                    my_cursor.execute(query, value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Your Password has been Reset, please enter your new password",parent=self.root)
                    self.root.destroy()



         # =======================Forget Password===========================
    def forget_data(self):
        if self.email.get() == "":
            messagebox.showerror("Error", "Please write the email address to reset the password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
            my_cursor = conn.cursor()
            query = "SELECT * FROM registers WHERE email = %s"
            value = (self.email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Error", "Please enter a valid email address")
            else:
                self.root = Toplevel()
                self.root.title("Forget password")
                self.root.geometry("340x450+610+170")

                l = Label(self.root, text="Forget Password", font=("times new roman", 12, "bold"), relief=RIDGE, bg="white", fg="red")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root, text="Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_Q.place(x=50, y=80)

                security_Q_combo = ttk.Combobox(self.root, font=("times new roman", 12, "bold"), width=17)
                security_Q_combo["values"] = ("Select Security Question", "Your Birth Place", "Your Pet's Name", "Your Father's Name", "Your Mum's Name")
                security_Q_combo.current(0)
                security_Q_combo.place(x=50, y=110, width=250)

                security_A = Label(self.root, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
                security_A.place(x=50, y=150)

                self.security_A_entry = ttk.Entry(self.root, textvariable=self.txt_security_A, font=("times new roman", 15, "bold"))
                self.security_A_entry.place(x=50, y=180, width=250)

                new_password = Label(self.root, text="New Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root, text="Reset", command=self.reset, font=("times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=100, y=290)

            # =================reset password=============

    

    # def reset(self):
    #     if self.combo_security_Q.get()=="":
    #         messagebox.showerror("Error","Select security question",parent=self.root)
    #     elif self.txt_security_A.get()=="":
    #         messagebox.showerror("Error","Please enter the answer to security question",parent=self.root)
    #     elif self.txt_newpass.get()=="":
    #         messagebox.showerror("Error","Please enter the new password",parent=self.root)
    #     else:
    #         conn=mysql.connector(host="localhost",user="root",password="",database="recognizer")
    #         my_cursor=conn.cursor()
    #         query=("select * from registers where email=%s and securityQ=%s and securityA=%s")
    #         value=(self.user.get(),self.combo_security_Q.get(),self.txt_security.get())
    #         my_cursor.execute(query,value)
    #         row=my_cursor.fetchone()
    #         if row==None:
    #             messagebox.showerror("Error","Please enter the correct answer",parent=self.root)
    #         else:
    #             query=("Update registers set password=%s where email=%s")
    #             value=(self.txt_newpass.get(),self.user.get())
    #             my_cursor.execute(query,value)
    #             conn.commit()
    #             conn.close()
    #             messagebox.showinfo("Success","Your Password has been Reset, please enter your new password",parent=self.root)

    #             self.root.destroy()


class Register_Windows:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confpass = StringVar()

        img = Image.open(r"ImagesBasics\loginbg.jpg")
        img = img.resize((1540, 780), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_bg = Label(self.root, image=self.photoimg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 15, "bold"), fg="black", bg="white")
        register_lbl.place(x=20, y=20)

        # label entry
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        lname.place(x=370, y=100)

        self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.lname_entry.place(x=370, y=130, width=250)

        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), fg="black", bg="white")
        contact.place(x=50, y=170)

        self.contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.contact_entry.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="black", bg="white")
        email.place(x=370, y=170)

        self.email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.email_entry.place(x=370, y=200, width=250)

        securityQ = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), state="disabled", fg="black", bg="white")
        securityQ.place(x=50, y=240)

        securityQ_combo = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 12, "bold"), width=17)
        securityQ_combo["values"] = ("Select", "Your Birth Place", "Your Pet's Name", "Your Father's Name", "Your Mum's Name")
        securityQ_combo.current(0)
        securityQ_combo.place(x=50, y=270, width=250)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        pass_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        pass_lbl.place(x=50, y=310)

        self.txt_pass = ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 15, "bold"), show="*")
        self.txt_pass.place(x=50, y=340, width=250)

        confpass_lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        confpass_lbl.place(x=370, y=310)

        self.txt_confpass = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"), show="*")
        self.txt_confpass.place(x=370, y=340, width=250)

        # check button
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree to the Terms & Conditions", font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        # buttons
        img = Image.open(r"ImagesBasics\register.jpg")
        img = img.resize((200, 45), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        b1 = Button(frame, command=self.register_data, image=self.photoimage, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="dark green", bg="white")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"ImagesBasics\heyy.jpg")
        img1 = img1.resize((200, 65), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        b2 = Button(frame, image=self.photoimage1, command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="dark green", bg="white")
        b2.place(x=330, y=420, width=200, height=60)

        # ========function declarations=======
    def register_data(self):
        required_fields = [self.var_fname, self.var_email, self.var_securityQ]
        if not all(field.get() for field in required_fields):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
                # Ensure password and confirm password match
        elif self.var_password.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
            return
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into registers values(%s, %s, %s, %s, %s, %s, %s)",(
                 self.var_fname.get(),
                 self.var_lname.get(),
                 self.var_contact.get(),
                 self.var_email.get(),
                 self.var_securityQ.get(),
                 self.var_securityA.get(),
                 self.var_password.get(),
            ))

            # Clear input fields
            self.var_fname.set('')
            self.var_lname.set('')
            self.var_email.set('')
            self.var_password.set('')
            self.var_confpass.set('')
            self.var_securityQ.set('')
            self.var_securityA.set('')

            conn.commit()
            messagebox.showinfo("Success", "Registered successfully", parent=self.root)


    
    def return_login(self):
        self.root.destroy()


# class face_recognition_system:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

# #         =================variables============
#         self.var_dep = StringVar()
#         self.var_course = StringVar()
#         self.var_year = StringVar()
#         self.var_semester = StringVar()
#         self.var_id = StringVar()
#         self.var_name = StringVar()
#         self.var_reg = StringVar()
#         self.var_gender = StringVar()
#         self.var_grp = StringVar()
#         self.var_email = StringVar()
#         self.var_phone = StringVar()
#         self.var_lec = StringVar()
#         self.var_photo = StringVar()


# #         first image
#         img = Image.open(r"ImagesBasics\detector.jpg")
#         img = img.resize((500, 130), Image.LANCZOS)
#         self.photoimga = ImageTk.PhotoImage(img)

#         f_lbl = Label(self.root, image=self.photoimga)
#         f_lbl.place(x=0, y=0, width=500, height=130)

# #     second image
#         img = Image.open(r"ImagesBasics\faces.jpg")
#         img = img.resize((500, 130), Image.LANCZOS)
#         self.photoimgb = ImageTk.PhotoImage(img)

#         f_lbl = Label(self.root, image=self.photoimgb)
#         f_lbl.place(x=500, y=0, width=500, height=130)

# #         third image
#         img = Image.open(r"ImagesBasics\img3.jfif")
#         img = img.resize((550, 130), Image.LANCZOS)
#         self.photoimgc = ImageTk.PhotoImage(img)

#         f_lbl = Label(self.root, image=self.photoimgc)
#         f_lbl.place(x=1000, y=0, width=550, height=130)

# #         background image
#         img = Image.open(r"ImagesBasics\bgimg1.jfif")
#         img = img.resize((1530, 710), Image.LANCZOS)
#         self.photoimgd = ImageTk.PhotoImage(img)

#         bg_img = Label(self.root, image=self.photoimgd)
#         bg_img.place(x=0, y=130, width=1530, height=710)

#         title_lbl = Label(bg_img, text="FACE DETECTION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"),
#                           bg="white", fg="dark green")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         # Time
#         def time():
#             string = strftime('%H:%M:%S %p')
#             lbl.config(text=string)
#             lbl.after(1000, time)

#         lbl = Label(title_lbl, font = ('times new roman', 14, 'bold'), bg='white', fg='blue')
#         lbl.place(x=0, y=0, width=110, height=50)
#         time()


#         #         Student button
#         img = Image.open(r"ImagesBasics\attendance.jpg")
#         img = img.resize((220, 200), Image.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)

#         b1 = Button(bg_img, image=self.photoimg, cursor="hand2")
#         b1.place(x=200, y=100, width=220, height=200)

#         b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
#                       font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
#         b1_1.place(x=200, y=300, width=220, height=40)


#         #         Administration button
#         img1 = Image.open(r"ImagesBasics\admin.jpg")
#         img1 = img1.resize((220, 200), Image.LANCZOS)
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         b4 = Button(bg_img, image=self.photoimg1, cursor="hand2")
#         b4.place(x=500, y=100, width=220, height=200)

#         b2_4= Button(bg_img, text="Administration", cursor="hand2", font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
#         b2_4.place(x=500, y=300, width=220, height=40)



#         #         Detect Face button
#         img2 = Image.open(r"ImagesBasics\detector.jpg")
#         img2 = img2.resize((220, 200), Image.LANCZOS)
#         self.photoimg2 = ImageTk.PhotoImage(img2)

#         b2 = Button(bg_img, image=self.photoimg2, cursor="hand2")
#         b2.place(x=800, y=100, width=220, height=200)

#         b2_2 = Button(bg_img, text="Face Detector", command=self.face_data, cursor="hand2", font=("times new roman", 12, "bold"),
#                     bg="darkblue", fg="white")
#         b2_2.place(x=800, y=300, width=220, height=40)


#         #         Attendance button
#         img3 = Image.open(r"ImagesBasics\student.jpg")
#         img3 = img3.resize((220, 200), Image.LANCZOS)
#         self.photoimg3 = ImageTk.PhotoImage(img3)

#         b3 = Button(bg_img, image=self.photoimg3, cursor="hand2")
#         b3.place(x=1100, y=100, width=220, height=200)

#         b3_1= Button(bg_img, text="Attendance", command=self.attendance_data, cursor="hand2", font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
#         b3_1.place(x=1100, y=300, width=220, height=40)


#         #         Train button
#         img4 = Image.open(r"ImagesBasics\recognizer.jpg")
#         img4 = img4.resize((220, 200), Image.LANCZOS)
#         self.photoimg4 = ImageTk.PhotoImage(img4)

#         b4 = Button(bg_img, image=self.photoimg4, cursor="hand2")
#         b4.place(x=200, y=380, width=220, height=200)

#         b2_4= Button(bg_img, text="Train Data", command=self.training_data, cursor="hand2", font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
#         b2_4.place(x=200, y=580, width=220, height=40)


#         #         Photos button
#         img5 = Image.open(r"ImagesBasics\pics.jpg")
#         img5 = img5.resize((220, 220), Image.LANCZOS)
#         self.photoimg5 = ImageTk.PhotoImage(img5)

#         b5 = Button(bg_img, image=self.photoimg5, cursor="hand2")
#         b5.place(x=500, y=380, width=220, height=220)

#         b5_4= Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
#         b5_4.place(x=500, y=580, width=220, height=40)


#         #         Exit button
#         img6 = Image.open(r"ImagesBasics\exit.png")
#         img6 = img6.resize((220, 220), Image.LANCZOS)
#         self.photoimg6 = ImageTk.PhotoImage(img6)

#         b6 = Button(bg_img, image=self.photoimg6, cursor="hand2")
#         b6.place(x=800, y=380, width=220, height=220)

#         b6_4= Button(bg_img, text="Exit", cursor="hand2", command=self.return_login, font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
#         b6_4.place(x=800, y=580, width=220, height=40)
        
#     def open_img(self):
#         os.startfile("data")


#     def iExit(self):
#         self.iExit=tkinter.messagebox.askyesno("Face Detection","Do you want to exit? ", parent=self.root)
#         if self.iExit>0:
#             self.root.destroy()
#         else:
#             return 
#         # return_login()
#     def return_login(self):
#         self.iExit=tkinter.messagebox.askyesno("Face Detection","Do you want to exit? ", parent=self.root)
#         if self.return_login>0:
#             self.root.destroy()
#         else:
#             return

#         # Function button
#     def student_details(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Student(self.new_window)



#     def face_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Face_Detector(self.new_window)


#     def training_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Train(self.new_window)


#     def attendance_data(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Attendance(self.new_window)


if __name__ == "__main__":
    main()
