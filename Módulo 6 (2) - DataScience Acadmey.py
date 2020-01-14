# Criando um banco de dados MongoDB

from pymongo import MongoClient
import datetime

# Estabelecemos a conexão ao Banco de Dados
conn = MongoClient('localhost', 27017)
print(type(conn))

# Uma única instância do MongoDB pode suportar diversos bancos de dados.
# Vamos criar o banco de dados cadastrodb
db = conn.cadastrodb
print(type(db))

# Uma coleção é um grupo de documentos armazenados no MongoDB
# (relativamente parecido com o conceito de tabelas em bancos relacionais)
# Cadastrodb é o nome do banco de dados dentro do banco db
collection = db.cadastrodb
print(type(collection))

# Uma nota importante sobre coleções (e bancos de dados) no MongoDB é que eles são criados posteriormente - nenhum dos
# comandos acima executou efetivamente qualquer operação no servidor MongoDB. Coleções e bancos de dados são criados
# quando o primeiro documento é inserido. Tudo acima são definições.

# Dados no MongoDB são representados (e armazenados) usando documentos JSON (Java Script Object Notation). Com o PyMongo
# usamos dicionários para representar documentos.
post1 = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp", "consul", "electrolux"],
        "data_cadastro": datetime.datetime.utcnow()}

print(type(post1))

# Comando para habilitar a inserção de dados no db
collection = db.posts

# Comando para inserir informação específica, no caso, o dicionário de post1
post_id = collection.insert_one(post1)
print(post_id.inserted_id)


# Quando um documento é inserido uma chave especial, "_id", é adicionada
# automaticamente se o documento ainda não contém uma chave "_id".
post2 = {"codigo": "ID-2209876",
        "prod_name": "Televisor",
        "marcas": ["samsung", "panasonic", "lg"],
        "data_cadastro": datetime.datetime.utcnow()}

collection = db.posts
post_id = collection.insert_one(post2).inserted_id
print(post_id)

# A função find() retorna um cursor e podemos então navegar pelos dados
collection.find_one({"prod_name": "Televisor"})
for post in collection.find():
    print(post)

# Verificando o nome do banco de dados
print(db.name)

# Listando as coleções disponíveis
print(db.collection_names())