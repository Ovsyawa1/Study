import tkinter as tk

root = tk.Tk()

root.title("Расчет электрических цепей")
root.geometry("1280x720")

label = tk.Label(root, text = "Расчет цепи", font = ('Arial', 18))
label.pack()

textbox = tk.Text(root, height = 3, font = ('Arial', 14))
textbox.pack()

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

button_1 = tk.Button(button_frame, text = "1", font = ('Arial', 18))
button_1.grid(row=0, column=0)

myentry = tk.Entry(root)
myentry.pack()

root.mainloop() 
"""button_right = tk.Button(root, text = "Постоянный ток")
button_right.pack(side="right", padx=10, pady=10)

button_left = tk.Button(root, text = "Переменный ток")
button_left.pack(side="left", padx=10, pady=10)"""