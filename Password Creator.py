import random
import tkinter as tk
from tkinter import Toplevel, Label

# Function to generate password
def generate_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/,._-"
    
    all_chars = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(all_chars, length))
    
    # Create a new window to show the password
    password_window = Toplevel(root)
    password_window.title("Generated Password")
    password_window.geometry("300x100")
    
    # Display the password
    Label(password_window, text="Generated Password:", font=("Arial", 12)).pack(pady=5)
    Label(password_window, text=password, font=("Arial", 18, "bold"), fg="green").pack()

# Function to stop command

def close_windows():
    quit()

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x200")

# Button to generate password
btn = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
btn.pack(pady=20)

# Button to Close Program
btn = tk.Button(root, text="Close", font=("Arial", 12), command=close_windows)
btn.pack(pady=20)

# Run the application
root.mainloop()
