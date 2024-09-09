frase = str(input('Informe uma frase: ')).strip().upper()
div = frase.split()
junção = ''.join(div)

if junção == junção[::-1]:
    print(f'''A palavra {frase} de ao contrario é: {junção[::-1]}
A frase é um polindromo.''')
else:
    print(f'''A' palavra {frase} ao contrario é: {junção[::-1]}
A frase não é um polindromo.''')

'''print(len(junção))
print(junção[::-1])'''