from sqlalchemy import select
from core import user_table

def seleciona_dados(dado):
    selecionar = select([user_table]).where(user_table.c.nome == dado)
    print([x for x in slecionar.execute()])

    l = [v for v in range(1, 100)]

    print(l)