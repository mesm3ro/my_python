print('''Фильм «Пятница»,
  сеансы: 12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб.
Фильм «Чемпионы»,
  сеансы: 10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб.
Фильм «Пернатая банда»,
  сеансы: 10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб.
от 20 человек - скидка 20%,
заказ за день до сеанса - скидка 5%''')

cinema = {'пятница': {'s_time': {'12': 250, '16': 350, '20': 450}},
          'чемпионы': {'s_time': {'10': 250, '13': 350, '16': 350}},
          'пернатая банда': {'s_time': {'10': 350, '13': 450, '16': 450}}}

film = input('Выбрать фильм: ').lower()
day = input('Выбрать день (сегодня, завтра): ')
s_time = input('Выбрать время: ')
numbr_of_tickets = int(input('Выбрать количество билетов: '))

try:
    print('Выбран фильм:', film,
          ', День:', day,
          ',  Время:', s_time,
          ',  Количество билетов:', numbr_of_tickets)

    discount = 0
    if day == 'завтра':
        discount += 5
    if numbr_of_tickets >= 20:
        discount += 20

    print('Цена билета', cinema[film]['s_time'][s_time])
    
    result = cinema[film]['s_time'][s_time] * numbr_of_tickets *\
        (100 - discount) // 100

    if result > 0:
        print('Результат:', result, 'руб.')
    else:
        print("Ошибка ввода")

except:
    print("Ошибка ввода")
