#pragma once
#include "Movie.h"

template <typename T>
class Repository {
    T* movies;
    int size;
    int capacity;
public:
    Repository(int capacity);
    Repository(const Repository<T>&);
    void AddMovie(T m);
    void DeleteMovie(int id);
    void UpdateMovie(int id, T m);
    int getSize();
    T getMovie(int index);
    ~Repository();
private:
    void resize(int);
};