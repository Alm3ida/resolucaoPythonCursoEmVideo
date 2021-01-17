"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

"""
val = float(input('Digite a distância até o local desejado:'))

if val > 200:
    preco = val * 0.45
else:
    preco = val * 0.5

print('O valor da sua passagem é de R${:.2f} para uma viagem de {:.2f}Km' .format (preco, val))
