from datetime import date

ano = date.today().year

data = {}

data["Nome"] = str(input("Nome do colaborador: ")).title().strip()
yearOfBirth = int(input("Ano de nascimento: "))
data["Idade Atual"] = ano - yearOfBirth
data["Carteira de Trabalho"] = int(input("Carteira de trabalho (Digite 0 caso não possua): "))

if data["Carteira de Trabalho"] == 0:
    for k, v in data.items():
        print(f"{k}: {v}")
else:
    data["Ano de Contratação"] = int(input("Ano de efetivação (Primeiro trabalho): "))
    data["Salário"] = float(input("Salário: "))
    data["Idade de Aposentadoria"] = (data["Ano de Contratação"] - yearOfBirth) + 35 
    for k, v in data.items():
        print(f"{k}: {v}")