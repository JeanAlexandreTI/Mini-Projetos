colocação = ('Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo',
             'Cruzeiro', 'Attlético-MG','Bragantino', 'Palmeiras', 'Internacional', 'Fortaleza',
             'Grêmio','Vasco da Gama', 'Criciúma', 'Juventude', 'Corinthians', 'Fluminense','EC Vitória','Atlético-GO', 'Cuiabá')
chapecoense = colocação
print('=-='*24)
print('OS CINCO PRIMEIROS'.center(70))
print(colocação[:5])
print('=-='*24)

print('OS 4 ÚLTIMOS COLOCADOS'.center(70))
print(colocação[16:])
print('=-='*24)

print('ORDEM ALFABÉTICA DOS TIMES'.center(70))
print(sorted(colocação))
print('=-='*25)

print('COLOCAÇÃO DA CHAPECOENSE'.center(70))
chape = 'chapecoense' in colocação
if chape == False:
    print('O time não da Chapecoense não está na primeira divisão do campeonato brasileiro de futebol.')
elif chape == True:
    print(f'A colocação do time da Chapecoense é a {colocação.index('chapecoense')}°.')