# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "Santo"

sua_cidade = str(input('Em que cidade você mora? ')).strip().title()
print('O nome da cidade começa com "Santo"? {}'.format(sua_cidade[0:5] == 'Santo'))