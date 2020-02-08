#  itens = []
#  for item in range (1,101):
#      itens.append(item)

# print(itens)

# Lacos de repeticao

# frutas = ['Abacaxi', 'banana', 'Caju']

# t = enumerate(frutas)
# for i, f in t:
#     if 

# carros = ['gol', 'fox', 'camaro', 'fusca', 'brasilia', 'corcel', 'variant']
# cores = ['azul', 'verde', 'lilas', 'verde', 'laraja', 'limao', 'vermlho']

# for carro in carros:
#     for cor in cores:
#         print(carros, cores)


# try:
#     nome = int(input('Digite seu nome: '))
#     if nome == 'Renato':
# #         print(nome)

# # except NameError:
# #     print('Variável nao existe')

# # except ValueError:
# #     print('Valor nao numeral')

# while True:
#     try:
#         x = int(input('Digite o primeiro valor: '))
#         y = int(input('Digite o segundo valor: '))
#         print(x + y)
#         break

#     except TypeError:
#         print('digite apenas números')

# while True:
# try:
#     x = int(input('Digite o primeiro valor: '))
#     y = int(input('Digite o segundo valor: '))
#     print(x + y)
    
# except TypeError:
#     print('digite apenas números')

# finally:
#     print('Saindo do try/except')

# blacklist = ['daniel', 'camila']

# try:
#     nome = input('Digite seu nome: ')
#     print(nome)
#     if nome in blacklist:
#         raise NameError('Usuario bloqueado')
# except NameError as n:
#     print(n)
#with open('arquivo.txt', 'r') as f:
with open('arquivo.txt', 'r') as f:
    print(f.read())
    #f.seek(10)
    #f.write('Novo arquivo txt  \n Teste \n teste2 \n teste3 \n para adicao de conteudo relacionando ao curso de python. OK ok?')

