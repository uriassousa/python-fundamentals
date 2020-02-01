# # # # # # # -*- coding: utf-8 -*-

# # # # # # dados = {
# # # # # #     'estados': {
# # # # # #         'sp': {
# # # # # #             'nome': 'Sao Paulo',
# # # # # #             'municipios': 645,
# # # # # #             'populacao': 44.04

# # # # # #         },
# # # # # #         'rj':{
# # # # # #             'nome': 'Rio de Janeiro',
# # # # # #             'municipios': 92,
# # # # # #             'populacao': 16.72

# # # # # #         },
# # # # # #         'mg': {
# # # # # #             'nome': 'Minas Geais',
# # # # # #             'municipios': 31,
# # # # # #             'populacao': 20.87

# # # # # #         }
# # # # # #     }
# # # # # # }

# # # # # # #Imprima as seguintes informações:

# # # # # # # 1 - nome dos estados
# # # # # # # 2 - nome dos estados e sua popupação em milhoes
# # # # # # # 3 - nome dos estados e quantdade de municipios

# # # # # # #print(dados['estados']['sp']['nome'],dados['estados']['rj']['nome'],dados['estados']['mg']['nome'])
# # # # # # #print(dados['estados']['rj']['nome'])
# # # # # # #print(dados['estados']['mg']['nome'])

# # # # # # #print(dados['estados']['sp']['nome']['populacao'],dados['estados']['rj']['nome']['populacaco'],dados['estados']['mg']['populacao'])

# # # # # # #print(dados['estados']['sp']['populacao'],dados['estados']['rj']['populacao'],dados['estados']['mg']['populacao'])

# # # # # # #print(dados['estados']['sp']['municipios'],dados['estados']['rj']['municipios'],dados['estados']['mg']['municipios'])

# # # # # # nomesp = dados['estados']['sp']['nome']
# # # # # # nomerj = dados['estados']['rj']['nome']
# # # # # # nomemg = dados['estados']['mg']['nome']

# # # # # # # print('Nome dos Estados: {2} {1} {0}'.format(nomesp, nomerj, nomemg))

# # # # # # popsp = 44.00 * 1000000
# # # # # # #munsp = float(input('Entre com o número de municipio: '))
# # # # # # munsp = 92.00

# # # # # # #print('Nome do estado é {}\n e a população é {:.2f}'.format(nomesp, popsp))

# # # # # # print('O nome do Estado {} e o múmero de municipio {}'.format(nomesp, munsp))


# # # # # idade = int(input('Digite dua idade; '))

# # # # # habilitacao = int(input('Possui Habilitação:\n1- Para Sim\n2- Para Não '))

# # # # # if idade >= 18 and habilitacao == 1:
# # # # #     print('Você pode dirigir')
# # # # # else:
# # # # #     print('Você não pode dirigir')


# # # # frutas = ['caju', 'banana', 'limao', 'uva']

# # # # if 'laranja' in frutas:
# # # #     print('Essa lista nao tem laranja')

# # # # else:
# # # #     print('Se na lista existir pera, imprima')

# # # lista = ['rafael', 'camila', 'paulo', 'pamela']

# # # if 'camila' in lista:
# # #     print('Acesso permitido')

# # # else:
# # #     print('Acesso negado')

# # listanum = 8, 12, 20, 234

# # if 233 in listanum:
# #     print('Este número existe na lista')

# # else:
# #     print('Este número não existe na lista')

# num = int(input('Digite um número: '))

# if(num<=10):
#     print('O número é menor')

# else:
#     if(num>=15):
#         print('Esse numero é maior')

#     else:
#         print('Não deu match')

