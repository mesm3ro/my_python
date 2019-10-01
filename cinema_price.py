def cinema_tickets(film, time):
    
    if film  == "пятница":    
        if time == '12':
            return 250
        elif time == '16':
            return 350        
        elif time == '20':
            return 450       
        else:
            return 0
    
    elif film  == "чемпионы":
        if time == '10':
            return 250
        elif time == '13':
            return 350        
        elif time == '16':
            return 350
        else:
            return 0
            
    elif film == "пернатая банда":
        if time == '10':
            return 350
        elif time == '14':
            return 450        
        elif time == '18':
            return 450
        else:
            return 0 
   
    else:
        return 0

film = input('Выбрать фильм: ').lower()
day = input('Выбрать день (сегодня, завтра): ')
time = input('Выбрать время: ')
num_tick = int(input('Выбрать количество билетов: '))

if film and day and time and num_tick:
    
    print('Выбран фильм:', film, '| День:', day,
          ' | Время:', time, ' | Количество билетов:', num_tick) 
    
    skidka = 0
    if day == 'завтра':
        skidka += 5

    if num_tick >= 20:
        skidka += 20
        
    result = cinema_tickets(film, time) * num_tick *\
             (100 - skidka) // 100
    
    
    if result > 0:
        print('Результат:', result)
    else:
        print("Ошибка")

