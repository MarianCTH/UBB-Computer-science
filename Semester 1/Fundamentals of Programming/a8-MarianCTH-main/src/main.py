from src.repository.ClientRepository import ClientRepository
from src.repository.RentalRepository import RentalRepository
from src.services.RentalService import RentalService
from src.validators.ClientValidator import ClientValidator
from src.services.ClientService import ClientService

from src.repository.MovieRepository import MovieRepository
from src.validators.MovieValidator import MovieValidator
from src.services.MovieService import MovieService

from src.ui.ui import UI
from src.validators.RentalValidator import RentalValidator


def main():
    client_repository = ClientRepository()
    client_validator = ClientValidator()
    client_service = ClientService(client_validator, client_repository)

    movie_repository = MovieRepository()
    movie_validator = MovieValidator()
    movie_service = MovieService(movie_validator, movie_repository)

    rental_repository = RentalRepository()
    rental_validator = RentalValidator()
    rental_service = RentalService(rental_validator, rental_repository)

    UserInterface = UI(client_service, movie_service, rental_service)
    UserInterface.initialize()

if __name__ == "__main__":
    main()