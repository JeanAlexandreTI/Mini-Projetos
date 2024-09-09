order_list = []
counter = 0

while True:

    counter += 1
    query = input(f'Informe o {int(counter)}° número: ')
    
    if query.isnumeric() == True:
        order_list += [query]
    
    while query.isnumeric() == False:
        print('Informe um número!')
        query = input(f'Informe o {int(counter)}° número: ') 
        order_list += [query]


    run = str(input('Deseja continuar? [S / N] ')).upper().strip()

    if  run != 'N' and run != 'S':
        while True:
            print('Não entendi o que foi informado, informe novamente. ')
            run = str(input('Deseja continuar? [ S / N ] ')).upper().strip()

            if run == 'N':
                break

            elif run == 'S':
                break


    if run == 'N':
        print(f'Foi digitado {len ( order_list ) } números.')
        print(f'A lista em ordem ficou da seguinte forma: {sorted(order_list, reverse = True)}')

        if 5 in order_list:
            print('O número 5 está na lista.')

        elif 5 not in order_list:
            print('O valor 5 não está na lista.')
        break
