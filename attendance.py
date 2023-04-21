# # pylint: disable=redefined-outer-name
# import face_recognition
# import cv2
# import numpy as np
# import os
# from datetime import datetime


# path = 'ImagesAttendance'
# images = []
# classNames = []
# myList = os.listdir(path)
# print(myList)
# for cl in myList:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
# print(classNames)


# def find_encodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList


# def mark_attendance(name):
#     with open('Attendance.csv', 'r+') as f:
#         my_data_list = f.readlines()
#         name_list = []
#         for line in my_data_list:
#             entry = line.split(',')
#             name_list.append(entry[0])
#         if name not in name_list:
#             now = datetime.now()
#             dtString = now.strftime('%H:%M:%S')
#             f.writelines(f'\n{name},{dtString}')


# encodeListKnown = find_encodings(images)
# print('Encoding Complete')

# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#     facesCurFrame = face_recognition.face_locations(imgS)
#     encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

#     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#         faceDist = face_recognition.face_distance(encodeListKnown, encodeFace)
#         # print(faceDist)
#         matchIndex = np.argmin(faceDist)

#         if matches[matchIndex]:
#             name = classNames[matchIndex].upper()
#             print(name)
#             y1, x2, y2, x1 = faceLoc
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.rectangle(img, (x1, y1 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img, name, (x1 + 6, y2 + 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#             mark_attendance(name)

#     cv2.imshow('webcam', img)
#     cv2.waitKey(1)




from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")

# =============variables===========
        self.var_atten_id = StringVar()
        self.var_atten_reg = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_att = StringVar()
        


    #         first image
        img = Image.open(r"ImagesBasics\img1.jfif")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

#     second image
        img1 = Image.open(r"ImagesBasics\img2.jfif")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)


        #    background image
        img3 = Image.open(r"ImagesBasics\bgimg1.jfif")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)


        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)


        #         left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=550)

        img_left = Image.open(r"ImagesBasics\hi.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=10, y=135, width=710, height=380)

        # labels

        #         attendance Id
        id_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 12, "bold"),
                               state="disabled", bg="white")
        id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        id_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=20, font=("times new roman", 12, "bold"))
        id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        #         admission
        reg_label = Label(left_inside_frame, text="Admission:", font=("times new roman", 12, "bold"),
                               state="disabled", bg="white")
        reg_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        reg_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_reg, width=20, font=("times new roman", 12, "bold"))
        reg_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        #         name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"),
                               state="disabled", bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #         department
        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), state="disabled", bg="white")
        dep_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        dep_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep, width=20, font=("times new roman", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #         time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"),
                               state="disabled", bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_time, width=20, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #         date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"),
                               state="disabled", bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_date, width=20, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #         attendance 
        att_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 12, "bold"),
                               state="disabled", bg="white")
        att_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        att_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_att, font=("times new roman", 12, "bold"), width=17)
        att_combo["values"] = ("Status", "Present", "Absent")
        att_combo.current(0)
        att_combo.grid(row=3, column=1, padx=2, pady=5, sticky=W)


        # button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        import_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=19, font=("times new roman", 12, "bold"),
                          bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=19, font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=19, font=("times new roman", 12,"bold"), bg="blue",fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19, font=("times new roman", 12,
                                                                                             "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)


        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        # img_right = Image.open(r"C:\Users\fivid\Downloads\developers.jpg")
        # img_right = img_right.resize((710, 130), Image.LANCZOS)
        # self.photoimg_right = ImageTk.PhotoImage(img_right)

        right_frame = Label(Right_frame, bd=2, relief=RIDGE, bg="white")
        right_frame.place(x=5, y=5, width=700, height=465)


        # ========scroll bar ======
        scroll_x = ttk.Scrollbar(right_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(right_frame, column=("dep", "name", "reg", "id", "date", "time", "att"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("dep", text="DEPARTMENT")
        self.AttendanceReportTable.heading("name", text="NAME")
        self.AttendanceReportTable.heading("reg", text="RegNO.")
        self.AttendanceReportTable.heading("id", text="ID")
        self.AttendanceReportTable.heading("date", text="DATE")
        self.AttendanceReportTable.heading("time", text="TIME")
        self.AttendanceReportTable.heading("att", text="STATUS")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("reg", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("dep", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("att", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


        #  Fetch Data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in data:
                    self.AttendanceReportTable.insert("", END, values=i)
                conn.commit()
            conn.close()


# import csv

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
                self.fetchData(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        
        except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_reg.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_att.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_reg.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_att.set("")

        # Clear the input fields
        self.var_atten_id.set('')
        self.var_atten_reg.set('')
        self.var_atten_name.set('')
        self.var_atten_dep.set('')
        self.var_atten_time.set('')
        self.var_atten_date.set('')
        self.var_atten_att.set('')

    def update_data(self):
        if self.var_atten_dep.get() == "Select Department" or self.var_atten_name.get() == "" or self.var_atten_id.get() == "":
            messagebox.showerror("ERROR", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s,name=%s,time=%s,date=%s,att=%s,reg=%s where id=%s",(
                                        self.var_atten_id.get(),
                                        self.var_atten_reg.get(),
                                        self.var_atten_name.get(),
                                        self.var_atten_dep.get(),
                                        self.var_atten_time.get(),
                                        self.var_atten_date.get(),
                                        self.var_atten_att.get(),
                                      )
                                      )
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()