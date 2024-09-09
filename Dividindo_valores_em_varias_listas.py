numberlist = []
listpar = []
listodd = []
counter = 0

while True:
    counter += 1
    query = input(f'Informe o {counter}° valor desejado: ')
    
    while query.isnumeric() == False:
        print('Valor invalido.')
        query = input(f'Informe o {counter}° valor novamente: ')
    

    keep = input('Deseja continuar? [S/N] ').upper().strip()
    numberlist += [query]

    while keep.isalpha() == False:
        print('Valor invalido.')
        keep = input('Informe novamente se deseja continuar: [S/N] ').upper().strip()

    if int(query) % 2 == 0:
        listpar += [query]
    else:
        listodd += [query]

    if keep == 'N':
        print(f'A lista ficou da seguinte forma: {numberlist}')
        print(f'Os valores pares são: {listpar}')
        print(f'Os valores ímpares são: {listodd}')
        break
