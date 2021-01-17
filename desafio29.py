"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa custará R$7,00 por cada Km acima do limite.
"""
v = float(input('Olá, digite a velocidade do seu carro:'))

if v > 80:
    print('MULTADO! Você excedeu o limite permitido de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}' .format((v-80)*7))

print('Tenha um bom dia! Dirija com segurança')