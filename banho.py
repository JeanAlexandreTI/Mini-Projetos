agua = str(input('Qual o estado da água? ')).strip().upper()

if agua == 'QUENTE':
    print ('Você pode tomar banho!')
elif agua == 'MORNA':
    print('Você pode tomar banho!')    
else: 
    print('Você precisa esquentar a água.')