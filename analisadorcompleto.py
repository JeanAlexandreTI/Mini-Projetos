idadeF = 0     #para poder saber as mulheres com menos de 20 anos
m = 0          #para realizar o calculo da média das idades do grupo
yearM = []     #lista para saber a idade do homem mais velho
manvelho = ''
for dados in range (1, 4+1):
    sexo = str(input('''Informe o seu sexo.
[ M ] Masculino.
[ F ] Feminino.
OPÇÃO: ''')).strip().upper()
    
    if sexo == 'M':
        nome = str(input('Informe o seu nome: ')).strip().upper()
        idade = int(input('Digite a sua idade: '))
        yearM = yearM + [idade]
        if idade == max(yearM):
            manvelho = nome
    elif sexo == 'F':
        nome = str(input('Informe o seu nome: ')).strip().upper()
        idade = int(input('Informe a sua idade: '))
        if idade < 20:
            idadeF = idadeF + 1
    
    m = idade + m
    print('-='*10)
    
print(f'A média de idade do grupo: {m/4}.')
print(f'Nome do homem mais velho e sua respectiva idade: {manvelho}, {max(yearM)} anos.')
print(f'Quantidade de mulheres com menos de 20 anos: {idadeF}.')
