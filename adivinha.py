import random 

print("="*65)
n = int(input('Tente adivinhar no número na qual eu pensei! Dica: de 0 a 10 '))
lista =random.choice([0,1,2,3,4,5,6,7,8,9,10])


if n == lista:
    print('Você me ganhou! Parabéns!')
else:
    print('Você perdeu! HAHAHA Ganhei! Eu pensei no número {}'.format(lista))

print("="*65)