s = 0

for c in range(1,6+1):
    n = int(input(f'Informe o {c}° número: '))
    if n % 2 == 0:
        s = n + s
        print(f'A soma de todos os números pares informados é de: {s}') 

        
    