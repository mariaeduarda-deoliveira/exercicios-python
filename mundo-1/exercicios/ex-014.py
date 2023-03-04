# Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

graus = float(input('Quantos graus quer converter? '))
f = 9 * graus / 5 + 32

print("{}° são {}F".format(graus, f))
