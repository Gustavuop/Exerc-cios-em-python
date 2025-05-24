n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(nome)-1]))
