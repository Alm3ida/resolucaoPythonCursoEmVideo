''' Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome completo com todas as letras maiúsculas
> O nome com todas minúsculas
> Quantas letras tem ao todo (sem considera os espaços)
> Quantas letras tem o primeiro nome

'''
nome = input('Digite o seu nome completo: ')



print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
primeironome = nome.split()
print(len(primeironome[0]))