import tkinter as tk
from tkinter import messagebox 
import openpyxl
from openpyxl import load_workbook

root=tk.Tk()
f = r"C:\Users\Asus\Desktop\AI_ML\hii_python\python_concepts\ADVANCED\Student Registration Frm.xlsx"
A=openpyxl.load_workbook(f)
B=A["Registration Form"]

#Creating function 
def Onclick_submit():
    name = name_textbox.get()
    email = email_textbox.get()
    mobile = mobile_textbox.get()
    if name and email and mobile:
        B.append([name, email, mobile])
        A.save(f)
        messagebox.showinfo("Status", "Data submitted successfully")
    else:
        messagebox.showinfo("Warning", "Please fill all the fields")    
    address = add_textbox.get()
    roll_no = roll_textbox.get()
    dob = dob_textbox.get()
    age = age_textbox.get()
    class_ = class_textbox.get()
    gender = gender_textbox.get()
    messagebox.showinfo("Data Entered", f"Name: {name}\nRoll_no: {roll_no}\nAge: {age}\nDOB: {dob}\nClass: {class_}\nGender: {gender}\nEmail: {email}\nMobile: {mobile}\nAddress: {address}")


#Added geometry, background color and title to the window
root.geometry("500x500")
root.configure(bg="#47506D")
root.title("Student Registration Form")

#Adding Name
name_label = tk.Label(root, text="Name : ")
name_label.pack(anchor = tk.W,padx=10)
name_textbox = tk.Entry(root)
name_textbox.pack(anchor=tk.W,padx=10)

#Adding Roll number
roll_label = tk.Label(root, text="Roll number : ")
roll_label.pack(anchor=tk.W,padx=10)
roll_textbox = tk.Entry(root)
roll_textbox.pack(anchor=tk.W,padx=10)

#Adding Age 
age_label = tk.Label(root, text="Age : ")
age_label.pack(anchor=tk.W,padx=10)
age_textbox = tk.Entry(root)
age_textbox.pack(anchor=tk.W,padx=10)

#Adding DOB(Date of Birth)
dob_label = tk.Label(root, text="DOB : ")
dob_label.pack(anchor=tk.W,padx=10)
dob_textbox = tk.Entry(root)
dob_textbox.pack(anchor=tk.W,padx=10)

#Adding Class 
class_label = tk.Label(root, text="Class : ")
class_label.pack(anchor=tk.W,padx=10)
class_textbox = tk.Entry(root)
class_textbox.pack(anchor=tk.W,padx=10)

#Adding Gender
gender_label = tk.Label(root, text="Gender :")
gender_label.pack(anchor=tk.W,padx=10)
gender_textbox = tk.Entry(root)
gender_textbox.pack(anchor=tk.W,padx=10)

#Ading Email
email_label = tk.Label(root, text="Email : ")
email_label.pack(anchor=tk.W,padx=10)
email_textbox =tk.Entry(root)
email_textbox.pack(anchor=tk.W,padx=10)

#Addding Mobile number 
mobile_label = tk.Label(root, text="Mobile Number :")
mobile_label.pack(anchor=tk.W,padx=10)
mobile_textbox = tk.Entry(root)
mobile_textbox.pack(anchor=tk.W,padx=10)

#Adding Address
add_label = tk.Label(root, text="Address :")
add_label.pack(anchor=tk.W,padx=10)
add_textbox = tk.Entry(root)
add_textbox.pack(anchor=tk.W,padx=10)

#Adding submit button
submit_button = tk.Button(root, text="Submit", command=Onclick_submit)
submit_button.pack(anchor=tk.W,padx=10)

root.mainloop()