from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
import face_recognition
from datetime import datetime
import base64
import dill



class Student:
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
        self.var_search_combo = StringVar()
        self.var_search_entry = StringVar()


#         first image
        img = Image.open(r"ImagesBasics\img1.jfif")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

#     second image
        img1 = Image.open(r"ImagesBasics\img2.jfif")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

#         third image
        img2 = Image.open(r"ImagesBasics\img3.jfif")
        img2 = img2.resize((550, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

#         background image
        img3 = Image.open(r"ImagesBasics\bgimg1.jfif")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

#         left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=550)

        img_left = Image.open(r"ImagesBasics\hi.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

#         current course
        Current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        Current_course_frame.place(x=5, y=135, width=720, height=115)

        dep_label = Label(Current_course_frame, text="Department", font=("times new roman", 12, "bold"),
                          state="disabled", bg="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=17)
        dep_combo["values"] = ("Select Department", "Computer Science", "IT", "Mathematics", "Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

#         course
        course_label = Label(Current_course_frame, text="Course", font=("times new roman", 12, "bold"),
                          state="disabled", bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), width=17)
        course_combo["values"] = ("Select Course", "Computer Science", "IT", "TLC", "Actuarial Sci","Electrical Eng.")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #         year
        year_label = Label(Current_course_frame, text="Year", font=("times new roman", 12, "bold"),
                             state="disabled", bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17)
        year_combo["values"] = ("Select year", "2016-2020", "2017-2021", "2018-2022", "2019-2023", "2020-2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #         semester
        semester_label = Label(Current_course_frame, text="Semester", font=("times new roman", 12, "bold"),
                           state="disabled", bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17)
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        Class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Class Student Information", font=("times new roman", 12, "bold"))
        Class_Student_frame.place(x=5, y=250, width=720, height=270)

        #         studentId
        id_label = Label(Class_Student_frame, text="StudentID:", font=("times new roman", 12, "bold"),
                               state="disabled", bg="white")
        id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        id_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_id, width=20, font=("times new roman", 12, "bold"))
        id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #         student name
        name_label = Label(Class_Student_frame, text="Student Name:", font=("times new roman", 12, "bold"),
                                state="disabled", bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #         class group
        grp_label = Label(Class_Student_frame, text="Group:", font=("times new roman", 12, "bold"),
                                  state="disabled", bg="white")
        grp_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        grp_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_grp,
                                    font=("times new roman", 12, "bold"), width=17)
        grp_combo["values"] = ("A", "B", "C")
        grp_combo.current(0)
        grp_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        #         registration number
        reg_label = Label(Class_Student_frame, text="Registration Number:", font=("times new roman", 12, "bold"),
                                state="disabled", bg="white")
        reg_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        reg_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_reg, width=20, font=("times new roman", 12, "bold"))
        reg_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #         Gender
        gender_label = Label(Class_Student_frame, text="Gender:", font=("times new roman", 12, "bold"),
                            state="disabled", bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_gender,
                                  font=("times new roman", 12, "bold"), width=17)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=5, sticky=W)

        #         Email
        email_label = Label(Class_Student_frame, text="Email:", font=("times new roman", 12, "bold"),
                             state="disabled", bg="white")
        email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #         Phone Number
        phone_label = Label(Class_Student_frame, text="Phone Number:", font=("times new roman", 12, "bold"),
                            state="disabled", bg="white")
        phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        #         Lecturer Name
        lec_label = Label(Class_Student_frame, text="Lecturer Name:", font=("times new roman", 12, "bold"),
                              state="disabled", bg="white")
        lec_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        lec_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_lec, width=20, font=("times new roman", 12, "bold"))
        lec_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        # radio Buttons
        self.var_radio1 = StringVar()
        radio_btn_1 = ttk.Radiobutton(Class_Student_frame, variable=self.var_radio1, text="Take Photo Sample",
                                      value="Yes")
        radio_btn_1.grid(row=6, column=0)

        radio_btn_2 = ttk.Radiobutton(Class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radio_btn_2.grid(row=6, column=1)

        # button frame
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=170, width=715, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=19, font=("times new roman", 12, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=19, font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=19, font=("times new roman", 12,
                                                                                                "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19, font=("times new roman", 12,
                                                                                             "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=1, y=200, width=715, height=35)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, width=40, font=("times new roman", 12, "bold"),
                                bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, command=self.update_photo, text="Update Photo Sample", width=40, font=("times new roman", 12, "bold")
                                  , bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=550)

        img_right = Image.open(r"ImagesBasics\developers.jpg")
        img_right = img_right.resize((710, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=710, height=130)

#         =============Search System==========

        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"),
                               state="disabled", bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), width=17)
        search_combo["values"] = ("Search By", "Reg_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame,command=self.search_data, text="Search", width=13, font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(Search_frame, text="Show All", width=13, font=("times new roman", 12, "bold"), bg="blue",
                           fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)
        # ======Table Frame=======
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=310)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course",
                                                               "year", "semester", "name",
                                                                "reg", "gender", "grp",
                                                               "email", "phone", "lec", "photo", "id"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("reg", text="Registration Number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("grp", text="Group")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("lec", text="Lecturer")
        self.student_table.heading("photo", text="Photo")
        self.student_table.heading("id", text="ID")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        def show_all_data(self):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
            cur = conn.cursor()
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            # Close the connection
            conn.close()

            # Create a table to display the data
            table = ttk.Treeview(self.root, columns=("reg", "name", "gender", "phone", "email", "dob", "address"))
            table.heading("reg", text="Reg No.")
            table.heading("name", text="Name")
            table.heading("gender", text="Gender")
            table.heading("phone", text="Phone No.")
            table.heading("email", text="Email")
            table.heading("dob", text="Date of Birth")
            table.heading("address", text="Address")

            # Add the data to the table
            for row in rows:
                table.insert("", END, values=row)

            table.pack(pady=20)

# =============function declaration=========
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("ERROR", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_reg.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_grp.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_lec.get(),
                                                                                                self.var_photo.get(),
                                                                                                self.var_id.get(),
                                                                                                # self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def search_data(self):
        selected_value = self.var_search_combo.get()
        search_text = self.var_search_entry.get()

        if selected_value == "Search By":
            messagebox.showerror("Error", "Please select a search category.")
            return

        if selected_value == "Reg_No":
            query = f"SELECT * FROM student WHERE reg = '{search_text}'"
        elif selected_value == "Phone_No":
            query = f"SELECT * FROM student WHERE phone = '{search_text}'"



    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

#         ===========get cursor===========
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_name.set(data[4]),
        self.var_reg.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_grp.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_lec.set(data[10]),
        self.var_photo.set(data[11]),
        self.var_id.set(data[12])
        # self.var_radio1.set(data[13])

# =====update function======

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("ERROR", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,"
                                      "reg=%s,gender=%s,grp=%s,email=%s,phone=%s,lec=%s,photo=%s where id=%s",
                                      (
                                          self.var_dep.get(),
                                          self.var_course.get(),
                                          self.var_year.get(),
                                          self.var_semester.get(),
                                          self.var_name.get(),
                                          self.var_reg.get(),
                                          self.var_gender.get(),
                                          self.var_grp.get(),
                                          self.var_email.get(),
                                          self.var_phone.get(),
                                          self.var_lec.get(),
                                          self.var_photo.get(),
                                          # self.var_radio1.get(),
                                          self.var_id.get()
                                      ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)



    def update_photo(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("ERROR", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student's photo? ", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set photo=%s where id=%s",
                                        (
                                            self.var_photo.get(),
                                            # self.var_radio1.get(),
                                            self.var_id.get()
                                        ))

                    messagebox.showinfo("Success", "Student's photo is successfully updated", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                    return

            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

#     delete function
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

#                 reset function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select semester"),
        self.var_name.set(""),
        self.var_reg.set(""),
        self.var_gender.set("Male"),
        self.var_grp.set("Select Group"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_lec.set(""),
        self.var_photo.set(""),
        self.var_id.set(""),
        self.var_radio1.set("")

# =============Generate dataset======
    def generate_dataset(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="recognizer"
        )

        # create a cursor object
        my_cursor = conn.cursor()

        # initialize the video capture object
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.waitKey(1) & 0xFF == ord('s'):
                folder_path = r"C:\Users\fivid\OneDrive\Desktop\FaceDetection\data"
                file_name = f"{self.var_name.get()}_{self.var_id.get()}.jpg"
                file_path = os.path.join(folder_path, file_name)
                cv2.imwrite(file_path, frame)
                print(f"Image saved successfully at {file_path}")
                with open(file_path, 'rb') as f:
                    image_binary = f.read()
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,"
                                    "reg=%s,gender=%s,grp=%s,email=%s,phone=%s,lec=%s,photo=%s where id=%s",
                                    (
                                            self.var_dep.get(),
                                            self.var_course.get(),
                                            self.var_year.get(),
                                            self.var_semester.get(),
                                            self.var_name.get(),
                                            self.var_reg.get(),
                                            self.var_gender.get(),
                                            self.var_grp.get(),
                                            self.var_email.get(),
                                            self.var_phone.get(),
                                            self.var_lec.get(),
                                            image_binary,
                                            self.var_id.get()
                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
