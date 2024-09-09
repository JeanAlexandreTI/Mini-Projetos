from datetime import date
nascimento = int(input('Me informe o ano na qual você nasceu para podermos definir a sua categoria: '))
atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print(f'Com {idade} anos você é categorizado como MIRIM.')
elif idade <= 14:
    print(f'Com {idade} anos você é categorizado como INFANTIL.') 
elif idade <= 19:
    print (f'Com {idade} anos você é categorizado como JUNIOR.')
elif idade <= 25:
    print(f'Com {idade} anos você é categorizado como SENIOR')
elif idade >= 26:
    print(f'Com {idade} anos você é categorizado como MASTER.')
else:
    print('Invalido')
