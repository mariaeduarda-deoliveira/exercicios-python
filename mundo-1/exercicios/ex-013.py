# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

salario = float(input('Salário atual: RS$ '))
novo = salario + (salario * 15 / 100)
print('Seu novo salário, com aumento de 15%, vai ser: R$ {:.2f}'.format(novo))