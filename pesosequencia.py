lista = []

for c in range(1, 5+1):
    peso = float(input(f'Quantos Kg a {c}° pessoa tem? '))
    lista = lista + [peso]   

print(f'A maior pessagem é de {max(lista)}Kg')
print (f'A menor pessagem é de {min(lista)}Kg')