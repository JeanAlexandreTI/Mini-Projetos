from random import randint
from operator import itemgetter

result = {
    "player01" : randint(1, 6),
    "player02" : randint(1, 6),
    "player03" : randint(1, 6),
    "player04" : randint(1, 6),
}

for k, v in result.items():
    print(f"O {k} ao jogar o dado conseguiu o número {v}")

ranking = sorted(result.items(), key = itemgetter(1), reverse = True)

print("-=" * 30)

for i, r in enumerate (ranking):
    print(f"Em {i+1}° lugar ficou o {r[0]} com {r[1]} pts")