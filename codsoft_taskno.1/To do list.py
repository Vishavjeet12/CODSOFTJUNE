import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 

def add():
    task = task_input.get()
    if not task:
        messagebox.showinfo("Error", "Empty task.")
    else:
        todo_list.append(task)
        cur.execute("INSERT INTO todo (task) VALUES (?)", (task,))
        update_list()
        task_input.delete(0, 'end')

def update_list():
    listbox.delete(0, 'end')
    for t in todo_list:
        listbox.insert('end', t)

def delete():
    try:
        selected = listbox.get(listbox.curselection())
        todo_list.remove(selected)
        update_list()
        cur.execute("DELETE FROM todo WHERE task = ?", (selected,))
    except:
       messagebox.showinfo("Error", "Nothing selected.")

def delete_all():
    if messagebox.askyesno("Confirm", "Delete everything?"):
        todo_list.clear()
        cur.execute("DELETE FROM todo")
        update_list()

def load_data():
    todo_list.clear()
    for row in cur.execute("SELECT task FROM todo"):
        todo_list.append(row[0])

def quit_app():
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List-Vishavjeet") 
    root.geometry("500x450")
    root.config(bg="#FAEBD7")
    root.resizable(False, False)

    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS todo (task TEXT)")

    todo_list = []

    left = tk.Frame(root, bg="#75f461")
    right = tk.Frame(root, bg="#75f461")
    left.pack(side="left", fill="both", expand=True)
    right.pack(side="right", fill="both", expand=True)

    ttk.Label(left, text="Enter task:", background="#75f461", font=("Arial", 10, "bold")).place(x=20, y=30)
    task_input = ttk.Entry(left, font=("Arial", 12), width=20)
    task_input.place(x=20, y=60)

    ttk.Button(left, text="Add", command=add).place(x=20, y=100)
    ttk.Button(left, text="Delete", command=delete).place(x=20, y=140)
    ttk.Button(left, text="Clear All", command=delete_all).place(x=20, y=180)
    ttk.Button(left, text="Exit", command=quit_app).place(x=20, y=220)

    listbox = tk.Listbox(right, width=25, height=15, bg="white", fg="black", selectbackground="green")
    listbox.place(x=10, y=20)

    load_data()
    update_list()

    root.mainloop()
    con.commit()
    cur.close()
    con.close()
