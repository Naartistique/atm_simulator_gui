from tkinter import messagebox
import csv

def check_balance(account_number):
    # Open csv file
    # Read csv content
    # Show balance with message box
    csv_file = open(file="accounts.csv", mode="r")
    accounts = csv.DictReader(csv_file)
    for account in accounts:
        if account_number == account["account_number"]:
# Show balance with message box
           messagebox.showinfo(
             title="Check Balance", 
             message=f"Your balance is {account["balance"]}")
           return
# Show user and account not found message
    messagebox.showerror(
    title="check_balance",
    message= f"Account number {account_number} does not exist!")