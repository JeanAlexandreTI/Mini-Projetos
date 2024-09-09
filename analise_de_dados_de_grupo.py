maior_idade = 0
h = 0
f = 0
while True:
    print('==='*25)  
    idade = int(input('Digite a sua idade: '))
    if idade > 18:
        maior_idade = maior_idade + 1
    print('==='*25)
    while idade <= 0:
        print('O sistema não permite idade negativa ou igual a 0.')
        idade = int(input('Digite a sua idade: '))
        if idade > 18:
            maior_idade = maior_idade + 1
        print('==='*25)

    sexo = str(input('''Informe o seu sexo:
[ M ] Masculino.
[ F ] Feminino.
Opção: ''')).strip().upper()      
    if sexo == 'M':
        h = h + 1
        print('==='*25)

    elif sexo == 'F' and idade < 20:
        f = f + 1
        print('==='*25)

    while sexo != 'M' and sexo != 'F':
        print('Desculpe, o sistema não identificou o sexo. Por favor preencha novamente.')
        sexo = str(input('''Informe o seu sexo:
[ M ] Masculino.
[ F ] Feminino.
Opção: ''')).strip().upper()
        
        if sexo == 'M':
            h = h + 1
            print('==='*25)
        elif sexo == 'F' and idade < 20:
            f = f + 1
            print('==='*25)

    print('==='*25)
    cadastro = str(input('''Deseja cadastrar mais pessoas?
[ S ] Sim.
[ N ] Não
Opção: ''')).strip().upper()
    print('==='*25)

    if cadastro == 'N':
        print('==='*25)
        print(f'Total de pessoas que são maiores de 18 anos: {maior_idade}')
        print(f'Total de homens cadastrados: {h}')
        print(f'Total de mulheres com a idade inferior a 20 anos: {f}')
        print('==='*25)
        break