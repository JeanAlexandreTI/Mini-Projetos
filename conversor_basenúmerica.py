num = int(input('Me informe um número qualquer: '))
base = int(input('''Escolha a base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal
Opção: '''))

if base == 1:
    print(f'O número {num} em binário é {bin(num)[2:]}')
elif base == 2:
    print(f'O número {num} em octal é {oct(num)[2:]}')
elif base == 3:
    print(f'O número {num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Conversão de base inexistente no sistema.')