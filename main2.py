import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time
import datetime

running = False


def reminder():
    global running

    name = name_entry.get()
    password = pass_entry.get()
    duration = duration_entry.get()

    if password != "1234":
        messagebox.showerror("Error", "Invalid Passkey!")
        return

    if not duration.isdigit():
        messagebox.showerror("Error", "Enter duration in seconds.")
        return

    messagebox.showinfo("Welcome", f"Welcome {name}!")

    running = True
    start = time.time()

    reminders = [
        "Reminder : Drink Water",
        "Reminder : Take Medicine",
        "Reminder : Go for a walk",
        "Reminder : Do some exercise"
    ]

    while running and time.time() - start < int(duration):
        for msg in reminders:
            if not running:
                break

            status.config(
                text=f"{datetime.datetime.now().strftime('%H:%M:%S')} : {msg}"
            )

            pyautogui.typewrite(msg)
            pyautogui.press("enter")
            time.sleep(1)

    status.config(text="Program Stopped")


def start_program():
    thread = threading.Thread(target=reminder)
    thread.daemon = True
    thread.start()


def stop_program():
    global running
    running = False


root = tk.Tk()
root.title("Health Reminder")
root.geometry("400x350")
root.resizable(False, False)

title = tk.Label(root, text="Health Reminder System",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

tk.Label(root, text="Name").pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Passkey").pack()

pass_entry = tk.Entry(root, show="*", width=30)
pass_entry.pack()

tk.Label(root, text="Duration (seconds)").pack()

duration_entry = tk.Entry(root, width=30)
duration_entry.insert(0, "20")
duration_entry.pack(pady=5)

start_btn = tk.Button(root,
                      text="Start Reminder",
                      bg="green",
                      fg="white",
                      width=20,
                      command=start_program)

start_btn.pack(pady=10)

stop_btn = tk.Button(root,
                     text="Stop",
                     bg="red",
                     fg="white",
                     width=20,
                     command=stop_program)

stop_btn.pack()

status = tk.Label(root,
                  text="Status : Waiting...",
                  fg="blue",
                  font=("Arial", 10))

status.pack(pady=20)

root.mainloop()