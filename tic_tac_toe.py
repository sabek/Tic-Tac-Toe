from re import search


class Board():
    """Define the board in TIC TAC TOE"""
    def __init__(self):
        self.reset_board()
        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0
#        self.winning_patterns = ([1,2,3], [4,5,6], [7, 8, 9])

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
        self.game_active = True

    def chose_move(self):
        while True:
            move = input(self.turn + "'s turn. Select a space 1-9,or q to end the game: ")
            if move == 'q':
                self.game_active = False
                return
            elif search("[1-9]", move) is None or len(move) > 1:
                print("That is an invalid move")
            elif self.board[move] != ' ':
                print("That space is taken by " + self.board[move] + ".")
            else:
                self.board[move] = self.turn
                self.check_win()
                self.check_tie()
                if self.turn == 'X':
                    self.turn = 'O'
                    break
                else:
                    self.turn = 'X'
                    break

    def check_game_end(self):
        while True:
            new_game = input ("Play another game? (y/n)")
            if new_game.lower() == 'n':
                self.game_active = False
            elif new_game.lower() == 'y':
                self.reset_board()
                self.game_active = True
            return

    def check_tie(self):
        if ' ' not in self.board.values():
            self.update_scores(self, 'T')

    def check_win(self):
        if self.board['1'] == self.board['2'] == self.board['3'] and self.board['1'] != ' ':
            self.update_scores('W')
        elif self.board['4'] == self.board['5'] == self.board['6'] and self.board['4'] != ' ':
            self.update_scores('W')
        elif self.board['7'] == self.board['8'] == self.board['9'] and self.board['7'] != ' ':
            self.update_scores('W')
        elif self.board['7'] == self.board['4'] == self.board['1'] and self.board['7'] != ' ':
            self.update_scores('W')
        elif self.board['8'] == self.board['5'] == self.board['2'] and self.board['8'] != ' ':
            self.update_scores('W')
        elif self.board['9'] == self.board['6'] == self.board['3'] and self.board['9'] != ' ':
            self.update_scores('W')
        elif self.board['7'] == self.board['5'] == self.board['3'] and self.board['7'] != ' ':
            self.update_scores('W')
        elif self.board['9'] == self.board['5'] == self.board['1'] and self.board['9'] != ' ':
            self.update_scores('W')
        else:
            return
        self.game_active = False

    def update_scores(self, result):
        if result == 'W':
            print(self.turn + " wins the game.")
            if self.turn == 'X':
                self.x_wins += 1
            elif self.turn == 'O':
                self.o_wins += 1
        elif result == 'T':
            print ("This game is a tie.")
            self.ties += 1


def main():
    # Define initial variables
    the_board = Board()

    while the_board.game_active:
        the_board.print_board()
        the_board.chose_move()
        if not the_board.game_active:
            the_board.check_game_end()

    print("\n--------------------------------")
    results = "X wins: {:2}  O wins: {:2}  Ties: {:2}".format(the_board.x_wins, the_board.o_wins, the_board.ties)
    print(results)
    print("--------------------------------")

main()
