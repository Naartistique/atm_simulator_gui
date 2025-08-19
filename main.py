import tkinter as tk
from commands import check_balance

# Create the main window. main window is called root
root = tk.Tk()

# Add a title to main window
root.title("ATM Simulator")
# Specify main window size
root.geometry("500x400")

# Add account number entry
account_number_entry = tk.Entry(root, width=30)
account_number_entry.pack(side="top")

# Add check balance button
check_balance_btn = tk.Button(root, text="Check Balance", command=lambda : check_balance(account_number=account_number_entry.get()))
check_balance_btn.pack(side="top")

# Add deposit button
deposit_button = tk.Button(root, text="deposit")
deposit_button.pack(side="bottom")

# Open the window
root.mainloop()

# In programming, there is separation of concerns where codes are kepts then imported to merge.
#  this is breaking things in to multiple files.