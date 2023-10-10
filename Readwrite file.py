import tkinter as tk
from tkinter import ttk, messagebox
import re

def submit_form():
    # Get user input
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    email = email_entry.get()  # New: Get email input
    name = name_entry.get()    # New: Get name input

    # Password validation regex
    password_regex = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$')

    # Email validation regex
    email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

    # Perform form validation
    if not (username and password and confirm_password and email and name):
        messagebox.showerror("Error", "All fields are required")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    elif not password_regex.match(password):
        messagebox.showerror("Error", "Password should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")
    elif not email_regex.match(email):
        messagebox.showerror("Error", "Invalid email address format")
    else:
        # Check if the username is unique
        with open("user_data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                stored_username = parts[0]
                stored_password = parts[1]
                if username == stored_username:
                    messagebox.showerror("Error", "Username already exists")
                    return

        # Save user data to the text file
        with open("user_data.txt", "a") as file:
            file.write(f"{username},{password},{email},{name}\n")  # Added email and name

        messagebox.showinfo("Success", "Registration successful")
        clear_fields()

# Function to search for a username
def search_username():
    target_username = search_entry.get()
    if not target_username:
        messagebox.showerror("Error", "Enter a username to search")
        return

    with open("user_data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(",")
            stored_username = parts[0]
            stored_password = parts[1]
            if target_username == stored_username:
                user_info = f"Username: {stored_username}\nEmail: {stored_password}"
                messagebox.showinfo("User Info", user_info)
                return

    messagebox.showerror("Error", "Username not found")

# Function to clear input fields
def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)  # Clear email field
    name_entry.delete(0, tk.END)    # Clear name field

def update_user_data():
    target_username = update_username_entry.get()
    new_password = update_password_entry.get()
    new_email = update_email_entry.get()
    new_name = update_name_entry.get()

    # Check if the username exists in the file
    with open("user_data.txt", "r") as file:
        lines = file.readlines()
    found = False
    updated_lines = []
    for line in lines:
        parts = line.strip().split(",")
        stored_username = parts[0]
        stored_password = parts[1]
        stored_email = parts[2]
        stored_name = parts[3]

        if target_username == stored_username:
            updated_lines.append(f"{target_username},{new_password},{new_email},{new_name}\n")
            found = True

    if not found:
        messagebox.showerror("Error", "Username not found")
    else:
        # Write the updated data back to the file
        with open("user_data.txt", "w") as file:
            file.writelines(updated_lines)
        messagebox.showinfo("Success", "User data updated successfully")

# Function to delete user data by username
def delete_user_data():
    target_username = delete_username_entry.get()

    # Check if the username exists in the file
    with open("user_data.txt", "r") as file:
        lines = file.readlines()
    found = False
    updated_lines = []
    for line in lines:
        parts = line.strip().split(",")
        stored_username = parts[0]

        if target_username == stored_username:
            found = True

    if not found:
        messagebox.showerror("Error", "Username not found")
    else:
        # Write the updated data back to the file
        with open("user_data.txt", "w") as file:
            file.writelines(updated_lines)
        messagebox.showinfo("Success", "User data deleted successfully")

def calculate():
    try:
        expression = calculator_entry.get()
        result = eval(expression)
        calculator_result.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")

# Create the main window
window = tk.Tk()
window.title("Registration and Search Form")

# Set the background color to light yellow
window.configure(bg="light yellow")

# Set the initial window size (width x height)
window.geometry("600x700")  # Adjust the width (600) and height (400) as needed

# Create labels and input fields for registration
registration_label = tk.Label(window, text="Registration Form", font=("Helvetica", 16), bg="light yellow")
registration_label.pack()

username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")  # Show asterisks for password
password_entry.pack()

confirm_password_label = tk.Label(window, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(window, show="*")  # Show asterisks for password
confirm_password_entry.pack()

email_label = tk.Label(window, text="Email:")  # New: Email label
email_label.pack()
email_entry = tk.Entry(window)                # New: Email input field
email_entry.pack()

name_label = tk.Label(window, text="Name:")    # New: Name label
name_label.pack()
name_entry = tk.Entry(window)                 # New: Name input field
name_entry.pack()

submit_button = tk.Button(window, text="Submit", command=submit_form, font=("Helvetica", 12), bg="green")
submit_button.pack()

# Create labels and input fields for search
search_label = tk.Label(window, text="Search Form", font=("Helvetica", 16), bg="light yellow")
search_label.pack()

search_username_label = tk.Label(window, text="Enter Username to Search:")
search_username_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()

search_button = tk.Button(window, text="Search", command=search_username, font=("Helvetica", 12), bg="green")
search_button.pack()
calculator_label = tk.Label(window, text="Calculator", font=("Helvetica", 16), bg="light yellow")
calculator_label.pack()

calculator_entry = tk.Entry(window, width=30)
calculator_entry.pack()

calculator_result = tk.StringVar()
calculator_result.set("")  # Initialize the result to an empty string
result_label = tk.Label(window, textvariable=calculator_result)
result_label.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate, font=("Helvetica", 12), bg="blue")
calculate_button.pack()

update_label = tk.Label(window, text="Update User Data", font=("Helvetica", 16), bg="light yellow")
update_label.pack()

update_username_label = tk.Label(window, text="Enter Username:")
update_username_label.pack()
update_username_entry = tk.Entry(window)
update_username_entry.pack()

update_password_label = tk.Label(window, text="New Password:")
update_password_label.pack()
update_password_entry = tk.Entry(window, show="*")  # Show asterisks for password
update_password_entry.pack()

update_email_label = tk.Label(window, text="New Email:")
update_email_label.pack()
update_email_entry = tk.Entry(window)
update_email_entry.pack()

update_name_label = tk.Label(window, text="New Name:")
update_name_label.pack()
update_name_entry = tk.Entry(window)
update_name_entry.pack()

update_button = tk.Button(window, text="Update", command=update_user_data, font=("Helvetica", 12), bg="green")
update_button.pack()

# Create a delete user data widget
delete_label = tk.Label(window, text="Delete User Data", font=("Helvetica", 16), bg="light yellow")
delete_label.pack()

delete_username_label = tk.Label(window, text="Enter Username:")
delete_username_label.pack()
delete_username_entry = tk.Entry(window)
delete_username_entry.pack()

delete_button = tk.Button(window, text="Delete", command=delete_user_data, font=("Helvetica", 12), bg="red")
delete_button.pack()

# Start the GUI application
window.mainloop()
