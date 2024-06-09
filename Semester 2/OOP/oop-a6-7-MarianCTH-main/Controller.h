#pragma once
#include "Movie.h"
#include "Repository.h"
#include "WatchListRepository.h"
#include <string>

class Controller {
	Repository<Movie> repository;
	WatchListRepository watchList;
public:
	Controller(Repository<Movie>, WatchListRepository);
	int SearchMovie(std::string, std::string);
	int SearchMovieWatchList(std::string, std::string);
	int* SearchMovies(std::string, std::string, int&);
	void AddMovie(std::string title, std::string genre, int release_year, int likes, std::string trailer);
	void DeleteMovie(std::string title);
	void UpdateMovie(std::string title, std::string new_title, std::string new_genre, int new_release_year, int new_likes, std::string new_trailer);
	int getRepositorySize();
	int getWatchListSize();
	Movie getMovie(int index);
	Movie getMovieFromWatchList(int index);
	void AddMovieToWatchList(Movie);
	void DeleteMovieFromWatchList(std::string title, int);
	std::string getFileTypeFromRepo();
	std::string getFileNameFromRepo();
};