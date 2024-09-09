'''CRIAR UMA ÚNICA LISTA QUE O USÚARIO INSERIU 7 VALORES
SEPARAR VALORES PARES DE ÍMPARES E MOSTRAR ELES NA ORDEM CRESCENTE'''

order = []
value = []
odd = []
pair = []

for _ in range(1, 8):

    while True:

        try:
                
            number = int(input(f'Insira o {_}° valor númerico: '))

            value.append(number)
            order.append(value[:])

            value.clear()
        
            if number >= 0 and number <= 100:
                break

        except ValueError:

            print('Valor invalido... Digite novamente.')


for v in order:

    if v[0] % 2 == 0:

        pair += v

    else:

        odd += v


print (f'Valores Pares: {sorted(pair, reverse = True)}')
print (f'Valores Ímpares: {sorted(odd, reverse = True)}')
print(f'Todos os valores digitados: {sorted(order, reverse = True)}')
