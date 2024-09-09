num = float(input('Me informe um número: '))
num2 = float(input('Me informe um segundo número: '))
num3 = float(input('Me informe o último valor: '))

if num > num2 > num3:
    print(f'{num} é maior que {num2}, que é maior que {num3}')
elif num2 > num > num3:
    print(f'{num2} é maior que {num}, que é maior que {num3}')
elif num > num3 > num2:
    print(f'{num} é maior que {num3}, que é maior que {num2}')
elif num2 > num3 > num:
    print(f'{num2} é maior que {num3}, que é maior que {num}') 
elif num3 > num > num2:
    print(f'{num3} é maior que {num}, que é maior que {num2}')
elif num3 > num2 > num3:
    print(f'{num3} é maior que {num2}, que é maior que {num}') 
else:
    print('Os valores são iguais.')