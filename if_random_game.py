import random
answer = int(input("Попробуйте отгадать число от 1 до 4: "))
number = random.randint(1, 4)
print(number)
if answer > number:
    print("Ваш ответ больше введенного числа")
elif answer < number:
    print("Ваш ответ меньше введенного числа")
else:
    print("Победа")
