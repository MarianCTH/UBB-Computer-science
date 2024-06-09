#pragma once
#include "Movie.h"
#include <vector>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>

template <typename T>
class Repository {
protected:
    std::vector<T> movies;
    std::string file_name;
public:
    Repository(std::string file_name);
    Repository(const Repository<T>&);
    void AddMovie(T m);
    void DeleteMovie(int id);
    void UpdateMovie(int id, T m);
    int getSize() const;
    T getMovie(int index) const;
    virtual void LoadDataFromFile();
    ~Repository();
private:
	virtual void SaveDataToFile();
};