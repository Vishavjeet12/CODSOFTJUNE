import tkinter as tk
from tkinter import ttk
import string
import random

def generate_password(min_len, add_numbers=True, add_specials=True):
    s1 = string.ascii_letters
    s2= string.digits
    s3 = string.punctuation
    chars =s1

    if add_numbers:
        chars += s2
    if add_specials:
        chars += s3
    pwd = ""
    got_number = False
    got_special = False
    valid = False

    while not valid or len(pwd) < min_len:
        ch = random.choice(chars)
        pwd += ch

        if ch in s2:
            got_number = True
        elif ch in s3:
            got_special = True

        valid = True
        if add_numbers:
            valid = got_number
        if add_specials:
            valid = valid and got_special

    return pwd

def handle_generate():
    try:
        val = int(length_field.get())
        nums = num_opt.get()
        specials = sym_opt.get()
        result.set(generate_password(val, nums, specials))
    except:
        result.set("Length must be a number!")

app = tk.Tk()
app.title("Password generator-Vishavjeet")
app.geometry("430x290")
app.configure(bg="#f2f2f2")
app.resizable(0, 0)

ttk.Label(app, text="Simple Password Generator", font=("Arial", 15)).pack(pady=12)
ttk.Label(app, text="Password Length:").pack()
length_field = ttk.Entry(app, width=12)
length_field.pack(pady=4)

num_opt = tk.BooleanVar(value=True)
sym_opt = tk.BooleanVar(value=True)

ttk.Checkbutton(app, text="Add numbers (0-9)", variable=num_opt).pack()
ttk.Checkbutton(app, text="Add symbols (@#$...)", variable=sym_opt).pack()

ttk.Button(app, text="Generate", command=handle_generate).pack(pady=14)

result = tk.StringVar()
tk.Entry(app, textvariable=result, width=36, font=("Courier", 12),
         bg="#ffdddd", fg="#800000", justify="center", state="readonly").pack(pady=10)

app.mainloop()
