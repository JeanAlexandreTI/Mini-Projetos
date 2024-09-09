n1 = float(input('Me informe um número qualquer: '))
n2 = float(input('Me informe o segundo número: '))
n3 = float(input('Me informe o terceiro número: '))

if n1 >= n2 >= n3:
    print(f'A sequência em ordem decrescente é: {n1}, {n2} e {n3}.')
else:
    if n2 >= n1 >= n3:
        print(f'A sequência em ordem decrescente é: {n2}, {n1} e {n3}.')
    else:
        if n3 >= n2 >= n1:
            print(f'A sequência em ordem decrescente é: {n3}, {n2} e {n1}')
        else:
            if n1 >= n3 >= n2:
                print(f'A sequência em ordem decrescente é: {n1}, {n3} e {n2}')
            else:
                if n2 >= n3 >= n1:
                    print(f'A sequência em ordem decrescente é: {n2}, {n3} e {n1}')
                else:
                    if n3 >= n1 >= n2:
                        print(f'A sequência em ordem decrescente é: {n3}, {n1} e {n2}')
                   