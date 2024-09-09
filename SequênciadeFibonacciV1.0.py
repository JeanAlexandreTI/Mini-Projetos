termos = int(input('Informe a quantidade de termos que a sequência Fibonacci deve ter: '))
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end = '')
cont = 3
while cont <= termos:

    t3 = t1 + t2
    print(f'{t3} - ', end = '')
    t1 = t2
    t2 = t3
    cont = cont + 1

    # sistema deu um pequeno erro!