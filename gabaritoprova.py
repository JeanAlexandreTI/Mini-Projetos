a = 0
n = 0
aluno = 0
todas_notas = 0
maiorA = []
menorA = []


while True:
    aluno = aluno + 1
    print('==='*25)
    print(f'Aluno {aluno}'.center(70))
    print('==='*25)
    
    print('~~~'*25)
    q1 = str(input(f'Informe a resposta referente a questão 1: ')).upper().strip()
    if q1 == 'A':
        a = a + 1
        n = n + 1

    q2 = str(input(f'Informe a resposta referente a questão 2: ')).upper().strip()
    if q2 == 'B':
        a = a + 1
        n = n + 1

    q3 = str(input(f'Informe a resposta referente a questão 3: ')).upper().strip()
    if q3 == 'C':
        a = a + 1
        n = n + 1

    q4 = str(input(f'Informe a resposta referente a questão 4: ')).upper().strip()
    if q4 == 'D':
        a = a + 1
        n = n + 1

    q5 = str(input(f'Informe a resposta referente a questão 5: ')).upper().strip()
    if q5 == 'E':
        a = a + 1
        n = n + 1

    q6 = str(input(f'Informe a resposta referente a questão 6: ')).upper().strip()
    if q6 == 'E':
        a = a + 1
        n = n + 1

    q7 = str(input(f'Informe a resposta referente a questão 7: ')).upper().strip()
    if q7 == 'D':
        a = a + 1
        n = n + 1

    q8 = str(input(f'Informe a resposta referente a questão 8: ')).upper().strip()
    if q8 == 'C':
        a = a + 1
        n = n + 1    

    q9 = str(input(f'Informe a resposta referente a questão 9: ')).upper().strip()
    if q9 == 'B':
        a = a + 1
        n = n + 1

    q10 = str(input(f'Informe a resposta referente a questão 10: ')).upper().strip()
    if q10 == 'A':
        a = a + 1
        n = n + 1
    print('~~~'*25)

    print('==='*25)
    print(f'Aluno {aluno} acertou {a}')
    print(f'Aluno {aluno} teve a nota de {n}')
    print('==='*25)
    maiorA = maiorA + [a]
    todas_notas = todas_notas + n
    novoaluno = str(input('''Outro aluno deseja utilizar o sistema?
[ S ] Sim
[ N ] Não
Opção: ''')).upper().strip()

    if novoaluno == 'S':
        a = 0
        n = 0

    elif novoaluno == 'N':
        print('==='*25)
        print(f'A prova com maior quantidade de acertos conteve {max(maiorA)} acertos.')
        print(f'O sistema foi acessado por {aluno} aluno(s).')
        print(f'A nota média da turma é de {todas_notas/aluno} pontos.')
        print('==='*25)
        break
