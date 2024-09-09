print('===========LOJA DO JEAN===========')
valor = float(input('Informe o valor total das compras: '))
pagamento = int(input('''Informe a forma de pagamento.
[1] À vista.
[2] Parcelado.
OPÇÃO: '''))

if pagamento == 1:
    vista = int(input('''Qual a forma de pagamento à vista?
[1] Dinheiro ou Cheque.
[2] Cartão.
OPÇÃO: '''))
    if vista == 1:
        print(f'Você recebeu 10% de desconto! Sua compras ficou no valor de R${valor - (valor*0.10)}')
    else:
        print(f'Você ganhou 5% de desconto! Sua compra ficou no valor de: R${valor - (valor*0.05)}')
elif pagamento == 2:
    parcelamento = int(input('''Informe o total de vezes que deseja realizar o parcelamento.
[1] 2x.
[2] 3x ou mais.
OPÇÃO: '''))
    if parcelamento == 1:
        print(f'Com o parcelamento em 2x, por mês você terá que pagar:R${valor/2}')
        print(f'Sua compra ficou no valor total de: R${valor}')
    elif parcelamento == 2:
        opção2 = int(input('Em quantas vezes gostaria de parcelar o sua compra?'))
        print (f'Parcelando a sua compra em {opção2}x, por mês você terá que pagar:R${(valor+(valor*0.20))/opção2}')
        print(f'Sua compra vai conter um juros de 20%. Sua compra ficou no valor de: R${valor + (valor*0.20)}')
else:
    print('Opção invalida')