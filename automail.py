import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import openpyxl

def send_emails(data_path, index_path, sender_email, sender_password):
    # Đọc nội dung email từ tệp HTML
    with open(index_path, "r", encoding="utf-8") as html_file:
        email_content = html_file.read()
    # Đọc dữ liệu từ file Excel
    wb = openpyxl.load_workbook(data_path)
    sheetname = wb.sheetnames
    ws = wb[sheetname[0]]
    ws.cell(row=1, column=24).value = "Check sent email"
    recipients = []
    for row in range(2, ws.max_row+1):
        false_count = 0
        for col in range(6, 25):
            cell_value = ws.cell(row=row, column=col).value
            if cell_value == False:
                false_count += 1
        if false_count >= 2 :
            if(ws.cell(row=row,column=24).value == None):
                ho=ws.cell(row=row,column=3).value
                ten=ws.cell(row=row,column=4).value  
                full_name=f"{ho} {ten}"
                email= ws.cell(row=row,column=5).value
                if email:
                    recipients.append((full_name, email))
                    ws.cell(row=row,column=24).value=True
    with open("daguiemail.txt", "w", encoding="utf-8") as f:
        for recipient in recipients:
            f.write(f"{recipient}\n")
        
    # # Kết nối đến máy chủ SMTP của Gmail
    # smtp_server = "smtp.gmail.com"
    # smtp_port = 587
    # server = smtplib.SMTP(smtp_server, smtp_port)
    # server.starttls()
    # # Đăng nhập vào tài khoản email
    # server.login(sender_email, sender_password)
    # # Gửi email cho từng người nhận
    # subject="[ CẢNH BÁO SỐ BUỔI VẮNG HỌC ] "
    # for full_name, receiver_email in recipients:
    #     # Tạo đối tượng MIMEMultipart để tạo email
    #     message = MIMEMultipart()
    #     message["From"] = sender_email
    #     message["To"] = receiver_email
    #     message["Subject"] = subject
    #     email_content_with_name = email_content.replace("$NAME", full_name)
    #     # Nội dung email lấy từ tệp HTML
    #     message.attach(MIMEText(email_content_with_name, "html"))

    #     # Gửi email
    #     server.sendmail(sender_email, receiver_email, message.as_string())

    # # Đóng kết nối SMTP
    # server.quit()

# Sử dụng hàm send_emails
# data_path = r'D:\Work_space\Attendance_Face_Recog_and_Email\DiemDanh.xlsx'
# index_path = r'D:\Work_space\Attendance_Face_Recog_and_Email\passcv.html'
# sender_email = "clbsomediaptit@gmail.com"
# sender_password = "gvszzolbdxqlviyi"
# send_emails(data_path, index_path, sender_email, sender_password)
