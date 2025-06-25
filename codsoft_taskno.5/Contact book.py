import tkinter as tk
from tkinter import messagebox

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book-Vishavjeet")
        self.root.geometry("600x550")
        self.root.config(bg="#e6f2ff")  
        self.contacts = []
        self.setup_variables()
        self.create_widgets()
        self.add_sample_contacts()

    def setup_variables(self):
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.search_var = tk.StringVar()

    def create_widgets(self):
        fields = ["Name", "Phone", "Email", "Address"]
        for i, label in enumerate(fields):
            tk.Label(self.root, text=label + ":", font=('Arial', 10, 'bold'), bg="#e6f2ff").grid(row=i, column=0, padx=10, pady=5, sticky="e")
        
        tk.Entry(self.root, textvariable=self.name_var, width=40).grid(row=0, column=1)
        tk.Entry(self.root, textvariable=self.phone_var, width=40).grid(row=1, column=1)
        tk.Entry(self.root, textvariable=self.email_var, width=40).grid(row=2, column=1)
        tk.Entry(self.root, textvariable=self.address_var, width=40).grid(row=3, column=1)

        # Action buttons
        tk.Button(self.root, text="Add Contact", command=self.add_contact, bg="#007acc", fg="white").grid(row=4, column=0, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact, bg="#ffa31a", fg="white").grid(row=4, column=1)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact, bg="#e60000", fg="white").grid(row=5, column=0)
        tk.Button(self.root, text="Clear Fields", command=self.clear_fields, bg="#5c5c8a", fg="white").grid(row=5, column=1)

        tk.Label(self.root, text="Search:", font=('Arial', 10, 'bold'), bg="#e6f2ff").grid(row=6, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.search_var, width=40).grid(row=6, column=1)
        tk.Button(self.root, text="Search", command=self.search_contact, bg="#339933", fg="white").grid(row=7, column=1, pady=5)

        list_frame = tk.Frame(self.root, bg="#cce0ff", bd=2, relief=tk.RIDGE)
        list_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=15, sticky="nsew")

        self.contact_listbox = tk.Listbox(
            list_frame, width=60, height=10, font=('Courier New', 10),
            bg="#ffffe6", fg="#000066", selectbackground="#80bfff", selectforeground="black"
        )
        self.contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.contact_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.contact_listbox.yview)
        self.contact_listbox.bind('<<ListboxSelect>>', self.on_contact_select)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()

        if not name or not phone:
            messagebox.showwarning("Missing Info", "Name and phone number are required.")
            return
        new_contact = {
            "name": name,
            "phone": phone,
            "email": self.email_var.get(),
            "address": self.address_var.get()
        }

        self.contacts.append(new_contact)
        messagebox.showinfo("Added", f"Contact '{name}' has been added.")
        self.clear_fields()
        self.refresh_contact_list()

    def update_contact(self):
        selection = self.contact_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a contact to update.")
            return
        index = int(self.contact_listbox.get(selection).split('.')[0]) - 1
        self.contacts[index] = {
            "name": self.name_var.get(),
            "phone": self.phone_var.get(),
            "email": self.email_var.get(),
            "address": self.address_var.get()
        }

        messagebox.showinfo("Updated", "Contact is updated successfully.")
        self.clear_fields()
        self.refresh_contact_list()

    def delete_contact(self):
        selection = self.contact_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a contact to delete.")
            return
        index = int(self.contact_listbox.get(selection).split('.')[0]) - 1
        deleted_contact = self.contacts.pop(index)

        messagebox.showinfo("Deleted", f"Deleted contact '{deleted_contact['name']}'.")
        self.refresh_contact_list()

    def search_contact(self):
        query = self.search_var.get().lower()
        self.contact_listbox.delete(0, tk.END)
        for i, contact in enumerate(self.contacts):
            if query in contact['name'].lower() or query in contact['phone']:
                self.contact_listbox.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")

    def refresh_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for i, contact in enumerate(self.contacts):
            self.contact_listbox.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")

    def on_contact_select(self, event):
        if not self.contact_listbox.curselection():
            return
        index = int(self.contact_listbox.get(self.contact_listbox.curselection()).split('.')[0]) - 1
        contact = self.contacts[index]

        self.name_var.set(contact['name'])
        self.phone_var.set(contact['phone'])
        self.email_var.set(contact['email'])
        self.address_var.set(contact['address'])

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

    def add_sample_contacts(self):
        self.contacts.append({"name": "Raju Sharma", "phone": "9462729947", "email": "raju@gmail.com", "address": "ward no.4,delhi"})
        self.refresh_contact_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
