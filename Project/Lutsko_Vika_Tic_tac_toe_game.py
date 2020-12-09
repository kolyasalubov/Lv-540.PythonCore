# import time library for using function time.sleep()
import time


# function creates list for storing '0' or 'X'
def create_list():

    board = []
    for x in range(0, 9):
        board.append(str(x + 1))
    return board


# function displays game board
def print_board(board):

    print('\n -----')
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print(' -----')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print(' -----')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print(' -----\n')


# function asks start info from players
def input_player_info():

    player_1 = input('Player 1 please enter your name:\n').capitalize()
    print('Hi', player_1, '!')
    player_2 = input('Player 2 please enter your name:\n').capitalize()
    print('Hi', player_2, '!')
    mark_1 = input('Player 1 please choose X or O:\n').upper()
    while mark_1 not in ['X', '0']:
        mark_1 = input('Player 1 please choose X or O:\n').upper()
    if mark_1 == 'X':
        mark_2 = '0'
    elif mark_1 == '0':
        mark_2 = 'X'
    print(player_1, 'plays:', mark_1)
    print(player_2, 'plays:', mark_2)
    print('Please wait...')
    time.sleep(3)
    return player_1, player_2, mark_1, mark_2


# function checks winning and draw conditions
def check_win(board):

    # horizontal winning conditions
    if board[0] == board[1] == board[2] and board[0] != ' ':
        game = 'win'
    elif board[3] == board[4] == board[5] and board[3] != ' ':
        game = 'win'
    elif board[6] == board[7] == board[8] and board[6] != ' ':
        game = 'win'

    # vertical winning conditions
    elif board[0] == board[3] == board[6] and board[0] != ' ':
        game = 'win'
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        game = 'win'
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        game = 'win'

    # diagonal winning conditions
    elif board[0] == board[4] == board[8] and board[4] != ' ':
        game = 'win'
    elif board[2] == board[4] == board[6] and board[4] != ' ':
        game = 'win'

    # draw condition
    elif (board[0] != '1' and board[1] != '2' and board[2] != '3' and board[3] != '4'
          and board[4] != '5' and board[5] != '6' and board[6] != '7'
          and board[7] != '8' and board[8] != '9'):
        game = 'draw'
    else:
        game = 'playing'
    return game


def check_if_is_turn_valid():

    turn = int(input('Please chose square:(1-9)\n'))
    while turn not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        turn = int(input('Please chose square:(1-9)\n'))
    return turn


# function asks want player play again
def resume_game():

    start = input('''Do you want to continue?\n Please enter Y or N:\n''').upper()
    while start not in ['Y', 'N']:
        start = input('Please enter Y or N:\n').upper()
    if start == 'N':
        print('Good Bay!')
        return False
    else:
        return True


print('Welcome to Tic Tac Toe!')
player_one, player_two, mark_one, mark_two = input_player_info()
start_game = True

# GAME PLAY
while start_game:

    if start_game:

        game_board = create_list()  # reload game board
        game_result = 'playing'
        player_turn_count = 1

        while game_result == 'playing':
            # update game board
            print_board(game_board)
            # player’s turn
            if (player_turn_count % 2) != 0:
                print(player_one, 'your turn:')
                mark = mark_one
            else:
                print(player_two, 'your turn:')
                mark = mark_two
            player_turn = check_if_is_turn_valid()
            # check is square free or occupied
            if game_board[player_turn - 1] == 'X' or game_board[player_turn - 1] == '0':
                print('Chose another square!')
            # put mark on board
            else:
                game_board[player_turn - 1] = mark
            # looking winning or draw conditions
            game_result = check_win(game_board)
            # switch player's turn
            player_turn_count += 1
            # this part run if found draw condition
            if game_result == 'draw':
                print_board(game_board)
                print('Game draw')
                start_game = resume_game()
                break
            # this part run if found winning conditions
            if game_result == 'win':
                print_board(game_board)
                if mark == 'X':
                    print(player_one, 'Won!!!')
                    start_game = resume_game()
                    break
                else:
                    print(player_two, 'Won!!!')
                    start_game = resume_game()
                    break
            else:
                continue










