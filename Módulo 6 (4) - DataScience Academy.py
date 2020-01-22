# Importando o módulo de acesso ao SQLite
import sqlite3
import random     # Importando a biblioteca de randomização
import time       # Importando o módulo time
import datetime
import os

# Reemove o arquivo com o banco de dados SQLite (caso exista)
os.remove(r'c:\Users\55819\Desktop\PythonFundamentos-master\Cap06\escola.db') if os.path.exists(r'c:\Users\55819\Desktop\PythonFundamentos-master\Cap06\escola.db') else None


# Cria uma conexão com o banco de dados.
# Se o banco de dados não existir, ele é criado neste momento.
# Para criar o arquivo em um diretório específico, colocar o caminho entre as '' de forma: (r'c:\users\desktop\escola.db')
con = sqlite3.connect(r'c:\Users\55819\Desktop\PythonFundamentos-master\Cap06\escola.db')

# Verificar o tpo do objeto, a resposta me mostra a biblioteca utilizada e se estará ativa
print(type(con))

# Criando um cursor
# Um cursor permite percorrer todos os registros em um conjunto de dados e é utilizado em varios momentos para adicionar ou remover dados
cur = con.cursor()

# Cria uma instrução sql
# Esta varíável é uma string de função SQL create
# Primeira coluna da tabela, chave primária
# Segunda coluna, vachar é designo do tipo caracter
# terceira coluna, vachar é designo do tipo caracter
sql_create = 'create table cursos '\
'(id integer primary key, '\
'titulo varchar(100), '\
'categoria varchar(140))'

# Executando a instrução sql no cursor. Desta forma a tabela foi criada, agora é necessário inserir os dados
cur.execute(sql_create)

# Criando outra sentença SQL para inserir registros, insert, into e values são palavras chaves de intrução enquanto cursos é uma tabela do banco
# Entre os parenteses serão colocados dados de algum objeto
sql_insert = 'insert into cursos values (?, ?, ?)'

# Dados que serão adicionados dentro dos parênteses do objeto acima
recset = [(1000, 'Ciência de Dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Análise de Dados')]

# Inserindo os registros. Para cada registro em meu conjunto de registros eu executo sql_insert deste registro no banco de dados cur.execute
for rec in recset:
    cur.execute(sql_insert, rec)

# Grava a transação, se a tabela for fechada antes disso os dados se perdem. con é a variável que representa a tabela criada anteriormente
con.commit()

# Criando outra sentença SQL para selecionar registros, neste caso o objeto sql_select terá sempre a ação de selecioanr da tabela cursos
sql_select = 'select * from cursos'

# Seleciona todos os registros e recupera os registros (sempre usando a conexão com o banco de dador, o objeto 'cur')
cur.execute(sql_select)   # é necessário usar o execute novamente para fazer a seleção, ou qualquer outro comando, aqui ele selecionou todos os registros da tabela 'curso'
dados = cur.fetchall()    # aqui ele salvou no objeto 'dados' os registros através do método fetchall()

# Mostra todos os registros selecionados da tabela 'curso', para cada linhas o iterador plotou os dados no locals das %
for linha in dados:
    print('Curso Id: {}, Título: {}, Categoria: {} \n'.format(linha[0], linha[1], linha[2]))
print(20 * '-=-=')

# Gerando outros registros
# Estou usando o objeto recset novamente, mas os registros anteriores ja estão gravados no banco de dados.
recset = [(1003, 'Gestão de Dados com MongoDB', 'Big Data'),
          (1004, 'R Fundamentos', 'Análise de Dados')]

# Inserindo os registros no banco
for rec in recset:
    cur.execute(sql_insert, rec)

# Gravando a transação
con.commit()

# Seleciona todos os registros
cur.execute('select * from cursos')

# Recupera os resultados
recset = cur.fetchall()

# Mostra
for rec in recset:
    print('Curso Id: {}, Título: {}, Categoria: {} \n'.format(rec[0], rec[1], rec[2]))

# Fecha a conexão
con.close()

'''================================================================================================================'''

# Comando INSERT

# Criando uma conexão
os.remove("dsa.db") if os.path.exists("dsa.db") else None
conn = sqlite3.connect('dsa.db')

# Criando um cursor
c = conn.cursor()

# Função para criar uma tabela
# A tabela só será criada se não existir, como especifica o comando em c.execute. Sera feita uma chave primária ID e serão gerados aotomaticamente valores de valor não nulo
# date será uma coluna do tipo texto, prod_name também e valor do tipo REAL
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)')

# Função para inserir uma linha. Em c.execute não estão sendo passados variáveis mas valores diretos
def data_insert():
    c.execute("INSERT INTO produtos VALUES(10, '2018-05-02 14:32:11', 'Teclado', 90)")
    conn.commit()

def data_close():
    c.close()
    conn.close()

# Usando variáveis para inserir dados
def data_insert_var():
    new_date = datetime.datetime.now()  # Inserindo a data e hora atual no objeto new_date
    new_prod_name = 'Monitor'
    new_valor = random.randrange(50,100)

    # Em c.execute estão sendo substituídos os valores nas colunas date, prod_name e valor pelos valores das novas variáveis, ao executar este método o comando irá substituir os dados automaticamente
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_prod_name, new_valor))
    conn.commit()

# Criando a tabela e inserindo os dados
create_table()
data_insert()

# Observando os dados na tabela
c.execute('select * from produtos')
fetch = c.fetchall()
for i in fetch:
    print(i)

# Gerando valores aleatórios e inserindo na tabela
for i in range(10):     # Serão inseridos 10 registros na tabela
    data_insert_var()   # Método randômico
    time.sleep(0.1)     # Será executado o comando a cada um décimo de segundo

# Observando os novos dados gerados
c.execute('select * from produtos')
fetch1 = c.fetchall()
for i in fetch1:
    print(i)

# Encerrando a operação
data_close()

'''================================================================================================================'''

