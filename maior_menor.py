num = int(input('Me informe um número: '))
num2 = int(input('Me informe outro número: '))
num3 = int(input('Me informe o último número: '))
'''VERIFICAR QUEM É O MAIOR'''
if num > num2 and num3:
    print(f'O maior valor é o {num}')
else:
    if num2 > num3:
        print(f'O maior valor é o {num2}')
    else:
        if num3 > num:
            print(f'O maior valor é o {num3}')
        else:
            print('Não tem maior número, pois todos tem o mesmo valor!')

'''VERIFICAR QUE É O MENOR'''
if num < num2 and num3:
    print(f'O menor valor é o {num}')
else:
    if num2 < num3:
        print(f'O menor valor é o {num2}')
    else:
        if num3 < num:
            print(f'O menor valor é o {num3}')
        else:
            print('Não tem menor número, pois todos tem o mesmo valor!')    
