# Crie um programa que leia um número inteiro e mostre na tela se ele e
# par ou ímpar.

num = int(input('Digite um número: '))
resto = num % 2
if resto == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))
