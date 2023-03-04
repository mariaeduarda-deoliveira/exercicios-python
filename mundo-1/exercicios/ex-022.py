# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas;
# 2. O nome com todas minúsculas;
# 3. Quantas letras ao todo (sem considerar espaços);
# 4. Quantas letras tem o primeiro nome.

seu_nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculo: {}'.format(seu_nome.upper()))
print('Seu nome em minúsculo: {}'.format(seu_nome.lower()))
print('O tamanho do seu nome: {} letras.'.format(len(seu_nome) - seu_nome.count(' ')))
# print('Seu primeiro nome tem {} letras.'.format(seu_nome.find(' ')))
separar = seu_nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separar[0], len(separar[0])))