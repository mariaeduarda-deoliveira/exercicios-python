# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre o
# comprimento da hipotenusa.

# sem math
"""oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))"""

# com math
from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
