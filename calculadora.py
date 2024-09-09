adiçãoLista = []
subLista = []
multiLista = []
divLista = []

print('==='*25)
operação = str(input('''Me informe a operação que deseja realizar. Sendo:
[ + ] Soma.
[ - ] Subtração. 
[ * ] Multiplicação.
[ / ] Divisão.
OPÇÃO: '''))
print('==='*25)

while operação != '+' or operação != '-' or operação != '*' or operação != '/':
    print('~~~'*25)
    print('ERRO!! O sistema não foi capaz de identificar a operação que você deseja.')
    print('Por favor, informe a operação novamente.')
    print('~~~'*25)
    print('==='*25)
    operação = str(input('''Me informe a operação que deseja realizar. Sendo:
[ + ] Soma.
[ - ] Subtração. 
[ * ] Multiplicação.
[ / ] Divisão.
OPÇÃO: '''))
    print('==='*25)

    if operação == '+' or operação == '-' or operação == '*' or operação == '/':
        break 

if operação == '+':
    for c in range(1,2+1):
        valor = float(input(f'Digite o {c}° valor: '))
        adiçãoLista = adiçãoLista + [valor] 
        adição = max(adiçãoLista) + min(adiçãoLista)
    print(f'O resultado de {max(adiçãoLista)} + {min(adiçãoLista)} é {adição}')

elif operação == '-':
    for c in range(1,2+1):
        valor = float(input(f'Digite o {c}° valor: '))
        subLista = subLista + [valor]
        sub = max(subLista) - min(subLista)
    print(f'O resultado de {max(subLista)} - {min(subLista)} é {sub}')

elif operação == '*':
    for c in range(1, 2+1):
        valor = float(input(f'Digite o {c}° valor: '))
        multiLista = multiLista + [valor]
        multi = max(multiLista) * min(multiLista)
    print(f'O resultado de {max(multiLista)} x {min(multiLista)} é {multi}')

elif operação == '/':
    for c in range(1, 2+1):
        valor = float(input(f'Informe o {c}° valor: '))
        divLista = divLista + [valor]
        div = max(divLista) / min(divLista)
    print(f'O resultado de {max(divLista)} / {min(divLista)} é {div}')