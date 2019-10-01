from math import sin
print("Введите x: ")
number = input(" ")

if number.isnumeric():
    x = float(number)
    
    if 0.2 <= x <= 0.9 :
        print(sin(x))
        
    else:
        print(1)
else:
    print("Ошибка")
