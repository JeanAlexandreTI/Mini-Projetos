salário = float(input('Informe o valor bruto do seu salário: R$'))
'''Aumenta o salário em 10% caso seja acima de R$1250
e 15% abaixo ou igual a R$1250'''
if salário > 1250.00:
    print(f'Seu salário passou a ser de R${salário} para R${(salário*0.10)+salário}')
elif salário <= 1250.00:
    print(f'Seu salário passou a ser de R${salário} para R${(salário*0.15)+salário}')