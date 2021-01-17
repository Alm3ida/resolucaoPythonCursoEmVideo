"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda 
não atingiram a maioridade e quantas já são maiores.
""" 
from datetime import date
atual = date.today().year
maior = 0
menor = 0

for pess in range(0, 7):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(pess+1)))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é maior de idade')
        maior += 1
    else:
        print('Essa pessoa é menor de idade')
        menor += 1
    print('Essa pessoa tem {} anos' .format(idade))

print('Existem {} pessoas maiores de idade'.format(maior))
print('Existem {} pessoas menores de idade'.format(menor))