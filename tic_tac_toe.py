from re import search


class Board():
    """Define the board in TIC TAC TOE"""
    def __init__(self):
        self.reset_board()
        self.score = {"O":0, "X":0, "T":0}
        self.winning_patterns = [["1", "2","3"], ["4", "5","6"], ["7", "8", "9"], ["7", "4", "1"], ["8", "5", "2"],["9", "6", "3"], ["7", "5", "3"], ["9", "5", "1"]]

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
                self.compare_board()
                if self.turn == 'X':
                    self.turn = 'O'
                    break
                else:
                    self.turn = 'X'
                    break

    def check_new_game(self):
        while True:
            new_game = input ("Play another game? (y/n)")
            if new_game.lower() == 'n':
                self.game_active = False
            elif new_game.lower() == 'y':
                self.reset_board()
                self.game_active = True
            return

    def compare_board(self):
        if ' ' not in self.board.values():
            self.update_scores('T')
            self.game_active = False
            return
        for cells in self.winning_patterns:
            if self.check_win(cells):
                self.update_scores('W')
                self.game_active = False

    def check_win(self, cells):
        first = self.board[cells[0]]
        if first == ' ':
            return False
        for cell in cells:
            if self.board[cell] != first:
                return False
        return True

    def update_scores(self, result):
        if result == 'W':
            print(self.turn + " wins the game.")
            self.score[self.turn] += 1
        elif result == 'T':
            print ("This game is a tie.")
            self.score['T'] += 1


def main():
    # Define initial variables
    the_board = Board()

    while the_board.game_active:
        the_board.print_board()
        the_board.chose_move()
        if not the_board.game_active:
            the_board.check_new_game()

    print("\n--------------------------------")
    results = "X wins:{:2}  O wins:{:2}  Ties:{:2}".format(the_board.score['X'], the_board.score['O'], the_board.score['T'])
    print(results)
    print("--------------------------------")

main()
