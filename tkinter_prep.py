#Tkinter is Python’s built‑in module for creating Graphical User Interfaces (GUIs). 
# It acts as a bridge between Python and the Tcl/Tk toolkit, allowing you to build windows, buttons, labels, text boxes ect.

import tkinter as tk
root=tk.Tk() #Here Tk = means tool kit and also root variable got permission to place all the tooles from the Tkinter module.
#root= will now become your main background window or container.
name_label = tk.Label(root, text="name?")
name_label.pack() #pack() method is used to display the widget on the screen. It organizes widgets in blocks before placing them in the parent widget.
name_textbox = tk.Entry(root)
name_textbox.pack()

email_label = tk.Label(root, text="email?")
email_label.pack() #pack() method is used to display the widget on the screen. It organizes widgets in blocks before placing them in the parent widget.
email_textbox = tk.Entry(root)
email_textbox.pack()

mobile_label = tk.Label(root, text="mobile number?")
mobile_label.pack() #pack() method is used to display the widget on the screen.
mobile_textbox = tk.Entry(root)
mobile_textbox.pack()

root.mainloop()