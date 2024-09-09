print('Vamos verificar se você foi aprovado!')
n1 = float(input('Me informe a sua primeira nota: '))
n2 = float(input('Me informe a sua segunda nota: '))

if (n1 + n2)/2 < 5:
    print('Você foi reprovado!')
elif (n1+n2)/2 > 5 and (n1+n2) < 6.9 :
    print('Você ficou de recuperação!')
else:
    print('Você passou!')