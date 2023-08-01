import tkinter as tk
from tkinter import messagebox
import time
import pygame
from PIL import Image, ImageTk
from datetime import datetime

def alarm():
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

# Load the image and display it using a label
image = Image.open("clock_image.jpeg")  # Replace "clock_image.jpeg" with your clock image file
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(root, width=1125, height=750)
canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.pack()

label = tk.Label(root, text="Enter Alarm Time (HH:MM AM/PM):", font=("Arial", 15))
label_window = canvas.create_window(20, 20, anchor="nw", window=label)

entry = tk.Entry(root, font=("Arial", 15))
entry_window = canvas.create_window(345, 20, anchor="nw", window=entry)

set_button = tk.Button(root, text="Set Alarm", font=("Arial", 12), command=set_alarm)
set_button_window = canvas.create_window(20, 60, anchor="nw", window=set_button)

# Add a label to display live time in the top right side of the window
time_label = tk.Label(root, text="", font=("Arial", 14))
time_label.place(x=990, y=20, anchor="ne")

# Start updating time_label every second
update_time_label()

root.mainloop()
