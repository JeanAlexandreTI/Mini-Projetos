extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove','vinte')

n = int(input('Digite um número inteiro: '))

while n < 0 or n > 20:
    print('Não aceitamos números menores que 0 ou maiores que 20!')
    n = int(input('Informe o número novamente: '))
print(f'{extenso[n]}')


c = str(input('Você deseja continuar? [ S / N ] :')).upper().strip()
while c == 'S':
    extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove','vinte')

    n = int(input('Digite um número inteiro: '))

    while n < 0 or n > 20:
        print('Não aceitamos números menores que 0 ou maiores que 20!')
        n = int(input('Informe o número novamente: '))
    print(f'{extenso[n]}')


    c = str(input('Você deseja continuar? [ S / N ] :')).upper().strip()
if c == 'N':
    print('Programa encerrado.')
    

