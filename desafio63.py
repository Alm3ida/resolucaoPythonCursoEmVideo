# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma sequência de Fibonacci Ex: 0->1->1->2->3


fibonnaci = [0, 1]

num = int(input('Digite a quantidade de termos: '))

for c in range(2, num+1):
    fibonnaci.append(fibonnaci[c-1] + fibonnaci[c-2]) 
    
print(fibonnaci)

