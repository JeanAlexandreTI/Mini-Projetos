termo = int(input('Informe o número que você deseja que comece a Progressão Aritmética: '))
razão = int(input('Informe a númeração referente a razão: '))
final = termo + (10 - 1) * razão
continuar = 0

while True:
    while termo < final:
        termo = termo + razão
        print(termo)
    continuar = int(input('Deseja continuar a PA com quantos números a mais? '))
    if continuar > 0:
        final = (continuar * razão) + final
        while termo < final:
            termo = termo + razão
            print(termo)
            
    elif continuar == 0:
        print('Caso precise fatorar algum número, só me procurar!')
        break