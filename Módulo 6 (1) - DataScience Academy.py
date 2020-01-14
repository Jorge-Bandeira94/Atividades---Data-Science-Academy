'''Banco de dados

Os bancos de dados são conjunto de dados organizados de forma que se possa facilmente acessar, são ainda
coleções de dados interligados e utilizados para forncer alguma informação. O banco de dados é basicamente
o local para depositar informações e forma de dados.

SGBD - Sistema gerenciador de banco de dados
O principal objetivo de um SGBD é retirar de um cliente a responsabilidade
de gerenciar o acesso e organização de dados, ele oferece uma interface simplificada
para que um cliente possa editar ou consultar um banco de dados. Um exemplo deste sistema
é o Oracle e o MySQL. O Oracle pode ser utilizado para receber os dados e gerencia-los. O SGBD é
responsável por manter os dados salvos em HD, fazer ligação entre dados e metaddos, manter
os dados organizados e em memória, disponibilizar interface para cesso externo, controlar o
acesso a informações, manter cópia dos dados, entre outras tarefas.

Um SGBD oferece diversos benefícios como controle de redundância de dados, compartilhamento, segurança, backup
,produtividade e disponibilidade, flexibilidade e padronização.
Estes SGBDs podem ser encontrados em Data Mining, Bancos de dados mUltimídia, Banco de dados móveis, espaciais e temporais
Banco de dados semiestruturados, e pode ser um das fontes para big data.

Bancos de dados Relacionas -
Principal modelo para gestão de banco de dados. Representam e armazenam os dados em tabelas organizadas em linhas e colunas.
São gerenciados por RDBMS, são os relacionamentos entre as tabelas que o torna relacional. Pode ser percebido como uma coleção de
tabelas. A estrutura deste DB permite unir informações de diferente tabelas através do uso de chaves estrangeiras que são usadas
para localizar qualquer peça de dados dentro destas tabelas, estas chaves conectam as tabelas.


Principais conceitos:

    Cada linha de uma tabela, com informações em suas colunas, representa um registro
    ,ou tupla, da tabela. Os registros não precisam conter ifnormações em todas as colunas podendo ser representados por
    valores nulos. As coluans são também chamadas de atributos, o tipod e valor que um atributo pode assumir é denominado
    domínio, por exemplo, em um campo em que só podem ser atribuidos valors numéricos o domínio e numérico.

    Atributo Chave - Permite identificar e diferenciar uma tupla de outra

    Chave primária - Uma ou mais colunas que visam garantir a unicidade das linhas (só pode haver uma chave primária)

    Chave estrangeira - coluna de uma tabela que contém valores da chave primária de outra tabela (pode haver mais de uma)

    índice - É uma lista ordenada de valores que apontam para os dados nas tabelas. Utilizado para agilizar a leitura de dados.
    Pode ser utilizado também para forçar a unicidade dos dados

    Integridade Referencial - É o conceito em que várias tabelas de banco de dados compartilham uma relação com base nos dados
    armazenados nas tabelas e essa relação deve ser coerente. Isso geralmente é imposto com ações de adição exclusão e atualização.
    Por exemplo, não se pode remover um registro sem remover seus registros relacionados.

    Normalização de dados - organização de campos e tabelas em um banco relacional para minimizar
    a redundância e a dependência. Facilitando a edição de um dado que se propagara para todos seus relacionados
    nas demais tabelas interligadas


Linguagem SQL :

Uma das linguagens mais antigas utilizada em qualquer banco de dados relacional. O acesso ao BD é feito por esta linguagem,
SQL significa Structure Query Language. Os comandos desta linguagem se dividem em DDL, DML e DCL.

    DML (Data Manipulation Language) - basicamente são os comandos SELECT (pesquisa de dados), UPDATE (Atualização de dados)
    DELETE (Eliminação de dados) e INSERT (Inserção de dados).
    Usadas basicamente para desenvolvimento do banco.

    DDL (Data Definition Language) - CREATE (definição de um objeto como tabela e índice) ALTER (alteração de objeto)
    e DROP (eliminar um objeto).
    Usada basicamente para suporte e manipulação do banco de dados

    DCL (Data Xontrol Language) - GRANT (fornecer um privilégio) e REVOKE (Tirar um privilégio)
    Também utilizado para suporte e desenvolvimento.

SQLite :

Um banco de dados relacional. A lingaguem python fornece acesso a praticamente qualquer BD disponível,
este foi selecionado para melhor aprendizagem durante o curso.
O SQLite é um engine (motor) de banco de dados SQL, é uma versão simplificada de um BD SQL, difernte de versões completas
como MySQL. É um único arquivo com poucos comandos complexos, apesar de ser um único arquivo O SQLite carrega em memória
apenas os registros que estão sendo usados. Por ser um BD leve e de pouca configuração alepm de não exigir um servido dedicado
ele é recomendável para atividades simples. Ele pode ser utilizado quando recursos avançados de SGBD's não foram necessários como
aplicações de smartphone. Ele vem automaticamente ao instalar o Anconda.

Pode ser utilizado efetivamente em dispositivos embarcados, websites (tráfego médio ou baixo), Análise de dados (médio porte), Cache para dados de RDBMS
, BDs temporários ou internos.


Bancos de dados NoSQl

São banco de dados distribuidos não relacionados projetados para Big Data, com arquitetura mais eficiente que os BDs SQL. Estes bancos de dados
oferecem quatrocategorais principais de bancos de dados: Graph Databases, Document database, Key-values Database e Column family store.

'''


