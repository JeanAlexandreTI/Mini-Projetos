#VAMOS ANALISAR SE A PRIMEIRA PALAVRA DA CIDADE COMEÇA COM "SANTO"  NO NOME!!!

city = str(input('Me informe o nome de uma cidade: '))
div = city.split()

print ('Analisando se a cidade começa com "Santo"...{}'.format('santo' in div[0].lower()))