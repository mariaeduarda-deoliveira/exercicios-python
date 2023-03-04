# Crie um programa que leia um número real qualquer pelo teclado e
# mostre na tela a sua porção inteira.
# ex: digite um número: 6.127; o número 6.127 tem a parte inteira 6.

"""from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
"""

# sem math
num = float(input('Digite um valor: '))
print('A porção inteira de {} é {}'.format(num, int(num)))
