#pragma once
#include "Repository.h"
#include "Movie.h"

class WatchListRepository : public Repository<Movie>{
private:
	std::string file_name;
	std::string file_type;
	void SaveDataToFile() override;
public:
	WatchListRepository(std::string file_name) : Repository(file_name){
		this->file_name = file_name;
	}
	void setFileName(const std::string&);
	void setFileType(const std::string&);
	std::string getFileType();
	std::string getFileName();
	~WatchListRepository() {}
};