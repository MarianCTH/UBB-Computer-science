import random
import texttable
from Ship.Ship import Ship


class Board:
    def __init__(self, size):
        self.__size = size
        self.__grid = [[" "] * size for _ in range(size)]
        self.__ships = [Ship(5), Ship(3), Ship(3), Ship(2), Ship(2)]

    def __str__(self):
        table = texttable.Texttable()

        array = [" "]
        for index in range(self.__size):
            array.append(chr(65 + index))
        table.header(array)

        for index in range(self.__size):
            row = [str(index + 1)] + self.__grid[index]
            table.add_row(row)
        return table.draw()

    def get_board_size(self):
        return self.__size

    def get_grid(self):
        return self.__grid

    def set_square(self, line, column, value):
        if 1 <= line <= self.__size and 1 <= column <= self.__size:
            self.__grid[line - 1][column - 1] = value
        else:
            raise ValueError("Invalid coordinates. Please provide valid line and column.")

    def get_square(self, line, column):
        if 1 <= line <= self.__size and 1 <= column <= self.__size:
            return self.__grid[line - 1][column - 1]
        else:
            raise ValueError("Invalid coordinates. Please provide valid line and column.")

    @staticmethod
    def check_place(x, y, direction, size, board):
        if direction == "up":
            for i in range(size):
                if x - i < 0:
                    return False
                if board[x - i][y] != ' ':
                    return False
        elif direction == "down":
            for i in range(size):
                if x + i >= len(board):
                    return False
                if board[x + i][y] != ' ':
                    return False
        elif direction == "left":
            for i in range(size):
                if y - i < 0:
                    return False
                if board[x][y - i] != ' ':
                    return False
        elif direction == "right":
            for i in range(size):
                if y + i >= len(board[0]):
                    return False
                if board[x][y + i] != ' ':
                    return False
        return True

    @staticmethod
    def place(x, y, direction, size, board):
        if direction == "up":
            for i in range(size):
                board[x-i][y] = "S"
        elif direction == "down":
            for i in range(size):
                board[x+i][y] = "S"
        elif direction == "left":
            for i in range(size):
                board[x][y-i] = "S"
        elif direction == "right":
            for i in range(size):
                board[x][y+i] = "S"

    def place_ships(self):
        for ship in self.__ships:
            while True:
                x = random.randint(0, self.__size - 1)
                y = random.randint(0, self.__size - 1)
                direction = random.choice(["up", "down", "left", "right"])
                if self.check_place(x, y, direction, ship.size, self.__grid):
                    self.place(x, y, direction, ship.size, self.__grid)
                    break

    def check_board_ships_not_existing(self):
        for row in self.__grid:
            if "S" in row:
                return False
        return True

    def make_board_table(self, given_board):
        table = texttable.Texttable()

        array = [" "]
        for index in range(self.__size):
            array.append(chr(65 + index))
        table.header(array)

        for index in range(self.__size):
            row = [str(index + 1)] + given_board[index]
            table.add_row(row)
        return table.draw()

    def to_normal(self):
        return self.__grid