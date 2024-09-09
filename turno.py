turno = str(input('Me informe o turno na qual você estuda."M" para matutino,"V" para vespertino e "N" para noturno: ')).strip().upper()

if turno == 'M':
    print('Bom dia! As aulas irão começar as 07:00am')
else:
    if turno == 'V':
        print('Boa tarde! As aulas irão começar as 13:00pm')
    else:
        if turno == "N":
            print('Boa noite! As aulas irão começar as 19:20pm')
        else:
            print('Não entendi o que foi digitado.')