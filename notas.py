print('Vamos verificar se você foi aprovado ou não. Por favor nos diga as suas notas!')
primeiro = float(input('Primeiro trimestre: '))
segundo = float(input('Segundo trimestre: '))
terceiro = float(input('Terceiro trimestre: '))

if primeiro >= 18 and primeiro <= 30:
    print('Você foi APROVADO no primeiro trimestre!')
else:
    if primeiro < 18:
        print('Você NÃO foi aprovado no primeiro trimestre!')
    else:
        print('Não é possível ficar acima de 30 pontos.')

if segundo >= 18 and segundo < 30:
    print('Você foi APROVADO no segundo trimestre!')
else:
    if segundo < 18:
        print('Você NÃO foi aprovado no segundo trimestre!')
    else:
        print('Não é possível ficar acima de 30 pontos.')

if terceiro >= 24 and terceiro <= 40:
    print('Você foi APROVADO no terceiro trimestre!')
else:
    if terceiro < 24:
        print('Você NÃO foi aprovado no terceiro trimestre!')
    else:
        print('Não é possível ficar acima de 40 pontos.')

if primeiro + segundo + terceiro >= 60 and primeiro + segundo + terceiro <= 100:
    print(f'Parabéns! Você PASSOU DE ANO com {primeiro+segundo+terceiro} pontos!')
else:
    if primeiro + segundo + terceiro < 60:
        print('Você está de RECUPERAÇÃO FINAL!')
        recuperação = str(input('Você fez a recuperação? ')).strip().lower()
        if recuperação == 's':
            pf = float(input('Qual foi a sua pontuação? '))
            if pf >= 60 and pf <100:
                print('Parabéns! Você conseguiu passar de ano!')
                if recuperação == 'n':
                    print('Você reprovou! Deveria ter tentado fazer a prova final...')
