


"""Customer Feedback Application"""




# This program collects customer feedback through a simple form and saves it to a file, then shows a thank-you message in a new window.

# Import necessary libraries

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import datetime

# --- Function to handle Submit button ---
def submit_feedback():
    name = entry_name.get().strip()
    satisfaction = satisfaction_var.get()
    feedback = text_feedback.get("1.0", tk.END).strip()

    # Input validation
    if not name:
        messagebox.showerror("Input Error", "Please enter your name.")
        return
    if not satisfaction:
        messagebox.showerror("Input Error", "Please select a satisfaction level.")
        return
    if not feedback:
        messagebox.showerror("Input Error", "Please enter your feedback.")
        return

    # Save feedback to a file with timestamp
    with open("feedback.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - {name} - {satisfaction} - {feedback}\n")

    show_thank_you(name)
    clear_form()

# --- Function to clear the form ---
def clear_form():
    entry_name.delete(0, tk.END)
    satisfaction_var.set(None)
    text_feedback.delete("1.0", tk.END)

# --- Function to exit the app ---
def exit_app():
    root.destroy()

# --- Function to show a thank you window ---
def show_thank_you(name):
    thank_you_window = tk.Toplevel(root)
    thank_you_window.title("Thank You")
    thank_you_window.geometry("300x300")

    tk.Label(thank_you_window, text=f"Thank you, {name}!", font=("Arial", 14)).pack(pady=10)
    tk.Label(thank_you_window, text="We appreciate your feedback.", font=("Arial", 10)).pack(pady=5)

    # Load and display thumbs-up image
    thumbs_image = Image.open("thumbsup.png").resize((100, 100))
    thumbs_photo = ImageTk.PhotoImage(thumbs_image)
    thumbs_label = tk.Label(thank_you_window, image=thumbs_photo)
    thumbs_label.image = thumbs_photo  # for reference
    thumbs_label.pack(pady=10)

    tk.Button(thank_you_window, text="Close", command=thank_you_window.destroy).pack(pady=20)

# --- Main Window Setup ---
root = tk.Tk()
root.title("Customer Feedback")
root.geometry("500x600")

# --- Image  ---

banner_image = Image.open("banner1.png").resize((400, 100))
banner_photo = ImageTk.PhotoImage(banner_image)
tk.Label(root, image=banner_photo).pack()
tk.Label(root, text="Your Feedback is Appreciated").pack(pady=(0, 20))

# --- Form Fields ---
tk.Label(root, text="Name:", font=("Arial", 12)).pack(anchor='w', padx=20)
entry_name = tk.Entry(root, width=50)
entry_name.pack(padx=20, pady=5)

tk.Label(root, text="Satisfaction Level:", font=("Arial", 12)).pack(anchor='w', padx=20, pady=(10, 0))
satisfaction_var = tk.StringVar()
ttk.Radiobutton(root, text="Satisfied", variable=satisfaction_var, value="Satisfied").pack(anchor='w', padx=40)
ttk.Radiobutton(root, text="Neutral", variable=satisfaction_var, value="Neutral").pack(anchor='w', padx=40)
ttk.Radiobutton(root, text="Dissatisfied", variable=satisfaction_var, value="Dissatisfied").pack(anchor='w', padx=40)

tk.Label(root, text="Feedback Message:", font=("Arial", 12)).pack(anchor='w', padx=20, pady=(10, 0))
text_feedback = tk.Text(root, height=6, width=50)
text_feedback.pack(padx=20, pady=5)

# --- Buttons ---
tk.Button(root, text="Submit", command=submit_feedback, width=15, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Clear", command=clear_form, width=15, bg="#f0ad4e", fg="white").pack(pady=5)
tk.Button(root, text="Exit", command=exit_app, width=15, bg="#d9534f", fg="white").pack(pady=5)

# --- Run the GUI app ---
root.mainloop()
