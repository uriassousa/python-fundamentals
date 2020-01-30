# Desconto de 5% de um produto

produto = float(input('Entre com o valor do produto R$ ' ))
desconto = produto*5/100
vfinal = produto - desconto
print('O valor do produto normal do produto R${}, tirando 5%, que é R${} o valor a ser pago é R${:.2f}'.format(produto, desconto, vfinal))


