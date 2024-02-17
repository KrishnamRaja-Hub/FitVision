import tkinter as tk
from tkinter import ttk, PhotoImage
import subprocess
import os

class AppDelegate:
    def applicationSupportsSecureRestorableState(self):
        return True

def start_exercise():
    selected_exercise = exercise_combobox.get()
    if selected_exercise == "Shoulder Press":
        status_label.config(text=f"Please wait, Starting exercise: {selected_exercise}...")
        subprocess.Popen(["python", "exercise_models/shoulder_press.py"])
    elif selected_exercise == "Bicep Curl":
        status_label.config(text=f"Please wait, Starting exercise: {selected_exercise}...")
        subprocess.Popen(["python", "exercise_models/bicep_curl.py"])
    elif selected_exercise == "Plank":
        status_label.config(text=f"Please wait, Starting exercise: {selected_exercise}...")
        subprocess.Popen(["python", "exercise_models/Plank.py"])
    elif selected_exercise == "Leg Lifting":
        status_label.config(text=f"Please wait, Starting exercise: {selected_exercise}...")
        subprocess.Popen(["python", "exercise_models/side_lying_leg_lifting.py"])
    elif selected_exercise == "Tricep":
        status_label.config(text=f"Please wait, Starting exercise: {selected_exercise}...")
        subprocess.Popen(["python", "exercise_models/tricep.py"])
    elif selected_exercise == "Lunges":
        status_label.config(text=f"Please wait, Starting exercise: {selected_exercise}...")
        subprocess.Popen(["python", "exercise_models/lunges.py"])
    else:
        status_label.config(text="Please select an exercise.")


# Create the main window
root = tk.Tk()
root.title("Fitvision")
root.geometry("600x400")
root.resizable(False, False)  # Fix window size

# Set application delegate to handle secure restorable state
app_delegate = AppDelegate()
root.createcommand("::tk::mac::ReopenApplication", app_delegate.applicationSupportsSecureRestorableState)

# Print current directory for debugging
print("Current directory:", os.getcwd())

# Print list of files in the directory for debugging
print("Files in current directory:", os.listdir())

# Load the background image with a try-except block
bg = None
try:
    bg = PhotoImage(file="background_image2.png")
    label1 = tk.Label(root, image=bg)
    label1.place(y=0, x=0)
except Exception as e:
    print("Error loading background image:", e)

# Load the icon image with a try-except block
icon_image = None
try:
    icon_image = PhotoImage(file="Running.png")
except Exception as e:
    print("Error loading icon image:", e)

# Create a label
title_label = ttk.Label(root, text="FitVision: Smart Posture Analysis for Effective Workouts", background="#b0c793",
                        font=("Helvetica", 16), foreground="#252518")
title_label.pack(pady=10)

instruction_label = ttk.Label(root, text="Select an exercise:", font=("Helvetica", 14), background="#b0c793")
instruction_label.place(x=150, y=120)

# Create a combo box for exercise selection with a rounded button
exercises = ["Select an exercise", "Shoulder Press", "Bicep Curl", "Plank", "Leg Lifting", "Tricep"]
style = ttk.Style()
style.map("TCombobox", fieldbackground=[("readonly", "white")])
exercise_combobox = ttk.Combobox(root, values=exercises, state="readonly", font=("Helvetica", 12), background="#b0c793", width=20)
exercise_combobox.set(exercises[0])
exercise_combobox.place(x=320, y=120)

# Create a button to start the exercise with rounded edges
if icon_image:
    style.configure("TButton", borderwidth=0, relief="flat", font=("Helvetica", 11), background="#b0c793", color ="#b0c793")
    start_button = ttk.Button(root, text="Start Exercise", command=start_exercise, image=icon_image, compound="left")
    start_button.place(x=320, y=150)
else:
    start_button = ttk.Button(root, text="Start Exercise", command=start_exercise)
    start_button.place(x=320, y=150)
    print("Icon image is not available.")

# Create a label for displaying the exercise status
status_label = ttk.Label(root, font=("Helvetica", 12), background="#b0c793")
status_label.place(x=250, y=220)

# Run the GUI
root.mainloop()
