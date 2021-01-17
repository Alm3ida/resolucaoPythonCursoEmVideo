"""
Desenvolva um programa que leia o primeiro termo de um PA e a razão. No final, mostre os 10 primeiros termos dessa
progressão.
"""
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = []

for g in range(a1, a1+10*r, r):
    pa.append(g)
print(pa)
print('FIM')