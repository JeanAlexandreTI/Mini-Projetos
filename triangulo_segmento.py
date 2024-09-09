'''Para formar um triângulo, a soma dos dois 
primeiros lado tem que ser maior que o terceiro lado!'''

lado1 = float(input('Me informe o tamanho da reta 1: '))
lado2 = float(input('Me informe o tamanho da reta 2: '))
lado3 = float(input('Me informe o tamanho da reta 3: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Os segmentos podem formar um triângulo! ')
else:
    print('Os 3 segmentos não podem formar um triângulo! ')