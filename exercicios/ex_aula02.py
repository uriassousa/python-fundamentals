# -*- coding: utf-8 -*-

dados = {
    'estados': {
        'sp': {
            'nome': 'Sao Paulo',
            'municipios': 645,
            'populacao': 44.04

        },
        'rj':{
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72

        },
        'mg': {
            'nome': 'Minas Geais',
            'municipios': 31,
            'populacao': 20.87

        }
    }
}

#Imprima as seguintes informações:

# 1 - nome dos estados
# 2 - nome dos estados e sua popupação em milhoes
# 3 - nome dos estados e quantdade de municipios

#print(dados['estados']['sp']['nome'],dados['estados']['rj']['nome'],dados['estados']['mg']['nome'])
#print(dados['estados']['rj']['nome'])
#print(dados['estados']['mg']['nome'])

#print(dados['estados']['sp']['nome']['populacao'],dados['estados']['rj']['nome']['populacaco'],dados['estados']['mg']['populacao'])

#print(dados['estados']['sp']['populacao'],dados['estados']['rj']['populacao'],dados['estados']['mg']['populacao'])

#print(dados['estados']['sp']['municipios'],dados['estados']['rj']['municipios'],dados['estados']['mg']['municipios'])

nomesp = dados['estados']['sp']['nome']
nomerj = dados['estados']['rj']['nome']
nomemg = dados['estados']['mg']['nome']

# print('Nome dos Estados: {2} {1} {0}'.format(nomesp, nomerj, nomemg))

popsp = 44.00 * 1000000

print('Nome do estado é {}\n e a população é {:.2f}'.format(nomesp, popsp))

