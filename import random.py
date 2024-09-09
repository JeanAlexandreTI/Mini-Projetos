import random

aluno1 = input('Me informe o nome do aluno: ')
aluno2 = input('Me informe o nome do aluno: ') 
aluno3 = input('Me informe o nome do aluno: ')
aluno4 = input('Me informe o nome do aluno: ')
aluno5 = input('Me informe o nome do aluno: ')
nomes = (aluno1, aluno2, aluno3, aluno4, aluno5)
sorteio = random.choice(nomes)

print('O aluno sorteado foi : {}'.format(sorteio))