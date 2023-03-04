# Faça um programa que leia alg pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis sobre ele.

user = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(user))
print('É alfanumerico? ', user.isalnum())
print('É alfabético? ', user.isalpha())
print('É numérico? ', user.isnumeric())
print('Só tem espaços? ', user.isspace())
print('Está em maiúsculas? ', user.isupper())
print('Está em minúsculas?', user.islower())
print('Está capitalizada?', user.capitalize())
