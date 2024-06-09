#include "Repository.h"
#include "Movie.h"

template class Repository<Movie>;

template <typename T>
Repository<T>::Repository(std::string file_name) {
	try {
		this->file_name = file_name;
	}
	catch (std::runtime_error& e) {
		std::cout << e.what();
	}
}

template <typename T>
Repository<T>::Repository(const Repository<T>& v) {
	this->movies = v.movies;
}

template <typename T>
int Repository<T>::getSize() const{
	return this->movies.size();
}

template <typename T>
T Repository<T>::getMovie(int index) const{
	return this->movies[index];
}

template <typename T>
void Repository<T>::AddMovie(T m) {
	this->movies.push_back(m);
	this->SaveDataToFile();
}

template <typename T>
void Repository<T>::DeleteMovie(int index) {
	this->movies.erase(this->movies.begin() + index);
	this->SaveDataToFile();
}

template <typename T>
void Repository<T>::UpdateMovie(int index, T m) {
	this->movies[index] = m;
	this->SaveDataToFile();
}

template <typename T>
Repository<T>::~Repository() {
}

template <typename T>
void Repository<T>::LoadDataFromFile() {
	std::ifstream file(this->file_name);

	if (!file.is_open())
		throw std::runtime_error("File could not be opened!");

	Movie m;
	while (file >> m) {
		this->movies.push_back(m);
	}

	file.close();
}

template <typename T>
void Repository<T>::SaveDataToFile() {
	std::ofstream file(this->file_name);

	if (!file.is_open())
	{
		return;
	}

	for (auto m : this->movies) {
		file << m.getTitle() << ", "
			<< m.getGenre() << ", "
			<< m.getReleaseYear() << ", "
			<< m.getLikes() << ", "
			<< m.getTrailer() << "\n";
	}
	file.close();
}
