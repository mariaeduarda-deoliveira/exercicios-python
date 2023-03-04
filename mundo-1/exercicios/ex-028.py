# Escreva um programa que faça o computador "pensar" em um número
# aleatório entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

usuario = int(input('O computador pensou em um número de 0 a 5. Tente adivinhar: '))
computador = randint(0, 5)
print('Um momento...')
sleep(1)
if usuario == computador:
    print('O computador pensou em {}. Parabéns, você acertou!'.format(computador))
else:
    print('O computador pensou em {}. Poxa, você errou. :('.format(computador))
