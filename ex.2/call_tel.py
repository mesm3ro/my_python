code = input('Код города: ')
time = input('Длительность переговоров: ')

if code and time:
    
    if code == '343':
        print('Стоимость', int(time) * 15)
    
    elif code == '381':
        print('Стоимость', int(time) * 18)
    
    elif code == '473':
        print('Стоимость', int(time) * 13)
    
    elif code == '485':
        print('Стоимость', int(time) * 11)
        
    else:
        print('Код отсутствует')
    
else:
    print('Нет значений')
