# # #Informações sobre salário

# valorhora = float(input('Entre com o valor da horas: '))
# horastrab = float(input('Entre com as horas trabalhadas: '))
# salariobruto = valorhora * horastrab
# #fgts = (salariobruto * 15 / 100)
# #sindicato = (salariobruto * 3 / 100)
# #inss = (salariobruto * 6 / 100)
# #descontos = fgts + sindicato + inss
# #salarioliq = salariobruto - descontos

# #print('Valor hora {} \n horas trabalhadas {} \n salario bruto {}, \n salario liquido {}'.format(valorhora, horastrab, salariobruto, salarioliq))

# #print(' Valor do FGTS {0} \n valor do INSS {2} \n valor do desconto do sindicato {1}'.format(fgts, sindicato, inss))

# #Imposto de renda

# faixa1 = 7
# faixa1 = 15
# faixa1 = 22
# faixa1 = 27

# if salariobruto >=1900:
#     print('Isento',salariobruto)

vlr_hora = float(input("Digite o valor hora: "))
qtd_hora = float(input('Digite a qtde de horas trabalhadas: '))

salario_bruto = (qtd_hora * vlr_hora)

if salario_bruto >= 4600:
    ir = 27
elif salario_bruto > 3700 and salario_bruto < 4600:
    ir = 22
elif salario_bruto > 2800 and salario_bruto < 3700:
    ir = 15
elif salario_bruto > 1900 and salario_bruto <= 2800:
    ir = 7
else:
    ir = 0

valorIR = salario_bruto * (ir / 100)
valor_sindicato = salario_bruto * (3 / 100)
valorFGTS = salario_bruto * (11 / 100
total_desconto = valorIR + valor_sindicato
salario_liquido = salario_bruto - total_desconto

print('Salario Bruto: ({} * {}): {}'.format(vlr_hora, qtd_hora, salario_bruto))
print('(-) IR {}%: {}'.format(ir, valorIR))
<<<<<<< HEAD
print('(- S) Sindicateo (3$: R${}'format(valorFGTS ))
=======
print('(- S) Sindicateo (3$: R${}'format(valorFGTS, ))
>>>>>>> ec82fde7c44d5379f931dc5d0faa82bcf50068e0
