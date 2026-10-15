import tkinter as tk 
root=tk.Tk()
root.title("Student Registration Form")

#Adding Name
name_label = tk.Label(root, text="Name : ")
name_label.pack()
name_textbox = tk.Entry(root)
name_textbox.pack()

#Adding Roll number
roll_label = tk.Label(root, text="Roll number : ")
roll_label.pack()
roll_textbox = tk.Entry(root)
roll_textbox.pack()

#Adding Age 
age_label = tk.Label(root, text="Age : ")
age_label.pack()
age_textbox = tk.Entry(root)
age_textbox.pack()

#Adding DOB(Date of Birth)
dob_label = tk.Label(root, text="DOB : ")
dob_label.pack()
dob_textbox = tk.Entry(root)
dob_textbox.pack()

#Adding Class 
class_label = tk.Label(root, text="Class : ")
class_label.pack()
class_textbox = tk.Entry(root)
class_textbox.pack()

#Adding Gender
gender_label = tk.Label(root, text="Gender :")
gender_label.pack()
gender_textbox = tk.Entry(root)
gender_textbox.pack()

#Ading Email
email_label = tk.Label(root, text="Email : ")
email_label.pack()
email_textbox =tk.Entry(root)
email_textbox.pack()

#Addding Mobile number 
mobile_label = tk.Label(root, text="Mobile Number :")
mobile_label.pack()
mobile_textbox = tk.Entry(root)
mobile_textbox.pack()

#Adding Address
add_label = tk.Label(root, text="Address :")
add_label.pack()
add_textbox = tk.Entry(root)
add_textbox.pack()

#Adding submit button
submit_button = tk.Button(root, text="Submit")
submit_button.pack()

root.mainloop()