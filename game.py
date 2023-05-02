'''importing modules'''
from time import sleep  # welcome message animation
import sys  # to access parameters and functions
import random  # computers turn

# welcome title with animations
welcome_message = "Welcome to My Ultimate Tic_Tac_Toe game!\n"

for x in welcome_message:
    print(x, end='')
    sys.stdout.flush()
    sleep(.1)

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winner = None
name = None
current_player = "O"
game_running = True


def print_board(board):

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# print game instructions


game_instructions = '''

Please read instructions carefully to play the game: \n
- The game is displayed as a 3X3 grid
- The user(you) will start the game and is denoted with the letter 'O'
- The computer (opposition) is denoted by the letter 'X'
- To place your letter type a number between 1-9
- This will choose a position on the board.
- You can win either horizontally, vertically or diagonally!
- If all 9 spaces are full and no one has won,
- The game  ends in a tie and there will be no winner
- The first among the players who have 3 same symbols in a line.

                           1 | 2 |  3
                          ------------
                           4 | 5  | 6
                          ------------
                           7 | 8  | 9
                           '''
print(game_instructions)


# Enter player's names
def valid_name():
    '''
    Gets player name and only accept letters.
    '''
    print("What is your name?")
    while True:
        name = input("My name is: ")
        if not name.isalpha():
            print("Invalid Entry Enter only letters.")
            continue

        else:
            print(f"Welcome {name}!")
            break
    return name


valid_name()


def start_game():
    '''
    asks the user to enter 's' so the game can start
    '''
    while True:
        start_game_input = input("Type 'S' Start the game:\n").lower()
        if start_game_input == 's':
            game_starting = 'The Game is starting...'
            print(game_starting, end="\r")
            sleep(1)
            print(" " * len(game_starting), end="\r")
            sleep(1)
            break
        else:
            print(f"{start_game_input}Invalid,press 'S' to start the game.")


start_game()



def player_input(board):
    while True:
        try:
            
           inp = int(input("Enter a number 1-9: "))
           if inp >= 1 and inp <= 9 and board[inp-1] == "-":
               board[inp-1] = current_player
               break
           else:
               print("The spot is Occupied!")
           switch_player()
        except ValueError:
            print ("Invalid entry Please enter From ")



# checking possible winning options
def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_diagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("The game is a Tie!")
        game_running = False

        return_to_main_page()


# switching player 'O' to computer 'X'
def switch_player():
    global current_player
    if current_player == "O":
        current_player = "X"
    else:
        current_player = "O"


# computer
def computer(board):
    while current_player == "X":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "X"
            switch_player()


# check to see who the winner is
def check_win(board):
    if check_row(board) or check_diagonally(board) or check_horizontal(board):
        print_board(board)
        if winner == 'O':
            print("You are the winner!")
        elif winner == 'X':
            print("The computer has won")

        return_to_main_page()

# clear the board if user want to play again


def reset_board():
    '''
    Resets the board if user wants to play again
    '''
    board.clear()
    board.extend([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])


def return_to_main_page():
    
    '''
    Ask the users if they want to Exit the game
    '''
    print("*** Game Over *** \n")
    print("Enter 'q' Would you like to End the game  \n")
    while True:
        global name
        make_a_choice = input().strip()
        if make_a_choice.lower() == 'q':
            sys.exit("Thanks For Playing.")
        else:
            start_game()


while game_running:
    print_board(board)
    player_input(board)
    check_win(board)
    check_tie(board)
    switch_player()
    computer(board)
    check_tie(board)

  

