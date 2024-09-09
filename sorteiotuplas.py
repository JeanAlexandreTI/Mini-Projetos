from random import choice

raffle = ( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
number_fiveList = []

for i in range(5):
    choose = choice(raffle)
    number_fiveList += [choose]

print(number_fiveList)
print(f'''O maior número: {max(number_fiveList)}
O menor número: {min(number_fiveList)}''')
    