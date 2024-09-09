import datetime
sexo = str(input('''Por favor, me informe o seu gênero.
[M] Masculino
[F] Feminino
Opção: ''')).strip().upper()
ano = int(input('Me informe o ano na qual você nasceu: '))
atual = datetime.date.today().year
idade = (atual - ano)

if sexo == 'F':
    print('Não precisa preocupar-se com questões de alistamento.')
elif idade < 18:
    print(f'Você ainda possui {idade} anos, deverá se alistar somente daqui {18-idade} anos.')
    print(f'Você deverá realizar o alistamento no ano de {(18-idade) + atual}!')
elif idade == 18:
    print (f'Você precisa alistar-se este ano!')
else:
    print(f'Você passou do prazo de alistamento, era para ter feito o alistamento a {idade-18} anos atrás!')
    print(f'Você deveria ter feito o alistamento no ano de {atual-(idade-18)}!')