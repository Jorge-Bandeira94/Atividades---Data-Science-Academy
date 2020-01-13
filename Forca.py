# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Variáveis globais

lista1 = []
lista2 = []
lista3 = []
tentativas = 0
erros = 0
acertos = 0
palavraG = ''
palavracorreta = ''
palavrasecreta = ''

# Biblioteca de randomização de palavras escolhidas

def rand_word():
    with open("teste.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip().lower()

# Classe

class Forca:

    # Método Construtor
    def __init__(self, palavra):
        global palavracorreta
        global palavraG
        global palavrasecreta
        self.palavra = palavra
        print('Palavra escolhida...')
        palavraG = len(palavra) * '-'
        palavracorreta = palavra
        palavrasecreta = list(palavraG)

    # Método para adivinhar a letra
    def palpite(self, letra):
        self.letra = letra
        global tentativas
        global erros
        global acertos
        if letra not in lista1 and letra not in lista2:
            if letra in self.palavra:
                tentativas += 1
                count = 0
                lista1.append(letra)
                for l in self.palavra:
                    if l == letra:
                        count += 1
                        acertos += 1
                print('letra "{}" aparece {} vezes'.format(letra, count))
                print('Contém a(s) letra(s) : {}'.format(lista1))
            else:
                lista2.append(letra)
                tentativas += 1
                erros += 1
                print('Não contém a(s) letra(s): {}'.format(lista2))
        if letra in lista1 or letra in lista2:
            print('Já digitou está letra, tente outra')


    # Método para verificar se o jogo terminou
    def fim(self):
        global derrota
        if erros == 6:
            print('Você perdeu, a palavra era {}. tente novamente!'.format(self.palavra))
        else:
            print('')

    # Método para verificar se o jogador venceu
    def venceu(self):
        global palavracorreta
        global tentativas
        global acertos
        lp = len(palavracorreta)
        if lp == acertos:
            print('Parabéns, você venceu com {} tentativas'.format(tentativas))
        else:
            print('...')

    # Método para não mostrar a letra no board
    def esconder(self, letra):
        self.letra = letra
        global palavracorreta
        global palavrasecreta
        if letra in palavracorreta:
            # Se a letra esta na palavra um contador inicia para me dar indexações
            count = 0
            for caractere in palavracorreta:
                # Apenas se um caractere for igual a uma letra da palavra este comando roda
                if caractere == letra:
                    # Aqui estou fazendo alterações no objeto fora da classe, de forma a não reinicia-lo do zero toda vez que digitar uma letra
                    palavrasecreta.insert(count, letra)
                    # Este contador novo serve para que o pop remova o ifem que foi empurrado pela frente pelo insert acima
                    contador = count + 1
                    palavrasecreta.pop(contador)
                # Este último contador vai somar ao count original para que caso uma nova letra apareça na palvra ela seja retirada da indexação correta
                count += 1

        print(palavrasecreta)

    # Método para checar o status do game e imprimir o board na tela
    def status(self):
        global erros
        if erros == 1:
            print(board[1])
        elif erros == 2:
            print(board[2])
        elif erros == 3:
            print(board[3])
        elif erros == 4:
            print(board[4])
        elif erros == 5:
            print(board[5])
        elif erros == 6:
            print(board[6])
        else:
            print(board[0])

# Executando o game

def main():

    # Objeto
    jogo = Forca(rand_word())
    print(20 * '=-=')
    print('\nO jogo começou, adivinhe a palavra\n')
    print(20 * '=-=')


    while True:
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
        if erros < 6:
            entrada = input('Dê seu palpite, digite uma letra:').lower().strip()
            jogo.palpite(entrada)

        # Verifica o status do jogo e printa as insformações
            jogo.status()
            jogo.esconder(entrada)
            print(erros)
            print(acertos)

            if acertos == len(palavracorreta):
                jogo.venceu()
                print('Término de jogo')
                break
            elif erros == 6:
                jogo.fim()
                print('Término de jogo')
                break

# Inicializador

main()

