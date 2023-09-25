import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pickle
import openpyxl
import time
path = r'student_images'
attendee = []
images = []
classNames = []
mylist = os.listdir(path)


now = datetime.now()  # date time cho tên cột điểm danh
date_str = now.strftime('%d-%B-%Y')


sobuoi_filename = 'sobuoi.txt'
if not os.path.exists(sobuoi_filename):
    with open(sobuoi_filename, 'w') as f:
        f.write('1')
with open(sobuoi_filename, 'r') as f:
    sobuoi_str = f.read()
    if sobuoi_str.strip():  # Kiểm tra xem chuỗi không phải là chuỗi rỗng
        sobuoi = int(sobuoi_str)
    else:
        sobuoi = 1
col_number = sobuoi
with open(sobuoi_filename, 'w') as f:
    f.write(f'{sobuoi+1}')


with open('Attendance.csv', 'w') as f:
    f.write('')

for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList


encoded_face_train = findEncodings(images)


def markAttendance(name):
    write_to_excel(name)
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

            attendee.append(name.upper())


def write_to_excel(name):
    wb = openpyxl.load_workbook("DiemDanh.xlsx")
    ws = wb['Sheet1']
    # Convert the session number to column letter (D, E, F, ...)
    col_name = chr(ord('D') + col_number)
    # Cell in row 1 for the session's attendance column
    cell_name = f"{col_name}1"
    ws[cell_name] = f"Buoi diem danh thu{col_number}- {date_str}"

    for i in range(2, 80):
        if ws.cell(row=i, column=2).value in attendee:
            # Set the cell format to Boolean and write True
            ws.cell(row=i, column=col_number + 5).value = True
        else:
            # Set the cell format to Boolean and write False
            ws.cell(row=i, column=col_number + 5).value = False

    wb.save("DiemDanh.xlsx")


def count_missing():
    wb = openpyxl.load_workbook("DiemDanh.xlsx")
    ws = wb['Sheet1']
    ws['Z1'] = "Sobuoivang"

    for row in range(2, 80):  # Dynamically determine the last row
        false_count = 0
        for col in range(6, 26):  # Columns E to Q are columns 5 to 16
            cell_value = ws.cell(row=row, column=col).value
            if cell_value == False:
                false_count += 1
        ws.cell(row=row, column=26, value=false_count)
    wb.save("DiemDanh.xlsx")
cap = cv2.VideoCapture(0)
try:
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
        for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
            matches = face_recognition.compare_faces(
                encoded_face_train, encode_face)
            faceDist = face_recognition.face_distance(
                encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)
            print(matchIndex)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-5),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name.upper())

        cv2.imshow('webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass  # This catches ctrl+C

count_missing()  # Call count_missing even if you manually interrupt the program
time.sleep(1)
print("Thank you for using the program")
# Optionally, you can add code here to release resources and close windows
cap.release()
cv2.destroyAllWindows()
