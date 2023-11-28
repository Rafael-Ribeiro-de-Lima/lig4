class Tabuleiro:
    def __init__(self, linhas=6, colunas=7):
        self.tabuleiro = [[' ' for x in range(colunas)] for x in range (linhas)]
    
    def mostrarTabuleiro(self):
        for l in self.tabuleiro:
            print(l)

    def inserirPeca(self, peca, coluna):
        for l in reversed(self.tabuleiro):
            if l[coluna - 1] == ' ':
                l[coluna - 1] = peca
                break
 


class Jogador:
    def __init__(self, nome, tipo, pecas, vitorias=0, derrotas=0):
        self.nome = nome
        self.tipo = tipo
        self.vitorias = vitorias
        self.derrotas = derrotas
        self.pecas = pecas

def iniciarJogo():
    print('### Bem-vindo ao Lig4! ### \n\nPara iniciar seu jogo, responda às seguintes perguntas: ')
    nomeJogador1 = input('Digite o nome do Jogador 1: ')
    tipoJogador1 = input(f'{nomeJogador1} é uma pessoa ou uma cpu? ')
    pecaJogador1 = input(f'Qual peça {nomeJogador1} utilizará? ')
    Jogador1 = Jogador(nomeJogador1, tipoJogador1, pecaJogador1)
    print('Certo! Agora preciso que responda às mesmas perguntas a respeito do Jogador 2.')
    nomeJogador2 = input('Digite o nome do Jogador 2: ')
    tipoJogador2 = input(f'{nomeJogador2} é uma pessoa ou uma cpu? ')
    pecaJogador2 = input(f'Qual peça {nomeJogador2} utilizará? ')
    Jogador2 = Jogador(nomeJogador2, tipoJogador2, pecaJogador2)
    return Jogador1, Jogador2



tabuleiro = Tabuleiro()
Jogador1, Jogador2 = iniciarJogo()
tabuleiro.inserirPeca(Jogador1.pecas, 1)
tabuleiro.inserirPeca(Jogador2.pecas, 2)
tabuleiro.inserirPeca(Jogador1.pecas, 1)
tabuleiro.inserirPeca(Jogador2.pecas, 2)
tabuleiro.mostrarTabuleiro()
#tabuleiro.mostrarTabuleiro()
