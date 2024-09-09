sal = float(input('Qual o salário de um funcionário? R$'))
totalAumentado = sal*0.15
novoSal = totalAumentado + sal 

print ('O salário mudou de R$ {} para R$ {:.2f}, obtendo um aumento de 15% (ou R$ {:.2f}).'.format(sal, novoSal, totalAumentado))