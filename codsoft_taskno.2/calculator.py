import tkinter as tk

def add_to_input(value):
    current = user_input.get()
    user_input.set(current + str(value))

def clear_input():
    user_input.set("")

def evaluate_expression():
    try:
        result = str(eval(user_input.get()))
        user_input.set(result)
    except:
        user_input.set("Error") 


root = tk.Tk()
root.title("Simple Calculator-Vishavjeet")
root.geometry("400x450")
root.resizable(False, False)

user_input = tk.StringVar()
entry = tk.Entry(root, textvariable=user_input, font=('Arial', 20),
                 bd=10, insertwidth=2, width=14, borderwidth=4,
                 relief='ridge', justify='right', bg='white', fg='black')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (label, row, col) in buttons:
    if label == '=':
        tk.Button(root, text=label, width=10, height=2,command=evaluate_expression).grid(row=row, column=col)
    elif label == 'C':
        tk.Button(root, text=label, width=40, height=2,command=clear_input).grid(row=row, column=col, columnspan=4)
    else:
        tk.Button(root, text=label, width=10, height=2,command=lambda val=label: add_to_input(val)).grid(row=row, column=col)


root.mainloop()
