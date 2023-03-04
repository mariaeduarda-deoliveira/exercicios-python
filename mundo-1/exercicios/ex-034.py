# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor de seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%;
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: R$ '))

if salario >= 1250:
    novo = salario + (salario * 10 / 100)
    print('Seu salário de R$ {:.2f} aumentou 10%. Agora você recebe R$ {:.2f}.'.format(salario, novo))
else:
    novo = salario + (salario * 15 / 100)
    print('Seu salário de R$ {:.2f} aumentou 15%. Agora você recebe R$ {:.2f}.'.format(salario, novo))