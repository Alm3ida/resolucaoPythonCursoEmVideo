"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
import math
a = int(input('Digite o valor do primeiro lado: '))
b = int(input('Digite o valor do segundo lado: '))
c = int(input('Digite o valor do terceiro lado: '))

if math.fabs(a-b) < c and c < (a + b) and math.fabs(a-c) < b and b < (a + c) and math.fabs(b-c) < a and a < (b + c):
    print('É possível formar um triângulo!!!')
    if a == c and c == b:
        print('O triângulo formado é Equilátero')
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('O triângulo formado é Isósceles!')
    elif (a != b) and (a != c) and (b != c):
        print('O triângulo formado é Escaleno!')
else:
    print('Não é possível formar um triângulo.')

