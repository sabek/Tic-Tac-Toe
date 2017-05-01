from re import search


class Board():
    """Define the board in TIC TAC TOE"""
    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}
        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0
        self.turn = 'X'
        self.game_active = True

    def print_board(self):
        print(self.board['7'] + "|" + self.board['8'] + "|" + self.board['9'])
        print('-+-+-')
        print(self.board['4'] + "|" + self.board['5'] + "|" + self.board['6'])
        print('-+-+-')
        print(self.board['1'] + "|" + self.board['2'] + "|" + self.board['3'])

    def reset_board(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}
        self.turn = 'X'


def chose_move(board):
    while True:
        move = input(board.turn + "'s turn. Select a space 1-9,or q to end the game: ")
        if move == 'q':
            board.game_over = True
            return
        elif search("[1-9]", move) is None:
            print("That is an invalid move")
        elif board.board[move] != ' ':
            print("That space is taken by " + board.board[move] + ".")
        else:
            board.board[move] = board.turn

            if board.turn == 'X':
                board.turn = 'O'
                break
            else:
                board.turn = 'X'
                break
    return


def check_win(board):
    if board.board['1'] == board.board['2'] == board.board['3'] and board.board['1'] != ' ':
        board.game_active = False
        update_scores(board, board.board['1'], 'W')
        return
    elif board.board['4'] == board.board['5'] == board.board['6'] and board.board['4'] != ' ':
        board.game_active = False
        update_scores(board, board.board['4'], 'W')
        return
    elif board.board['7'] == board.board['8'] == board.board['9'] and board.board['7'] != ' ':
        board.game_active = False
        update_scores(board, board.board['7'], 'W')
        return
    elif board.board['7'] == board.board['4'] == board.board['1'] and board.board['7'] != ' ':
        board.game_active = False
        update_scores(board, board.board['7'], 'W')
        return
    elif board.board['8'] == board.board['5'] == board.board['2'] and board.board['8'] != ' ':
        update_scores(board, board.board['8'], 'W')
        board.game_active = False
        return
    elif board.board['9'] == board.board['6'] == board.board['3'] and board.board['9'] != ' ':
        update_scores(board, board.board['9'], 'W')
        board.game_active = False
        return
    elif board.board['7'] == board.board['5'] == board.board['3'] and board.board['7'] != ' ':
        update_scores(board, board.board['7'], 'W')
        board.game_active = False
        return
    elif board.board['9'] == board.board['5'] == board.board['1'] and board.board['9'] != ' ':
        update_scores(board, board.board['9'], 'W')
        board.game_active = False
        return
    elif ' ' not in board.board.values():
        board.game_active = False
        update_scores(board, ' ', 'T')
        return
    else:
        return


def update_scores(board, player, result):
    if result == 'W':
        print(player + " wins the game.")
        if player == 'X':
            board.x_wins += 1
        elif player == 'O':
            board.o_wins += 1
    elif result == 'T':
        print ("This game is a tie.")
        board.ties += 1
    return


def check_game_end(board):
    while True:
        new_game = input ("Play another game? (y/n)")
        if new_game.lower() == 'n':
            board.game_active = False
            return
        elif new_game.lower() == 'y':
            board.reset_board()
            board.game_active = True
            return


# Define initial variables
theBoard = Board()

while theBoard.game_active:
    theBoard.print_board()
    chose_move(theBoard)
    check_win(theBoard)
    if not theBoard.game_active:
        check_game_end(theBoard)

results = "X wins: {} O wins: {} Ties: {}".format(theBoard.x_wins, theBoard.o_wins, theBoard.ties)
print(results)
