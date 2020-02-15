import psycopg2

try:
    con = psycopg2.connect("host=localhost \
                        dbname=projeto \
                        user=admin \
                        password=4linux ")

    cur = con.cursor()

    cur.execute("insert into scripts(nome,conteudo) values ('testetry.py','Test de comexao ao banco')")

    con.commit()

except Exception as e:
    print('Erro: {}'.format())
    print('Fazendo rollback')
    con.rollback()

finally:
    print('Finalizando conexao com o banco de dados')
    cur.close()
    con.close()
