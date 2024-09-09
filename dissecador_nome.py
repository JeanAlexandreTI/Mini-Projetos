nome = str(input('Me informe seu nome completo: ').strip())
maiúsculo = nome.upper()
minúsculo = nome.lower()
div = nome.split()
noEspace = nome.count(' ')
caracteres = len(nome)-noEspace
n1 = len(div[0])


print(('''em maiúsculo ficou: {}
em minúsculo ficou: {}
o total de letras que o seu nome contém é: {}
o seu primeiro nome contém: {} caracteres''').format(maiúsculo, minúsculo, caracteres, n1))
