import tkinter as tk
from tkinter import messagebox

class IterationError(Exception):
    pass

class AgeError(Exception):
    pass

class HeightError(Exception):
    pass

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        
        if weight > 300:
            raise IterationError("Weight value is too high for this calculation.")
        
        if age < 0 or age > 120:
            raise AgeError("Invalid age. Please enter a valid age between 0 and 120.")
        
        if height < 0.5 or height > 3.0:
            raise HeightError("Invalid height. Please enter a valid height between 0.5 and 3.0 meters.")
        
        bmi = weight / (height * height)
        result_label.config(text=f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            messagebox.showinfo("BMI Category", "Underweight")
        elif 18.5 <= bmi < 24.9:
            messagebox.showinfo("BMI Category", "Normal weight")
        elif 24.9 <= bmi < 29.9:
            messagebox.showinfo("BMI Category", "Overweight")
        else:
            messagebox.showinfo("BMI Category", "Obese")
            
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except TypeError as e:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")
    except IterationError as e:
        messagebox.showerror("Error", str(e))
    except AgeError as e:
        messagebox.showerror("Error", str(e))
    except HeightError as e:
        messagebox.showerror("Error", str(e))
    finally:
        # Clear input fields and reset result label
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)
        result_label.config(text="")

def reset_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

def show_help():
    help_text = """
    BMI Calculator Help
    This program calculates your Body Mass Index (BMI).
    BMI is a measure of body fat based on weight and height.
    Enter your name, age, weight in kilograms, and height in meters,
    then click the 'Calculate BMI' button to get your BMI value.

    BMI Categories:
    - Underweight: BMI < 18.5
    - Normal weight: 18.5 <= BMI < 24.9
    - Overweight: 24.9 <= BMI < 29.9
    - Obese: BMI >= 30
    """
    messagebox.showinfo("Help", help_text)

root = tk.Tk()
root.title("Weight Calculator for Students and Teachers!")
root.geometry("500x400")
root.config(bg="light blue")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Reset", command=reset_fields)

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About BMI", command=show_help)

frame = tk.Frame(root)
frame.pack(pady=20)

name_label = tk.Label(frame, text="Name:")
name_label.grid(row=0, column=0, padx=10)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10)

age_label = tk.Label(frame, text="Age:")
age_label.grid(row=1, column=0, padx=10)
age_entry = tk.Entry(frame)
age_entry.grid(row=1, column=1, padx=10)

weight_label = tk.Label(frame, text="Weight (kg):")
weight_label.grid(row=2, column=0, padx=10)
weight_entry = tk.Entry(frame)
weight_entry.grid(row=2, column=1, padx=10)

height_label = tk.Label(frame, text="Height (m):")
height_label.grid(row=3, column=0, padx=10)
height_entry = tk.Entry(frame)
height_entry.grid(row=3, column=1, padx=10)

calculate_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=4, columnspan=2, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=5, columnspan=2)

root.mainloop()
