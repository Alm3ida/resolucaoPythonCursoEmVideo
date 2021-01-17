largura = int(input('Qual a largura da sua parede em metros?: '))
altura = int(input('Qual a altura da sua parede em metros?: '))

area = largura*altura
capacidade = 2

quantidade = round((area/capacidade),1)

print('A area de sua parede é de {}m², e a quantidade de latas de tinta é de {}' .format(area, quantidade))


