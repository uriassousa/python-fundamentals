# import psycopg2

# try:
#     con = psycopg2.connect("host=localhost \
#                             dbname=projeto \
#                             user=admin \
#                             password=4linu")

#     cur = con.cursor()
#     print(cur)
#     cur.execute(
#         "insert into s(nome,conteudo) values ('testetry.py', 'teste de tratamentos de exceções')")


#     con.commit()

# except Exception as e:
#     print('Erro: {}'.format(e))
#     print('Fazendo rollback')
#     con.rollback()


# finally:
#     print('Finalizando conexao com o banco de dados')

#     cur.close()
#     con.close()


from pymongo import MongoClient

client = MongoClient('127.0.0.1')
db = client['dexterops']
teste = MongoClient()


def inserir_dados():
    try:

        db.fila.insert({"_id": 1, "empresa": "4linux",
                        "cursos": [{"nome": "python fundamentals",
                                    "carga horaria": 40},
                                   {"nome": "linux fundamentals",
                                    "carga horaria": 40}]})
    except Exception as e:
        print('Erro: {}'.format(e))


def buscar_dados():
    for r in db.fila.find():
        print('Empresa'.format(r['empresa']))
        for c in r['cursos']:
            print(20*'=')
            print('Nome: {} \n Carga Horaria: {}'.format(c['nome'],c['carga horaria']))

buscar_dados()

def adicionar_sub():
    db.fila.update({"_id":1},{'instrutores':{'nome':'Maria'}})
dic = {'chave':'valor','chave2':[{'chave3':'valor3'},{'chave4':'valor4'}]}
print(dic['chave2'][0])







        