import random
import sys
from os import system, name
from time import sleep
 
# welcome title with animations
welcome_message = "Welcome to My Ultimate Tic_Tac_Toe game!\n"

for x in welcome_message:
    print(x, end='')
    sys.stdout.flush()
    sleep(.2)
    
game_instructions = ['Please read instructions carefully to play the game:',
'- The game is displayed as a 3X3 grid',
'- The user(you) will start the game and is denoted with the letter "O"',
'- The computer (opposition) is denoted by the letter "X"',
'- To place your letter type a number between 1-9',
'- This will choose a position on the board.',
'- You can win either horizontally, vertically or diagonally!',
'- If all 9 spaces are full and no one has won',
'- The game  ends in a tie and there will be no winner',
'- The first among the players who have 3 same symbols in a line. ']

for i in game_instructions:
    print(i)
    sys.stdout.flush()
    sleep(.2)

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


#variables
game_on = True

game_list = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']

#game setup dictionary
board = {'a1':' ','a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ','c2':' ','c3':' '}

current_player = 1 
comp_move = ''
 
def reset_game():
	
    global game_list
    global board
    global current_player
    global comp_move
    
    # Resets game
    game_list = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
    board = {'a1':' ','a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ','c2':' ','c3':' '}
    current_player = 1
    comp_move = ''
 
def display_board(board):
    # BOARD  EXAMPLE
    #      
    #       |   |   
    # 3   X | O |   
    #    ___|___|___
    #       |   |   
    # 2   O | X |   
    #    ___|___|___
    #       |   |   
    # 1   O |   | X 
    #       |   |   
    #     a   b   c
    
    # 
    
    print('     |   |   ')
    print('3  ' + board.get('a3') + ' | '+ board.get('b3') + ' | ' + board.get('c3') + ' ')
    print('  ___|___|___')
    print('     |   |   ')
    print('2  ' + board.get('a2') + ' | '+ board.get('b2') + ' | ' + board.get('c2') + ' ')
    print('  ___|___|___')
    print('     |   |   ')
    print('1  ' + board.get('a1') + ' | '+ board.get('b1') + ' | ' + board.get('c1') + ' ')
    print('     |   |   ')
    print('   a   b   c ')
 
def clear():
	# Clears screen
	
	# Clears for Windows
	if name == 'nt':
		_ = system('cls')
	
	# Clears for mac and linux
	else:
		_ = system('clear')
 
def position_choice(player):
    # Ask for choice
 
    global game_list
    global board
    global current_player
    
    valid_choice = False
    choice = ''
    count = 0
    
    # Checks user choice
    while not valid_choice:
        choice = input(f'Player {current_player}, choose a position by typing the row and column (e.g. a1, b3, c2): ')
        if choice in game_list:
            valid_choice = True
        else:
            print('Try again, not a valid choice!')
    
    # Updates the board with the player's choice with X or O
    board[choice] = player
    
    # pops out chosen choice from list of available choices
    for x in game_list:
        if choice == x:
            game_list.pop(count)
            break
        else:
            count += 1
 
def gameon_choice(x):
    # Ask to either restart game or not
 
    continue_playing = ['YES','NO', 'Y', 'N']
    result = ''
    continue_check = False
    
    while not continue_check:
        result = input('Would you like to play again? Yes or No?: ').upper()
        if result in continue_playing:
            if result == 'YES' or 'Y':
                x = True
            else:
                x = False
            continue_check = True
        else:
            print('Sorry, not a valid choice!')
    return x
 
def gameover_check(game_list,board):
    # Check for win if board is full
    if not game_list:
        return True
    else:
        return victory_check(board)


