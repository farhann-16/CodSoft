import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Generator")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f2f5")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Segoe UI", 11), padding=8)
        self.style.configure("TCheckbutton", font=("Segoe UI", 10))

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Secure Password Generator",
            font=("Segoe UI", 16, "bold"),
            bg="#f0f2f5",
            fg="#333"
        )
        title.pack(pady=10)

        frame = tk.Frame(self.root, bg="#f0f2f5")
        frame.pack(pady=10)

        tk.Label(
            frame,
            text="Password Length:",
            font=("Segoe UI", 12),
            bg="#f0f2f5"
        ).grid(row=0, column=0, sticky="w")
        self.length_entry = ttk.Entry(frame, width=10)
        self.length_entry.grid(row=0, column=1, padx=5)

        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        ttk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.include_upper).pack(anchor="w", padx=20)
        ttk.Checkbutton(self.root, text="Include Lowercase Letters", variable=self.include_lower).pack(anchor="w", padx=20)
        ttk.Checkbutton(self.root, text="Include Numbers", variable=self.include_digits).pack(anchor="w", padx=20)
        ttk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols).pack(anchor="w", padx=20)

        ttk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=15)

        self.result_entry = ttk.Entry(self.root, font=("Segoe UI", 12), width=30, justify="center")
        self.result_entry.pack(pady=5)

        ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

        tk.Button(
            self.root,
            text="Exit",
            font=("Segoe UI", 11),
            bg="#d9534f",
            fg="white",
            width=20,
            height=2,
            relief="raised",
            bd=2,
            command=self.root.quit
        ).pack(pady=15)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showwarning("Too Short", "Password length should be at least 4.")
                return

            characters = ""
            if self.include_upper.get():
                characters += string.ascii_uppercase
            if self.include_lower.get():
                characters += string.ascii_lowercase
            if self.include_digits.get():
                characters += string.digits
            if self.include_symbols.get():
                characters += string.punctuation

            if not characters:
                messagebox.showwarning("No Options", "Please select at least one character set.")
                return

            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, password)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for length.")

    def copy_to_clipboard(self):
        password = self.result_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update()
            messagebox.showinfo("Copied", "Password copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
