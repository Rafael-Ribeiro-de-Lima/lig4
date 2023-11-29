class Tabuleiro:
    def __init__(self, linhas=6, colunas=7):
        self.tabuleiro = [[' ' for x in range(colunas)] for x in range (linhas)]
        self.linhas = linhas
        self.colunas = colunas
    
    def mostrarTabuleiro(self):
        
        for l in self.tabuleiro:
            print(str(l).replace("'", ' ').replace(', ', '|')) # As String não são mutáveis, então fiz por listas. Talvez haja uma maneira mais elegante e eficiente!
        print('‾'*29)
        [print(f'  {i} ', end='') for i in range(self.colunas)]
        print('\n')

    def inserirPeca(self, peca, coluna):
        for l in reversed(self.tabuleiro):
            if l[coluna - 1] == ' ':
                l[coluna - 1] = peca
                break
 
class Jogador:
    def __init__(self, nome='', tipo='cpu', pecas='x', vitorias=0, derrotas=0, empates=0):
        self.nome = nome
        self.tipo = tipo
        self.vitorias = vitorias
        self.derrotas = derrotas
        self.empates = empates
        self.pecas = pecas


class Arbitro:
    def __init__(self):
        pass

    def inscreveJogadores(self):
        print('### Bem-vindo ao Lig4! ### \n\nPara iniciar seu jogo, responda às seguintes perguntas: ')
        jogador1 = Jogador()
        jogador2 = Jogador()
        self.criaJogador(1, jogador1)
        if jogador1.pecas == 'X':
            jogador2.pecas = 'O'
        else:
            jogador2.pecas = 'X'
        self.criaJogador(2, jogador2)
        return jogador1, jogador2

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

class Jogo:
    def __init__(self):
        pass
    
    def iniciarJogo(self, tabuleiro, jogador1, jogador2):
        rodada = 1
        max_rodadas = tabuleiro.colunas * tabuleiro.linhas
        partida_finalizada = False
        while rodada <= max_rodadas and not partida_finalizada:
            break
        




tabuleiro = Tabuleiro()
#arbitro = Arbitro()
#jogador1, jogador2 = arbitro.inscreveJogadores()
'''tabuleiro.mostrarTabuleiro()
tabuleiro.inserirPeca('X', 1)
tabuleiro.inserirPeca('X', 1)
tabuleiro.inserirPeca('X', 2)
tabuleiro.inserirPeca('X', 2)
tabuleiro.inserirPeca('X', 2)
tabuleiro.inserirPeca('X', 2)
tabuleiro.inserirPeca('X', 4)
tabuleiro.inserirPeca('X', 5)
tabuleiro.inserirPeca('X', 6)'''
tabuleiro.mostrarTabuleiro()
