import random
import time

class Board:
    def __init__(self, rows=6, columns=7):
        self.board = [[' ' for x in range(columns)] for x in range(rows)]
        self.rows = rows
        self.columns = columns
    
    def display(self):
        for row in self.board:
            print(str(row).replace("'", ' ').replace(', ', '|')) 
        print('‾' * (4 * self.columns + 1))
        [print(f'  {i} ', end='') for i in range(self.columns)]
        print('\n')

    def dropPiece(self, piece, column):
        row = self.rows
        for r in reversed(self.board):
            row -= 1
            if r[column] == ' ':
                r[column] = piece
                break
        return row
        
    def isValidMove(self, column):
        if not isinstance(column, int):
            return False
        elif column < 0 or column > self.columns - 1:
            return False
        elif self.board[0][column] != ' ':
            return False
        else:
            return True
            
class Player:
    def __init__(self, name='', player_type='cpu', pieces='X'):
        self.name = name
        self.player_type = player_type
        self.pieces = pieces
        
    def play(self, board):
        if self.player_type == 'human':
            column = int(input(f'In which column {self.name} would you like to play? '))
            while not board.isValidMove(column):
                column = int(input(f'Oops, invalid move! {self.name}, try playing in another column: '))
            row = board.dropPiece(self.pieces, column)
            
        elif self.player_type == 'cpu':
            column = random.randint(0, board.columns - 1)
            while not board.isValidMove(column):
                column = random.randint(0, board.columns - 1)
            row = board.dropPiece(self.pieces, column)
            time.sleep(1)
        board.display()
        
        if self.hasWon(board, column, row):
            print(f'{self.name} wins! Congratulations!')
            print('----- Game Over -----')
            return True
        
    def hasWon(self, board, column, row):
        # Horizontal Check
        piece_count = 0
        for piece in board.board[row]:
            if piece == self.pieces:
                piece_count += 1
                if piece_count == 4:
                    return True
            else:
                piece_count = 0
        
        # Vertical Check
        piece_count = 0
        for r in range(board.rows):
            if board.board[r][column] == self.pieces:
                piece_count += 1
                if piece_count == 4:
                    return True
            else:
                piece_count = 0
                
        # Diagonal Check (/)
        r = row
        c = column
        while r > 0 and c > 0:
            r -= 1
            c -= 1
        if r < board.rows - 3: 
            piece_count = 0
            while r <= (board.rows - 1) and c <= (board.columns - 1):
                if board.board[r][c] == self.pieces:
                    piece_count += 1
                    if piece_count == 4:
                        return True
                else:
                    piece_count = 0
                r += 1
                c += 1
                
        # Diagonal Check (\)
        r = row
        c = column
        while r > 0 and c < board.columns - 1:
            r -= 1
            c += 1
        if r < board.rows - 3: 
            piece_count = 0
            while r <= (board.rows - 1) and c >= 0:
                if board.board[r][c] == self.pieces:
                    piece_count += 1
                    if piece_count == 4:
                        return True
                else:
                    piece_count = 0
                r += 1
                c -= 1
                                          
        return False
        

class Game:
    def start(self, board=Board()):
        player1, player2 = self.registerPlayers()
        round_number = 1
        max_rounds = board.columns * board.rows
        time.sleep(1)
        board.display()
        while round_number <= max_rounds:
            print(f'{round_number}th Round')
            winningMove = player2.play(board)
            if winningMove:
                return 
            round_number += 1
            print(f'{round_number}th Round')
            winningMove = player1.play(board)
            if winningMove:
                return 
            round_number += 1
        print('The game ended in a tie! How about playing again?')
        print('----- Game Over -----')
        return 
    
    def registerPlayers(self):
        print('### Welcome to Connect 4! ### \n\nTo start your game, answer the following questions: ')
        player1 = Player()
        player2 = Player()
        self.createPlayer(1, player1)
        if player1.pieces == 'X':
            player2.pieces = 'O'
        else:
            player2.pieces = 'X'
        self.createPlayer(2, player2)
        return player1, player2

    def validateType(self, player_type=''):
        while player_type.lower() not in ['cpu', 'human']:
            print('Oops! Invalid type, player type should be "human" or "cpu"!')
            player_type = input('Is the player a human or a cpu? ')
        return player_type.lower()
    
    def choosePieces(self, pieces):
        while pieces.upper() not in ['X', 'O']:
            print('\nOops! Invalid piece, the piece should be X or O')
            pieces = input('With which piece do you want to play? ')
        return pieces.upper()

    def createPlayer(self, player=1, player_obj=Player('BOT', 'cpu', 'x')):
        player_obj.name = input(f'\nEnter the name of Player {player}: ')
        player_obj.player_type = self.validateType(input(f'\n{player_obj.name} is a human or a cpu? '))
        if player == 1:
            player_obj.pieces = self.choosePieces(input(f'\nPlayer 1 has the right to choose their pieces. With which pieces will {player_obj.name} play? (X or O) '))
        elif player == 2:
            if player_obj.pieces == 'X':
                pieces1, pieces2 = 'O', 'X'
            else:
                pieces1, pieces2 = 'X', 'O'
            print(f'\nThe other player has already chosen {pieces1}, so {player_obj.name} will play with {pieces2}!\n')
      
Game().start()
