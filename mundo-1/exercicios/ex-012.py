# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto.

preço = float(input('Qual é o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('O produto de R$ {} na promoção de 5% vai custar R${}'.format(preço, novo))