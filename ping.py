#!/usr/bin/python3
import os
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Ping function
def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", host]
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Handle ping from GUI input
def perform_ping():
    host = host_entry.get().strip()
    if not host:
        messagebox.showwarning("Input Error", "Please enter a hostname or IP address.")
        return
    
    result_text.delete(1.0, tk.END)  # Clear previous results
    response = ping(host)
    
    if response.returncode == 0:
        result_text.insert(tk.END, f"Ping to {host} was successful.\n\n")
        result_text.insert(tk.END, response.stdout)
    else:
        result_text.insert(tk.END, f"Ping to {host} failed.\n\n")
        result_text.insert(tk.END, response.stderr)

# Create the GUI window
window = tk.Tk()
window.title("Ping Tool")
window.geometry("600x400")
window.resizable(False, False)

# Input field
tk.Label(window, text="Enter host (e.g. google.com or 8.8.8.8):").pack(pady=10)
host_entry = tk.Entry(window, width=50)
host_entry.pack()

# Button
ping_button = tk.Button(window, text="Ping Host", command=perform_ping)
ping_button.pack(pady=10)

# Result box
result_text = scrolledtext.ScrolledText(window, width=70, height=15)
result_text.pack(pady=10)

# Run the GUI event loop
window.mainloop()
