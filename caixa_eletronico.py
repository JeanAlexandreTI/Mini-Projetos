dinheiro = 0

valor = int(input('Informe o valor que deseja sacar:R$'))

while dinheiro != valor:
    c = valor // 50
    sc = valor - (50 * c)  #23
    v = sc // 20
    sv = sc - (20 * v)
    d = sv // 10
    sd = sv - (10 * d)
    u = sd // 1
    print(f'cédulas de R$50: {c} ')
    print(f'cédulas de R$20: {v}')
    print(f'cédulas de R$10: {d}')
    print(f'cédelas de R$1: {u}')
    break