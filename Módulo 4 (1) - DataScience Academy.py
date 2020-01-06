# Neste módulo serão apresentadas as funções built-in, tratamento de arquivos e bibliotecas.

# Algumas funções built-ins no python que oferece a possibilidade de acessar arquivos são:
'''Métodos
open() - Usada para abrir um arquivo
read() - Litura de um arquivo
write() - Gravação no arquivo
seek() - Retornar para início do arquivo
readlines() - Lê o arquivo linha à linha
close() - fecha o arquivo'''


arq1 = open('modulo4.txt', 'r') # nome do arquivo e o modo de acesso, 'r' significa modo leitura. Caso a arquivo este ja em alguma pasta diferente, digitar nome da pasta '/' e noem do arquivo ou caminho completo
print(arq1.read()) #lê as linhas do arquivo
print(arq1.tell()) #Conta o número de caracteres de um arquivo
print(arq1.seek(0, 0)) #retorna para coordenadas do arquivo, no caso linha 0 e coluna 0
print(arq1.read(10)) #Ler os primeiros 10 caracteres (bara de espaço conta)

#Abrindo arquivo para escrita:
arq2 = open('modulo4.txt', 'w') #não é possível usar o método read() neste módo, para abrir para leitura e escrita usar 'r', e 'w'. Um arquivo aberto para escrita não precisa ser criaod previamente, o python o cria
arq2.write('Testando gravação em python') #escrevendo esta linha
arq2.close #fechando arquivo

#lendo arquivo gravado
arq2 = open('modulo4.txt', 'r')
print(arq2.read())

#Acrescentando conteúdo
arq2 = open('modulo4.txt', 'a')# 'a' de apppend (desta forma toda vez que o programar rodar ele vai adicionar o .write() no txt, ficando cada vez maior, caos eu quero sobescrever o que ja existe no .txt, abrir em formato 'w'
arq2.write(' Acrescentando conteúdo')
arq2.close() # é necessário fechar e abrir no modo leitura.
arq2 = open('modulo4.txt', 'r')
print(arq2.read())
arq2.seek(0,0) #voltar para ler arquivo do inicio
print(arq2.read())

#Automatizando o processo de gravação:
filename = input('Digite o nome do arquivo: ') #consigo criar um arquivo com este comando, na pasta do programa
filename = filename + '.txt' #irá transformar a string digitada em uma rquivo com extensão txt
arq3 = open(filename, 'w') #abrir para edição
arq3.write(input('Digite seu texto')) #posso digitar um texto e adiciona-lo noa rquivo criado
arq3.close()

arq3 = open(filename, 'r')
print(arq3.read())
arq3.close()

#Abrindo dataset (arquivo csv)
f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n') #dividindo-o baseado em algum critério, neste caso no enter (\n)
print(rows)

f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n') #separar por linha novamente
full_data = [] #criar lista vazia
for row in rows: #esse comando ira percorrer linahs na variável rows
    split_row = row.split(',') #percorrendo a linha o split vai separar as strings a cada virgula
    full_data.append(split_row) #estou adicionando na lista 'full_data' cada fragmento separado pelo split
    print(full_data)

#Contando as linhas do documento csv
f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n') #separar por linha novamente
full_data = [] #criar lista vazia
for row in rows: #esse comando ira percorrer a linha
    split_row = row.split(',')
    full_data.append(split_row) # criar as colunas na lista
count = 0 #será usado para contar as linhas
for row in full_data: # percorrerrá cada linha na lista
    count += 1 # para cada linha percorrida em full data o count adicionara 1 a ele mesmo
print(count)

# Também é possível contar as colunas:
f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0] #first row representa a primeira indexação de indice 0, esta sendo pego uma linha e contabilizando quantas colunas existem nela
count = 0 #este count vai contabilizar as indexações
for colmumn in first_row:
    count = count + 1
print(count)

# usar dois comandos .read(), os egundo já estará no final do arquivo e não irá ler nada

# Importando datasets do PANDAS, um dos muitos pacotes da linguagem python para manipulação de arquivos. Este pacote ja vem no anaconda, é um tipo de excel para o python
import pandas as pd #estou chamando o pandas de pd para simplificar, o 'as' apelida a biblioteca
file_name = 'binary.csv'
df = pd.read_csv(file_name) #estou lendo uma rquivo csv através do panda, entre os parentes a variavel do arquivo aberto na linha acima
print(df.head()) #imprimir apenas as primeira linhas do arquivo (a cabeça do arquivo)

file_name2 = 'salarios.csv'
df1 = pd.read_csv(file_name2)
print(df1.head())

# O pandas ja separou o arquivo em linhas e colunas, possuindo diversas ferramentas uteis para modificação

# Agora vamos modificar arquivos txt da seguinte forma:
# 1) Criando strings
texto = 'Cientista de dados é uma profissão que cresce bastante em todo mundo.'
texto = texto + ' Estes profissionais precisam se especializar em programação, Estatística e Machine leraning'

