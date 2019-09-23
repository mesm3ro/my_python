def get_parity(num):
    if (num % 2) == 0:
        print('Число четное')
    else:
        print('Число нечетное')

num = input('Число: ')

if num:
    get_parity(int(num))

else:
    print('Нет значений!')
