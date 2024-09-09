n = int(input('Informe um número: '))
cont = 0

for c in range(1, n+1):
    if n % c == 0:
        cont = cont + 1 
if cont == 2:
    print('O número é primo!')
else:
    print('O número NÃO é primo!')