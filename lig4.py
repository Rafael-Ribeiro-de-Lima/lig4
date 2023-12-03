import random
import time

class Tabuleiro:
    def __init__(self, linhas=6, colunas=7):
        self.tabuleiro = [[' ' for x in range(colunas)] for x in range (linhas)]
        self.linhas = linhas
        self.colunas = colunas
    
    def mostrar(self):
        for l in self.tabuleiro:
            print(str(l).replace("'", ' ').replace(', ', '|')) 
        print('‾'*(4 * self.colunas+1))
        [print(f'  {i} ', end='') for i in range(self.colunas)]
        print('\n')

    def inserirPeca(self, peca, coluna):
        linha = self.linhas
        for l in reversed(self.tabuleiro):
            linha -= 1
            if l[coluna] == ' ':
                l[coluna] = peca
                break
        return linha
        
    def jogadaValida(self, coluna):
        if not isinstance(coluna, int):
            return False
        elif coluna < 0 or coluna > self.colunas - 1:
            return False
        elif self.tabuleiro[0][coluna] != ' ':
            return False
        else:
            return True
            
class Jogador:
    def __init__(self, nome='', tipo='cpu', pecas='X'):
        self.nome = nome
        self.tipo = tipo
        self.pecas = pecas
        
    def jogar(self, tabuleiro):
        if self.tipo == 'pessoa':
            coluna = int(input(f'Em qual coluna {self.nome} deseja jogar? '))
            while not tabuleiro.jogadaValida(coluna):
                coluna = int(input(f'Ops, jogada inválida! {self.nome}, tente jogar em outra coluna: '))
            linha = tabuleiro.inserirPeca(self.pecas, coluna)
            
        elif self.tipo == 'cpu':
            coluna = random.randint(0, tabuleiro.colunas)
            while not tabuleiro.jogadaValida(coluna):
                coluna = random.randint(0, tabuleiro.colunas)
            linha = tabuleiro.inserirPeca(self.pecas, coluna)
            time.sleep(1)
        tabuleiro.mostrar()
        
        if self.venceu(tabuleiro, coluna, linha):
            print(f'{self.nome} venceu! Parabéns!')
            print('----- Jogo finalizado -----')
            return True
        
    def venceu(self, tabuleiro, coluna, linha):
        # Verificação Horizontal
        ocorrencias_peca = 0
        for peca in tabuleiro.tabuleiro[linha]:
            if peca == self.pecas:
                ocorrencias_peca += 1
                if ocorrencias_peca == 4:
                    return True
            else:
                ocorrencias_peca = 0
        
        #Verificação Vertical
        ocorrencias_peca = 0
        for lin in range(tabuleiro.linhas):
            if tabuleiro.tabuleiro[lin][coluna] == self.pecas:
                ocorrencias_peca += 1
                if ocorrencias_peca == 4:
                    return True
            else:
                ocorrencias_peca = 0
                
        #Verificação Diagonal (/)
        lin = linha
        col = coluna
        while lin > 0 and col > 0:
            lin -= 1
            col -= 1
        if lin < tabuleiro.linhas - 3: 
            ocorrencias_peca = 0
            while lin <= (tabuleiro.linhas - 1) and col <= (tabuleiro.colunas - 1):
                if tabuleiro.tabuleiro[lin][col] == self.pecas:
                    ocorrencias_peca += 1
                    if ocorrencias_peca == 4:
                        return True
                else:
                    ocorrencias_peca = 0
                lin += 1
                col += 1
                
        #Verificação Diagonal Invertida (\)
        lin = linha
        col = coluna
        while lin > 0 and col < tabuleiro.colunas - 1:
            lin -= 1
            col += 1
        if lin < tabuleiro.linhas - 3: 
            ocorrencias_peca = 0
            while lin <= (tabuleiro.linhas - 1) and col >= 0:
                if tabuleiro.tabuleiro[lin][col] == self.pecas:
                    ocorrencias_peca += 1
                    if ocorrencias_peca == 4:
                        return True
                else:
                    ocorrencias_peca = 0
                lin += 1
                col -= 1
                                          
        return False
        

class Jogo:
    def iniciar(self, tabuleiro=Tabuleiro()):
        jogador1, jogador2 = self.inscreveJogadores()
        rodada = 1
        max_rodadas = tabuleiro.colunas * tabuleiro.linhas
        tabuleiro.mostrar()
        while rodada <= max_rodadas:
            print(f'{rodada}ª Rodada')
            jogadaVencedora = jogador2.jogar(tabuleiro)
            if jogadaVencedora:
                return 
            rodada += 1
            print(f'{rodada}ª Rodada')
            jogadaVencedora = jogador1.jogar(tabuleiro)
            if jogadaVencedora:
                return 
            rodada += 1
        print('O jogo terminou empatado! Que tal jogar novamente?')
        print('----- Jogo finalizado -----')
        return 
    
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
      
Jogo().iniciar()

