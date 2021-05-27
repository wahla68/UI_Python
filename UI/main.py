import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

# function to add applications to the list
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", ".exe"), ("all files", "*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, fg="orange",bg="grey")
        label.pack()

# function to run all applications in the list
def runApps():
    for app in apps:
        os.startfile(app)


# root.minsize(300, 300)
# root.geometry("800x800")
# create canvas
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

root.title("Start-Up Applications")
# root.configure(bg="green")

openfile = tk.Button(root, text="Open Applications", padx=10, pady=5, fg="white", bg="black", command=addApp)
openfile.pack()
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="black", command=runApps)
runApps.pack()
# show the data in saved text file on next login
for app in apps:
   label = tk.Label(frame, text=app,font=("Arial",18))
   label.pack()
root.mainloop()
# create txt file
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
