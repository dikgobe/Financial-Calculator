
import math
 
while True:
    print("======Welcome to the Midnight Coders Finance Calculator!======")
    print("Please choose either 'i' for investment, 'b' for bond, or 'e' for exit.")
    user_choice = input("Enter your choice: ").lower()
 
    if user_choice == "i":
        while True:
            try:
                principal = float(input("Enter the amount of money: R "))
                if principal >= 0.1:
                    break
                else:
                    print("Invalid input. Principal amount cannot be zero or negative.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
 
        years = 0
        while years <= 0:
            try:
                years = float(input("Enter the number of years: "))
                if years <= 0:
                    print("Invalid input. Number of years must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
 
        interest_type = input("Choose 's' for simple or 'c' for compound interest: ").lower()
 
       if interest_type == "s":
                 interest_rate = 8
                 final_amount = principal * (1 + (interest_rate / 100) * years)
        elif interest_type == "c":
             interest_rate = 8
              #Compound interest calculation
             final_amount = principal * math.pow(1 + (interest_rate / 100), years)
            # compound_interest = principal * (math.pow(1 + (interest_rate / 100), time)) - principal
        else:
            print("Invalid interest type. Please choose 's' for simple or 'c' for compound interest.")
            continue

        # Simple Interest Calculation
       # final_amount = (principal * interest_rate  *years)/ 100
        print(f"The total amount of your investment will be R {final_amount:.2f} after {years} years at an interest rate of {interest_rate}%.")
 
    elif user_choice == "b":
        while True:
            try:
                principal = float(input("Enter the present value of the house: R "))
                if principal >= 0:
                    break
                else:
                    print("Invalid input. Principal amount cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
 
        months = 0
        while months <= 0:
            try:
                months = float(input("Enter the number of months for repayment: "))
                if months <= 0:
                    print("Invalid input. Number of months must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
 
        interest_rate = 8.25
        monthly_interest_rate = (interest_rate / 100) / 12
        bond_repayment = (principal * monthly_interest_rate) / (1 - math.pow((1 + monthly_interest_rate), -months))
 
        print(f"Your monthly bond repayment will be R {bond_repayment:.2f} at an interest rate of {interest_rate}%.")
 
    if user_choice == "e":
        print("Thank you for using the Finance Calculator. Goodbye!")
        break
 
    else:
        print("Invalid input. Please enter 'i' for investment, 'b' for bond, or 'e' for exit to proceed.")
 
