import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Simple Calculator")
        self.root.geometry("350x400")
        self.root.configure(bg="#f5f5f5")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Segoe UI", 12), padding=10)
        self.style.configure("TEntry", font=("Segoe UI", 14))
        
        self.build_ui()

    def build_ui(self):
        title = tk.Label(self.root, text="Simple Calculator", font=("Segoe UI", 18, "bold"), bg="#f5f5f5", fg="#333")
        title.pack(pady=10)

        self.entry1 = ttk.Entry(self.root, width=15, justify="center")
        self.entry1.pack(pady=10)

        self.entry2 = ttk.Entry(self.root, width=15, justify="center")
        self.entry2.pack(pady=10)

        self.operation = ttk.Combobox(self.root, values=["Add", "Subtract", "Multiply", "Divide"], state="readonly", font=("Segoe UI", 12))
        self.operation.current(0)
        self.operation.pack(pady=10)

        calc_btn = ttk.Button(self.root, text="Calculate", command=self.calculate)
        calc_btn.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Segoe UI", 14), bg="#f5f5f5", fg="#007acc")
        self.result_label.pack(pady=10)

        exit_btn = ttk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_btn.pack(pady=5)

    def calculate(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            op = self.operation.get()

            if op == "Add":
                result = num1 + num2
            elif op == "Subtract":
                result = num1 - num2
            elif op == "Multiply":
                result = num1 * num2
            elif op == "Divide":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2

            self.result_label.config(text=f"Result: {result:.2f}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
