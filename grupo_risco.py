idade = int(input('Qual a sua idade? '))

if idade <= 50:
    doença = str(input('Contém alguma doença pré-existente? ')).strip().upper()

    if doença == 'N':
        sexo = str(input('Qual o seu gênero? Para masculino "M", para feminino "F": ')).strip().upper()

        if sexo == 'F':
            gestante = str(input('Etá em período de gestação? "S" para sim e "N" para não ')).strip().upper()

            if gestante == 'N':
                print('''Você não está no grupo de risco, mas deve atentar-se aos cuidados!
Como: Evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos''')
                
else:
    print('''Você está no grupo de risco! Por favor, vamos evitar contato físico, não dividir copos 
e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos''')
    
