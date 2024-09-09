data = {}

data["aluno"] = str(input("Nome do estudante: "))
data["media"] = float(input(f"Informe a média da nota de {data["aluno"]}: "))


if data["media"] >= 7:
    data["situacao"] = "Aprovado"
else:
    data["media"] = "Reprovado"

for k, v in data.items():
    print(f"{k}: {v}")