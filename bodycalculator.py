import tkinter as tk
import tkinter.messagebox as tkm

def calculate_bmi():
    kg = int(weight_write.get())
    m = int(height_write.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    if bmi < 18.5:
        tkm.showinfo(title = "Показатель", message = "Показатель " + str(bmi) + " соответсвует недостатку")
    elif (bmi > 18.5) and (bmi < 24.9):
         tkm.showinfo(title = "Показатель", message = "Показатель " + str(bmi) + " соответсвует норме")
    elif (bmi > 24.9) and (bmi < 29.9):
         tkm.showinfo(title = "Показатель", message = "Показатель " + str(bmi) + " соответсвует превышению")
    else:
         tkm.showinfo(title = "Показатель", message = "Показатель " + str(bmi) + " соответсвует ожирение")


root = tk.Tk()
root.title("Калькулятор")
root.geometry('500x500')

frame = tk.Frame(root, padx = 10, pady = 10)
frame.pack(expand=True)

height_lb = tk.Label (frame, text = "Введите свой рост в см ")
height_lb.grid(row=3, column=1)

weight_lb = tk.Label(frame, text = "Введите свой весь в кг")
weight_lb.grid(row=4, column=1)

height_write = tk.Entry(frame)
height_write.grid(row=3, column=2)

weight_write = tk.Entry(frame)
weight_write.grid(row=4, column=2)

cal_button = tk.Button(frame, text = "Рассичтать ИМТ", command = calculate_bmi)
cal_button.grid(row=5, column=2)

root.mainloop()