from random import choice, randrange

wlist = ['самовар', 'весна', 'лето']
wrandom = choice(wlist)
randomchar = randrange(0, len(wrandom))
print(f'{wrandom[:randomchar]}?{wrandom[randomchar+1:]}')
gchar = input('Буква: ')
if gchar == wrandom[randomchar]:
    print(f'Победа! Слово - {wrandom}')
else:
    print(f'Проигрыш Слово - {wrandom}')
