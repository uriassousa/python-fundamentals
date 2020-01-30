# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
# importa modulo math
import math

#n1 = 2 * 2
#n2 = 2 * 3

#num = float(input("Entre com um número:\n"))
#raiz = math.sqrt(num)
#print('A raiz quadrada de {num} é {raiz}'.format(n1, n2))
#print(f'\nA raiz quadrada de {num} é {raiz}\n')
#print('A multicação do primeiro numero é {} e a segunda é {}'.format(n1, n2))

#num = float(input("Entre com um número:"))
#raiz = math.sqrt(num)
#print('A raiz quadrada de {num} é {raiz}'.format(n1, n2))
#print('A raiz quadrada de {} é {}!'.format(num, raiz))
#print('A multicação do primeiro numero é {} e a segunda é {}'.format(n1, n2))

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:2f}.'.format(n, t, n, r))