from exceptions.Game import GameException

START_GAME = 1
QUIT_GAME = 2
PLAYER_ONE = 1
PLAYER_TWO = 2


class Console:
    def __init__(self, game):
        self.__game = game

    @staticmethod
    def print_menu():
        print("Welcome to Battleship!")
        print("1. Start Game")
        print("2. Quit")

    @staticmethod
    def get_menu_choice():
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in [START_GAME, QUIT_GAME]:
                    return choice
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def start(self):
        while True:
            self.print_menu()
            player_choice = self.get_menu_choice()

            if player_choice == START_GAME:
                print(f"\n\n\nHi, {self.__game.get_player_name(PLAYER_ONE)} !")

                self.__game.place_ships(PLAYER_ONE)
                self.__game.place_ships(PLAYER_TWO)
                while True:
                    print("Here's your board: ")
                    print(self.__game.get_player_hidden_board(PLAYER_ONE))
                    print(self.__game.get_player_board(PLAYER_ONE))
                    try:
                        first_player_move_response = self.__game.make_player_move(input("Please enter your move: "),
                                                                                  "First")
                        print(f"{self.__game.get_player_name(PLAYER_ONE)}: {first_player_move_response} !")
                        second_player_move_response = self.__game.make_player_move("", "Second")
                        print(f"{self.__game.get_player_name(PLAYER_TWO)}: {second_player_move_response} !")

                        if self.__game.get_player_name_win() == self.__game.get_player_name(PLAYER_ONE):
                            print("You WIN !")
                            break
                        elif self.__game.get_player_name_win() == self.__game.get_player_name(PLAYER_TWO):
                            print("You lost !")
                            break
                    except GameException as GE:
                        print(f"Game error: {GE}")
            elif player_choice == QUIT_GAME:
                print("Game ended!")
                break
