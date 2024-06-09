from src.exceptions.ValidatorException import ValidatorException
class MovieValidator:
    def __init__(self):
        pass
    def ValidateNewMovie(self, new_movie):
        errors = ""
        if new_movie.GetID() < 0:
            errors += "Invalid ID !\n"
        if new_movie.GetTitle() == "":
            errors += "Invalid title !\n"
        if new_movie.GetDescription() == "":
            errors += "Invalid description !\n"
        if new_movie.GetGenre() == "":
            errors += "Invalid genre !\n"

        if errors != "":
            raise ValidatorException(errors)
