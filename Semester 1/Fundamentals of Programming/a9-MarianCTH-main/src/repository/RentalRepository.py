from src.exceptions.RepositoryExceptions import RepositoryException
from datetime import datetime, date

class RentalRepository:
    def __init__(self):
        self.__rentals = {}

    def add_rental(self, rental):
        if rental.GetRentalID() in self.__rentals:
            raise RepositoryException("Rental already exists !")
        for rental_id in self.__rentals:
            if (self.__rentals[rental_id].GetClientID() == rental.GetClientID() and
                    date.today() > datetime.strptime(self.__rentals[rental_id].GetDueDate(), "%d/%m/%Y").date() and
                    self.__rentals[rental_id].GetReturnedDate() == "None"):
                raise RepositoryException("Client has rented movies that passed their due date for return")

        self.__rentals[rental.GetRentalID()] = rental

    def delete_rental(self, rental_id):
        if rental_id in self.__rentals.keys():
            self.__rentals.pop(rental_id)
        else:
            raise RepositoryException("Rental doesn't exist !")

    def update_rental(self, rental_id):
        if rental_id in self.__rentals.keys():
            new_date = date.today()
            self.__rentals[rental_id].SetReturnedDate(new_date)
        else:
            raise RepositoryException("Rental doesn't exist !")

    def get_all(self):
        return self.__rentals
    def set_all(self, new_rentals):
        self.__rentals = new_rentals
