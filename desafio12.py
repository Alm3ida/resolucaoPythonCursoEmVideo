#Faça um algoritmo que leia o preço de um produto e mostreu seu novo preço com 5% de desconto.

preco = float(input('Insira o valor do produto: '))

precoNovo = round((preco * 0.95),3)

print('O valor do produto com 5% de desconto é R${}' .format(precoNovo))    