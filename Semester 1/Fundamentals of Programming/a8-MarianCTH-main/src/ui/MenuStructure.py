ManageClientOrMovies = "Manage clients and movies"
ManageClients = "Manage clients"
ManageMovies = "Manage movies"
ADD = "1"
REMOVE = "2"
UPDATE = "3"
LIST = "4"

RentOrReturn = "Rent or return a movie"
RentAMovie = "Rent a movie"
ReturnAMovie = "Return a movie"

Search = "Search for clients or movies"
SearchForClient = "Search for client"
CLIENT_ID = "Client ID"
CLIENT_NAME = "Client Name"
SearchForMovie = "Search for movie"
MOVIE_ID = "Movie ID"
MOVIE_TITLE = "Movie Title"
MOVIE_DESCRIPTION = "Movie Description"
MOVIE_GENRE = "Movie Genre"

Statistics = "Statistics"
MostRentedMovies = "Most rented movies"
MostActiveClients = "Most active clients"
LateRentals = "All the movies that are currently rented, for which the due date for return has passed"

MenuOptions = {
    "1": {
        "Title": ManageClientOrMovies,
        "1": ManageClients,
        "2": ManageMovies
    },
    "2": {
        "Title": RentOrReturn,
        "1": RentAMovie,
        "2": ReturnAMovie
    },
    "3": {
        "Title": Search,
        "1": SearchForClient,
        "2": SearchForMovie
    },
    "4": {
        "Title": Statistics,
        "1": MostRentedMovies,
        "2": MostActiveClients,
        "3": LateRentals
    }
}
SearchByClient = {
    "1": CLIENT_ID,
    "2": CLIENT_NAME
}
SearchByMovie = {
    "1": MOVIE_ID,
    "2": MOVIE_TITLE,
    "3": MOVIE_DESCRIPTION,
    "4": MOVIE_GENRE
}
ClientCRUD = {
    "1": "Add client",
    "2": "Remove client",
    "3": "Update client",
    "4": "List clients"
}
MovieCRUD = {
    "1": "Add movie",
    "2": "Remove movie",
    "3": "Update movie",
    "4": "List movies"
}
