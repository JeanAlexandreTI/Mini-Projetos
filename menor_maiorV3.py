qtdeN = 0
s = 0
mm = []


while True:
    n = int(input('Digite um número: '))
    c = str(input('''Quer continuar a informar números?
[ S ] Sim
[ N ] Não
Opção: ''')).strip().upper()
    

    qtdeN = qtdeN + 1
    s = s + n
    mm = mm + [n]


    if c == 'N':
        print(f'A média entre os números é {s/qtdeN:.1f}')
        print(f'''O menor número informado foi {min(mm)} 
O maior número informado foi {max(mm)}''')
        break