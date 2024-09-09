value = []
list_value = []
cont = 0

value.append(int (input ('Informe o valor para a posição [0][0]: ')))
value.append(int (input('Informe o valor para a posição [0][1]: ')))
value.append(int (input('Informe o valor para a posição [0][2]: ')))


list_value.append(value[:])
value.clear()


value.append(int ( input('Informe o valor para a posição [1][0]: ')))
value.append(int (input('Informe o valor para a posição [1][1]: ')))
value.append(int (input('Informe o valor para a posição [1][2]: ')))


list_value.append(value[:])
value.clear()


value.append(int ( input('Informe o valor para a posição [2][0]: ')))
value.append(int (input('Informe o valor para a posição [2][1]: ')))
value.append(int (input('Informe o valor para a posição [2][2]: ')))


list_value.append(value[:])
value.clear()


print('==' * 15)
for v in list_value:

    print(v)

print()

for v in list_value:

    if v[0] % 2 == 0:
        cont += v[0]

    if v[1] % 2 == 0:
        cont += v[1]

    if v[2] % 2 == 0:
        cont += v[2]

print(f'Soma dos valores pares: {cont}')
print(f'Soma dos valores na terceira coluna: {list_value[0][2] + list_value[1][2] + list_value[2][2]}')
print(f'Maior valor da 2° linha: {max(list_value[1])}')
print('==' * 15)



