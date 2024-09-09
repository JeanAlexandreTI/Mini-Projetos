print ('Vou te ajudar a resolver o seu problema matemático!')
print ('Vamos te dizer se com os tamanhos do segmentos que você informar é possível formar um triãngulo!')

s1 = float(input('Para isso preciso que você me informe o tamanho do segmento 1: '))
s2 = float(input('Me informe o tamanho do segmento 2: '))
s3 = float(input('Me informe o segmento 3: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 :
    if s1 == s2 == s3 or s3 == s2 == s1:
        print('É possível formar um triângulo equilatero!')
    elif  s1 == s2 != s3 or s2 == s3 != s1 or s1 == s3 != s2:
        print ('É possível formar um triângulo isósceles!')
    elif s1 != s2 != s3 or s3 != s2 != s1:
        print('É possível formar um triângulo escaleno!')
else:
    print('Não é possível formar um triângulo.')        