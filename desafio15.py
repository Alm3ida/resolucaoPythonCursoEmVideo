'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o 
carro custa R$60 por dia e R$0.15 por Km rodado'''

dias = int(input('O carro foi alugado por quantos dias?: '))
kilometers = float(input('Quantos Km o carro percorreu?: '))

pDias = dias * 60
pKilometers = kilometers * 0.15
preco = pDias + pKilometers

print('O valor a ser pago por {} dias de uso e {} Km percorridos é de R${:.2f}' .format(dias, kilometers, preco))
