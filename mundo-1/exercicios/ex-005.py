# Faça um programa que leia um número inteiro e mostre na tela o
# seu sucessor e antecessor.

#seu_num = int(input('Digite um número: '))
#antecessor = seu_num - 1
#sucessor = seu_num + 1

#print('Valor antecessor: {}'.format(antecessor))
#print('Valor sucessor: {}'.format(sucessor))

num = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'
      .format(num, (num-1), (num+1)))
