from random import choice 
print (f'{'JOKENPÔ':=^40}')

comp = choice([1,2,3]) 
jogada = int(input('''Escolha um item.
[1] PEDRA
[2] TESOURA
[3] PAPEL
OPÇÃO: '''))

if jogada == 1 and comp == 2:
    print('Você ganhou! O comutador jogou TESOURA.')
elif jogada == 1 and comp ==3:
    print('Você perdeu! O computador jogou PAPEL.')
elif jogada ==1 and comp == 1:
    print('Ocorreu um EMPATE! O computador também jogou PEDRA.')
elif jogada == 2 and comp == 1:
    print ('Você perdeu! O computador jogou PEDRA.')
elif jogada == 2 and comp == 2:
    print('Ocorreu um EMPATE! O computador também jogou TESOURA.')
elif jogada == 2 and comp == 3:
    print('Você ganhou! O computador jogou PAPEL.')
elif jogada == 3 and comp == 1:
    print('Você ganhou! O computador jogou PEDRA.')
elif jogada == 3 and comp == 2:
    print('Você perdeu! O computador jogou TESOURA.')
elif jogada == 3 and comp == 3:
    print('Ocorreu um EMPATE! O computador jogou PAPEL.') 
else:
    print('Opção invalida.')
    