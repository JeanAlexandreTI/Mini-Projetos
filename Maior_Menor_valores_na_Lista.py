value_list = []
ind_Vmax = []
ind_Vmin = []

for c in range(1,5+1):
    value = int(input(f'Informe o valor referente a {c}° posição: '))
    value_list = value_list + [value]

for i,v in enumerate (value_list):
    if v == max(value_list):
        ind_Vmax = ind_Vmax + [i]

    elif v == min(value_list):
        ind_Vmin = ind_Vmin + [i]        


print(f'A listagem ficou da seguinte forma: {value_list}')
print(f'O maior valor da lista está na(s) posição(ões) {ind_Vmax} e seu valor é {max(value_list)}')
print(f'O menor valor da lista está na(s) posição(ões {ind_Vmin} e seu valor é: {min(value_list)}')