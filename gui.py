import tkinter as tk
from tkinter import END, Text, ttk
from tkinter import filedialog
import tkinter

from PIL import Image, ImageTk
import customtkinter
from customtkinter import CTkSegmentedButton

import main
import automail


def go_to_screen2():    
    play_frame.pack()
    main_frame.pack_forget()


def back_to_screen1():
    main_frame.pack()
    play_frame.pack_forget()

def back_to_screen_2():
    play_frame.pack()
    list_stu_frame.pack_forget() 
    
def open_camera():
    print("start click")

def show_list():
    list_stu_frame.pack()
    play_frame.pack_forget()


def show_clicked():
    print("print show click")


def add_path():
    path = filedialog.askopenfilename()  # Hiển thị hộp thoại chọn tệp
    # Thực hiện xử lý với đường dẫn được chọn




def send_mail():
    automail.send_emails()

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
next_button = tk.Button(main_frame, image=photo, bd=0, command=go_to_screen2)
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
font_title = customtkinter.CTkFont(family="Montserrat", size=25, weight="bold")
text_label = tk.Label(main_frame, text="PTIT ATTENDANCE SYSTEM",
                      font=font_title, fg="white", bg="red")
text_label.place(relx=0.5, rely=0.1, anchor=tk.N)

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
font_title = customtkinter.CTkFont(family="Montserrat", size=12, weight="bold")
text_label = tk.Label(play_frame, text="PTIT ATTENDANCE SYSTEM ",
                      font=font_title, fg="white", bg="red")
text_label.place(relx=0.16, rely=0.025, anchor=tk.N)

# Start Button
image = Image.open("app_images/image1.png")
image = image.resize((800, 200))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)
back_button = tk.Button(play_frame, image=photo, command=open_camera)
back_button.photo = photo
back_button.place(relx=0, rely=0.08, width=800, height=300)


ds_vang = ttk.Button(
    play_frame, text="Sinh viên chưa điểm danh", style="Custom.TButton", command=show_list)

# student_button = ttk.Button(play_frame, text="Danh sách học sinh chưa được điểm danh hôm nay", command=show_list)
# send_email_button = ttk.Button(play_frame, text="Sent Email", style="TButton", command=show_clicked)
# Back Button
image = Image.open("app_images/ptit.png")  # Replace with your image file path
image = image.resize((40, 40))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)
back_button = tk.Button(play_frame, image=photo, command=back_to_screen1)
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

# student_button.place(relx=0.4, rely=0.61, anchor=tk.CENTER)
# send_email_button.place(relx=0.6, rely=0.61, anchor=tk.CENTER)

# Man hinh 3---------------------------
list_stu_frame = tk.Frame(app, bg="#93bbfa", width=800, height=600)

# Tạo background đỏ của màn hình 3
canvas = tk.Canvas(list_stu_frame, width=800, height=50, bg="red")
canvas.pack()

# # Tạo background trắng của màn hình 3
# bottom_frame = tk.Frame(list_stu_frame, width=800, height=550, bg="white")
# bottom_frame.pack()

# App title ở màn hình 2
font_title = customtkinter.CTkFont(family="Montserrat", size=12, weight="bold")
text_label = tk.Label(list_stu_frame, text="Face Recognition PTIT",
                      font=font_title, fg="white", bg="red")
text_label.place(relx=0.16, rely=0.025, anchor=tk.N)

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

with open("absent_list.txt", "r",encoding="utf-8") as f:
    element_list = f.readlines()
txt_output = Text(list_stu_frame, height=50, width=50)
txt_output.pack()
for item in element_list:
   txt_output.insert(END, item + "\n")

# Initially, show the Main Screen
back_to_screen1()

app.mainloop()
