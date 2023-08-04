import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

field = tk.Entry(root, width=40, borderwidth=5)
field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def click_button(user_number):
    #field.delete(0, tk.END)
    current = field.get()
    field.delete(0, tk.END)
    field.insert(0, str(current) + str(user_number))

def plus_numb():
    first_number = field.get()
    global f_num
    global action
    action = "addition"
    f_num = int(first_number)
    field.delete(0, tk.END)

def subtract_func():
    first_number = field.get()
    global f_num
    global action
    action = "subtraction"
    f_num = int(first_number)
    field.delete(0, tk.END)

def multiply_func():
    first_number = field.get()
    global f_num
    global action
    action = "multiplication"
    f_num = int(first_number)
    field.delete(0, tk.END)

def divide_func():
    first_number = field.get()
    global f_num
    global action
    action = "division"
    f_num = int(first_number)
    field.delete(0, tk.END)

'''def equal_func():
    pass'''

def equal_func():
    second_number = field.get()

    if action == "addition":
        field.delete(0, tk.END)
        field.insert(0, f_num + int(second_number))
    elif action == "subtraction":
        field.delete(0, tk.END)
        field.insert(0, f_num - int(second_number))
    elif action == "multiplication":
        field.delete(0, tk.END)
        field.insert(0, f_num * int(second_number))
    elif action == "division":
        field.delete(0, tk.END)
        field.insert(0, f_num / int(second_number))

def clear_func():
    field.delete(0, tk.END)

#buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: click_button(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: click_button(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: click_button(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: click_button(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: click_button(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: click_button(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: click_button(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: click_button(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: click_button(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: click_button(0))

button_add = tk.Button(root, text = "+", padx=39, pady=20, command = plus_numb)
button_subract = tk.Button(root, text = "-", padx=39, pady=20, command = subtract_func)
button_multiply = tk.Button(root, text = "*", padx=39, pady=20, command = multiply_func)
button_divide = tk.Button(root, text="/", padx=39, pady=20, command = divide_func)
button_equal = tk.Button(root, text = "=", padx=80, pady=20, command = equal_func)
button_clear = tk.Button(root, text = "Clear", padx=80, pady=20, command = clear_func)

#вывод на экран
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row = 4, column = 1, columnspan = 2)
button_add.grid(row = 5, column = 0)
button_subract.grid(row = 5, column = 1)
button_multiply.grid(row = 5, column = 2)
button_divide.grid(row = 6,column = 0)
button_equal.grid(row = 6, column = 1,columnspan = 2)

root.mainloop()