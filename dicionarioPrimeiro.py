'''O PROGRAMA DEVE LER O NOME E A MÉDIA DO ALUNO
VERIFICAR A SITUAÇÃO DELE E GUARDAR TUDO EM UM DICIONARIO 
(Mostrar o resultado no final).'''

studant = {}

studant['name'] = str(input("Estudante, informe o seu nome: "))
studant['avg'] = float(input(f"{studant['name']}, informe a sua média final: "))

if studant['avg'] >= 7:
    studant['stuation'] = "APROVADO"

elif studant['avg'] < 7:
    studant['situation'] = "REPROVADO"

print(studant)