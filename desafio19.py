'''Um professor quer sortear um dos seus quatro alunos. Faça um programa que ajude ele, lendo o nome deles e 
escrevendo o nome do escolhido'''
import math
import random

nome1 = input('Digite o lugar 1: ')
nome2 = input('Digite o lugar 2: ')
nome3 = input('Digite o lugar 3: ')
nome4 = input('Digite o lugar 4: ')

sorteio = random.randint(1,4)

if sorteio == 1:
    mostrar = nome1
    pass    
if sorteio == 2:
    mostrar = nome2
    pass
if sorteio == 3:
    mostrar = nome3
    pass
if sorteio == 4:
    mostrar = nome4
    pass
print('O aluno escolhido foi o {}' .format(mostrar))