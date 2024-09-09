n = str(input('Me diga o seu nome inteiro: ')).strip().lower()
div = n.split()
name = div[0]
sobrenome = div[-1]

print ('Prazer em te conhecer!')
print ('O seu primeiro nome é: {}'.format(name))
print ('O seu último nome é: {}'.format(sobrenome))