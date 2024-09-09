accont = input('Informe uma expressão que contenha parênteses: ')
add, remove = 0

for _ in accont:
    
    if '(' in _:
        add += 1
    if ')' in _:
        remove += 1

if add - remove == 0:
    print('Os parênteses foram fechados corretamente.')
else:
    print('Os parênteses não foram fechados corretamente.')    