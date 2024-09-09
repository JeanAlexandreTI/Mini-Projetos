import random

a1 = input('Me informe o nome de um aluno: ')
a2 = input('Me informe o nome de um aluno: ')
a3 = input('Me informe o nome de um aluno: ')
a4 = input('Me informe o nome de um aluno: ')

ordem1 = a1, a2, a3, a4
ordem2 = a4, a3, a2, a1
ordem3 = a1, a3, a2, a4
ordem4 = a4, a2, a3, a1

lista = [ordem1, ordem2, ordem3, ordem4]

apresentação = random.choice(lista)

print('A ordem de apresentação será {}'.format(apresentação))