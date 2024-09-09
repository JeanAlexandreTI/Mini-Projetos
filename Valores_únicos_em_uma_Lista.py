num = []
while True:
    addnumber = int(input('Informe os números que deseja adicionar a lista: '))
    if addnumber in num:
        num.remove(addnumber)

    if addnumber is not num:
        num = num + [addnumber]
        

    stop = str(input('Deja adicionar outro número? [ S / N ] ')).upper().strip()
    if stop == 'N':
        print('Estamos encerrando o sistema.')
        print(f'A sua listagem ficou da seguinte forma: {sorted(num)}')
        break
    