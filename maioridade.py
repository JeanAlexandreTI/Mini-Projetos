from datetime import date

atual = date.today().year
maior = 0
menor = 0
for c in range(1, 7+1):
    ano = int(input(f'Qual o ano de nascimento da {c}° pessoa? '))
    if atual - ano >= 18:
        maior = maior + 1
    elif atual - ano < 18: 
        menor = menor + 1
print(f'''De acordo com as pesquisas, o grupo contem:
{maior} pessoas com ou mais de 18 anos.
{menor} pessoas com a idade inferior aos 18 anos.''')