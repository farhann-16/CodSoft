import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "gui_tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List App")
        self.root.geometry("450x500")
        self.root.configure(bg="#f0f2f5")

        self.tasks = load_tasks()

        header = tk.Label(root, text="To-Do List", font=("Arial", 20, "bold"), bg="#f0f2f5", fg="#333")
        header.pack(pady=10)

        self.task_input = tk.Entry(root, font=("Arial", 14), width=30)
        self.task_input.pack(pady=10)

        button_frame = tk.Frame(root, bg="#f0f2f5")
        button_frame.pack(pady=5)

        self.add_button = tk.Button(button_frame, text="➕ Add Task", width=12, command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(button_frame, text="✅ Mark Done", width=12, command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="🗑️ Delete Task", width=12, command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.task_listbox = tk.Listbox(root, width=45, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=15)
        self.load_task_listbox()

        self.exit_button = tk.Button(root, text="🚪 Exit", width=12, bg="#d9534f", fg="white", command=self.confirm_exit)
        self.exit_button.pack(pady=10)

    def add_task(self):
        task_title = self.task_input.get().strip()
        if task_title:
            self.tasks.append({"title": task_title, "completed": False})
            self.task_input.delete(0, tk.END)
            self.load_task_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = True
            self.load_task_listbox()
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            deleted_task = self.tasks.pop(index)
            self.load_task_listbox()
            save_tasks(self.tasks)
            messagebox.showinfo("Deleted", f"Deleted task: {deleted_task['title']}")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def load_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['completed'] else "✗"
            display = f"[{status}] {task['title']}"
            self.task_listbox.insert(tk.END, display)

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
