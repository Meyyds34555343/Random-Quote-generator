import tkinter as tk
import random
from tkinter import messagebox

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don't let yesterday take up too much of today.",
    "It's not whether you get knocked down, it's whether you get up.",
    "If you are working on something exciting, it will keep you motivated.",
    "Success is not in what you have, but who you are.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don't watch the clock; do what it does. Keep going."
]

def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)

def copy_quote():
    quote = quote_label.cget("text")
    if quote:
        root.clipboard_clear()
        root.clipboard_append(quote)
        messagebox.showinfo("Copied", "Quote copied to clipboard!")

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("600x300")
root.resizable(0, 0)
root.configure(bg="#f0f0f0")


heading = tk.Label(root, text="Random Quote Generator", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
heading.pack(pady=20)

quote_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=500, justify="center", bg="white", fg="#333", pady=10, width=50)
quote_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

show_button = tk.Button(button_frame, text="Show Quote", font=("Helvetica", 12), bg="#4CAF50", fg="white", width=15, command=show_quote)
show_button.grid(row=0, column=0, padx=10)

copy_button = tk.Button(button_frame, text="Copy Quote", font=("Helvetica", 12), bg="#2196F3", fg="white", width=15, command=copy_quote)
copy_button.grid(row=0, column=1, padx=10)

root.mainloop()
