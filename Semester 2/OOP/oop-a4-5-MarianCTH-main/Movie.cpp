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
	os << movie.title << " "
		<< "Genre: " << movie.genre << " "
		<< "Release Year: " << movie.release_year << " "
		<< "Likes: " << movie.likes << " "
		<< "Trailer: " << movie.trailer << "\n";
	return os;
}