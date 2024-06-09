#include "Movie.h"

Movie::Movie() {
}
Movie::Movie(std::string title, std::string genre, int release_year, int likes, std::string trailer) {
	this->title = title;
	this->genre = genre;
	this->release_year = release_year;
	this->likes = likes;
	this->trailer = trailer;
}

int Movie::getLikes() {
	return this->likes;
}
std::string Movie::getTitle() {
	return this->title;
}
std::string Movie::getGenre() {
	return this->genre;
}
int Movie::getReleaseYear() {
	return this->release_year;
}
std::string  Movie::getTrailer() {
	return this->trailer;
}

void Movie::setLikes(int likes) {
	this->likes = likes;
}
void Movie::setTitle(const std::string& title) {
	this->title = title;
}
void Movie::setGenre(const std::string& genre) {
	this->genre = genre;
}
void Movie::setReleaseYear(int release_year) {
	this->release_year = release_year;
}
void Movie::setTrailer(const std::string& trailer) {
	this->trailer = trailer;
}
std::ostream& operator<<(std::ostream& os, const Movie& movie) {
	os << movie.title << ", "
		<< movie.genre << ", "
		<< movie.release_year << ", "
		<< movie.likes << ", "
		<< movie.trailer << "\n";
	return os;
}
std::istream& operator>>(std::istream& is, Movie& movie) {
	std::string title, genre, trailer;
	int release_year, likes;

	std::getline(is, title, ',');
	std::getline(is, genre, ',');
	is >> release_year;
	is.ignore();
	is >> likes;
	is.ignore();
	std::getline(is, trailer, '\n');

	movie.setTitle(title);
	movie.setGenre(genre);
	movie.setReleaseYear(release_year);
	movie.setLikes(likes);
	movie.setTrailer(trailer);

	return is;
}