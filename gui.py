import tkinter as tk
from tkinter import END, Text, ttk
from tkinter import filedialog
import tkinter
from PIL import Image, ImageTk
import customtkinter
from customtkinter import CTkSegmentedButton
import sys
import os
application_files_dir = os.path.join(os.path.dirname(__file__), "application_files")
sys.path.append(application_files_dir)
import application_files.automail as automail
import application_files.main as main
def screen_2():
    play_frame.pack()
    main_frame.pack_forget()


def screen_1():
    main_frame.pack()
    play_frame.pack_forget()

def back_to_screen_2():
    play_frame.pack()
    list_stu_frame.pack_forget() 
    
def start_clicked():
    main.main()


def end_clicked():
    
    list_stu_frame.pack()
    with open("attendance/absent_list.txt", "r",encoding="utf-8") as f:
        element_list = f.readlines()
    txt_output = Text(list_stu_frame, height=50, width=50)
    txt_output.pack()
    for item in element_list:
        txt_output.insert(END, item + "\n")
    play_frame.pack_forget()

def add_path():
    path = filedialog.askopenfilename()  # Hiển thị hộp thoại chọn tệp
    # Thực hiện xử lý với đường dẫn được chọn
def send_mail():
    automail.send_emails()
def open_user_manual():
    # Provide the path to your user manual file here
    user_manual_path = r'application_files\user_manual.txt'
    
    try:
        with open(user_manual_path, "r", encoding="utf-8") as manual_file:
            user_manual_text = manual_file.read()
            
        # Create a new window to display the user manual text
        manual_window = tk.Toplevel(app)
        manual_window.title("User Manual")
        
        manual_text = Text(manual_window)
        manual_text.pack()
        manual_text.insert(END, user_manual_text)
        
    except Exception as e:
        print(f"Error opening the user manual: {str(e)}")

# ----------------------------------------------------------------------------------------------------------------------
app = tk.Tk()
app.title("Face Recognition App")
app.geometry("800x600")
app.resizable(False, False)

# Màn hình 1
main_frame = tk.Frame(app, width=800, height=600)
main_frame.pack()

# Tạo background đỏ của màn hình 1
canvas = tk.Canvas(main_frame, width=800, height=160, bg="red")
canvas.pack()

# Tạo background trắng của màn hình 1
bottom_frame = tk.Frame(main_frame, width=800, height=440, bg="white")
bottom_frame.pack()
# Image Button
image = Image.open("app_images/face.jpg")
image = image.resize((400, 296))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)
next_button = tk.Button(main_frame, image=photo, bd=0, command=screen_2)
next_button.photo = photo
next_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER, width=400, height=290)
# Logo
image = Image.open("app_images/ptit.png")
image = image.resize((100, 100))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(main_frame, image=photo)
image_label.photo = photo
image_label.place(relx=0.05, rely=0.05, anchor=tk.NW)

# Title App
font_title = customtkinter.CTkFont(family="Montserrat", size=22, weight="bold")
text_label = tk.Label(main_frame, text="WELCOME TO PTIT ATTENDANCE SYSTEM",
                      font=font_title, fg="white", bg="red")
text_label.place(relx=0.5, rely=0.1, anchor=tk.N)
text2 =  tk.Label(main_frame, text="CLICK THE BUTTON TO START",font=font_title, fg="white", bg="red", anchor=tk.N)
text2.place(relx=0.5, rely=0.8, anchor=tk.N)
# Create a custom style for the "User Manual" button
style = ttk.Style()
style.configure("UserManual.TButton", 
               foreground="red",  # Text color
               background="#5681c7",  # Background color
               font=("Arial", 10),  # Font style
               padding=(10, 5),  # Padding around the text
               relief="raised"  # Button relief style
              )

user_manual_button = ttk.Button(main_frame, text="User Manual", command=open_user_manual, style="UserManual.TButton")
user_manual_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER, width=100, height=40)

# -----------------------------------------------------------------------------------------------------------------
# Màn hình thứ 2
play_frame = tk.Frame(app, bg="red", width=800, height=600)

# Tạo background đỏ của màn hình 2
canvas = tk.Canvas(play_frame, width=800, height=50, bg="red")
canvas.pack()

# Tạo background trắng của màn hình 2
bottom_frame = tk.Frame(play_frame, width=800, height=550, bg="white")
bottom_frame.pack()

# App title ở màn hình 2
font_title = customtkinter.CTkFont(family="Montserrat", size=16, weight="bold")
text_label = tk.Label(play_frame, text="PTIT ATTENDANCE SYSTEM",
                      font=font_title, fg="white", bg="red")
text_label.place(relx=0.5, rely=0.025, anchor=tk.N)

# Start Button
# Create a Label for the background
background_image = Image.open("app_images/image1.png")
background_image = background_image.resize((800, 550))  # Resize the background image as needed
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(play_frame, image=background_photo)
background_label.photo = background_photo
background_label.place(relx=0, rely=0.1, width=800, height=550)

# Create the Start Button
button_image = Image.open("app_images/button.png")  # Change to the desired button image
button_photo = ImageTk.PhotoImage(button_image)
start_button = tk.Button(play_frame, image=button_photo, command=start_clicked)
start_button.photo = button_photo
start_button.place(relx=0.85, rely=0.65, anchor=tk.CENTER, width=200, height=80)

ds_vang = ttk.Button(
    play_frame, text="View absent list today", style="Custom.TButton", command=end_clicked)

# Back Button
image = Image.open("app_images/ptit.png")  # Replace with your image file path
image = image.resize((40, 40))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)
back_button = tk.Button(play_frame, image=photo, command=screen_1)
back_button.photo = photo
back_button.place(relx=0.01, rely=0.01, anchor="nw", width=40, height=40)


style = ttk.Style()
style.configure("TButton",
                font=("Montserrat", 14),
                background="#44475a",
                foreground="black")
style.configure("Custom.TButton",
                font=("Montserrat", 10),
                background="red",
                foreground="black")  # Màu chữ trắng

ds_vang.place(relx=0.85, rely=0.04, anchor=tk.CENTER)
# Man hinh 3---------------------------
list_stu_frame = tk.Frame(app, bg="#93bbfa", width=800, height=600)

# Tạo background đỏ của màn hình 3
canvas = tk.Canvas(list_stu_frame, width=800, height=50, bg="red")
canvas.pack()
# App title ở màn hình 2
font_title = customtkinter.CTkFont(family="Montserrat", size=12, weight="bold")
text_label = tk.Label(list_stu_frame, text="STUDENT ABSENT LIST TODAY",
                      font=font_title, fg="white", bg="red")
text_label.place(relx=0.5, rely=0.025, anchor=tk.N)

# Back Button
image = Image.open("app_images/ptit.png")  # Replace with your image file path
image = image.resize((40, 40))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)
back_button = tk.Button(list_stu_frame, image=photo, command=back_to_screen_2)
back_button.photo = photo
back_button.place(relx=0.01, rely=0.01, anchor="nw", width=40, height=40)

send = ttk.Button(
    list_stu_frame, text="Send Mail", style="Custom.TButton", command=send_mail)
send.place(relx=0.9, rely=0.04, anchor=tk.CENTER)

# Initially, show the Main Screen
screen_1()

app.mainloop()