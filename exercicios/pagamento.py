# #Informações sobre salário

valorhora = float(input('Entre com o valor da horas: '))
horastrab = float(input('Entre com as horas trabalhadas: '))
salariobruto = valorhora * horastrab
fgts = (salariobruto * 15 / 100)
sindicato = (salariobruto * 3 / 100)
inss = (salariobruto * 6 / 100)
descontos = fgts + sindicato + inss
salarioliq = salariobruto - descontos

print('Valor hora {} \n horas trabalhadas {} \n salario bruto {}, \n salario liquido {}'.format(valorhora, horastrab, salariobruto, salarioliq))

print(' Valor do FGTS {0} \n valor do INSS {2} \n valor do desconto do sindicato {1}'.format(fgts, sindicato, inss))
