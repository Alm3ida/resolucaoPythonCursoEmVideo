#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.


import math

num = float(input('Digite um número: '))
numC = math.floor(num)

print('O número {} tem a parte inteira {}.' .format(num, numC))