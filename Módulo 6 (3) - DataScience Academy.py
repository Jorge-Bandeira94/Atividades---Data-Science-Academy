# Importamos o Módulo PyMongo
import pymongo

# Criando a conexão com o MongoDB (neste caso, conexão padrão)
# Neste caso não está sendo utilizado os parâmetros como LocalHost e a porta 27, o Mongo Já as adota como padrão
client_con = pymongo.MongoClient()

# Listando os bancos de dados disponíveis
# Irá aparecer o cadastrodb criado anteriormente e os padrões 'admin', 'config' e 'local'
print(client_con.database_names())

# Definindo o objeto db para conectar especificamente ao banco cadastrodb
db = client_con.cadastrodb

# Listando as coleções disponíveis, irá aparecer somente 'posts' criado anteriormente
print(db.collection_names())

# Criando uma nova coleção
db.create_collection("mycollection")

# Listando as coleções disponíveis
print(db.collection_names())

# Inserindo um documento na coleção criada
# Lembrar que insert_one é uma função para inserir as informações no db
db.mycollection.insert_one({
   'titulo': 'MongoDB com Python',
   'descricao': 'MongoDB é um Banco de Dados NoSQL',
   'by': 'Data Science Academy',
   'url': 'http://www.datascienceacademy.com.br',
   'tags': ['mongodb', 'database', 'NoSQL'],
   'likes': 100
})

# Retornando o documento criado
print(db.mycollection.find_one())

# Preparando um novo documento
doc1 = {"Nome":"Donald","sobrenome":"Trump","twitter":"@POTUS"}

# Inserindo um novo documento
db.mycollection.insert_one(doc1)

# Preparando um novo documento novamente
doc2 = {"Site":"http://www.datascienceacademy.com.br",
        "facebook":"facebook.com/dsacademybr"}

# Inserindo um novo documento novamente
db.mycollection.insert_one(doc2)

# Retornando os documentos na coleção
for rec in db.mycollection.find():
    print(rec)

# Conectando a uma coleção
# Assim como slicing, o [] irá designar o db nas coleções
col = db["mycollection"]
print(type(col))

# Contando os documentos em uma coleção
print(col.count())

# Encontrando um único documento
redoc = col.find_one()
print(redoc)