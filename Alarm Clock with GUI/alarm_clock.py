import tkinter as tk
from tkinter import messagebox
import time
import pygame
from PIL import Image, ImageTk
from datetime import datetime

alarm_triggered = False  # Flag to keep track of whether the alarm has been triggered or not

def alarm():
    global alarm_triggered

    if not alarm_triggered:
        alarm_time = entry.get()
        current_time = datetime.now().strftime("%I:%M %p")  # Get current time in 12-hour format
        if current_time == alarm_time:
            pygame.mixer.init()
            pygame.mixer.music.load("alarm_sound.mp3")  # Replace "alarm_sound.mp3" with your alarm sound file
            pygame.mixer.music.play()

            # Show a message box to acknowledge the alarm and stop the sound
            response = messagebox.askokcancel("Alarm", "Time's up! Click OK to stop the alarm.")
            if response:
                pygame.mixer.music.stop()
                alarm_triggered = True  # Set the flag to indicate that the alarm has been triggered

def set_alarm():
    set_button.config(state=tk.DISABLED)
    alarm()

    # Schedule the alarm check every second
    root.after(1000, set_alarm)

def update_time_label():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    root.after(1000, update_time_label)

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("1125x750")
root.config(bg="#F0F0F0")  # Set a background color

# Load the modern clock image and display it using a label
image = Image.open("modern_clock_image.jpeg")  # Replace "modern_clock_image.jpeg" with your modern clock image file
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(root, width=1125, height=750, bg="#F0F0F0")  # Use a modern canvas background color
canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.pack(side=tk.LEFT)

label = tk.Label(root, text="Enter Alarm Time (HH:MM AM/PM):", font=("Helvetica", 15))  # Use a modern font
label.place(x=20, y=20, anchor="nw")

entry = tk.Entry(root, font=("Helvetica", 15))  # Use a modern font
entry.place(x=575, y=20, anchor="ne")

set_button = tk.Button(root, text="Set Alarm", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=set_alarm)  # Modern styling for the button
set_button.place(x=20, y=70, anchor="nw")

# Add a label to display live time in the top right side of the window
time_label = tk.Label(root, text="", font=("Helvetica", 18), bg="#F0F0F0")  # Use a modern font and background color
time_label.place(x=1100, y=20, anchor="ne")

# Start updating time_label every second
update_time_label()

root.mainloop()
