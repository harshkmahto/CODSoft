from tkinter import *
from random import randint

root = Tk()
root.title("Strong Password Generator")
root.iconbitmap("PasswordGenerator/icon.ico")
root.geometry("500x400")

my_password = chr(randint(33, 126))

def new_rand():
    # Clear the password box
    pw_entry.delete(0, END)
    # Get password length and convert to integer
    password_length = int(my_entry.get())
    # Create a variable to hold password
    my_password = ""
    # Loop through password length
    for x in range(password_length):
        my_password += chr(randint(33, 126))
    # Output password to screen
    pw_entry.insert(0, my_password)
# Function to copy password to clipboard
# Label frame
lf = LabelFrame(root, text="How many characters")
lf.pack(pady=20)

# Entry box for number of characters
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Entry box for returned password
pw_entry = Entry(root, text="", font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# Create frame for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

root.mainloop()
