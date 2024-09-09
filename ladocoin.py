import random

coin = random.choice(['cara','coroa'])
escolha = str(input('Vou jogar a moeda! Qual lado você acha que caí? Cara ou coroa? ')).strip().lower()

if escolha == coin:
    print('Você acertou, o lado que caiu foi {}'.format(coin))
else:
    print('Você errou! O lado que caiu foi {}'.format(coin))
