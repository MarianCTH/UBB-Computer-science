from tkinter import *
from tkinter import messagebox
PLAYER_ONE = 1
PLAYER_TWO = 2


class GUI:
    def __init__(self, game):
        self.__game = game
        self.__window = Tk()
        self.style_window()

    def style_window(self):
        self.__window.geometry("1000x700")

    def clear_grid(self):
        for widget in self.__window.winfo_children():
            widget.destroy()

    def start_game(self):
        self.clear_grid()

        self.__game.place_ships(PLAYER_ONE)
        self.__game.place_ships(PLAYER_TWO)
        self.show_player_table(column_offset=0)
        self.show_table_spacer(column_offset=self.__game.get_board_size())
        self.show_hidden_table(column_offset=self.__game.get_board_size() + 1)

    def show_table_spacer(self, column_offset):
        spacer_label = Label(self.__window, text=" ", width=5, height=2)
        spacer_label.grid(row=0, column=column_offset, rowspan=self.__game.get_board_size() * 2, sticky="nsew")

    def show_player_table(self, column_offset):
        for i in range(self.__game.get_board_size()):
            for j in range(self.__game.get_board_size()):
                cell_value = self.__game.get_player_board(PLAYER_ONE).to_normal()[i][j]
                button = Button(self.__window,
                                text=cell_value,
                                width=5,
                                height=2,
                                command="")
                button.grid(row=i,
                            column=j + column_offset,
                            sticky="nsew",
                            padx=2,
                            pady=2)

    def show_hidden_table(self, column_offset):
        for i in range(self.__game.get_board_size()):
            for j in range(self.__game.get_board_size()):
                cell_value = self.__game.get_player_hidden_board_as_list(PLAYER_ONE)[i][j]
                button = Button(self.__window,
                                text=cell_value,
                                width=5,
                                height=2,
                                command=lambda i=i, j=j: self.handle_button_click(chr(65 + j) + str(i+1)))
                button.grid(row=i,
                            column=j + column_offset,
                            sticky="nsew",
                            padx=2,
                            pady=2)

    def handle_button_click(self, move):
        self.clear_grid()

        if self.__game.get_player_name_win() == self.__game.get_player_name(PLAYER_ONE):
            self.show_alert("You WIN !")

        elif self.__game.get_player_name_win() == self.__game.get_player_name(PLAYER_TWO):
            self.show_alert("You lost !")

        self.__game.make_player_move(move, "First")
        self.__game.make_player_move("", "Second")

        self.show_player_table(column_offset=0)
        self.show_table_spacer(column_offset=self.__game.get_board_size())
        self.show_hidden_table(column_offset=self.__game.get_board_size() + 1)

    def show_alert(self, message):
        messagebox.showinfo("Game Over", message)
        self.__window.destroy()

    def start(self):
        self.intro_label = Label(self.__window,
                                 text=f"Welcome to Battleship!",
                                 font=("Arial", 16))
        self.intro_label.grid(row=1, column=0, columnspan=3)

        self.start_game_button = Button(self.__window,
                                        text="Start Game",
                                        command=lambda: self.start_game(),
                                        width=15,
                                        font=("Arial", 14))
        self.start_game_button.grid(row=2, column=0, columnspan=3)

        self.__window.mainloop()
