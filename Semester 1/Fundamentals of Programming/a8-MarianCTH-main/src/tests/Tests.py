from unittest import TestCase
from src.repository.RentalRepository import RentalRepository
from src.repository.MovieRepository import MovieRepository
from src.repository.ClientRepository import ClientRepository
from src.exceptions.RepositoryExceptions import RepositoryException
from src.domain.ClientDomain import Client
from src.domain.MovieDomain import Movie
from src.domain.RentalDomain import Rental

class TestClientRepository(TestCase):
    def setUp(self):
        self.client_repository = ClientRepository()

    def test_add_client(self):
        client = Client(client_id=1, name="John Doe")
        self.client_repository.add_client(client)
        self.assertEqual(self.client_repository.find_one_client(1), client)

    def test_add_existing_client(self):
        client = Client(client_id=1, name="John Doe")
        self.client_repository.add_client(client)
        with self.assertRaises(RepositoryException):
            self.client_repository.add_client(client)

    def test_delete_client(self):
        client = Client(client_id=1, name="John Doe")
        self.client_repository.add_client(client)
        self.client_repository.delete_client(1)
        with self.assertRaises(RepositoryException):
            self.client_repository.find_one_client(1)

    def test_update_client(self):
        client = Client(client_id=1, name="John Doe")
        self.client_repository.add_client(client)
        self.client_repository.update_client(1, "Jane Doe")
        updated_client = self.client_repository.find_one_client(1)
        self.assertEqual(updated_client.GetID(), 1)
        self.assertEqual(updated_client.GetName(), "Jane Doe")

class TestMovieRepository(TestCase):
    def setUp(self):
        self.movie_repository = MovieRepository()

    def test_add_movie(self):
        movie = Movie(movie_id=1, title="Inception")
        self.movie_repository.add_movie(movie)
        self.assertEqual(self.movie_repository.find_one_movie(1), movie)

    def test_add_existing_movie(self):
        movie = Movie(movie_id=1, title="Inception")
        self.movie_repository.add_movie(movie)
        with self.assertRaises(RepositoryException):
            self.movie_repository.add_movie(movie)

    def test_delete_movie(self):
        movie = Movie(movie_id=1, title="Inception")
        self.movie_repository.add_movie(movie)
        self.movie_repository.delete_movie(1)
        with self.assertRaises(RepositoryException):
            self.movie_repository.find_one_movie(1)

    def test_update_movie(self):
        movie = Movie(movie_id=1, title="Inception")
        self.movie_repository.add_movie(movie)
        self.movie_repository.update_movie(1, "Interstellar")
        updated_movie = self.movie_repository.find_one_movie(1)
        self.assertEqual(updated_movie.GetID(), 1)
        self.assertEqual(updated_movie.GetTitle(), "Interstellar")

class TestRentalRepository(TestCase):
    def setUp(self):
        self.rental_repository = RentalRepository()

    def test_add_rental(self):
        client = Client(client_id=1, name="John Doe")
        movie = Movie(movie_id=1, title="Inception")
        rental = Rental(rental_id=1, client=client, movie=movie, due_date="01/01/2024")
        self.rental_repository.add_rental(rental)
        self.assertEqual(self.rental_repository.get_all()[1], rental)

    def test_add_existing_rental(self):
        client = Client(client_id=1, name="John Doe")
        movie = Movie(movie_id=1, title="Inception")
        rental = Rental(rental_id=1, client=client, movie=movie, due_date="01/01/2024")
        self.rental_repository.add_rental(rental)
        with self.assertRaises(RepositoryException):
            self.rental_repository.add_rental(rental)

    def test_update_rental(self):
        client = Client(client_id=1, name="John Doe")
        movie = Movie(movie_id=1, title="Inception")
        rental = Rental(rental_id=1, client=client, movie=movie, due_date="01/01/2024")
        self.rental_repository.add_rental(rental)
        self.rental_repository.update_rental(1)
        updated_rental = self.rental_repository.get_all()[1]
        self.assertIsNotNone(updated_rental.GetReturnedDate())
