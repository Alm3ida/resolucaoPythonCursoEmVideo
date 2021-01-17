"""Faça um programa que leia 5 valores e guarde-os em uma lista.

No final, mostre qual foi o maior valor digitado e as suas respectivas posições na lista."""
maior = menor = 0
posiçãoM = posiçãom = 0
lista = []
for i in range(0,5):
    lista.append(int(input('Digite um número: ')))
    if i == 0:
        maior = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
            posiçãoM = i
        elif lista[i] <= menor:
            menor = lista[i]
            posiçãom = i

"""for c in range(0, len(lista)):
    if lista[c] == maior:
        posiçãoM"""



print(f'''O maior valor digitado foi {maior} e se encontra na posição {posiçãoM}.
O menor valor digitado foi {menor} e se encontra na posição {posiçãom}''')




