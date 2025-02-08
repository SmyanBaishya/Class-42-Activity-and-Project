import tkinter as tk
from tkinter import messagebox

# Function to calculate interest

def calculate_interest():
    try:
        P = float(principal_entry.get())
        T = float(time_entry.get())
        R = float(rate_entry.get())
        interest = (P * T * R) / 100
        result_label.config(text="Simple Interest: ₹" + str(round(interest, 2)))

    except ValueError:

        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Creating main window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("300x250")

# Labels and Entry Fields
tk.Label(root, text="Principal Amount (₹):").pack(pady=5)
principal_entry = tk.Entry(root)
principal_entry.pack(pady=5)

tk.Label(root, text="Time Period (years):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calculate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Simple Interest: ₹0.00", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()

# CODE DOES NOT WORK ON VS, GO TO REPLIT > TKINTER.