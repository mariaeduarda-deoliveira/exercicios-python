# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
# um dos dígitos separados.
# Exemplo: digite o número: 1834
# unidade: 4; dezena: 3; centena: 8; milhar: 1.

seu_num = int(input('Digite um número de 0 a 9999: '))
nums = str(seu_num)
uni = seu_num // 1 % 10
dez = seu_num // 10 % 10
cen = seu_num // 100 % 10
mi = seu_num // 1000 % 10
print('Seu número é: {}'.format(seu_num))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(uni, dez, cen, mi))
