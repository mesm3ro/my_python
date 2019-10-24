import random
attnum = 3
answer = random.randint(1,10)
print('Компьютер загадал число.\nУ вас есть', attnum, 'попытки. Удачи!')

while True:
    att = input('Попробуйте угадать: ')

    if att == 'Выход':
        break 

    try:
        att = int(att)
    except:
        continue

    if att == answer:
        print('Победа!')
        break
    else:
        if att > answer:
            print('Попробуйте число меньше!')
        else:
            print('Попробуйте число больше!')

    attnum -= 1
    if attnum == 0:
        print('Game Over!\nЧисло:',answer)
        break
