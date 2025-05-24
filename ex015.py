d = int(input('Quantos dias você alugou o carro? '))
k = float(input('Quantos quilômetros foram rodados? '))
p = (60*d) + (0.15*k)
print('O valor do aluguel do carro com {} dias alugados e {}km rodados é de: R${}'.format(d, k, p))
