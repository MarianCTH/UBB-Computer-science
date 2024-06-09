#pragma once
#include <string>
#include <iostream>

class Movie {
	std::string title;
	std::string genre;
	int release_year;
	int likes;
	std::string trailer;

public:
	Movie();
	Movie(std::string, std::string, int, int, std::string);

	int getLikes();
	int getReleaseYear();
	std::string getTitle();
	std::string getGenre();
	std::string getTrailer();

	void setLikes(int likes);
	void setTitle(const std::string& title);
	void setGenre(const std::string& genre);
	void setReleaseYear(int release_year);
	void setTrailer(const std::string& trailer);

	friend std::ostream& operator<<(std::ostream& os, const Movie& movie);
};