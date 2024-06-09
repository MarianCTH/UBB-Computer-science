import pickle
from src.exceptions.RepositoryExceptions import RepositoryException
from datetime import datetime, date
class RentalRepository:
    def __init__(self):
        self.__rentals = {}
        self.__file_name = "data/rents.bin"
        self.__load_file()

    def __load_file(self):
        try:
            read_file = open(self.__file_name, "rb")
            self.__rentals = pickle.load(read_file)
            read_file.close()
        except EOFError:
            self.__rentals = {}
    def __save_file(self):
        file_write = open(self.__file_name, "wb")
        pickle.dump(self.__rentals, file_write)
        file_write.close()

    def add_rental(self, rental):
        if rental.GetRentalID() in self.__rentals:
            raise RepositoryException("Rental already exists !")
        for rental_id in self.__rentals:
            if (self.__rentals[rental_id].GetClientID() == rental.GetClientID() and
                    date.today() > datetime.strptime(self.__rentals[rental_id].GetDueDate(), "%d/%m/%Y").date() and
                    self.__rentals[rental_id].GetReturnedDate() == "None"):
                raise RepositoryException("Client has rented movies that passed their due date for return")

        self.__rentals[rental.GetRentalID()] = rental
        self.__save_file()
    def update_rental(self, rental_id):
        if rental_id in self.__rentals.keys():
            new_date = date.today()
            self.__rentals[rental_id].SetReturnedDate(new_date)
            self.__save_file()
        else:
            raise RepositoryException("Rental doesn't exist !")
    def get_all(self):
        return self.__rentals
