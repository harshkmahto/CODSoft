import tkinter as tk
from tkinter import messagebox
import random

def play(choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        return "You win!"
    else:
        return "You lose!"

# Setting up the UI
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x400")

label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play('Rock'), width=10)
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play('Paper'), width=10)
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play('Scissors'), width=10)

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), pady=20)
result_label.pack()

root.mainloop()