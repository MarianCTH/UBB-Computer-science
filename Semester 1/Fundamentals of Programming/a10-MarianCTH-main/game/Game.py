from exceptions.Game import GameException
import random


PLAYER_ONE = 1
PLAYER_TWO = 2


class Game:
    def __init__(self, first_player_board, second_player_board, first_player, second_player):
        self.__first_player_board = first_player_board
        self.__first_player = first_player

        self.__second_player_board = second_player_board
        self.__second_player = second_player

    def get_player_board(self, player_index):
        if player_index == PLAYER_ONE:
            return self.__first_player_board
        elif player_index == PLAYER_TWO:
            return self.__second_player_board

    def get_player_name(self, player_index):
        if player_index == PLAYER_ONE:
            return self.__first_player.get_name()
        elif player_index == PLAYER_TWO:
            return self.__second_player.get_name()

    def place_ships(self, player_index):
        if player_index == PLAYER_ONE:
            self.__first_player_board.place_ships()
        elif player_index == PLAYER_TWO:
            self.__second_player_board.place_ships()

    def get_board_size(self):
        return self.__first_player_board.get_board_size()

    def make_player_move(self, move, turn):
        if turn == "First":
            if 2 <= len(move) <= 3:
                allowed_lines = [str(i) for i in range(1, self.__first_player_board.get_board_size() + 1)]
                allowed_columns = [chr(65 + i) for i in range(self.__first_player_board.get_board_size())]

                literal = move[0].upper()
                if len(move) == 2:
                    number = move[1:]
                else:
                    number = move[1] + move[2]
                if literal not in allowed_columns or number not in allowed_lines:
                    raise GameException("Invalid move. Please try again !")

                column = ord(literal.upper()) - ord('A') + 1
                line = int(number)

                if self.__second_player_board.get_square(line, column) == "S":
                    self.__second_player_board.set_square(line, column, "X")
                    return "HIT"
                elif self.__second_player_board.get_square(line, column) == ' ':
                    self.__second_player_board.set_square(line, column, "M")
                    return "MISS"
                elif (self.__second_player_board.get_square(line, column) == 'M' or
                      self.__second_player_board.get_square(line, column) == 'X'):
                    return "You've already tried this one"
            else:
                raise GameException("Invalid move. Please try again !")
        elif turn == "Second":
            random_line = random.randint(1, 10)
            random_column = random.randint(1, 10)
            if self.__first_player_board.get_square(random_line, random_column) == "S":
                self.__first_player_board.set_square(random_line, random_column, "H")
                return "HIT"
            elif self.__first_player_board.get_square(random_line, random_column) == ' ':
                self.__first_player_board.set_square(random_line, random_column, "X")
                return "MISS"
            elif (self.__second_player_board.get_square(random_line, random_column) == 'X' or
                  self.__second_player_board.get_square(random_line, random_column) == 'H'):
                return "You've already tried this one"

    def get_player_name_win(self):
        if self.__first_player_board.check_board_ships_not_existing():
            return self.__first_player.get_name()
        elif self.__second_player_board.check_board_ships_not_existing():
            return self.__second_player.get_name()

    def get_player_hidden_board(self, player_index):
        size = self.__first_player_board.get_board_size()
        hidden_board = [[" "] * size for _ in range(size)]

        for line in range(1, size + 1):
            for column in range(1, size + 1):
                if player_index == PLAYER_ONE:
                    if self.__second_player_board.get_square(line, column) == "S":
                        hidden_board[line - 1][column - 1] = " "
                    else:
                        hidden_board[line - 1][column - 1] = self.__second_player_board.get_square(line, column)
                elif player_index == PLAYER_TWO:
                    if self.__first_player_board.get_square(line, column) == "S":
                        hidden_board[line - 1][column - 1] = " "
                    else:
                        hidden_board[line - 1][column - 1] = self.__first_player_board.get_square(line, column)

        return self.__first_player_board.make_board_table(hidden_board)

    def get_player_hidden_board_as_list(self, player_index):
        size = self.__first_player_board.get_board_size()
        hidden_board = [[" "] * size for _ in range(size)]

        for line in range(1, size + 1):
            for column in range(1, size + 1):
                if player_index == PLAYER_ONE:
                    if self.__second_player_board.get_square(line, column) == "S":
                        hidden_board[line - 1][column - 1] = " "
                    else:
                        hidden_board[line - 1][column - 1] = self.__second_player_board.get_square(line, column)
                elif player_index == PLAYER_TWO:
                    if self.__first_player_board.get_square(line, column) == "S":
                        hidden_board[line - 1][column - 1] = " "
                    else:
                        hidden_board[line - 1][column - 1] = self.__first_player_board.get_square(line, column)

        return hidden_board
