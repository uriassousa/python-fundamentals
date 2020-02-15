# Faça um sistema de login

usuarios = ['Caio', 'Felipe', 'Manuela', 'Paula', 'Daniel', ]

# Se o usuário digitado estiver na lista de usuários
#    imprima acesso permitido


# se nao
#     imprima acesso negado
#     e peça para mostrar acesso negado.

# while True:
#     try:
#         nome = input('Digite seu nome: ')
#         if nome in usuarios:
#            print('Acesso Permitido!')
#            break

#         else:
#             raise NameError('O usuario {} é negado no sistema!'.format(nome))

#     except NameError as n:
#         print(n)
#         continue

while True:
    try:
        login = input('Login: ')

        if login.capitalize() not in usuarios:
            raise NameError ('Acesso negado! Digite novamnete: ')
            continue

        else:
            print('Acesso permitido!')
            break

    except NameError as n:
        print(n)