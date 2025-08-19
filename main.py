import tkinter as tk

# Create the main window. main window is called root
root = tk.Tk()

# Add a title to main window
root.title("ATM Simulator")
# Specify main window size
root.geometry("500x400")

# Add check balance button
check_balance_btn = tk.Button(root, text="Check Balance")
check_balance_btn.pack(side="left")

# Open the window
root.mainloop()
