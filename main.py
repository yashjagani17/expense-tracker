import pandas as pd
from datetime import datetime as dt
import os
import getpass

FILE = 'expenses.csv'

def add_expense(df, amount, category, notes):
    now = dt.now()
    df.loc[len(df.index)] = [
        now.strftime('%d/%m/%Y'),
        now.strftime('%H:%M'),
        amount,
        category.strip().title(),
        notes
    ]
    return df

def validate_choice():
    while True:
        userinput = input("1 - Add Expense\n2 - View Expenses\n3 - Expenses Summary\n4 - Exit\n\n")
        try:
            choice = int(userinput)
            if 1 <= choice <= 4:
                return choice
            else:
                print(f"{userinput} is invalid. Must be a valid option from 1-4\n")
        except ValueError:
            print(f"{userinput} is invalid. Please enter a number\n")

def validate_amount():
    while True:
        userinput = input("Enter the amount: £").strip().replace(',', '')
        try:
            amount = float(userinput)
            if amount > 0:
                return amount
            else:
                print(f"£{userinput} is invalid. Must be greater than £0\n")
        except ValueError:
            print(f"{userinput} is invalid. Please enter a number\n")
        
def clear_screen():
    print("\033[H\033[J", end="")

def spend_by_category(df):
    if df.empty:
        return "No recorded expenses available to query"
    summary = df.copy().groupby('Category')['Amount'].sum().reset_index()
    summary['Amount'] = summary['Amount'].map('£{:.2f}'.format)
    return summary.to_string(index=False)

def format_expenses(df):
    if df.empty:
        return "No recorded expenses available to query"
    df_print = df.copy()
    df_print['Amount'] = df_print['Amount'].map('£{:.2f}'.format)
    return df_print.to_string(index=False)

def main():
    try:
        if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
            df = pd.read_csv(FILE)
        else:
            df = pd.DataFrame(columns=["Date", "Time", "Amount", "Category", "Notes"])
    except (pd.errors.ParserError, FileNotFoundError):
        print("Error parsing the expenses file\nGenerating a blank template\n")
        df = pd.DataFrame(columns=["Date", "Time", "Amount", "Category", "Notes"])
    while True:
        clear_screen()
        greeting = "CLI-based Personal Expense Tracker\n"
        print(f"{greeting}{'-' * len(greeting)}")
        choice = validate_choice()
        if choice == 1:
            clear_screen()
            df = add_expense(
                df,
                validate_amount(),
                input("Category: "),
                input("Notes: ")
                )
            try:
                df.to_csv(FILE, index=False)
                print("\nExpense has been saved")
            except:
                print("Failed to save the expense")
            getpass.getpass(prompt="Press Enter to go back to the menu\n")
        elif choice == 2:
            clear_screen()
            print(f"{format_expenses(df)}\n")
            getpass.getpass(prompt="Press Enter to go back to the menu\n")
        elif choice == 3:
            clear_screen()
            print(f"{spend_by_category(df)}\n")
            getpass.getpass(prompt="Press Enter to go back to the menu\n")
        else:
            print("\nThank you for using the Personal Expense Tracker")
            break
    
if __name__ == "__main__":
    main()