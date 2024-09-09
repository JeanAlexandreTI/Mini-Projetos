from time import sleep

começo = int(input('Me informe o número inícial da contagem: '))
final = int(input('Me informe o número final da contagem: '))

for c in range(começo,final+1):
    print(c)
    sleep(1)
    if c == final:
        print('VAI EXPLODIR!...BUUMM!!')
for c in range(começo, final-1, -1):
    print(c)
    sleep(1)
    if c == final:
        print('VAI EXPLODIR!...BUUMMM!!')
