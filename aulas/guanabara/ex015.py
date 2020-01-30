#Aluguel de carros
dias = float(input('Quantidade de dias para o aluguel: '))
valor = dias * 60 
kmrodado = float(input('Digite o valor dos KMs rodados: '))
km = kmrodado * 0.15
total = valor + km
print(' O valor a pagar é R${}, somando os R${} dos KM´s rodados o valor final a ser pago é R${} '.format(valor, km, total))

