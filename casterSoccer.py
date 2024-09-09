goalsTotal = 0
data = {
    "Jogador" : str(input("Nome do Jogador de Futebol: ")).title().strip(),
    "Partidas Jogadas" : int(input("Total de partidas jogadas: "))
}

for goalOfMatches in range(data["Partidas Jogadas"]):

    goals = {
        "gol" : int(input(f"Quantos gols o jogador marcou na {goalOfMatches + 1}° partida? "))
    }

    goalsTotal += goals["gol"]
    data["Total de Gols"] = goalsTotal

for k, v in data.items():
    print(f"{k}: {v}")

