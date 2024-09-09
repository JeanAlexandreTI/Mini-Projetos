distância = float(input('Qual foi a distância da sua viagem? '))

if distância <= 200:
    print('O valor da sua viagem ficou em:R$ {:.2f}'.format(distância*0.50))
if distância > 200:
    print('O valor da sua viagem ficou em:R$ {:.2f}'.format(distância*0.45))