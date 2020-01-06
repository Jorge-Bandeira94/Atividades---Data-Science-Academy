# Módulos e pacotes
'''Módulos são arquivos de extensão .py que implemental um conjunto de funções, o comando 'import' traz ao script o módulo desejado, uma vez importado ele fica disponível para uso
em tod o script. Pode-se criar uma função em arquivo py, e sempre que precisar, importa-la através do import + nome do módulo. Importar fatias de um módulo são úteis para não superlotar o programa, isos se faz
com o 'from' xxxx 'import' xxx.
    Para instalar módulos manualmente basta abrir o prompt de comando e digita conda install "nome-do-modulo" ou pip install "nome do módulo
    Já os pacotes, são uma forma de estruturas módulos, por exemplo, podemos utiliza "import pacote.modulo". Enquanto um módulo é um arquivo, um pacote é um compilado
de módulos python. O repositório de pacotes do python é o PyPI."'''

#Um pacote bastante util é o datetime, que possui um módulo de mesmo nome. O comando datetime.datetime.now() pode informar o exato momento em que sepede o comando desde o ano até o centésimo de segundo
#também é possível formatar a hora com date.time(3, 10, 12), mudanod hora minuto e segundos de acordo com os parametros nos parenteses. Manipulando uma variável designada como o dia atual podemos extrair informações de modo:

hoje = datetime.date.today()
print(hoje)

print(hoje.ctime())
print(hoje.year())
print(hoje.moth())
print(hoje.day())

#Ainda podemos fazer operações com as datas
#Em uma variavel gravar
d1 = datetime.data(2015, 4, 28)
print(d1)

d2 = d1.replace(year=2016)
print(d2) #O resultado que irá sair será a substituição de 2015 por 2016

d3 = d2 - d1
print(d3) #mostrará a quantidade de dias entre as duas datas

#Erros e exceções

'''Erros podem ocorrer quando uma expressão está sintaticamente errada, escrita de forma não convencional e que acarretará, na
não execução do script, as exceções são erros, não de sintaxe, mas de operação, como uma divisão por zero, que a máquina não é capaz 
de conduzir. Utilizamos as palavras reservadas Try e Except para tratar erro, de forma:'''

try:
    aqui vão as operações
except Exceção1:
    Se houver , execute este bloco
except Exceção2:
    Se houver esta outra exceção, execute este bloco
else:

# Temos ainda a palavra reservada finally, que nos permite executar código, mesmo que exceções ocorram.

#erros
print('Olá) '# string sem o fechamento das aspas

def numv (a, b):
    c = a / b
    return c
numv(4/0) # Divisão por zero

d = 8 + 'a'
print(d)

#tratando erros
try:
    8 + 'a'
except TypeError: # é necessário colocar o TypeError
    print('Operação não permitida')

try:
    f = open('testandodados.txt', 'w') #caso eu tire a extensão ou coloque para ler 'r' arquivo que não existe, resultará em erro
    f.write('Gravando arquivo')
except IOError:
    print('Este arquivo não foi encontrado, ou não pode ser salvo')
else:
    print('Gravação completa')
    f.close()

# Caso eu adicione finally: como bloco após o else, ele será executado independente de ocorrer o erro ou não

def askint():
    try:
        a = int(input('Digite um número inteiro: '))
    except UnboundLocalError:
        print('Você não digitou um número')
        a = int(input('Digite um número inteiro: ')) #desta forma eu irei perguntar mais uma vez pelo número, se o usuário colocar outro caractere novamente resultará em erro
    finally:
        print('Obrigado')


def askint():
    while True: #criou um loop na função, enquanto for verdadeira ele irá fazer a memsa pergunta ao usuário até ser quebrada pelo break quando o usuario digitar corretamente um numero e entrar no bloco else
        try:
            a = int(input('Digite um número inteiro: '))
        except: #quando o erro ocorrer, o 'except' abrirá este bloco
            print('Você não digitou um número!')
            continue
        else:
            print('Obrigado por digitar um número!')
            break #o programa irá finalizar depois de ter o numero digitado, sem isto, o loop continuará ativo
        finally:
            print('FIM!')
        print(a)

askint()

# Link com o nome de todos os possíveis erros https://docs.python.org/3.6/library/exceptions.html


