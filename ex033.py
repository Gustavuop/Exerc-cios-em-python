n = float(input('Digite um número qualquer: '))
n2 = float(input('Digite um número qualquer: '))
n3 = float(input('Digite um número qualquer: '))
menor = n
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
maior = n
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))