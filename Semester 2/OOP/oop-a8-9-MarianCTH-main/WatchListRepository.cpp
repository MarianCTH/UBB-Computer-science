#include "WatchListRepository.h"

void WatchListRepository::SaveDataToFile() {
	std::ofstream file(this->file_name);
	if (!file.is_open())
		throw std::runtime_error("File could not be opened!");

	if (this->file_type == "csv") {
		for (auto m : this->movies) {
			file << m.getTitle() << ", "
				<< m.getGenre() << ", "
				<< m.getReleaseYear() << ", "
				<< m.getLikes() << ", "
				<< m.getTrailer() << "\n";
		}
	}
	else if (this->file_type == "html") {
		file << "<!DOCTYPE html><html><head><title>Movie watch list</title></head><body><table border='1'>";
		file << "<tr><td>Title</td><td>Genre</td><td>Release year</td><td>Likes</td><td>Trailer</td></tr>";
		for (auto m : this->movies) {
			file << "<tr>" 
					<< "<td>" << m.getTitle() << "</td>"
					<< "<td>" << m.getGenre() << ", "
					<< "<td>" << m.getReleaseYear() << "</td>"
					<< "<td>" << m.getLikes() << "</td>"
					<< "<td>" << m.getTrailer() << "</td>"
				<< "</tr>";
		}
		file << "</table></body></html>";
	}

	file.close();
}

void WatchListRepository::setFileName(const std::string& file_name) {
	this->file_name = file_name;
}

void WatchListRepository::setFileType(const std::string& file_type) {
	this->file_type = file_type;
}

std::string WatchListRepository::getFileType() {
	return this->file_type;
}

std::string WatchListRepository::getFileName() {
	return this->file_name;
}