# Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e raiz quadrada.

seu_num = int(input("Digite um número: "))

dobro = seu_num * 2
triplo = seu_num * 3
raiz = seu_num ** (1/2)

print('O dobro de {} é {} \nO triplo é {} \nE a raiz quadrada é {:.2f}.'.
      format(seu_num, dobro, triplo, raiz))
