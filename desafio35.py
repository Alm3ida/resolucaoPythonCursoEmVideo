"""Analise os comprimentos e verifique se é possível formar um triângulo"""
from math import fabs

a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))

"""
A condição de existência de um triângulo de lados a, b, c é dada por:
|a-b| < c < a + b
|a-c| < b < a + c
|b-c| < a < b + c
"""
if fabs(a-b) < c and c < (a + b) and fabs(a-c) < b and b < (a + c) and fabs(b-c) < a and a < (b + c):
    print('É possível formar um triângulo com esses lados!!!')
else:
    print('Não é possível formar um triângulo com esses lados!!!')
