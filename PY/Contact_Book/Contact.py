import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📒 Contact Book")
        self.root.geometry("500x600")
        self.root.configure(bg="#f1f3f5")

        self.contacts = load_contacts()

        tk.Label(root, text="Contact Book", font=("Segoe UI", 20, "bold"), bg="#f1f3f5", fg="#343a40").pack(pady=10)

        self.listbox = tk.Listbox(root, font=("Segoe UI", 12), width=50, height=15)
        self.listbox.pack(pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.contact_details = tk.Label(root, text="", font=("Segoe UI", 11), bg="#f1f3f5", fg="#495057")
        self.contact_details.pack()

        btn_frame = tk.Frame(root, bg="#f1f3f5")
        btn_frame.pack(pady=10)

        self.add_btn = tk.Button(btn_frame, text="Add Contact", width=15, bg="#0d6efd", fg="white", command=self.add_contact)
        self.add_btn.grid(row=0, column=0, padx=5, pady=5)

        self.update_btn = tk.Button(btn_frame, text="Update Contact", width=15, bg="#ffc107", fg="black", command=self.update_contact)
        self.update_btn.grid(row=0, column=1, padx=5, pady=5)

        self.delete_btn = tk.Button(btn_frame, text="Delete Contact", width=15, bg="#dc3545", fg="white", command=self.delete_contact)
        self.delete_btn.grid(row=0, column=2, padx=5, pady=5)

        self.search_btn = tk.Button(root, text="🔍 Search Contact", width=25, bg="#20c997", fg="white", command=self.search_contact)
        self.search_btn.pack(pady=10)

        self.exit_btn = tk.Button(root, text="Exit", width=20, bg="#6c757d", fg="white", command=root.quit)
        self.exit_btn.pack(pady=5)

        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def on_select(self, event):
        selected = self.listbox.curselection()
        if selected:
            contact = self.contacts[selected[0]]
            details = f"📞 {contact['phone']}\n📧 {contact['email']}\n🏠 {contact['address']}"
            self.contact_details.config(text=details)
        else:
            self.contact_details.config(text="")

    def add_contact(self):
        name = simpledialog.askstring("Name", "Enter contact name:")
        phone = simpledialog.askstring("Phone", "Enter phone number:")
        email = simpledialog.askstring("Email", "Enter email:")
        address = simpledialog.askstring("Address", "Enter address:")
        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            save_contacts(self.contacts)
            self.refresh_listbox()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required.")

    def update_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a contact to update.")
            return
        index = selected[0]
        contact = self.contacts[index]
        name = simpledialog.askstring("Name", "Update name:", initialvalue=contact['name'])
        phone = simpledialog.askstring("Phone", "Update phone:", initialvalue=contact['phone'])
        email = simpledialog.askstring("Email", "Update email:", initialvalue=contact['email'])
        address = simpledialog.askstring("Address", "Update address:", initialvalue=contact['address'])
        if name and phone:
            self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            save_contacts(self.contacts)
            self.refresh_listbox()
            messagebox.showinfo("Updated", "Contact updated successfully!")
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required.")

    def delete_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a contact to delete.")
            return
        contact = self.contacts.pop(selected[0])
        save_contacts(self.contacts)
        self.refresh_listbox()
        self.contact_details.config(text="")
        messagebox.showinfo("Deleted", f"Contact '{contact['name']}' deleted.")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone number:")
        if query:
            results = [c for c in self.contacts if query.lower() in c['name'].lower() or query in c['phone']]
            if results:
                self.listbox.delete(0, tk.END)
                for contact in results:
                    self.listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
            else:
                messagebox.showinfo("No Results", "No contacts found matching your search.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
