#include "UserUI.h"

UserUI::UserUI(Controller controller) : controller(controller) {

}

void UserUI::displayMenu() {
    std::cout << "[1] Search movies by genre\n[2] Delete movie from watch list \n[3] See watch list\n[4] Exit\n>> ";
}

void UserUI::Init() {
    while (true) {
        displayMenu();

        int choice;
        try {
            std::cin >> choice;
        }
        catch (std::exception& e) {
            std::cout << e.what();
        }

        switch (choice) {
        case SEARCH_BY_GENRE: {
            std::string genre;
            std::cout << "Please enter the genre: ";
            std::cin >> genre;
            if (genre == "") {
                std::cout << "Movies:\n";
                for (int i = 0; i < this->controller.getRepositorySize(); i++) {
                    std::cout << i + 1 << ". " << this->controller.getMovie(i);
                }
            }
            else {
                int found_movies_size;
                int* found_movies = this->controller.SearchMovies(genre, "genre", found_movies_size);
                if (found_movies[0] == -1) {
                    std::cout << "No movies found with the genre " << genre << "\n";
                }
                else {
                    for (int i = 0; i < found_movies_size; i++) {
                        Movie m = this->controller.getMovie(found_movies[i]);
                        std::cout << "Title: " << m.getTitle() << "\n";
                        std::cout << "Genre: " << m.getGenre() << "\n";
                        std::cout << "Release year: " << m.getReleaseYear() << "\n";
                        std::cout << "Likes: " << m.getLikes() << "\n";
                        std::cout << "Trailer: " << m.getTrailer() << "\n";
                        system(("start " + m.getTrailer()).c_str());

                        int choice3;
                        std::cout << "\n Do you want to add the movie to the watch list?\n[1] Yes\n[2] Next\n[3] Exit search\n>> ";
                        std::cin >> choice3;
                        if (choice3 == 1) {
                            this->controller.AddMovieToWatchList(m);
                        }
                        else if (choice3 == 2)
                        {
                            if (i == found_movies_size - 1)
                                i = 0;
                        }
                        else if (choice3 == 3)
                        {
                            delete[] found_movies;
                            break;
                        }
                    }
                }
            }
            break;
        }
        case DELETE_MOVIE_WATCH_LIST: {
            std::string title;
            int like;
            std::cout << "Please enter the title of the movie you want to delete from the watch list: ";
            try {
                std::cin >> title;
                std::cout << "Did you like the movie?\n[1] Yes\n[2] No\n>> ";
                std::cin >> like;
                if (like == 1)
                    this->controller.DeleteMovieFromWatchList(title, 1);
                else if (like == 2)
                    this->controller.DeleteMovieFromWatchList(title, 0);

                std::cout << "Movie deleted from watch list\n";
            }
            catch (std::exception& e) {
                std::cout << e.what();
            }

            break;
        }
        case SEE_WATCH_LIST: {
            std::cout << "Movies:\n";
            for (int i = 0; i < this->controller.getWatchListSize(); i++) {
                std::cout << i + 1 << ". " << this->controller.getMovieFromWatchList(i);
            }
            break;
        }
        case EXIT:
            exit(1);
        default:
            std::cout << "Invalid choice\n";
            break;
        }
    }
}