#check for victory 
def victory_check(board):
   
    if board['a1'] != " " and board['a1'] == board['a2'] and board['a1'] == board['a3']:
        return True
    elif board['b1'] != " " and board['b1'] == board['b2'] and board['b1'] == board['b3']:
        return True
    elif board['c1'] != " " and board['c1'] == board['c2'] and board['c1'] == board['c3']:
        return True
    elif board['a1'] != " " and board['a1'] == board['b1'] and board['a1'] == board['c1']:
        return True
    elif board['a2'] != " " and board['a2'] == board['b2'] and board['a2'] == board['c2']:
        return True
    elif board['a3'] != " " and board['a3'] == board['b3'] and board['a3'] == board['c3']:
        return True
    elif board['a1'] != " " and board['a1'] == board['b2'] and board['a1'] == board['c3']:
        return True
    elif board['a3'] != " " and board['a3'] == board['b2'] and board['a3'] == board['c1']:
        return True
    else:
        return False
 
 
 #switch player
def switch_player(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player


#moves 
def computer_move():

    global board
    global comp_move
    global game_list
    
    count = 0
    move_found = False
    
    # Clear previous move
    comp_move = ''
    
    while not move_found:
        if check_comp_win(game_list,board):
            move_found = True
            break
        elif block_player(game_list,board):
            move_found = True
            break
    
        # Will check if any corners are available for the computer
        elif take_corner(game_list):
            move_found = True
            break
    
        # will check center if other places are filled
        elif take_center(game_list):
            move_found = True
            break
    
        # check for available space
        elif take_any(game_list):
            move_found = True
            break
    
    # Computer move 
    board[comp_move] = 'O'
    
    # Remove from available spaces
    for x in game_list:
        if x == comp_move:
            game_list.pop(count)
            break
        else:
            count += 1
 
 
 #check for win
def check_comp_win(game_list,board):
    
    global comp_move
    
    for x in game_list:
        board[x] = 'O'
        
        if victory_check(board):
            comp_move = x
            return True
        else:
            board[x] = ' '
    return False


#block player 
def block_player(game_list,board):
    global comp_move
    
    # Will determine if a computer lost
    for x in game_list:
        board[x] = 'X'
        
        # If victory resets the board space and continue for all remaining options.
        if victory_check(board):
            comp_move = x
            return True
        else:
            board[x] = ' '
    return False
 
def take_corner(game_list):
    global comp_move
    
    temp_list = []
    
    # Computer determines if a corner is available and picks it
    for x in game_list:
        if x == 'a1' or x == 'a3' or x == 'c1' or x == 'c3':
            temp_list.append(x)
    
    # Checks if any of the corners are available.
    if len(temp_list) == 0:
    	return False
    else:
    	random.shuffle(temp_list)
    	comp_move = temp_list[0]
    	return True
 
def take_center(game_list):

    global comp_move
    
    # Checks if the center ('b2')
    if 'b2' in game_list:
        comp_move = 'b2'
        return True
    else:
        return False
 
def take_any(game_list):
    global comp_move
    
    # Randomize the game_list to grab a random corner for the computer to choose
    random.shuffle(game_list)
    
    # Computer determines if a corner is available and chooses it
    for x in game_list:
        comp_move = x
        return True
 
# Player 1 = 'X' and Computer = 'O'
 
# Resets the game values and displays the current board
reset_game()
clear()
display_board(board) 
game_on = True # Allows someone to restart the game
 
# Loop to continue the game
while game_on:
    # Checks the player move and updates the board
    if current_player == 1:
        position_choice('X')
    else:
        # Have run Computer here
        sleep(2)
        computer_move()
    
    clear()
    display_board(board)
    
    # Checks if the game is over and if the game is over will output if Tie or Winner
    if gameover_check(game_list,board):
        if victory_check(board) and current_player == 1:
            print(f"Congratulations! Player {current_player} is the Winner!")
        elif victory_check(board) and current_player == 2:
            print(f"The computer has won! Player 1 has been defeated!")
        else:
            print("The game ended in a Tie")
        
        reset_game() 
        game_on = gameon_choice(game_on) 
        current_player = switch_player(current_player) 
        
        # If playing again will display the new board, clear board
        if game_on:
            clear()
            display_board(board)
        else:
            print('Thank you for playing ❤️!')
            
    # Switches player turn to the next player
    current_player = switch_player(current_player)