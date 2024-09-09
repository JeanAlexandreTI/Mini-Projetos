print('-=-'*25)
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
print('-=-'*25)
menu = int(input('''O que deseja realizar com os valores informados?
[ 1 ] Somar.
[ 2 ] Multiplicar.
[ 3 ] Maior número.
[ 4 ] Novos números.
[ 5 ] Sair do programa.
Opção: '''))
print('-=-'*25)
while menu < 0 or menu > 5:
    print('A opção informada não consta nos nossos sistemas.')
    print('Por favor, informe as opções novamente.')
    menu = int(input('''O que deseja realizar com os valores informados?
[ 1 ] Somar.
[ 2 ] Multiplicar.
[ 3 ] Maior número.
[ 4 ] Novos números.
[ 5 ] Sair do programa.
Opção: '''))

if menu == 1:
    print(f'Somando os valores {v1} e {v2}, temos: {v1 + v2}')
    print ('-=-'*25)
elif menu == 2:
    print(f'Multiplicando o valor {v1} por {v2} temos:{v1 * v2}')
    print('-=-'*25)
elif menu == 3:
    if v1 > v2:
        print(f'O valor {v1} é o maior.')
        print('-=-'*25)
    elif v1 == v2:
        print('Os valores são iguais.')
        print('-=-'*25)
    else:
        print(f'O valor {v2} é o maior.')
        print('-=-'*25)
elif menu == 5:
    print('Programa encerrado.')
while menu == 4:
    print('-=-'*25)
    print('Ok informe outros valores.')
    v1 = float(input('Digite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))
    print('-=-'*25)
    menu = int(input('''O que deseja realizar com os novos valores informados?
[ 1 ] Somar.
[ 2 ] Multiplicar.
[ 3 ] Maior número.
[ 4 ] Novos números.
[ 5 ] Sair do programa.
Opção: '''))
    print('-=-'*25)
    while menu < 0 or menu > 5:
        print('A opção informada não consta nos nossos sistemas.')
        print('Por favor, informe as opções novamente.')
        menu = int(input('''O que deseja realizar com os valores informados?
[ 1 ] Somar.
[ 2 ] Multiplicar.
[ 3 ] Maior número.
[ 4 ] Novos números.
[ 5 ] Sair do programa.
Opção: '''))
    if menu == 1:
        print(f' A somando os valores {v1} e {v2}, temos: {v1 + v2}')
    elif menu == 2:
        print(f'Multiplicando o valor {v1} por {v2} temos:{v1*v2}')
    elif menu == 3:
        if v1 > v2:
            print(f'O valor {v1} é o maior.')
        elif v1 == v2:
            print('Os valores são iguais.')
        else:
            print(f'O valor {v2} é o maior.')
    elif menu == 5:
        print('Programa encerrado.')
