from src.exceptions.RepositoryExceptions import RepositoryException
from src.exceptions.ValidatorException import ValidatorException
from src.ui.MenuStructure import *
from datetime import date
from src.exceptions.UndoRedoExceptions import *

class UI:
    def __init__(self, ClientService, MovieService, RentalService, UndoRedoService):
        self.__client_service = ClientService
        self.__movie_service = MovieService
        self.__rental_service = RentalService
        self.__undo_redo_service = UndoRedoService

    def ShowMenuOptions(self):
        for key, value in MenuOptions.items():
            print(f"{key} - {value['Title']}")

    def initialize(self):
        while True:
            print("")
            self.ShowMenuOptions()

            UserInput = input("Please choose an option:\n>> ")
            print("")
            if UserInput in MenuOptions:
                selected_menu = MenuOptions[UserInput]

                for key, value in selected_menu.items():
                    if key != "Title":
                        print(f"{key} - {value}")

                SecondUserInput = input(">> ")
                print("")
                if MenuOptions[UserInput]["Title"] == ManageClientOrMovies:
                    if selected_menu[SecondUserInput] == ManageClients:
                        print(ADD + ": Add client\n" +
                              REMOVE + ": Remove client\n" +
                              UPDATE + ": Update client\n" +
                              LIST + ": List clients")
                        CRUD_USER_INPUT = input(">> ")
                        if CRUD_USER_INPUT == ADD:
                            try:
                                client_id = int(input("ID: "))
                                name = input("Name: ")
                                self.__client_service.add_client(client_id, name)
                                print("Client added successfully !")
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                            except ValidatorException as ve:
                                print(f"Validator error: {ve}")
                        elif CRUD_USER_INPUT == REMOVE:
                            try:
                                client_id = int(input("ID: "))
                                self.__client_service.delete_client(client_id)
                                self.__rental_service.delete_all_rentals_from_client(client_id)
                                print("Client removed successfully !")
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        elif CRUD_USER_INPUT == UPDATE:
                            try:
                                client_id = int(input("ID: "))
                                new_client_name = input("New name: ")
                                self.__client_service.update_client(client_id, new_client_name)
                                print("Client updated successfully !")
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        elif CRUD_USER_INPUT == LIST:
                            try:
                                for key, client_object in self.__client_service.list_clients():
                                    print(client_object)
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        else:
                            print("Invalid user input !")
                    elif selected_menu[SecondUserInput] == ManageMovies:
                        print(ADD + ": Add movie\n" +
                              REMOVE + ": Remove movie\n" +
                              UPDATE + ": Update movie\n" +
                              LIST + ": List movies")
                        CRUD_USER_INPUT = input(">> ")
                        if CRUD_USER_INPUT == ADD:
                            try:
                                movie_id = int(input("ID: "))
                                title = input("Title: ")
                                description = input("Description: ")
                                genre = input("Genre: ")
                                self.__movie_service.add_movie(movie_id, title, description, genre)
                                print("Movie added successfully !")
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                            except ValidatorException as ve:
                                print(f"Validator error: {ve}")
                        elif CRUD_USER_INPUT == REMOVE:
                            try:
                                movie_id = int(input("ID: "))
                                self.__movie_service.delete_movie(movie_id)
                                self.__rental_service.delete_all_rentals_from_movie(movie_id)
                                print("Movie removed successfully !")
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        elif CRUD_USER_INPUT == UPDATE:
                            try:
                                movie_id = int(input("ID: "))
                                new_movie_title = input("New title: ")
                                self.__movie_service.update_movie(movie_id, new_movie_title)
                                print("Movie updated successfully !")
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        elif CRUD_USER_INPUT == LIST:
                            try:
                                for key, movie_object in self.__movie_service.list_movies():
                                    print(movie_object)
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        else:
                            print("Invalid user input !")
                    else:
                        print("Invalid user input !")

                elif MenuOptions[UserInput]["Title"] == RentOrReturn:
                    if selected_menu[SecondUserInput] == RentAMovie:
                        try:
                            movie_id = int(input("Movie ID: "))
                            client_id = int(input("Client ID: "))
                            rented_date = date.today()
                            due_date = input("Due date: ")
                            returned_date = "None"
                            self.__rental_service.add_rental(movie_id, client_id, rented_date, due_date, returned_date)
                            print("Rental made successfully !")
                        except ValueError as ve:
                            print(f"Value error: {ve}")
                        except RepositoryException as re:
                            print(f"Repository error: {re}")
                        except ValidatorException as ve:
                            print(f"Validator error: {ve}")
                    elif selected_menu[SecondUserInput] == ReturnAMovie:
                        try:
                            rental_id = int(input("Rental ID: "))
                            self.__rental_service.return_rental(rental_id)
                            print("Return made successfully !")
                        except ValueError as ve:
                            print(f"Value error: {ve}")
                        except RepositoryException as re:
                            print(f"Repository error: {re}")
                    else:
                        print("Invalid user input !")

                elif MenuOptions[UserInput]["Title"] == Search:
                    print("Search by:")
                    if selected_menu[SecondUserInput] == SearchForClient:
                        for key, value in SearchByClient.items():
                            print(f"{key}: {value}")
                        SEARCH_BY_INPUT = input(">> ")

                        if SearchByClient[SEARCH_BY_INPUT] == CLIENT_ID:
                            try:
                                client_id = int(input("Client ID: "))
                                print(self.__client_service.search(client_id, None))
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        elif SearchByClient[SEARCH_BY_INPUT] == CLIENT_NAME:
                            try:
                                client_name = input("Client Name: ")
                                for clients_found in self.__client_service.search(None, client_name):
                                    print(clients_found)
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                    elif selected_menu[SecondUserInput] == SearchForMovie:
                        for key, value in SearchByMovie.items():
                            print(f"{key} : {value}")
                        SEARCH_BY_INPUT = input(">> ")
                        if SearchByMovie[SEARCH_BY_INPUT] == MOVIE_ID:
                            try:
                                movie_id = int(input("Movie ID: "))
                                print(self.__movie_service.search(movie_id, None, None, None))
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        elif SearchByMovie[SEARCH_BY_INPUT] == MOVIE_TITLE:
                            try:
                                movie_title = input("Movie Title: ")
                                for movies_found in self.__movie_service.search(None, movie_title, None, None):
                                    print(movies_found)
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        elif SearchByMovie[SEARCH_BY_INPUT] == MOVIE_DESCRIPTION:
                            try:
                                movie_description = input("Movie Description: ")
                                for movies_found in self.__movie_service.search(None, None, movie_description, None):
                                    print(movies_found)
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                        elif SearchByMovie[SEARCH_BY_INPUT] == MOVIE_GENRE:
                            try:
                                movie_genre = input("Movie Genre: ")
                                for movies_found in self.__movie_service.search(None, None, None, movie_genre):
                                    print(movie_genre)
                            except ValueError as ve:
                                print(f"Value error: {ve}")
                            except RepositoryException as re:
                                print(f"Repository error: {re}")
                    else:
                        print("Invalid user input !")

                elif MenuOptions[UserInput]["Title"] == Statistics:
                    if selected_menu[SecondUserInput] == MostRentedMovies:
                        try:
                            most_rented_movies_dict = self.__rental_service.most_rented_movies()

                            for movie_id, rental_times in most_rented_movies_dict.items():
                                print(f"{self.__movie_service.find_one_movie(movie_id)} - Rental Times: {rental_times}")
                        except RepositoryException as re:
                            print(f"Repository error: {re}")
                    elif selected_menu[SecondUserInput] == MostActiveClients:
                        try:
                            most_active_clients_dict = self.__rental_service.most_active_clients()
                            for client_id, rental_days in most_active_clients_dict.items():
                                print(f"{self.__client_service.find_one_client(client_id)} - Rental Days: {rental_days}")
                        except RepositoryException as re:
                            print(f"Repository error: {re}")
                    elif selected_menu[SecondUserInput] == LateRentals:
                        try:
                            late_rentals = self.__rental_service.late_rentals()
                            for movie_id, rental_days_passed in late_rentals.items():
                                print(f"{self.__movie_service.find_one_movie(movie_id)} - Rental Times: {rental_days_passed}")
                        except RepositoryException as re:
                            print(f"Repository error: {re}")
                    else:
                        print("Invalid user input !")

                elif MenuOptions[UserInput]["Title"] == Others:
                    if selected_menu[SecondUserInput] == Undo:
                        try:
                            self.__undo_redo_service.undo()
                            print("Undo made successfully !")
                        except UndoException as ue:
                            print(f"Undo exception: {ue}")
                    elif selected_menu[SecondUserInput] == Redo:
                        try:
                            self.__undo_redo_service.redo()
                            print("Redo made successfully !")
                        except RedoException as re:
                            print(f"Undo exception: {re}")
            else:
                print("Invalid user input !")


