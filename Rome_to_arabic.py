#My_Number_Rome = input("Введите римское число: ")
def Rome_to_arabic(X_Number):
    Rome_Numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for k in Rome_Numbers.keys():
        print(X_Number.find(k))
    '''for k in Rome_Numbers.keys():
        if k in X_Number:
            Master_Number = k
    print (Master_Number)'''
Rome_to_arabic("XVI")