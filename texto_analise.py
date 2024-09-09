f = str(input('Me informe uma frase para realizar uma análise: ').split()).lower()
a = f.count('a')
posição = f.find('a')+1
fatia = f.rfind('a')+1


print ('''Quantidade de letras "a" encontradas: {}
Primeira aparição da letra "a": indíce {}
O último indíce na qual a letra "a" aparece: {}'''.format(a, posição, fatia))