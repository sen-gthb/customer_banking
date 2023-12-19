# Import the create_cd_account and create_savings_account functions
from cd_account_SM import create_cd_account 
from savings_account_SM import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Please enter your savings account balance."))
    savings_interest = float(input("Please enter your interest rate."))
    savings_maturity = float(input("Please enter the number of months for your savings account."))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The interest earned on your savings account is {interest_earned:.2f}, your updated savings balance is {updated_savings_balance:.2f} in {savings_maturity} months.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Please eneter your cd account balance."))
    cd_interest = float(input("Please enter your cd interest rate."))
    cd_maturity = float(input("Please enter the number of months for your cd account."))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your cd account interest earned is {cd_interest:.2f}, your updated cd account balance with interest is {updated_cd_balance:.2f}, in {cd_maturity} months.")

if __name__ == "__main__":
    main()