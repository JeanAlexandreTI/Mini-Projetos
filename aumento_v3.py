'''salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

print('Nós da Organizações Tabajara, resolvemos dar um aumento salárial a vocês!')
valor = float(input('Nós informe a sua renda bruta: R$'))

if valor <= 280.00:
    print(f'''O seu salário antes do reajuste era de: R${valor}.
O percentual de aumento foi de: 20%.
O valor aumentado foi de: R${valor*0.20:.2f}.
O novo salário após o aumento: R${(valor*0.20)+valor:.2f}''')
else:
    if valor > 280.00 and valor < 700.00:
        print(f'''O seu salário antes do reajuste era de: R${valor}.
O percentual aumentado foi de: 15%.
O valor do aumento foi de: R${valor*0.15:.2f}.
O novo salário após o aumento: R${(valor*0.15)+valor:.2f}''')
    else:
        if valor > 700 and valor < 1500:
            print(f'''O seu salário antes do reajuste era de: R${valor}.
O percentual aplicado foi de: 10%.
O valor aumentado foi de: R${valor*0.10:.2f}.
O novo salário após o aumento: R${(valor*0.10)+valor:.2f}.''')
        else:
            if valor > 1500:
                print(f'''O seu salário antes do reajuste era de: R${valor}.
O percentual aumentado foi de: 5%.
O valor aumentado foi de: R${valor*0.05:.2f}.
O novo salário após o aumento: R${(valor*0.05)+valor:.2f}''')
                