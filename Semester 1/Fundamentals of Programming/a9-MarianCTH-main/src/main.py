from src.repository.ClientRepository import ClientRepository
from src.repository.ClientRepositoryBinary import ClientRepositoryBinary
from src.repository.MovieRepository import MovieRepository
from src.repository.RentalRepository import RentalRepository
from src.repository.RentalRepositoryBinary import RentalRepositoryBinary
from src.services.RentalService import RentalService
from src.services.UndoRedoService import UndoRedoService
from src.validators.ClientValidator import ClientValidator
from src.services.ClientService import ClientService

from src.repository.MovieRepositoryBinary import MovieRepositoryBinary
from src.validators.MovieValidator import MovieValidator
from src.services.MovieService import MovieService

from src.ui.ui import UI
from src.validators.RentalValidator import RentalValidator

def read_settings():
    with open("settings.properties", "r") as file:
        settings = {}
        for line in file:
            key, value = line.strip().split("=")
            settings[key.strip()] = value.strip()
    return settings

def main():
    settings = read_settings()

    if settings.get("repository") == "binaryfiles":
        client_repository = ClientRepositoryBinary(file_path=settings.get("clients"))
        movie_repository = MovieRepositoryBinary(file_path=settings.get("movies"))
        rental_repository = RentalRepositoryBinary(file_path=settings.get("rentals"))
    elif settings.get("repository") == "inmemory":
        client_repository = ClientRepository()
        movie_repository = MovieRepository()
        rental_repository = RentalRepository()
    else:
        raise ValueError("Invalid repository setting in settings.properties")

    undo_redo_service = UndoRedoService()
    client_validator = ClientValidator()
    client_service = ClientService(client_validator, client_repository, undo_redo_service)

    movie_validator = MovieValidator()
    movie_service = MovieService(movie_validator, movie_repository, undo_redo_service)

    rental_validator = RentalValidator()
    rental_service = RentalService(client_repository, movie_repository, rental_validator, rental_repository, undo_redo_service)

    UserInterface = UI(client_service, movie_service, rental_service, undo_redo_service)
    UserInterface.initialize()

if __name__ == "__main__":
    main()