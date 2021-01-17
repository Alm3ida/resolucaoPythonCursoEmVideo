'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
Ex:
Digite um número: 1834

unidade:4
dezena3
centena:8
milhar:1
'''

num = input('Digite um número: ')
milhar = num[0]
centena = num[1]
dezena = num[2]
unidade = num[3]

print("""
Unidade:    {}
Dezena:     {}
Centena:    {}
Milhar:     {}
""" .format(unidade, dezena, centena, milhar))


