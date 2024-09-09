velocidade = float(input('Qual a velocidade do seu carro? '))


if velocidade > 80:
    print('Você foi multado em R${:.2f}'.format((velocidade-80)*7))
else:
    print('Você não foi multado, mas tome cuidado com o limite de velocidade!')