sum = 0
x = input("Число = ")
try:
    for i in range(len(x)):
        if int(x[i]) % 2 != 0:
            sum += int(x[i])**2
    print(sum)
except:
    print("Ошибка")
