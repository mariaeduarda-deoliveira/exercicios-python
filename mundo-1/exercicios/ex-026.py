# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A";
# 2. Em que posição ela aparece a primeira vez;
# 3. Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
aparece = frase.count("A")
primeira = frase.find("A") + 1
ultima = frase.rfind("A") + 1

print('A letra "A" aparece {} vezes.'.format(aparece, primeira))
print('Ela aparece pela primeira vez na posição {}.'.format(primeira))
print('Ela aparece pela última vez na posição {}.'.format(ultima))
