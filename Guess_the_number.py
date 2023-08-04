import random as ran

a = ran.randint(1,50)
print (a)
for i in range(0,7):
    b = int(input("Попробуйте угадать число. Ваше число - "))
    if b == a:
        print("Верно")
        break
    else:
        if 6-i > 4:
            print(f"Попробуйте еще раз. У Вас осталось {6-i} попыток")
        elif 6-i >= 2:
            print(f"Попробуйте еще раз. У Вас осталось {6-i} попытки")
        elif 6-i == 1:
            print(f"Попробуйте еще раз. У Вас осталось {6-i} попытка")
        elif 6-i == 0:
            print("Вы не угадали число")