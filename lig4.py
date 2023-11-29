class Tabuleiro:
    def __init__(self, linhas=6, colunas=7):
        self.tabuleiro = [[' ' for x in range(colunas)] for x in range (linhas)]
        self.linhas = linhas
        self.colunas = colunas
    
    def mostrarTabuleiro(self):
        
        for l in self.tabuleiro:
            print(str(l).replace("'", ' ').replace(',', '|').replace(''))
        print('‾'*35)
        print([str(col) for col in range(self.colunas)])
        print()

    def inserirPeca(self, peca, coluna):
        for l in reversed(self.tabuleiro):
            if l[coluna - 1] == ' ':
                l[coluna - 1] = peca
                break
 
class Jogador:
    def __init__(self, nome='', tipo='cpu', pecas='x', vitorias=0, derrotas=0):
        self.nome = nome
        self.tipo = tipo
        self.vitorias = vitorias
        self.derrotas = derrotas
        self.pecas = pecas

class Arbitro:
    def __init__(self):
        pass

    def inscreveJogadores(self):
        print('### Bem-vindo ao Lig4! ### \n\nPara iniciar seu jogo, responda às seguintes perguntas: ')
        jogador1 = Jogador()
        jogador2 = Jogador()
        print(f'test {jogador1.pecas}')
        self.criaJogador(1, jogador1)
        if jogador1.pecas == 'X':
            jogador2.pecas = 'O'
        else:
            jogador2.pecas = 'X'
        self.criaJogador(2, jogador2)
    
    def validaTipo(self, tipo=''):
        while tipo.lower() not in ['cpu', 'pessoa']:
            print('Ops! Tipo inválido, o tipo do jogador deve ser "pessoa" ou "cpu!')
            tipo = input('O jogador é uma pessoa ou uma cpu? ')
        return tipo.lower()
    
    def escolhaPecas(self, peca):
        while peca.upper() not in ['X', 'O']:
            print('\nOps! Peça inválida, a peça deve ser X ou O')
            peca = input('Com qual peça você quer jogar? ')
        return peca.upper()


    def criaJogador(self, player=1, jogador=Jogador('BOT', 'cpu', 'x')):
        jogador.nome = input(f'\nDigite o nome do Jogador {player}: ')
        jogador.tipo = self.validaTipo(input(f'\n{jogador.nome} é uma pessoa ou uma cpu? '))
        if player == 1:
            jogador.pecas = self.escolhaPecas(input(f'\nO Jogador 1 tem o direito de escolher as suas peças. Com quais peças {jogador.nome} irá jogar? (X ou O) '))
        elif player == 2:
            if jogador.pecas == 'X':
                pecas1, pecas2 = 'O', 'X'
            else:
                pecas1, pecas2 = 'X', 'O'
            print(f'\nO outro jogador já escolheu {pecas1}, então {jogador.nome} jogará com as {pecas2}!')




tabuleiro = Tabuleiro()
#arbitro = Arbitro()
#arbitro.inscreveJogadores()
tabuleiro.mostrarTabuleiro()
tabuleiro.inserirPeca('X', 1)
tabuleiro.mostrarTabuleiro()
