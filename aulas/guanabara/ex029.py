velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você execedeu o limite permitido que é 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${}!'.format(multa))
print('Tenha um bom dia! Dia! Dirija com segurança!')