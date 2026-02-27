import tkinter as tk
from tkinter import messagebox

def messageboxx():
    messagebox.showinfo("Hello", "Hello, World!")

root = tk.Tk()
root.title("Hello, World!")

button1 = tk.Button(root, text="Click Me", command=messageboxx)
button1.pack(pady=20)


if __name__ == "__main__":
    root.mainloop()