def my_max(first, second):
    if first >= second:
        return first
    else:
        return second

num = input('Первое число: ')
num2 = input('Второе число: ')

if num and num2:
    print('Максимальное число',my_max(int(num), int(num2)))

else:
    print('Нет значений!')
