# Faça um programa que leia o nome completo de uma pessoa, mostrando em
# seguida o primeiro e o último nome separadamente.
# Exemplo: Ana de Souza Santos
# Primeiro: Ana
# Segundo: Santos.

seu_nome = str(input('Digite seu nome completo: ')).strip()
nome = seu_nome.split()
print('Seu nome é: {}.'.format(seu_nome))
print('E seu primeiro nome é: {}.'.format(nome[0]))
print('Por fim, seu último nome é: {}.'.format(nome[len(nome)-1]))
