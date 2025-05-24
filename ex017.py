import math
co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjescente: '))
c = math.hypot(co,ca)
print ('De acordo com o comprimento dos catetos, o comprimento da hipotenusa é: {:.2f}'.format(c))