vlr_hora = float(input('Enter com o valor hora: '))
qtd_hora = float(input('Entre com a quantidade de horas: '))

sal_bruto = vlr_hora * qtd_hora

print('O salário bruto é {:.2f}!'.format(sal_bruto))

if sal_bruto >= 4600:
    ir = 27
elif sal_bruto > 3700 and sal_bruto < 4600:
    ir = 22
elif sal_bruto > 2800 and sal_bruto < 3700:
    ir = 15
elif sal_bruto > 1900 and sal_bruto < 2800:
    ir = 7
else:
    ir = 0

valorIR = sal_bruto * (ir / 100.0)
valorSIND = sal_bruto * (3 / 100.0)
valorFGTS = sal_bruto * (11 / 100.0)
totalDESC = valorIR + valorSIND
sal_liq = sal_bruto - totalDESC

print('Salario Bruto: {} * {}: {}'.format(valor_vlr))