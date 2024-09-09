decimal = int(input('Informe um número decimal: '))
div = decimal // 2 
resto = div % 2
div2 = div // 2
resto1 = div2 % 2
div3 = div2 // 2
resto2 = div3 % 2
div4 = div3 // 2
resto3 = div4 % 2

print('O número {} no sistema binário ficaria assim: {}{}{}{}'.format(decimal, resto3, resto2, resto1, resto))