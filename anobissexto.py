ano = int(input('Me informe um ano: '))

'''PARA UM ANO SER BISSEXTO
É NECESSÁRIO QUE O MESMO SEJA
DIVISÍL POR 4, 100 E POR 400'''

if ano % 4 and ano % 100 !=0 or ano % 400 == 0:
    print(f'Que legal! O ano {ano} é Bissexto!')
else:
    print('Que sem graça, é um ano comum! :c')
