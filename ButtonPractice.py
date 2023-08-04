import tkinter as tk
import webbrowser as wb

def link():
    wb.open('https://www.youtube.com/')

def showtext1():
    Labeltext=tk.Label(text="FUCK YOU!", font=('Comic Sans',14))
    Labeltext.grid(row=4,column=2)
    Image1=tk.Image(name="resistor")
    Image1.grid(row=5, column=2)
root = tk.Tk()
root.geometry("1280x720")
root.title("Grid Practice")

Label1=tk.Label(text="Hello World!", font=('Times New Roman',18))
Label2=tk.Label(text="Hello World!", font=('Times New Roman',18))
Button1=tk.Button(text = "Youtube", font=('Times New Roman', 20), bg="black", fg="white", command= link, padx=50, pady=10)
Button2=tk.Button(text = "Click!", command=showtext1)

Label1.grid(row=0,column=0)
Label2.grid(row=1,column=5)
Button1.grid(row=2,column=2)
Button2.grid(row=3,column=2)
root.mainloop()