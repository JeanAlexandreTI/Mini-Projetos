house = float(input('Qual o valor da casa na qual o Sr(a) quer comprar? R$'))
sal = float(input('Qual o salário do Sr(a)? R$'))
tempo = int(input('Em quantos meses pretende pagar a casa? '))
mensal = house/tempo

if sal*0.30 > mensal:
    print('Perfeito! Realizaremos o empréstimo!')
elif sal*0.30 <= mensal:
    print('Infelizmente não podemos realizar o empréstimo!')