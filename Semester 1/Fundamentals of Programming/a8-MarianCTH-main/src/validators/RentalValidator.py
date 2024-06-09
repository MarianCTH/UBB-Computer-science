from src.exceptions.ValidatorException import ValidatorException
class RentalValidator:
    def __init__(self):
        pass
    def ValidateNewRental(self, rental):
        errors = ""
        if rental.GetRentalID() < 0:
            errors += "Invalid ID !\n"

        if errors != "":
            raise ValidatorException(errors)