import math 

catetoOposto = float(input('Me informe o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Me informe o comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(math.pow(catetoOposto,2) + math.pow(catetoAdjacente,2))

print ('O comprimento do cateto oposto é {} e do cateto adjacente é {}'.format(catetoOposto, catetoAdjacente))
print ('Logo o comprimento da hipotenusa será {:.2f}'.format(hipotenusa))