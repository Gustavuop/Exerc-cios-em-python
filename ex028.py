from random import randint
from time import sleep
numero_aleatorio = randint (1, 5)
tentativa = int(input('Digite um número de 1 a 5, e tente acertar o número escolhido pela máquina: '))
while tentativa < 1 or tentativa > 5:
    print('Número inválido! Digite apenas um número entre 1 e 5.')
    tentativa = int(input('Tente novamente: '))
print('PENSANDO EM UM NÚMERO DE 1 A 5...')
sleep(3)
print('Você acertou o número aleatório! Parabéns!') if numero_aleatorio == tentativa else print('Você errou, eu pensei no número: {}'.format(numero_aleatorio))