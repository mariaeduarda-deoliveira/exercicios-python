# Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Insira o valor R$: '))

dolar = carteira / 5.22

print('Você pode comprar US${:.2f} dólares.'.format(dolar))