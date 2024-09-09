termo = int(input('Informe a numeração a qual deseja que a progressão aritmética seja iniciada: '))
razão = int(input('Informe a numeração respectiva a razão: '))
final = termo + (10 - 1) * razão

while termo < final:
    termo = termo + razão
    print(termo)