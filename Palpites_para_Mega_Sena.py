from random import randint

value = []
sort = []

print('--' * 15)
print('JOGO DA MEGA SENA'.center(30))
print('--' * 15)

game = int(input('Digite a quantidade de jogos que deseja realizar: '))

print('==' * 15)

for c in range(game):

    while len(value) < 6:

        sort += [randint(1, 60)]
        value.append(sort[:])
        sort.clear()

    if len(value) == 6:
        print(f'Jogo {c + 1}°: {sorted(value)}')
        value.clear()
