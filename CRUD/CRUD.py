import MySQLdb


'''
Projeto final do curso Python MySQL, CRUD usando alunos e cursos
'''

host = "localhost"
user = "aplicacao"
password = "12345"
db = "escola_curso"
port = 3306

connection = MySQLdb.connect(host,user,password,db,port)
#c = con.cursor() #resultado tupla de tuplas
c = connection.cursor(MySQLdb.cursors.DictCursor) #resultado é uma tupla de dicionario

def select(campos, tables, where=None):
    global c
    query = "select "+ campos + " from " + tables
    if(where):
        query = query + " where "+ where 
    c.execute(query)
    return c.fetchall()

def insert(values, table, campos=None):
    global c, connection

    query = "insert into "+ table 
    if(campos):
        query = query + " ("+campos+") "
 
    query = query+ " values" + ",".join(["("+ v + ")" for v in values]) 
    
    c.execute(query)
    connection.commit() #garante que a query executada faça o comando pedido

def update(table, sets, where = None):
    global c, connection
    query = "update "+ table
    query = query + " set "+ ",".join([field +" = '"+ value +"'" for field, value in sets.items()])
    if(where):
        query = query + " where "+ where 

    c.execute(query)
    connection.commit()

def delete(table, where):
    global c,connection
    query = "delete from "+ table + " where " + where

    c.execute(query)
    connection.commit()

# sets = {"nome": "Rodrigo", "cpf" : '08812389'}
# update("alunos", sets, "idAluno = 14")
# values = [
#     "default, 'Joao Pedro', '2000-02-02', 'Av. Rio Branco', 12345667890",
#     "default, 'Maria Pedro', '2000-02-02', 'Av. Rio Branco', 10345667890"]

#insert(values, "alunos")

# delete("alunos", "nome = 'Joao Pedro'")

result = select("*", "alunos", "nome = 'Rodrigo'")
# result = select("nome,cpf", "alunos")
print(result)
