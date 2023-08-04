import tkinter as tk

root=tk.Tk()
root.geometry("1280x720")

field = tk.Entry(root, width=100)
field.grid(row=0, column=0)

def Button_Click():
    Label1 = tk.Label(root, text = ("Hello, " + field.get()))
    Label1.grid(row=2,column=0)

Button1 = tk.Button(root, text="Enter your whatever", command=Button_Click)
Button1.grid(row=1,column=0)

root.mainloop()