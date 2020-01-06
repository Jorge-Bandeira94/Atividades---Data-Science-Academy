#Introdução à programação orientada a objetos (POO)
'''
A orientação a objetos é um modelo de análise, projeto e programação de sistemas de software baseado na
composição e interação entre diversas unidades de software chamadas de objetos.
Na programação orientada a objetos, o programador é responsável por moldar o mundo dos objetos,
e definir como os objetos devem interagir entre si. Os objetos conversam uns com os outros através de 'mensganes', o
papel do programador é definir quais serão as mensagens que cada objeto pode receber e também qual a ação que
o objeto deve realizar ao receber cada mensagem.

Diferenças entre programação estruturada e POO:

Estruturada - Forma de programação que preconiza que os programas sejam reduzidos a sequencias, decisões e iterações
(repetição). Nesta programação, dados e funções compões a aplicação através de estruturas basicas de controle.

POO - Se da ao fato da escrita do código trazer objetos do mundo real para se tornar parte do código com o uso de classes
e instancias. nesta programação, métodos são funções dentro de classes com objetivos de manipular os atributos de um objeto
'''

#Classes e Objetos

'''A classe é a estrutura básica do paradigma de orientação a objetos, que representa o tipo do objeto, um modelo a 
partir do qual os objetos serão criados. Uma classe é um molde, uma especificação que define o que um objeto desse tipo 
deverá ter como atributo e como ele deve se comportar.
A partir de classes construimos instâncias, cada isntancia é um objeto específico, criado a partir de uma classe. 
Os objetos representam entidades, com suas qualidades (atributos) e ações (métodos) que podem realizar. 

Objetos poderão ser criados a partir de instâncias de classes criadas usando a palavra reservada 'class'. O nome de um classe
começa com letra maiúscula. Em python, novos objetos são criados a partir das classes. O objeto é uma instância da classe,
que possui características próprias.'''

#Criando classes e objetos
class Livro:
    # os dois defs (funções) são métodos desta classe

    def __init__(self): #Este método irá inicializar cada objeto a partir desta classe (__init__), self é uma referência a cada atriuto de um objeto criado a partir desta classe
        self.titulo = 'O monge e o executivo' # estas duas linhas são atributos de cada objeto criado a partir desta classe, 'self' indica que estes são atributos dos objetos
        self.ISBN = 9988686
        print('Construtor chamado para criar um objeto desta classe')
    def imprime(self):
        print('Foi criado o livro {} e ISBN {}'.format(self.titulo, self.ISBN))

# esta classe possui dois atributos e uma ação (segundo def)

'''
# criando uma istância de classe livro
Livro1 = Livro()
print(type(Livro1)) # me inforará que livro1 é da classe livro

print(Livro1.titulo)
#com o objeto e o atributo criado, usar '.titulo' ou '.ISBN' me retornará estas informações que estão dentor da classe
# ao chamar o atributo não precisa abrir e fechar os parenteses, mas quando chama o método sim, 'imprime' é uma função e
# precisa destes parenteses.

print(Livro1.imprime())

Caso eu designe outra classe de mesmo nome, a anterior será sobrescrita.
'''
class Livro:
    def __init__(self, titulo, ISBN): #quando for criado um objeto desta classe, poderá ser criado dois parâmetros que irão para Titulo e ISBN, ex: Livro1 = Livro(O monge e o executivo, 9288948)
        self.titulo = titulo
        self.ISBN = ISBN
        print('Construtor chamado para criar um objeto desta classe')
    def imprime(self, titulo, ISBN):
        print('Este é o livro {} de ISBN {}'.format(titulo, ISBN))

a = input('Digite o nome do livro: ') #dei a liberdade de eu mesmo escrever a estância
a1 = input('Digite seu ISBN: ')
Livro2 = Livro(a, a1) #dei a variável 'Livro2' para desenvolver os métodos da classe 'Livro'
Livro2.imprime(a, a1) #o método imprime() me mostrará a informação desejada

# Criando a classe cachorro
class Cachorro:
    def __init__(self, raça): #evitar usar cedilha ou palavras com acento
        self.raça = raça
        print('Construtor chamado para criar um objeto desta classe')
#criando um objeto para esta classe
a1 = input('Digite a raça de seu cachorro: ')
a2 = input('Digite a raça de seu outor cachorro: ')
Rex = Cachorro(a1)
Golias = Cachorro(a2)
print(Rex.raça)
print(Golias.raça)

#Criando outros objetos
class funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def listFunc(self):
        print('O nome do funcionário é {}, e ele recebe {} R$'.format(self.nome, self.salario)) #neste caso eu preciso colocar 'self.nome' em format() por corresponderem as parâmetros da função def

func1 = funcionarios('Obama', 20000)
func1.listFunc()

