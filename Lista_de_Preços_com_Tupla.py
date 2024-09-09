list_price = ('Lápis',1.75,
'Borracha',3.25,
'Caneta',2.25,
'Caderno Capa Dura',35.90,
'Agenda',13.99,
'Adesivos',0.25,
'Grampeador',11.75)

print('---'*20)
print('PAPELARIA'.center(60))
print('---'*20)
for i in range(0,len(list_price)):
    if i % 2 == 0:
        print(f'{list_price[i]:.<30}', end='')
    else:
        print(f'R${list_price[i]:>5.2f}')