# 2) Criando um arquivo
arquivo = open('cientista.txt', 'w')

# 3) Criando um adicionador da string no arquivo txt
for palavras in texto.split(): #essa linha ira contar os elementos chamados de variavel 'palavra' no texto separada pelo split
    arquivo.write(palavras + ' ') #essa linha irá escrever cada elemento do split no arquivo, separando-os por espaço destacado por ' '
arquivo.close #precisa fechar o arquivo para ler depois

arquivo = open('cientista.txt', 'r')
conteúdo = arquivo.read() #preciso mandar o arquivo ser lido, não da para simplesmente printar o arquivo
arquivo.close()
print(conteúdo)

# Outra função útil é 'with' que significa 'com', detsa forma podemos ler um arquivo de forma simplificada como:
with open('cientista.txt', 'r') as arquivo: #siginifica: com o arquivo cientistia.txt aberto como a variável 'arquivo'
    conteúdo = arquivo.read() # ... faça leitura do 'arquivo' e grave em 'conteúdo'
print(conteúdo)

#Ferramentas de slicing tbm podem se mostrar úteis desta forma:
with open('cientista.txt', 'w') as arquivo:
    arquivo.write(conteúdo[:21])
    arquivo.write('\n')
    arquivo.write(conteúdo[:33])
arquivo.close() #não esquecer de fechar o arquivo e abri-lo novamente para leitura

with open('cientista.txt' , 'r') as arquivo:
    conteúdo = arquivo.read()
print(conteúdo)

'''Modificando arquivos do escell (csv). São arquivos separados por virgula por definição, onde as colunas são separadas pelas próprias, para lidar com estes tipos de arquivos em python
temos o pacote csv que pode ser baixado. Esta biblioteca possui alguns comandos diferentes e adicionais como será mostrado logo abaixo'''

import csv #importando a biblioteca csv
with open('numeros.csv', 'w') as arquivo1:
    escreva = csv.writer(arquivo1) #variável que representará algo que será escrito no arquivo1, neste módulo usamos csv.writer como comando
    escreva.writerow(('Primeiro', 'Segundo', 'Terceiro')) #comando que ira criar uma linha com estes elementos, a virgula irá separa-los em colunas
    escreva.writerow(('1', '2', '3')) #obs, usa-se dois parenteses nestes comandos
    escreva.writerow(( 10, 20, 30))
arquivo1.close

#leitura do arquivo acima:
with open('numeros.csv', 'r') as arquivo1:
    leitor = csv.reader(arquivo1) #comando para o pacote csv ser lido
    for x in leitor: #preciso utilizar este loop para percorrer as linhas e usar a variavel no print para vizualizar
        print(x)

#transformando os dados em uma lista
with open('numeros.csv', 'r') as arquivo1:
    leitor = csv.reader(arquivo1)
    lista = list(leitor) #transformando a variavel leitor em uma lista, é útil para modificar um conteúdo dentro de uma lista, podendo percorrer a lista com um loop 'for'
print(lista)

for linha in lista[1:]: #utilizando a lista'dados' que foi criada posso começar a leitura do loop 'for' a partir da indexação que eu escolher, nesse caso 1
    print(linha) #neste caso sós erão printados o 2 e o 3 elemento da lista que são ['1', '2', '3'] e ['10', '20', '30']. Isso por que leitor ja eram 3 listas, e a lista virou uma lista de listas



# Funções built-in (MAP)
'''Podemos dizer que programação funcional é uma programação direcionada à expressão, diferentemente a programação orientada a objetos. Algumas delas são map, reduce, filter, lambda e list comprehension.
MAP é uma função que recebe dois argumentos, uma função e uma sequência, a função map aplica a função que recebeu a cada item em um objeto iteravel (como uma lista) retornando uma lista com todos os resultados. O primeiro argumento será o nome
de uma função. MAP aplica a função recebida como parâmetro a todos elementos de uma sequência. Uma nova lista é gerada. Exemplo:'''

def farenheit (T):
    return ((float(9)/5) * T + 32)
def celsius (C):
    return (float(5)/9) * (T - 32)
#criar lista
temperaturas = [0, 22.5 , 40, 100]

#aplicando MAP
a = map(farenheit, temperaturas) #será aplicada a função 'farenheit' a cada elemento da sequencia 'temperaturas', esta função retorna o iterator e não o resultado, então preciso converter o resultado em lista
b = list(a) #posso colocar a função lista antes da map tbm
print(b)

#Também é possível criar um loop for:
for temp in map(farenheit, temperaturas):
    print(temp)

#também podemos fazer a mesma operação em lambda:
l = list(map(lambda x: (5.0/9) * (x - 32), temperaturas)) #usando a formula para conversão em graus célsius
print(l)

#somando elementos de mais de uma lista
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = list(map(lambda x, y: x + y, a, b)) #somando o valor da primeira lista com seu correspondente na segunda lista
print(c)

