from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
import face_recognition
import cv2
import numpy as np
from tkinter import messagebox
import mysql.connector
from datetime import datetime

class Face_Detector:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.path = r"C:\Users\fivid\OneDrive\Desktop\FaceDetection\data"
        images = []
        classNames = []
        self.myList = os.listdir(self.path)
        for cl in self.myList:
            self.images = [cv2.imread(f'{self.path}/{cl}') for cl in self.myList]
            images.append(self.images)
            self.classNames = [os.path.splitext(cl)[0] for cl in self.myList]
            classNames.append(self.classNames)


        title_lbl = Label(self.root, text="FACE DETECTION", font=("times new roman", 35, "bold"),
                          bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_reg = StringVar()
        self.var_id = StringVar()

# 1st image
        img_top = Image.open(r"ImagesBasics\recognizer.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)


# 2nd image
        img_bottom = Image.open(r"ImagesBasics\ai.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)




        btn = Button(self.root, text="Face Detection", command=self.face_detector, cursor="hand2",
                    font=("times new roman", 18, "bold"), bg="dark green", fg="white")
        btn.place(x=710, y=620, width=200, height=40)


        # =========Attendance=============


    def mark_attendance(self, dep, name, reg, id):
        with open("Attendance.csv","r+",newline="\n") as f:
            my_data_list = f.readlines()
            dep_list = []
            name_list = []
            reg_list = []
            id_list = []
            for line in my_data_list:
                entry = line.split(',')
                dep_list.append(entry[0])
                name_list.append(entry[0])
                reg_list.append(entry[0])
                id_list.append(entry[0])
            if ((dep not in dep_list), (name not in name_list), (reg not in reg_list) and (id not in id_list)):
                now = datetime.now()
                dtString = now.strftime("%d-%m-%Y , %H:%M:%S ")
                f.writelines(f"\n{dep},{name},{reg},{id},{dtString},Present")


    def find_encodings(self, images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_encodings = face_recognition.face_encodings(img)
            if len(face_encodings) > 0:
                encode = face_encodings[0]
                encodeList.append(encode)
        return encodeList


    def face_detector(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="recognizer")
        my_cursor = conn.cursor()

        encodings = self.find_encodings(self.images)

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            imgS = cv2.resize(img,(0,0),None,0.25,0.25)
            imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

            for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                matches = face_recognition.compare_faces(encodings,encodeFace)
                faceDis = face_recognition.face_distance(encodings,encodeFace)
                matchIndex = np.argmin(faceDis)


        #         if matches[matchIndex]:
        #             dep = self.classNames[matchIndex].upper()
        #             name = self.classNames[matchIndex].upper()
        #             reg = self.classNames[matchIndex].upper()
        #             id = self.classNames[matchIndex].upper()
        #             my_cursor.execute("SELECT dep FROM student WHERE dep = %s", (self.var_dep.get(),))
        #             dep = my_cursor.fetchone()

        #             my_cursor.execute("SELECT name FROM student WHERE name = %s", (self.var_name.get(),))
        #             name = my_cursor.fetchone()

        #             my_cursor.execute("SELECT reg FROM student WHERE reg = %s", (self.var_reg.get(),))
        #             reg = my_cursor.fetchone()

        #             my_cursor.execute("SELECT id FROM student WHERE id = %s", (id,))
        #             id = my_cursor.fetchone()


        #             # my_cursor.execute("select dep from student where dep= '%s' ",(self.var_dep.get()))
        #             # dep_result = my_cursor.fetchone()
        #             # if dep_result is not None:
        #             #     dep = dep_result[0]
        #             # else:
        #             #     dep = ""

        #             # my_cursor.execute("select name from student where name= '%s' ",(self.var_name.get()))
        #             # name_result = my_cursor.fetchone()
        #             # if name_result is not None:
        #             #     name = name_result[0]
        #             # else:
        #             #     name = ""

        #             # my_cursor.execute("select reg from student reg= '%s' ",(self.var_reg.get()))
        #             # reg_result = my_cursor.fetchone()
        #             # if reg_result is not None:
        #             #     reg = reg_result[0]
        #             # else:
        #             #     reg = ""

        #             # my_cursor.execute("select id from student where student.id= '%s' " % id)
        #             # id_result = my_cursor.fetchone()
        #             # if id_result is not None:
        #             #     id = id_result[0]
        #             # else:
        #             #     id = ""

        #             dep = dep.upper()
        #             name = name.upper()
        #             reg = reg.upper()
        #             id = id.upper()

        #             print(dep,name,reg,id)

        #             y1, x2, y2, x1 = faceLoc
        #             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        #             cv2.rectangle(img, (x1, y1 - 35), (x2, y2), (255, 0, 255), 2)

        #             cv2.putText(img, f'Dep:{dep} {matches} {round(faceDis[0],2)}',  (x1,y1-125), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
        #             cv2.putText(img, f'Name:{name} {matches} {round(faceDis[0],2)}', (x1,y1-95), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
        #             cv2.putText(img, f'Reg:{reg} {matches} {round(faceDis[0],2)}', (x1,y1-65), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
        #             cv2.putText(img, f'ID:{id} {matches} {round(faceDis[0],2)}', (x1,y1-35), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

        #             self.mark_attendance(dep,name,reg,id)

        #         else:
        #             y1, x2, y2, x1 = faceLoc
        #             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        #             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        #             cv2.putText(img, "Unknown Face", f'{matches} {round(faceDis[0],2)}', (x1 + 6, y2 + 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)


        #     cv2.imshow('Webcam', img)

        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break

        # cap.release()
        # cv2.destroyAllWindows()


# +str(id)
                if matches[matchIndex]:
                    # id = self.classNames[matchIndex]
                    my_cursor.execute("select dep from student where dep = %s",(self.var_dep.get()))
                    dep = my_cursor.fetchone()


                    my_cursor.execute("select name from student where name = %s",(self.var_name.get()))
                    name = my_cursor.fetchone()

                    my_cursor.execute("select reg from reg = %s",(self.var_reg.get()))
                    reg = my_cursor.fetchone()
                    # , (self.var_reg.get())

                    my_cursor.execute("select id from student where student.id = %s" % id)
                    id = my_cursor.fetchone()

                    dep = self.classNames[matchIndex].upper()
                    name = self.classNames[matchIndex].upper()
                    reg = self.classNames[matchIndex].upper()
                    id = self.classNames[matchIndex].upper()
                    print(dep,name,reg,id)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1 - 35), (x2, y2), (255, 0, 255), 2)

                    cv2.putText(img, f'Dep:{dep}',  (x1,y1-125), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
                    cv2.putText(img, f'Name:{name}', (x1,y1-95), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
                    cv2.putText(img, f'Reg:{reg}', (x1,y1-65), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
                    cv2.putText(img, f'ID:{id}', (x1,y1-35), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
                    self.mark_attendance(dep,name,reg,id)
                    # f"Name:{name}", 
                else:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", f'{matches}{round(faceDis[0],2)}', (x1 + 6, y2 + 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
            cv2.imshow('Webcam',img)
            if cv2.waitKey(1)==13 & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


    
if __name__ == "__main__":
    root = Tk()
    obj = Face_Detector(root)
    root.mainloop()

                        