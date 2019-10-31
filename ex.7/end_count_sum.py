sum = 0
while True:
    inpt = input(" ")
    if inpt == "Стоп":
        print(sum)
        break
    try:
        sum += int(inpt)
    except:
        print("Повторите ввод")
        continue
