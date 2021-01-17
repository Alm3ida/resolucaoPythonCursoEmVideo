"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o 
valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado.
"""
houseValue = float(input('Qual é o valor da casa?: R$'))
salary = float(input('Qual é o seu salário?: R$'))
period = int(input('Em quantos anos deseja pagar?: '))

quota = (houseValue/period)/12

if quota > (salary * (30/100)):
    print('Empréstimo negado!!! Valor de parcela excede 30% do seu salário')
else:
    print('Parabéns, empréstimo realizado com sucesso!!!')

