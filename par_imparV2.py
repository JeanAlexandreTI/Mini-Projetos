from random import choice

pc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
v = 0

while True:
    escolha = str(input('Escolha! Par ou ímpar? ')).strip().upper()
    n = int(input('Jogue o seu número! '))
    ia = choice(pc)
    s = n + ia

    print('==='*25)
    if escolha == 'PAR' and s % 2 == 0:
        print('Ah não! Você me venceu desta vez! Deu par! ')
        print(f'Você jogou {n} e o computador jogou {ia}, que deu {s}')
        v = v + 1
        
    elif escolha == 'ÍMPAR' and s % 2 == 1:
        print('Ah não! Você me venceu desta vez! Deu ímpar!')
        print(f'Você jogou {n} e o computador jogou {ia}, que deu {s}')
        v = v + 1

    elif escolha == 'PAR' and s % 2 == 1:
        print(f'Você perdeu! Otário! O resultado foi {s} que é um número ímpar!')
        print(f'Você jogou {n} e o computador jogou {ia}.')
        if v == 0:
            print('Você nem sequer teve uma sequência de vítorias! PATÉTICO!')
        elif v > 0:
            print(f'Sua sequência de {v} vítorias seguidas acabou! HAHAHA!')
        break

    elif escolha == 'ÍMPAR' and s % s == 0:
        print(f'Você perdeu! Otário! O resultado foi {s} que é um número par!')
        print(f'Você jogou {n} e o computador jogou {ia}.')
        if v == 0:
            print('Você nem sequer teve uma sequência de vítorias! PATÉTICO!')
        elif v > 0:
            print(f'Sua sequência de {v} vítorias seguidas acabou! HAHAHA!')
        break