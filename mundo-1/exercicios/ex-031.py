# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de
# até 200 km e R$0,45 para viagens mais longas.

d = float(input('Qual foi a distância da viagem? '))
curta = d * 0.50
longa = d * 0.45
if d <= 200:
    print('Você vai pagar R${} de passagem.'.format(curta))
else:
    print('Você vai pagar R${} de passagem'.format(longa))