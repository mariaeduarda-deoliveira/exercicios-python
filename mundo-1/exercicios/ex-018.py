# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}.'.format(angulo, seno, cos, tang))
