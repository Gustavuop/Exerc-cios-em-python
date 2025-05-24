viagem = float(input('Digite quantos quilomêtros sua viagem vai dar: '))
vf1 = viagem * 0.5
vf2 = viagem * 0.45
print('Sua viagem de {}km custa um total de R${}'.format(viagem, vf1 )) if viagem <=200 else print('Sua viagem de {}km custa um total de R${}'.format(viagem, vf2))