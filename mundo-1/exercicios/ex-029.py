# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai
# custar R$7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade atual: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você foi multado, o limite é 80 km. Sua multa é de R${:.2f}'.format(multa))
else:
    print('Você não foi multado. :)')
