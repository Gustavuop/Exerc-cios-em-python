from random import choice
n1 = str(input("Digite o nome de um aluno: "))
n2 = str(input("Digite outro nome: "))
n3 = str(input("Digite outro nome: "))
n4 = str(input("Digite outro nome: "))
nomes = [n1, n2, n3, n4]
nome_sorteado = choice(nomes)
print("O aluno sorteado é: {}".format(nome_sorteado))