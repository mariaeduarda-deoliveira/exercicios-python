# Desenvolva um programa que leia as duas notas de um aluno, calcule
# e mostre sua média.

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

print('A média do(a) aluno(a) é: {:.1f}'.format(media))