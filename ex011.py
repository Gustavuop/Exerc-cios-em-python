l = float(input('Qual a largura da sua parede? '))
a = float(input('Qual a altura da sua parede? '))
area = a*l
t = area/2
print('É necessário {} litros de tinta para pintar uma área de {} metros²'.format(t, area))