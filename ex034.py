salario = float(input('Qual o seu salário? '))
aumento1 = (salario * 0.1) + salario
aumento2 = (salario * 0.15) + salario
print('O seu salário de R${} aumentou para R${}'.format(salario, aumento1)) if salario > 1250 else print('O seu salário de R${} aumentou para R${}'.format(salario, aumento2))