'''Além da função map, tbm temos a função reduce, que recebe dois argumentos (função, sequencia) e aplcia a função aos elementos da sequencia até que reste apenas um elemento, é bastante
útil para operações em que precisamos ir encontrando novos caminhos a partir de outros dois ja utilizados, como:

40 + 30 + 20 + 10
40 + 30 = 70
70 + 20 = 90
90 + 10 = 100

Embora seja built-in, deve ser importada do pacote functools'''

from functools import reduce
lista = [47, 11, 42, 13]
def soma(a,b):
    x = a + b
    return x

a = reduce(soma, lista)
print(a)

#criando o memso com lambda
b = reduce(lambda x,y: x + y, lista)
print(b)

#Podemos atribuir a expressão lambda a uma variavel como:
m = lambda a,b: a if (a>b) else b #isto é uma função com a expressão lambda onde, se a foir maior que b, retornará A, se não, B
n = reduce(m, lista) # sairá comparado o primeiro e o segundo elemento até sobrar apenas um
print(m) #criamos a expressão 'm' para ser utiliada na lista pela função reduce, irá retornar apenas o maior elemento devido a especificação em lambda

'''Além de MPA e REDUCE, temos tbm a função FILTER. Recebe dois argumentos, uma função e uma sequência filter(função, sequência). Ela oferece uma maneira de fitrar todos os elementos de uma sequência
, para os quais a função retorne TRUE. A função passada para filter deve retornar um valor booliano, ela será aplicada a todos os valores de uma sequência e os valores serão retornados, apenas se
retornarem como TRUE para a função.'''

def verificaPAR(num):
    if num % 2 == 0:
        return True
    else:
        return False
verificaPAR(35) #verificando para apenas um elemento

#verificando para vários elementos
lista = [1, 2, 3, 4,5 ,6 ,7 ,8 ,9]
a = list(filter(verificaPAR, lista)) #precisamos tbm converter o resultado em lista, por isso antes de filter usar list

#listar apenas os pares usando lambda:
b = list(filter(lambda x: x % 2 == 0, lista))

#List Comprehension
'''Aplica uma expressão arbitraria (ao invés de aplicar apenas uma função) a uma sequência de elementos. Permite desenvolver listas uando uma notação diferente
sendo essencialmente uma linha de loop for dentro de colchetes.

lst = [x for x in 'sequência']

Normalmente usamos loop for quando trabalhamos com a função map, e list comprehension quando for mais facil de ser aplicada
porém, list comprehension possui vantagem de desempenho.
'''

lst = [x for x in 'Python']
print(lst) #retorna uma lista separando cada letra da string em um elemento

#usando em operações
lst1 = [x ** 2 for x in range(1, 10)] #usei range para criar uma sequencia de 10 elementos
print(lst1)

#operações mais complexas
lst2 = [x for x in range(1, 10) if x % 2 == 0] #só retorna os números pares( um condicional if adicionada)

#usando para converter valores de graus celsius em farenheit
celsius = [10, 34, 104, 59, 70]
farenheit = [((float(9)/5) * temp + 32) for temp in celsius]
print(farenheit)

#também é possível fazer estas listas dentro de outras

#Função zip() e enumerate()
'''A função zip() agrega os valores de duas sequências e retorna uma tupla zip(sequncia, sequencia). Pode ser usada se o numero de elementos for diferente em cada sequencia
mas o objeto resultante terá o mesmo número de elementos da sequência menor:

zip([1, 2, 3 ,4], [1, 2, 3]
[(1,1) (2,2) (3,3)] #as tuplas retornadas estarão dentro de uma lista

São pareados os primeiros elementos de cada sequência seguido dos segundos e assim sucesisvamente,não necessariamente serão pareados
elementos iguais entre si.

Já a função enumarate() permite retornar o indice de cada valor em uma sequencia, à medida que você percorre toda a sequencia, ele retorna
uma tupla no formato tupla(indice, valor), ela recebe apenas o parametro 'sequencia'.'''

x = [1, 2 , 3]
y = [4, 5, 6]
lst = list(zip(x,y))
print(lst)

#Zip pode ser usada em dicionários tbm
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
dic = list(zip(d1,d2)) #as uniões serão pelas chaves, para unir valores deve-se usar:
dic = lst(zip(d1, d2.values())) #chaves de d1 + valores de d2, podendo mudar estes retornos da forma que eu achara melhor

'''A função enumerate() irá nos informar o indice dos elementos de uma sequencia, funciona da seguinte forma:'''
seq = ['a', 'b', 'c']
a = list(enumerate(seq))
print(a) #o retorno serão tuplas, porém, o índice seguido do elemento.

#utilizando o loop for:
for indice, valor in enumerate(seq): #estou dando a cada indice a variavel de memso nome, e a cada elemento a variavel valor
    print(indice, valor)

#Vizualizando os indices de uma string
string = 'Olá Mundo'
for i, element in enumerate(string):
    print(i, element)






