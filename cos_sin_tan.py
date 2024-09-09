import math

angulo = float(input('Me informe um ângulo: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print ('''Baseado no ângulo informado temos:
       seno de {:.2f}
       cosseno de {:.2f}
       tangente de {:.2f}'''.format(seno, cos, tan))