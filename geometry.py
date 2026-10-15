import tkinter as tk 
root=tk.Tk()
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
submit_button = tk.Button(root, text="Submit")
submit_button.pack(anchor=tk.W,padx=10)

root.mainloop()