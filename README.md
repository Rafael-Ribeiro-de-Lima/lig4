# Connect 4 Game
## Project Description
This project serves as the Final Project for the Object-Oriented Programming Introduction (INE5603) course in the Information Systems program at UFSC (Federal University of Santa Catarina).

In the context of this project, only topics covered in class were applied. Therefore, error handling, exceptions, and additional features that could enhance development were not implemented.

## Game Files

- `lig4.py`: Implementation of the Connect 4 game in Portuguese.
- `conn4.py`: Implementation of the Connect 4 game in English.

## Running the Game

To run the game, you need an environment that allows the execution of Python files (`.py`). Follow the instructions below to start the game:

1. Open a terminal or command prompt in the directory where the files are located.

2. Make sure you have Python installed. If you don't have it yet, you can download it from [python.org](https://www.python.org/downloads/).

3. Run the game using the following command, replacing `[file_name]` with the specific name of the file you want to execute (e.g., `lig4.py` or `conn4.py`):

   ```bash
   python [file_name].py

## Game Rules
Connect 4 is a classic two-player connection game in which the players take turns dropping their colored discs from the top into a vertically suspended grid. The objective of the game is to connect four of one's own discs of the same color consecutively in a line - horizontally, vertically, or diagonally — before the opponent.

The game is played on a 6x7 grid, and players take turns to drop their discs into one of the columns. The disc will then fall to the lowest available space within that column. In the context of the code developed, the colored discs have been represented by "X" and "O". The player who successfully connects four discs in a row wins the game.

<p align="center">
  <img src="https://a-static.mlcdn.com.br/800x560/jogo-lig-4-estrela-brinquedo-pedagogico-de-raciocinio-logico/fusaogeekpresentes/7947577118/e2818952cce93d04ff112ec1591c6f9c.jpeg" max-width=140px width=auto/>
</p>

## CPU Player Behavior 
When one of the players is of the "cpu" type, their moves are randomly generated. The CPU player selects a column at random and drops its disc into the lowest available space in that column. This random move simulates the decision-making process of a computer player.

## About the Name "Lig4"
The term "Lig4" is a contraction of "Ligue 4," which is the Brazilian Portuguese equivalent of "Connect 4." The game is known by different names in various regions, and in Brazil, it is commonly referred to as "Ligue 4" or simply "Lig4." The gameplay remains the same, with players aiming to connect four discs of their color in a row.

## Note
This project was developed as part of the curriculum for the Object-Oriented Programming Introduction course, and it may lack certain advanced features found in commercial games. The primary focus is on applying fundamental OOP concepts and principles learned during the course.
