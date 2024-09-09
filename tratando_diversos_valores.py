q = 0
s = 0
while True:
    n = int(input('Me informe um número. CASO NÃO QUEIRA MAIS INFORMAR NÚMEROS DIGITE [999]: '))
    q = q + 1
    s = s + n
    if n == 999:
        print(f'Você digitou {q-1} números.')
        print(f'A soma entre os números digitados é {s-999}')
        break