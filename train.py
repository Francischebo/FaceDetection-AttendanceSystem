# pylint: disable=redefined-outer-name
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
import face_recognition
import numpy as np
import cv2
from tkinter import messagebox


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"),
                          bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"ImagesBasics\faces.jpg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)


        btn = Button(self.root, text="TRAIN DATA", command=self.testing, cursor="hand2",
                    font=("times new roman", 30, "bold"), bg="red", fg="white")
        btn.place(x=0, y=380, width=1530, height=60)



        img_bottom = Image.open(r"ImagesBasics\train.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=0, y=440, width=1530, height=325)
       

    def testing(self):
        cap = cv2.VideoCapture(0)

        # Load the image(s) to encode
        folder_path = r"C:\Users\fivid\OneDrive\Desktop\FaceDetection\data"
        file_names = os.listdir(folder_path)
        image_paths = [os.path.join(folder_path, file_name) for file_name in file_names]
        images = [face_recognition.load_image_file(image_path) for image_path in image_paths]

        # Encode the images
        encoded_images = []
        for image in images:
            try:
                encoding = face_recognition.face_encodings(image)[0]
                encoded_images.append(encoding)
            except IndexError:
                pass

        # Loop over webcam frames
        while True:
            ret, frame = cap.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            # Loop over face encodings in the current frame
            for face_encoding in face_encodings:
                # Compare the face encoding with the encoded images
                matches = face_recognition.compare_faces(encoded_images, face_encoding)
                name = "Unknown"
                faceDis = face_recognition.face_distance([encoded_images], face_encoding)
                match_index = np.argmin(faceDis)

                # Check if there is a match
                if True in matches:
                    match_index = matches.index(True)
                    name = file_names[match_index].split('.')[0]

                # Draw a box around the face and label it
                top, right, bottom, left = face_locations[0]
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 255), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255), 2)
                # cv2.putText(images, f'{matches}{round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

            # save image
            if cv2.waitKey(1) & 0xFF == ord('s'):
                image_name = ""
                image_path = os.path.join(folder_path, image_name)
                cv2.imwrite(image_path, frame)

            # Display the resulting image
            cv2.imshow('frame', frame)

            # Exit the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()








# import face_recognition
# import cv2
# import numpy as np

# imgFrans = face_recognition.load_image_file('ImagesBasics/Francis.jpg')
# imgFrans = cv2.cvtColor(imgFrans, cv2.COLOR_BGR2RGB)
# imgTest = face_recognition.load_image_file('ImagesBasics/Test.jpg')
# imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# faceLoc = face_recognition.face_locations(imgFrans)[0]
# encodeFrans = face_recognition.face_encodings(imgFrans)[0]
# start_point = (184,632)
# end_point = (339,477)
# cv2.rectangle(imgFrans, start_point, end_point, (255, 0, 255), 2)
# # print(faceLoc)

# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# start = (134,562)
# end = (455,241)
# cv2.rectangle(imgTest, start, end, (255, 0, 255), 2)
# # print(faceLocTest)

# results = face_recognition.compare_faces([encodeFrans], encodeTest)
# faceDis = face_recognition.face_distance([encodeFrans], encodeTest)
# print(results, faceDis)
# cv2.putText(imgTest, f'{results}{round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)



# cv2.imshow("Francis", imgFrans)
# cv2.imshow("Test", imgTest)
# cv2.waitKey(0)

