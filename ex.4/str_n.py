def happy(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s


string = input('Напишите строку: ')
number = int(input('Введите число: '))
print(happy(string, number))
