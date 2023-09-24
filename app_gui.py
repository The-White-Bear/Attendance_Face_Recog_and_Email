import cv2
import face_recognition
import numpy as np
from datetime import datetime
import pickle
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FaceRecognitionApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Face Recognition Attendance System")

        self.path = None
        self.images = []
        self.classNames = []
        self.encoded_face_train = None
        self.attendance_list = []

        self.start_button = tk.Button(self, text="Start Attendance System", command=self.start_attendance_system)
        self.start_button.pack(pady=10)

        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.pack(pady=10)

    def findEncodings(self, images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encoded_face = face_recognition.face_encodings(img)[0]
            encodeList.append(encoded_face)
        return encodeList

    def markAttendance(self, name):
        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                time = now.strftime('%I:%M:%S:%p')
                date = now.strftime('%d-%B-%Y')
                f.writelines(f'{name}, {time}, {date}\n')
                self.attendance_list.append(name)  # Thêm tên vào danh sách điểm danh
    def start_attendance_system(self):
        self.path = filedialog.askdirectory(title="Select Images Folder")
        if not self.path:
            messagebox.showerror("Error", "Please select the images folder.")
            return

        self.images = []
        self.classNames = []
        mylist = os.listdir(self.path)
        for cl in mylist:
            curImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])

        self.encoded_face_train = self.findEncodings(self.images)

        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            faces_in_frame = face_recognition.face_locations(imgS)
            encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
            for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
                matches = face_recognition.compare_faces(self.encoded_face_train, encode_face)
                faceDist = face_recognition.face_distance(self.encoded_face_train, encode_face)
                matchIndex = np.argmin(faceDist)
                if matches[matchIndex]:
                    name = self.classNames[matchIndex].upper().lower()
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    self.markAttendance(name)
            cv2.imshow('webcam', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Ghi dữ liệu điểm danh vào file CSV
        self.save_attendance_to_txt()

if __name__ == "__main__":
    app = FaceRecognitionApp()
    app.mainloop()
    
