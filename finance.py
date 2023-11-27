
import tkinter as tk
from tkinter import ttk
import math

def calculate_investment():
    principal = float(principal_entry.get())
    years = float(years_entry.get())
    interest_type = interest_type_var.get()

    if interest_type == "Simple":
        interest_rate = 8
        final_amount = principal * (1 + (interest_rate / 100) * years)
    elif interest_type == "Compound":
        interest_rate = 8
        final_amount = principal * math.pow(1 + (interest_rate / 100), years)

    result_label.config(text=f"The total amount of your investment will be R {final_amount:.2f} after {years} years at an interest rate of {interest_rate}%.")

    # Reset input fields
    clear_inputs()

def calculate_bond():
    principal = float(principal_entry_bond.get())
    months = float(months_entry.get())
    interest_rate = 8.25

    monthly_interest_rate = (interest_rate / 100) / 12
    bond_repayment = (principal * monthly_interest_rate) / (1 - math.pow((1 + monthly_interest_rate), -months))

    result_label.config(text=f"Your monthly bond repayment will be R {bond_repayment:.2f} at an interest rate of {interest_rate}%.")

    # Reset input fields
    clear_inputs()

def clear_inputs():
    principal_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)
    principal_entry_bond.delete(0, tk.END)
    months_entry.delete(0, tk.END)

# Main GUI window
root = tk.Tk()
root.title("Midnight Coders Finance Calculator")

# Label for user choice
choice_label = ttk.Label(root, text="Choose 'Investment' or 'Bond':")
choice_label.grid(row=0, column=0, columnspan=2)

# Combobox for user choice
user_choice_var = tk.StringVar()
user_choice_combobox = ttk.Combobox(root, textvariable=user_choice_var, values=["Investment", "Bond"])
user_choice_combobox.grid(row=1, column=0, columnspan=2)

# Investment Frame
investment_frame = ttk.Frame(root)
investment_frame.grid(row=2, column=0, padx=10, pady=10)

# Bond Frame
bond_frame = ttk.Frame(root)
bond_frame.grid(row=2, column=1, padx=10, pady=10)

# Investment Frame Widgets
principal_label = ttk.Label(investment_frame, text="Enter the amount of money: R")
principal_label.grid(row=0, column=0, padx=5, pady=5)
principal_entry = ttk.Entry(investment_frame)
principal_entry.grid(row=0, column=1, padx=5, pady=5)

years_label = ttk.Label(investment_frame, text="Enter the number of years:")
years_label.grid(row=1, column=0, padx=5, pady=5)
years_entry = ttk.Entry(investment_frame)
years_entry.grid(row=1, column=1, padx=5, pady=5)

interest_type_label = ttk.Label(investment_frame, text="Choose 'Simple' or 'Compound' interest:")
interest_type_label.grid(row=2, column=0, padx=5, pady=5)

interest_type_var = tk.StringVar()
interest_type_combobox = ttk.Combobox(investment_frame, textvariable=interest_type_var, values=["Simple", "Compound"])
interest_type_combobox.grid(row=2, column=1, padx=5, pady=5)

calculate_investment_button = ttk.Button(investment_frame, text="Calculate Investment", command=calculate_investment)
calculate_investment_button.grid(row=3, column=0, columnspan=2, pady=10)

# Bond Frame Widgets
principal_label_bond = ttk.Label(bond_frame, text="Enter the present value of the house: R")
principal_label_bond.grid(row=0, column=0, padx=5, pady=5)
principal_entry_bond = ttk.Entry(bond_frame)
principal_entry_bond.grid(row=0, column=1, padx=5, pady=5)

months_label = ttk.Label(bond_frame, text="Enter the number of months for repayment:")
months_label.grid(row=1, column=0, padx=5, pady=5)
months_entry = ttk.Entry(bond_frame)
months_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_bond_button = ttk.Button(bond_frame, text="Calculate Bond Repayment", command=calculate_bond)
calculate_bond_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
