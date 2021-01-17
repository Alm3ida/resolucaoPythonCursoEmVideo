#Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa.
import math

catO = float(input('Insira o comprimento do cateto oposto: '))
catA = float(input('Insira o comprimento do cateto adjascente: '))

hip = math.sqrt(math.pow(catO, 2) + math.pow(catA, 2))

print('O valor da hipotenusa do triângulo retângulo com cateto oposto {:.2f} e cateto adjascente {:.2f} é {:.2f} ' .format(catO, catA, hip))
