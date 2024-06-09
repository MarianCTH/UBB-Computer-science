from src.domain.RentalDomain import Rental
from datetime import datetime
from src.exceptions.RepositoryExceptions import RepositoryException
from src.services.UndoRedoService import FunctionCall, Operation
class RentalService:
    def __init__(self, client_repository, movie_repository, rental_validator, rental_repository, undo_redo_service):
        self.__client_repository = client_repository
        self.__movie_repository = movie_repository
        self.__rental_repository = rental_repository
        self.__validator = rental_validator
        self.__undo_redo = undo_redo_service

    def add_rental(self, movie_id, client_id, rented_date, due_date, returned_date):
        rental_id = len(self.__rental_repository.get_all()) + 1
        if self.__client_repository.find_one_client(client_id):
            raise RepositoryException("The client doesn't exist !")
        if self.__movie_repository.find_one_movie(movie_id):
            raise RepositoryException("The movie doesn't exist !")

        new_rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__validator.ValidateNewRental(new_rental)
        self.__rental_repository.add_rental(new_rental)

        redo = FunctionCall(self.add_rental, rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        undo = FunctionCall(self.delete_rental, rental_id)
        operation = Operation(redo, undo)
        self.__undo_redo.recordOperation(operation)
    def return_rental(self, rental_id):
        self.__rental_repository.update_rental(rental_id)
        redo = FunctionCall(self.return_rental, rental_id)
        undo = FunctionCall(self.return_rental, rental_id)
        operation = Operation(redo, undo)
        self.__undo_redo.recordOperation(operation)

    def most_rented_movies(self):
        rentals = self.__rental_repository.get_all()
        movies_and_rentals = {}
        unique_movie_ids = set()

        for id, rental in rentals.items():
            movie_id = rental.GetMovieID()
            if movie_id not in unique_movie_ids:
                unique_movie_ids.add(movie_id)
                movies_and_rentals[movie_id] = 0
            movies_and_rentals[movie_id] += 1
        sorted_movies_and_rentals = dict(sorted(movies_and_rentals.items(), key=lambda x: x[1], reverse=True))
        return sorted_movies_and_rentals

    def most_active_clients(self):
        rentals = self.__rental_repository.get_all()
        most_active_clients = {}
        unique_client_ids = set()

        for id, rental in rentals.items():
            client_id = rental.GetClientID()
            if client_id not in unique_client_ids:
                unique_client_ids.add(client_id)
                most_active_clients[client_id] = 0
            rented_date = rental.GetRentedDate()
            due_date_str = rental.GetDueDate()
            due_date = datetime.strptime(due_date_str, "%d/%m/%Y").date()
            rental_days = (due_date - rented_date).days
            most_active_clients[client_id] += rental_days

        sorted_most_active_clients = dict(sorted(most_active_clients.items(), key=lambda x: x[1], reverse=True))
        return sorted_most_active_clients

    def late_rentals(self):
        rentals = self.__rental_repository.get_all()
        late_rentals = {}
        today = datetime.today().date()  # Convert to datetime.date
        unique_movie_id = set()

        for id, rental in rentals.items():
            movie_id = rental.GetMovieID()
            due_date_str = rental.GetDueDate()
            due_date = datetime.strptime(due_date_str, "%d/%m/%Y").date()

            if due_date < today and rental.GetReturnedDate() == "None":
                unique_movie_id.add(movie_id)
                if movie_id not in late_rentals:
                    late_rentals[movie_id] = 0
                rental_days_passed = (today - due_date).days
                late_rentals[movie_id] += rental_days_passed

        return late_rentals

    def delete_all_rentals_from_client(self, client_id):
        rentals_copy = self.__rental_repository.get_all().copy()
        for rental_id, rental in rentals_copy.items():
            if rental.GetClientID() == client_id:
                self.__rental_repository.delete_rental(rental_id)

    def delete_all_rentals_from_movie(self, movie_id):
        rentals_copy = self.__rental_repository.get_all().copy()
        for rental_id, rental in rentals_copy.items():
            if rental.GetMovieID() == movie_id:
                self.__rental_repository.delete_rental(rental_id)
