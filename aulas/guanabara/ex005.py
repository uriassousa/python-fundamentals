#Exercicio Python Guanabara 005
# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Dgite um número: '))
#a = n - 1 
#s = n + 1
#print('Analisando o valor {}, seu antecessor é {}, e o seu sucessor é {}'.format(n, a, s))
print('Analisando o valor {}, seu antecessor é {}, e o seu sucessor é {}'.format(n, (n-1), (n+1)))