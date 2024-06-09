#pragma once
#include "Movie.h"
#include "Repository.h"

class Action {
public:
	virtual void executeUndo() = 0;
	virtual void executeRedo() = 0;
};

class ActionAdd : public Action {
	int addedMovieIndex;
	Movie addedMovie;
	Repository<Movie> &repo;
public:
	ActionAdd(int addedMovieIndex, Movie addedMovie, Repository<Movie>& repo) : addedMovieIndex{ addedMovieIndex }, addedMovie{ addedMovie }, repo{ repo } {}
	void executeUndo() override;
	void executeRedo() override;
};

class ActionRemove : public Action {
	int removedMovieIndex;
	Movie removedMovie;
	Repository<Movie> repo;
public:
	ActionRemove(int removedMovieIndex, Movie removedMovie, Repository<Movie>& repo) : removedMovieIndex{ removedMovieIndex }, removedMovie{ removedMovie }, repo{ repo } {}
	void executeUndo() override;
	void executeRedo() override;
};

class ActionUpdate : public Action {
	int movieIndex;
	Movie oldMovie;
	Movie newMovie;
	Repository<Movie> repo;
public:
	ActionUpdate(int movieIndex, Movie oldMovie, Movie newMovie, Repository<Movie>& repo) : movieIndex{ movieIndex }, oldMovie{ oldMovie }, newMovie{ newMovie }, repo{ repo } {}
	void executeUndo() override;
	void executeRedo() override;
};;