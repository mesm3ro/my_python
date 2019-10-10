def calculator(firstnum, secondnum, operator):
    if operator == '+':
        return firstnum + secondnum
    elif operator == '-':
        return firstnum - secondnum
    elif operator == '*':
        return firstnum * secondnum
    elif operator == '/':
        return firstnum / secondnum
    else:
        return 'Оператор неверен!'


try:
    firstnumb = float(input('Введите первое число: '))
    secondnumb = float(input('Введите второе число: '))
    secoperator = input('Введите оператора: ')
    print(calc(firstnumb, secondnumb, secoperator))
except ZeroDivisionError as err:
    print('Деление на ноль!')
except ValueError:
    print('Число не введено')
except Exception as err:
    print(err)
