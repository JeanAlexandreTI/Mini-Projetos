n = (int(input('Informe o 1° número: ')),
     int(input('Informe o 2° número: ')),
     int(input('Informe o 3° número: ')),
     int(input('Informe o 4° número: ')))
list_par = []

print(f'Os valores digitados foram: {n}')

if 9 in n: 
    print(f'O 9 repete-se apenas {n.count(9)} vez(es)')
elif 9 != n:
    print(f'Não contém 9.')


if 3 in n:
    print(f'O indíce do primeiro 3, é {n.index(3,0)}')
elif 3 != n:
    print(f'Não contém 3.')


if n[0] % 2 == 0:
    list_par += [n[0]]

if n[1] % 2 == 0:
    list_par += [n[1]]

if n[2] % 2 == 0:
    list_par += [n[2]]

if n[3] % 2 == 0:
    list_par += [n[3]]
  
else:
    list_par +='Não contém números pares.'

print(f'Os números pares são: {list_par}')