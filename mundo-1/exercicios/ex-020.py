# O mesmo professor do exercício anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia o nome
# dos quatro alunos e mostre a ordem sorteada.

import random
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto nome: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A apresentação será nessa ordem: {}'.format(lista))
