#include "Repository.h"
#include "Movie.h"

template class Repository<Movie>;

template <typename T>
Repository<T>::Repository(int capacity) {
	this->size = 0;
	this->capacity = capacity;
	this->movies = new T[capacity];
}

template <typename T>
Repository<T>::Repository(const Repository<T>& v) {
	this->size = v.size;
	this->capacity = v.capacity;
	this->movies = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->movies[i] = v.movies[i];
}

template <typename T>
int Repository<T>::getSize() {
	return this->size;
}

template <typename T>
T Repository<T>::getMovie(int index) {
	return this->movies[index];
}

template <typename T>
void Repository<T>::resize(int factor) {
	this->capacity *= factor;

	T* els = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		els[i] = this->movies[i];

	delete[] this->movies;
	this->movies = els;
}

template <typename T>
void Repository<T>::AddMovie(T m) {
	if (this->size == this->capacity)
		this->resize(2);
	this->movies[this->size] = m;
	this->size++;
}

template <typename T>
void Repository<T>::DeleteMovie(int index) {
	for (int i = index; i < this->size - 1; i++) {
		this->movies[i] = this->movies[i + 1];
	}
	this->size--;
}

template <typename T>
void Repository<T>::UpdateMovie(int index, T m) {
	this->movies[index] = m;
}

template <typename T>
Repository<T>::~Repository() {
	delete[] this->movies;
}