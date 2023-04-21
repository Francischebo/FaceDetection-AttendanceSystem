from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from face_detector import Face_Detector
from train import Train
from tkinter import messagebox
from attendance import Attendance



class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

#         =================variables============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_reg = StringVar()
        self.var_gender = StringVar()
        self.var_grp = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_lec = StringVar()
        self.var_photo = StringVar()


#         first image
        img = Image.open(r"ImagesBasics\detector.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimga = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimga)
        f_lbl.place(x=0, y=0, width=500, height=130)

#     second image
        img = Image.open(r"ImagesBasics\faces.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimgb = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimgb)
        f_lbl.place(x=500, y=0, width=500, height=130)

#         third image
        img = Image.open(r"ImagesBasics\img3.jfif")
        img = img.resize((550, 130), Image.LANCZOS)
        self.photoimgc = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimgc)
        f_lbl.place(x=1000, y=0, width=550, height=130)

#         background image
        img = Image.open(r"ImagesBasics\bgimg1.jfif")
        img = img.resize((1530, 710), Image.LANCZOS)
        self.photoimgd = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimgd)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE DETECTION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"),
                          bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font = ('times new roman', 14, 'bold'), bg='white', fg='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()


        #         Student button
        img = Image.open(r"ImagesBasics\attendance.jpg")
        img = img.resize((320, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1 = Button(bg_img, image=self.photoimg, cursor="hand2")
        b1.place(x=200, y=100, width=320, height=200)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                      font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=320, height=40)



        #         Detect Face button
        img2 = Image.open(r"ImagesBasics\detector.jpg")
        img2 = img2.resize((320, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(bg_img, image=self.photoimg2, cursor="hand2")
        b2.place(x=600, y=100, width=320, height=200)

        b2_2 = Button(bg_img, text="Face Detector", command=self.face_data, cursor="hand2", font=("times new roman", 12, "bold"),
                    bg="darkblue", fg="white")
        b2_2.place(x=600, y=300, width=320, height=40)


        #         Attendance button
        img3 = Image.open(r"ImagesBasics\student.jpg")
        img3 = img3.resize((320, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(bg_img, image=self.photoimg3, cursor="hand2")
        b3.place(x=1000, y=100, width=320, height=200)

        b3_1= Button(bg_img, text="Attendance", command=self.attendance_data, cursor="hand2", font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=1000, y=300, width=320, height=40)


        #         Train button
        img4 = Image.open(r"ImagesBasics\recognizer.jpg")
        img4 = img4.resize((320, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        b4.place(x=200, y=380, width=320, height=200)

        b2_4= Button(bg_img, text="Train Data", command=self.training_data, cursor="hand2", font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
        b2_4.place(x=200, y=580, width=320, height=40)


        #         Photos button
        img5 = Image.open(r"ImagesBasics\pics.jpg")
        img5 = img5.resize((320, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b5.place(x=600, y=380, width=320, height=220)

        b5_4= Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
        b5_4.place(x=600, y=580, width=320, height=40)


        #         Exit button
        img6 = Image.open(r"ImagesBasics\exit.png")
        img6 = img6.resize((320, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b6.place(x=1000, y=380, width=320, height=220)

        b6_4= Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
        b6_4.place(x=1000, y=580, width=320, height=40)
        
    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Detection","Do you want to exit? ", parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        # Function button
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)



    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Detector(self.new_window)


    def training_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()