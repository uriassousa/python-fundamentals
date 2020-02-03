#Aluguel de carros
dias = float(input('Quantidade de dias para o aluguel: '))
valor = dias * 60 
kmrodado = float(input('Quantidade de KMs rodados: '))
km = kmrodado * 0.15
total = valor + km
print(' O valor somando os dias é R${:.2f}, mais os R${:.2f} dos KM´s rodados, o valor final a ser pago é R${:.2f} '.format(valor, km, total))

