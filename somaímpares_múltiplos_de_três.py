acumulador = 0
contador = 0
for c in range( 1, 500, 2):
    if c % 3 == 0:
        acumulador = acumulador + c
        contador = contador + 1
    print(f'A soma de todos os {contador} valores é igual a: {acumulador}')
