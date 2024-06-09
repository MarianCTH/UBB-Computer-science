class Rental:
    def __init__(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        self.__rental_id = rental_id
        self.__movie_id = movie_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__returned_date = returned_date

    def GetRentalID(self):
        return self.__rental_id
    def GetMovieID(self):
        return self.__movie_id
    def GetClientID(self):
        return self.__client_id
    def GetRentedDate(self):
        return self.__rented_date
    def GetDueDate(self):
        return self.__due_date
    def GetReturnedDate(self):
        return self.__returned_date
    def SetReturnedDate(self, new_date):
        self.__returned_date = new_date