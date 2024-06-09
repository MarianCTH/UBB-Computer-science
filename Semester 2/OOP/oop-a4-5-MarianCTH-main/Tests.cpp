#include "Tests.h"

void Tests::StartTests(){
	Repository<Movie> repo(51);
	Repository<Movie> watchlist(51);
	Controller c(repo, watchlist);
	
	std::cout << "Testing...\n";
	//test Movie, repository: add, getsize, getmovie
	Movie m1("Test", "Genre", 2023, 5, "Link");
	repo.AddMovie(m1);
	assert(repo.getSize() == 1);
	assert(repo.getMovie(0).getTitle() == "Test");
	assert(repo.getMovie(0).getGenre() == "Genre");
	assert(repo.getMovie(0).getReleaseYear() == 2023);
	assert(repo.getMovie(0).getLikes() == 5);
	assert(repo.getMovie(0).getTrailer() == "Link");

	//test repository update
	Movie m2("Testasd", "Genre", 2023, 5, "Link");
	repo.UpdateMovie(0, m2);
	assert(repo.getMovie(0).getTitle() == "Testasd");

	//test repository remove
	repo.DeleteMovie(0);
	assert(repo.getSize() == 0);

	//test controller add movie, reposize, delete not existing movie
	c.AddMovie("Test", "Genre", 2023, 5, "Link");
	assert(c.getRepositorySize() == 1);
	try {
		c.DeleteMovie("asdg");
	}
	catch (std::exception &e) {
	}
	assert(c.getRepositorySize() == 1);

	//test search movie and search movies
	assert(c.SearchMovie("Te", "title") == 0);
	assert(c.SearchMovie("en", "genre") == 0);
	int size;
	assert(c.getMovie(c.SearchMovies("Te", "title", size)[0]).getTitle() == "Test");

	//add movie to watch list, get movie from watch list
	c.AddMovieToWatchList(m1);
	assert(c.getMovieFromWatchList(0).getTitle() == "Test");

	//test delete movie from watch list not existing
	try {
		c.DeleteMovieFromWatchList("asdg", 0);
		assert(c.getWatchListSize() == 1);
	}
	catch (std::exception& e) {
	}

	//test movie likes from repository after deleting the movie from watch list
	assert(c.getMovie(0).getLikes() == 5);
	c.DeleteMovieFromWatchList("Te", 1); // 1 for increasing the likes
	assert(c.getWatchListSize() == 0);
	assert(c.getMovie(0).getLikes() == 6);
}