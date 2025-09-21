import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

bmi_history = []

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
        bmi_history.append(bmi)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

def show_graph():
    if not bmi_history:
        messagebox.showinfo("No Data", "No BMI history available.")
        return
    plt.plot(bmi_history, marker="o", linestyle="-", color="blue")
    plt.title("BMI Trend")
    plt.xlabel("Entry Number")
    plt.ylabel("BMI Value")
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Show Graph", command=show_graph).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
