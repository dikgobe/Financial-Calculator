
import tkinter as tk
from tkinter import ttk
import math

def calculate_investment():
    # Check if the user has selected "Investment"
    if user_choice_var.get() != "Investment":
        result_label.config(text="Please select 'Investment' from the dropdown.")
        return

    try:
        principal = float(principal_entry.get())
        years = float(years_entry.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numeric values for principal and years.")
        return

    interest_type = interest_type_var.get()

    if interest_type == "Simple":
        interest_rate = 8
        final_amount = principal * (1 + (interest_rate / 100) * years)
    elif interest_type == "Compound":
        interest_rate = 8.25
        final_amount = principal * math.pow(1 + (interest_rate / 100), years)

    result_label.config(text=f"The total amount of your investment will be R {final_amount:.2f} after {years} years at an interest rate of {interest_rate}%.")

    # Reset input fields
    clear_inputs()

def calculate_bond():
    # Check if the user has selected "Bond"
    if user_choice_var.get() != "Bond":
        result_label.config(text="Please select 'Bond' from the dropdown.")
        return

    try:
        principal = float(principal_entry_bond.get())
        months = float(months_entry.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numeric values for principal and months.")
        return

    interest_rate = 8.25

    monthly_interest_rate = (interest_rate / 100) / 12
    bond_repayment = (principal * monthly_interest_rate) / (1 - math.pow((1 + monthly_interest_rate), -months))

    result_label.config(text=f"Your monthly bond repayment will be R {bond_repayment:.2f} at an interest rate of {interest_rate}%.")

    # Reset input fields
    clear_inputs()

def clear_inputs():
    principal_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)
    interest_type_combobox.set("")  # Clear the selection if any

    principal_entry_bond.delete(0, tk.END)
    months_entry.delete(0, tk.END)

try:
    root = tk.Tk()
    root.title("Midnight Coders Finance Calculator")
    root.configure(bg="black")  # Light Blue background color

    # Title label
    title_label = ttk.Label(root, text="WELCOME TO MIDNIGHT CODERS FINANCIAL CALCULATOR", font=("Tahoma", 15))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Label for user choice
    choice_label = ttk.Label(root, text="Choose 'Investment' or 'Bond':", background="#e44578")
    choice_label.grid(row=1, column=0, columnspan=2, pady=10)

    # Combobox for user choice
    user_choice_var = tk.StringVar()
    user_choice_combobox = ttk.Combobox(root, textvariable=user_choice_var, values=["Investment", "Bond"])
    user_choice_combobox.grid(row=2, column=0, columnspan=2, pady=10)

    # Investment Frame
    investment_frame = ttk.Frame(root, style="Blue.TFrame")  # Use a style for background color
    investment_frame.grid(row=3, column=0, padx=10, pady=10)

    # Investment Frame Widgets
    investment_subtitle_label = ttk.Label(investment_frame, text="Investment", font=("Tahoma", 12, "bold"))
    investment_subtitle_label.grid(row=0, column=0, columnspan=2, pady=5)

    principal_label = ttk.Label(investment_frame, text="Enter the amount of money: R")
    principal_label.grid(row=1, column=0, padx=5, pady=5)
    principal_entry = ttk.Entry(investment_frame)
    principal_entry.grid(row=1, column=1, padx=5, pady=5)

    years_label = ttk.Label(investment_frame, text="Enter the number of years:")
    years_label.grid(row=2, column=0, padx=5, pady=5)
    years_entry = ttk.Entry(investment_frame)
    years_entry.grid(row=2, column=1, padx=5, pady=5)

    interest_type_label = ttk.Label(investment_frame, text="Choose 'Simple' or 'Compound' interest:", background="#e44578")
    interest_type_label.grid(row=3, column=0, padx=5, pady=5)

    interest_type_var = tk.StringVar()
    interest_type_combobox = ttk.Combobox(investment_frame, textvariable=interest_type_var, values=["Simple", "Compound"])
    interest_type_combobox.grid(row=3, column=1, padx=5, pady=5)

    calculate_investment_button = ttk.Button(investment_frame, text="Calculate Investment", command=calculate_investment)
    calculate_investment_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Bond Frame
    bond_frame = ttk.Frame(root, style="Blue.TFrame")  # Use a style for background color
    bond_frame.grid(row=3, column=1, padx=10, pady=10)

    # Bond Frame Widgets
    bond_subtitle_label = ttk.Label(bond_frame, text="Bond", font=("Tahoma", 12, "bold"), background="#e44578")
    bond_subtitle_label.grid(row=0, column=0, columnspan=2, pady=5)

    principal_label_bond = ttk.Label(bond_frame, text="Enter the present value of the house: R", background="#e44578")
    principal_label_bond.grid(row=1, column=0, padx=5, pady=5)
    principal_entry_bond = ttk.Entry(bond_frame)
    principal_entry_bond.grid(row=1, column=1, padx=5, pady=5)

    months_label = ttk.Label(bond_frame, text="Enter the number of months for repayment:", background="#e44578")
    months_label.grid(row=2, column=0, padx=5, pady=5)
    months_entry = ttk.Entry(bond_frame)
    months_entry.grid(row=2, column=1, padx=5, pady=5)

    calculate_bond_button = ttk.Button(bond_frame, text="Calculate Bond Repayment", command=calculate_bond)
    calculate_bond_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Result Label
    result_label = ttk.Label(root, text="", background="#e44578")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    # Style for blue frame
    style = ttk.Style()
    style.configure("Blue.TFrame", background="#e44578")

    root.mainloop()

except Exception as e:
    print(f"An error occurred: {e}")
    # Handle the error as needed
