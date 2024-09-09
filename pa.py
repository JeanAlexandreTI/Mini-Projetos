termo = int(input('Informe o termo inicial: '))
razão = int(input('Informe a razão: '))    
decimo = termo + (10 - 1) *razão
for c in range( termo, decimo + razão, razão):
    print(f'{c}')
    