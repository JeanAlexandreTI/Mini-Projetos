print ('Vamos realizar um calculo da velocidade média na qual seu carro percorreu.Informe o que se pede: ')

distância = float(input('Informe a distância na qual seu carro percorreu: '))
tempov = float(input('Informe o tempo que a viagem durou: '))
velocidadem = float(distância / tempov)

print ('Para realizarmos este calculo, dividimos {} por {}, dando que a velocidade média foi de {}km'.format(distância, tempov, velocidadem))
