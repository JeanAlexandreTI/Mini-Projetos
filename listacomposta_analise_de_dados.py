
data = []
information = []
count = 0
smaller = bigger = 0


while True:

    count += 1
    data.append(str(input('Informe o seu nome: ')))
    data.append(float(input('Informe o seu peso: ')))


    if len(data) == 0:

        bigger = smaller = data[1]

    else:

        if data[1] > bigger:
            bigger = data[1]

        if data[1] < smaller:
            smaller = data[1] 


    information.append(data[:])
    data.clear()


    cont = str(input('Deseja continuar?[S/N] ')).strip().upper()

    if cont == 'N':
        break


print(f'Total de pessoas cadastradas: {count}.')
print(f'O maior peso foi de {bigger}Kg.')
print(f'O menor peso foi de {smaller}Kg.')