'''
Algumas funções especiais nos permitem manipular os atributos de um objeto, são elas:

hasattr(func1, 'nome') - procura se no objeto func1 existe o atributo nome
hasattr(func1, 'salario') - procura se no objeto func1 existe o atributo salario
setattr(func1, 'salario', 4500) - A partir do objeto func1, verifique se ele tem o atributo salario e defina para o valor 4500
getattr(func1, 'salario') - Obtenha este atributo a partir deste objeto
delattr(func1, 'salario) - deletar o atributo

Estas respostas serão em True ou False
#Detalhes sobre metodos em POO

Os métodos são (ações do objeto) funções definidas dentro do corpo de uma classe, são usados para realizar operações com os atributos dos nosso objetod. Métodos são
usados no conceito de encapsulamento, do paradigma de POO. São basicamente funções definidas dentro de uma classe, para manipular os objetos criados a partid
da classe. Utiliza-se a palavra def para criar métodos, da mesmo forma que se cria funções. Podemos criar classes para nossas atividades de análise de
dados e criar métodos específicos para cada tarefa, encapsulando nossa lógica de programação.'''

class Circulo():

    # Este atributo fora do construtor é util para que seja utilizado em diversos construtores diferentes ao longo da classe, sendo constante
    pi = 3.14

    #quando um objeto desta classe for criado, este método será executado e o valor padrão do raio será 5 caso não receba nenhum valor, se receber, 5 é sobrescrito
    def __init__(self, raio = 5):
        self.raio = raio

    # Esse método calcula a área, self utiliza os atributos deste mesmo objeto
    def area(self):
        return(self.raio * self.raio) * Circulo.pi #a palavra 'circulo' é necessária pois a variavel está fora da def, e dentro da classe circulo

    #Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    #Obter o raio do circulo
    def getRaio(self):
        return self.raio

#Criando um objeto para a classe Circulo()
circ = Circulo()

#Executando um método da classe Circulo()
c = circ.getRaio()
print(c)
a = circ.area()
print(a)
d = circ.setRaio(9) #modulei o raio setando um novo valor
e = circ.getRaio() #obtive na tela o valor modificado
f = circ.area() #refiz o calculo de area onde foi sobreescrito p novo raio
print('O novo raio é {}'.format(e))
print('A nova área é {}'.format(f))

'''Outro conceito fundamental em POO é o conceito de Herança. Uma forma de usar novas classes usando classes definidas previamente. Estas
novas classes formadas são chamadas de sub-classes ou derivadas'''

class Animal(): #Criando uma classe normalmente

    def __init__(self):  #Atribuindo seus métodos
        print('Animal criado')
    def identify(self):
        print('Animal')
    def comendo(self):
        print('Comendo')


class Cachorro(Animal): #Criando classe cachorro e linkando com classe mãe Animal, herdando seus métodos

    def __init__(self):
        Animal.__init__(self) # No método construtor tbm será executado o método construtor de animal
        print('Cachorro criado')
    def identify(self):
        print('Cachorro')  #haverá conflito devido ser o memso método em Aniamal, mas será retornado o método mais específico da classe, no caso este mesmo
    def latir(self):
        print('Latindo')  #apenas está classe possui este método, outras classes que utilizaram Animal como herança n herdaram métodos desta subclasse, a menos que a utilizem como herança


#Testando
rex = Cachorro()
print(rex.identify())
print(rex.comendo())
print(rex.latir())

'''Classes em python podem criar determinadas situações utilizando métodos especiais, __innit__ é um deles. A linguagem python oferece diversos
outros métodos especiais que podem ser identificados exatamente pelas iniciais e finais __, __ (CONSULTAR DOCUMENTAÇÃO PARA ENTENDER CADA UMA).
Quando se utiliza a função del para remover um objeto, internamente o python usa __dellattr__ para executar a ação.

Ao digitar:
del objeto.atributo_1 (deletar atributo_1 do objeto)

O python executa internamente como:
obj.__delattr__("atributo_1")

Outro exemplo é o método __str__. Ao criar uma classe que possui o método __str__, ao instanciar um objeto a esta classe e pedir um print(),
sempre o método que será executado será o __str__. Da mesma forma, se for comandando str(objeto_instanciado) será printado, em forma de string
o método __str__ que houver na classe. De forma semelhante, ao atribuir o método __len__ dentro da classe, se houver uma chamado ao objeto 
escrita de forma len(objeto_instanciado) o método __len__ é que será executado de dentor da função. Desta forma estou dando métodos simples
ao objeto criado. Se dentro da classe, ao invés de utilizar os métodos especiais __str__(self) ou __len__(self), eu utilizar apenas len(self) ou str(self)
será necessário especificar qual método eu quero extrair a classe da forma: objeto_instanciado.len()'''