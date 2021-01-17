# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

ang = float(input('Digite o valor do ângulo: '))

angSen = round(math.sin(math.radians(ang)), 2)
angCos = round(math.cos(math.radians(ang)), 2)
angTan = round(math.tan(math.radians(ang)), 2)

print('Para um ângulo de {:.2f}°, temos que o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}' .format(ang, angSen, angCos, angTan))
