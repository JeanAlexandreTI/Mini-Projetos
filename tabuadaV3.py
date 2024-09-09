n = 0
valor = int(input('Quer saber qual tabuada hoje? Digite o número: '))
while n <= 9:
    
    if valor < 0:
        print('Não aceitamos valores negativos.')
        break
    
    n = n +1
    print(f'{valor} * {n:2} = {n * valor}')