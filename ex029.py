velocidade = float(input('Digite a velocidade em que você estava percorrendo: '))
limite = 80
multa = 7
velocidade_excedente = velocidade - limite
valor_multa = velocidade_excedente * multa
print('Você foi multado em R${} por estar em velocidade acima do limite (80km/h), e estar dirigindo a {}km/h'.format(valor_multa, velocidade)) if velocidade > limite else print('Você estava dentro da velocidade limite, continue assim')
