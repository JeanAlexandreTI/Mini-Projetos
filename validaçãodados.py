sexo = str(input('''Informe o seu sexo:
[ M ] Masculino.
[ F ] Feminino.
Opção: ''')).upper().strip()
while sexo not in ['M','F']:
    sexo = str(input('Invalido. Digite o sexo novamente: ')).upper().strip()
print('Registro realizado.')