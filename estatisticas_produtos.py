preço_total = 0
mais_mil = 0
valormin = []
produto_b = ''
while True:
    print('==='*25)
    produto = str(input('Qual o produto comprado? ')).strip().lower()
    valor = float(input('Qual o valor deste produto? '))
    print('==='*25)
    if valor > 1000:
        mais_mil = mais_mil + 1

    valormin = valormin + [valor]
    if valor == min(valormin):
        produto_b = produto

     
    cadastro = str(input('Deseja informar outros produtos? Digite [ S ] ou [ N ]: ')).strip().upper()
    preço_total = preço_total + valor

    if cadastro == 'N':
        print(f'Valor total gasto: R${preço_total}')
        print(f'Quantidade de produtos que ultrapassaram R$1000: {mais_mil}')
        print(f'O produto mais barato foi {produto_b}, custando o valor de: R${min(valormin)}')
        break