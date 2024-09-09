from random import choice

computador = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tentativa = 0
print('-=-'*25)
print('JOGO DA ADIVINHAÇÃO'.center(70))
print('-=-'*25)
print('Será que você consegue adivinhar o número que estou pensando? Dica: entre 0-10.')

jogador = int(input('Faça sua jogada! Em qual número estou pensando? '))

while jogador > computador :
        jogador = int(input('Menor...Jogue novamente: '))
        tentativa = tentativa + 1 
else:
    while jogador < computador:
          jogador = int(input('Maior...Jogue novamente: '))
          tentativa = tentativa + 1
    else:
          print(f'Acertou! Você precisou tentar {tentativa}x')