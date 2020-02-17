# -*- coding: latin-1 -*-
valor_hora = float(input('Digite o valor da hora de trabalho: '))
quant_hora_trabalhada = float(input('Digite a quantidade de hora trabalhada no mês: '))
salario_bruto = (valor_hora*quant_hora_trabalhada)


def descontos(salario_bruto):
    desc_sindicato = (salario_bruto/100)*3
    fgts = (salario_bruto/100)*11
    ir = 0
    if salario_bruto <= 1900:
        salario_liquido = salario_bruto - desc_sindicato
        
    elif salario_bruto > 1900:
        ir = (salario_bruto/100)*7
        salario_liquido = salario_bruto - desc_sindicato - ir
        
    elif salario_bruto <= 2500:
        ir = (salario_bruto/100)*15
        salario_liquido = salario_bruto - desc_sindicato - ir
        
    elif salario_bruto <= 3700:
        ir = (salario_bruto/100)*22
        salario_liquido = salario_bruto - desc_sindicato - ir

    else:
        salario_bruto >= 4600
        ir = (salario_bruto/100)*27
        salario_liquido = salario_bruto - desc_sindicato - ir   

    imprime_desconto(salario_bruto, desc_sindicato, ir, fgts, salario_liquido)

def imprime_desconto(salario_bruto, desc_sindicato, ir, fgts, salario_liquido):
    print('''
    Salario Bruto: %.2f
    Desconto Sindicato: %.2f
    Desconto IR: %.2f
    FGTS: %.2f
    
    Salario Liquido: %.2f
    '''%(salario_bruto, desc_sindicato, ir, fgts, salario_liquido))

descontos(salario_bruto)