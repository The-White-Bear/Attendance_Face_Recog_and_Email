# Face Recognition Attendance and Email Project

## Introduction
This project uses facial recognition technology to perform attendance tracking in a classroom or event setting. It automatically records student attendance and sends email notifications to students who are absent for a specified number of sessions.

## Installation
Before running the project, you need to install the following prerequisites:

- Python 3.x
- The required Python libraries are listed in the `requirements.txt` file.

To install the required libraries, run the following command in the project's root directory. 

###### IF YOU HAVE TROUBLE WHEN INSTALL DLIB OR FACE_RECOGNITION ,TRY TO INSTALL VISUAL STUDIO AND INSTALL C++. #####


## Directory Structure
Below is the directory structure of the project:

- `.idea`: IDE-specific directory (if used).
- `app_images`: Directory containing images attached in email notifications.
- `student_images`: Directory containing student images (each image is named after the student's ID).
- `__pycache__`: Directory created by Python.
- `absent_list.txt`: List of absent students.
- `Attendance.csv`: List of students and their attendance records.
- `automail.py`: Code for sending email notifications to absent students.
- `DiemDanh.xlsx`: Excel file storing attendance data.
- `gui.py`: User interface code for the application.
- `index.html`: Content attached in email notifications.
- `main.py`: Main code for facial recognition and attendance tracking.
- `README.md`: Current project description file.
- `requirements.txt`: List of required libraries for the project.
- `sent_emails.txt`: List of emails that have been sent.
- `sobuoi.txt`: Number of attendance sessions.

## Usage
This project has a user interface implemented in `gui.py`. The interface consists of the following pages:
- Start Page: Allows you to initiate attendance tracking.
- Attendance Page: Displays the facial recognition interface and saves data to `Attendance.csv`.
- Absentee List Page: Displays the list of absent students and sends email notifications. There is a "Sent Emails" button to send email.

Just run gui.py , remember to check that file sobuoi.txt have been reset to 0, and File "DiemDanh.txt" in format : column B is Student id, column C and D is student name, column E is student email.
## Contact
If you have any questions or contributions, please feel free to reach out to us.

This project is developed by me and my friend - Quang Thang.
