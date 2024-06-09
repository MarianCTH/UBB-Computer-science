#include "Controller.h"

Controller::Controller(Repository<Movie> movieRepository, WatchListRepository watchlist) : repository(movieRepository), watchList(watchlist) {
}

void Controller::AddMovie(std::string title, std::string genre, int release_year, int likes, std::string trailer) {
	Movie m(title, genre, release_year, likes, trailer);
	this->repository.AddMovie(m);
}

void Controller::DeleteMovie(std::string title) {
	int found_id = this->SearchMovie(title, "title");
	if (found_id != -1)
		this->repository.DeleteMovie(found_id);
	else throw std::exception("Movie not found !");
}

void Controller::UpdateMovie(std::string title, std::string new_title, std::string new_genre, int new_release_year, int new_likes, std::string new_trailer) {
	int found_id = this->SearchMovie(title, "title");

	if (found_id != -1) {
		Movie m(new_title, new_genre, new_release_year, new_likes, new_trailer);
		this->repository.UpdateMovie(found_id, m);
	}
	else throw std::exception("Movie not found !");

}

int Controller::getRepositorySize() {
	return this->repository.getSize();
}

int Controller::getWatchListSize() {
	return this->watchList.getSize();
}

Movie Controller::getMovie(int index) {
	return this->repository.getMovie(index);
}

Movie Controller::getMovieFromWatchList(int index) {
	return this->watchList.getMovie(index);
}

int Controller::SearchMovie(std::string string_to_search, std::string type) {
	for (int i = 0; i < this->getRepositorySize(); i++) {
		if (type == "title") {
			std::string movieTitle = this->getMovie(i).getTitle();
			if (movieTitle.find(string_to_search) != std::string::npos) {
				return i;
			}
		}
		else if (type == "genre") {
			std::string movieGenre = this->getMovie(i).getGenre();
			if (movieGenre.find(string_to_search) != std::string::npos) {
				return i;
			}
		}
	}
	return -1;
}

int* Controller::SearchMovies(std::string string_to_search, std::string type, int& size) {
	int* found_movies = new int[this->getRepositorySize()];
	size = 0;
	found_movies[size] = -1;
	for (int i = 0; i < this->getRepositorySize(); i++) {
		if (type == "title") {
			std::string movieTitle = this->getMovie(i).getTitle();
			if (movieTitle.find(string_to_search) != std::string::npos) {
				found_movies[size++] = i;
			}
		}
		else if (type == "genre") {
			std::string movieGenre = this->getMovie(i).getGenre();
			if (movieGenre.find(string_to_search) != std::string::npos) {
				found_movies[size++] = i;
			}
		}
	}
	return found_movies;
}

void Controller::AddMovieToWatchList(Movie m1) {
	this->watchList.AddMovie(m1);
}

int Controller::SearchMovieWatchList(std::string string_to_search, std::string type) {
	for (int i = 0; i < this->getWatchListSize(); i++) {
		if (type == "title") {
			std::string movieTitle = this->getMovieFromWatchList(i).getTitle();
			if (movieTitle.find(string_to_search) != std::string::npos) {
				return i;
			}
		}
	}
	return -1;
}

void Controller::DeleteMovieFromWatchList(std::string title, int like) {
	int found_id = this->SearchMovieWatchList(title, "title");
	if (found_id != -1)
	{
		this->watchList.DeleteMovie(found_id);
		Movie m = this->repository.getMovie(this->SearchMovie(title, "title"));
		m.setLikes(m.getLikes() + like);
//		this->repository.UpdateMovie(found_id, m);
	}
	else throw std::exception("Movie not found !\n");
}

std::string Controller::getFileTypeFromRepo() {
	return this->watchList.getFileType();
}

std::string Controller::getFileNameFromRepo() {
	return this->watchList.getFileName();
}