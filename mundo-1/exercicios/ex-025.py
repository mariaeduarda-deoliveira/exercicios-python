# Crie um programa que leia o nome de uma pessoa e diga se ela tem
# "Silva" no nome.

seu_nome = str(input('Insira seu nome completo: ')).strip().title()
print('Você tem "Silva" no nome? {}'.format('Silva' in seu_nome))