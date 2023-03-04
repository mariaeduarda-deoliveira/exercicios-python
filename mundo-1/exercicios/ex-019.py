# Um professor quer sortear um dos seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo o nome escolhido.

import random

a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto nome: ')

print('O aluno sorteado é {}'.format(random.choice([a1, a2, a3, a4])))
