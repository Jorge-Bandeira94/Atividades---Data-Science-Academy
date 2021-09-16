# A função MAP é utilizada para aplicar uma função A em um elemento iteravel B
# Primeiro vamos criar duas funções
def farenheit(T):
    return ((float(9)/5) * T +32)

def celsius(C):
    return (float(5)/9) * (C -32)

temperaturas = [0, 22.5, 40, 100]

# Aplicando a função map com as funções para iterar cada elemento da lista, para receber o output preciso converter a
# variavel que recebe map em algo, nesse caso, numa lista, se não o print vai informar o que é um map ao invés do que
# ele contém. Nesse caso, o parametro T ou C nas defs foram modificados por cada elemento da lista temperaturas
a = map(farenheit, temperaturas)
print(list(a))
b = map(celsius, temperaturas)
print(list(b))

# Podemos printar esses valores tambe´m com um for em vez de uma lista
for item in map(farenheit, temperaturas):
    print(item)

# Lambda também pode ser utilizado nestes casos, aqui informamos a variavel mutavel em labda "T" e damos a função após os
# dois pontos. o labda + a função são o primeiro item do map(), e a temperatura é o segundo item (a virgula separa)
c = list(map(lambda T : (9/5.0) * T +32, temperaturas))
print(c)

# Podemos usar o lambda também para interagir com listas como somar elementos. Nste caso, somamos o valor de d com e.
# Neste caso, map usa como iteraveis dois elementos, "d" e "e".
d = [1, 2, 3]
e = [4, 5, 6]

dr = map(lambda x, y: x+y, d, e)
print(list(dr))

d1 = [1, 2, 3]
e1 = [4, 5, 6]
f1 = [7, 8, 9]

fr = map(lambda x, y, z: x+y+z, d1, e1, f1)
print(list(fr))

# A função reduce recebe 2 argumentos, uma função e uma sequencia (como uma lista). Ao contrario de map que aplica a
# função a cada elemento da sequencia, reduce aplica a função a cada um até que reste um último. Por exemplo, na soma das
# listas acima, seria retornado apenas a soma de todos os valores ao inves dos valores x, valores y, e valores z
# As funções do reduce precisam ser importadas do functools

from functools import reduce

lista = [47, 11, 42, 13]

def soma(x, y):
    return (x + y)

print(reduce(soma, lista))

# Testando com lambda

re = reduce(lambda x, y: x + y, lista)
print (re)

# Lambda também pode receber um nome e ser usada na reduce como uma variavel, neste caso, labda é maxfind que irá
# retornar x se x for maior que y, caso contrario retorna y. O reduce vai fazer que cada item da lista seja comparado
# com X (primeiro elemento) e a condicional IF vai fazer com que o reduce conserve o resultado mais alto.

maxfind = lambda x, y: x if x > y else y
red1 = reduce(maxfind, lista)
print(red1)

# A função filter é capaz de aplicar algum tipo de filtro. Ela tbm recebe dois argumentos, função + sequencia. Esta
# função filtra todos os elementos de uma sequencia e retorna todos os resultados de acordo com valores boolianos TRUE
# ou FALSE. Os valores só retornam se forem TRUE. Abaixo verificando apenas valores pares

def verificar(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(verificar(34))
lista2 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fi = filter(verificar, lista2)
print(list(fi))

# Agora usando lambda, nesse caso, a expressão em labda só funciona com numeros pares, automaticamente retornando tudo
# que seja TRUE

veripar = lambda num: num % 2 == 0

fi2 = filter(veripar, lista2)
print(list(fi2))

veripar = lambda num: num % 2 == 0 and num > 7
fi3 = filter(veripar, lista2)
print(list(fi3))

# A função list comprehesion replica uma expressão arbitraria, permiti criar listas com anotações diferentes. Por exemplo
lst0 = [ x for x in "sequencia"]
# São usadas quando em casos mais simples que usar map() sendo mais veloz também

# No exmeplo abaixo iremos retornar x elevado ao quadrado para cada x no conjunto e elementos, nesse caos um range de 1 a 10

lst1 = [ x ** 2 for x in range(0, 10)]
print(lst1)

# Podemos deixar ainda com condicionais, como retornar apenas pares

lst2 = [ x ** 2 for x in range(0, 10) if x % 2 == 0]
print(lst2)

# Agora um exemplo com uma função que ja foi usada, a conversão em graus farenheit
temperaturas = [0,22.5, 40, 100]
lst3 = [((float(9)/5) * T +32) for T in temperaturas]
print(lst3)

# Ainda podemos fazer sequencias aninhadas, como aplicar A em B sendo que B faz alguma aplicação em C, exemplo:

lst4 = [ x ** 2 for x in [x ** 2 for x in range(0, 10)]]
print(lst4)

# A função Zip agrega os valores de 2 sequencias e retorna uma tupla, unindo 2 sequencias numa nova. Pode ser usado quando
# o numero de elementos for diferente em cada sequencia, mas o objeto resultante tera o mesmo numero resultante que o menor
# Ou seja, no exemplo abaixo, serão agrupados 1,1 2,2 e 3,3 mas 4 n sera agrupado e como o menor elemento tem 3 entidade
# logo o resultado são tres grupamento

az = zip([1,2,3,4],[1,2,3])
print(list(az))

# Essa função pode ser util para modificação de dicionários, como unir chaves, nesse caso, ficando (a,c) e (b,d). Tambem
# podemos unir chaves e valores especficando com .values() onde queremos receber valores, em ditv1 a recebe a chave 17,
# por exmeplo, em ditv2 asmbas as chaves (12, 17) são agrupadas e em ditv3 o valor de a, 12 recebe a chave C

di1 = {'a': 12, 'b' : 15}
di2 = {'c': 17, 'd': 23}
ditc = zip(di1,di2)
print(list(ditc))

ditv1 = zip(di1,di2.values())
print(list(ditv1))

ditv2 = zip(di1.values(),di2.values())
print(list(ditv2))

ditv3 = zip(di1.values(),di2)
print(list(ditv3))

# Enumerate permite retornar o inidce de cada valor em uma squencia, a medida que ela é percorrida. É retornada uma tupla
# no formato tupla(indice,valor) e recebe apenas um parametro

enu = [1, 3, 10]
enu1 = (enumerate(enu))
print(list(enu1))

enu1 = ['Marketing', 'Engenharia', 'Medicina']
for indice, valor in enumerate(enu1):
    print(indice, valor)

# assim são retornados o indice e o elemento numa tupla para cada elemento na lista