#include "AdminUI.h"

AdminUI::AdminUI(Controller controller) : controller(controller) {

}

void AdminUI::displayMenu() {
    std::cout << "\n[1] Add movie\n[2] Delete movie\n[3] Update movie\n[4] Show all movies\n[5] Exit\n>> ";
}

void AdminUI::Init() {
    while (true) {
        displayMenu();

        int choice;
        std::cin >> choice;

        switch (choice) {
        case ADD: {
            int release_year, likes = 0;
            std::string title, genre, trailer;

            std::cout << "Title: "; std::cin >> title;
            std::cout << "Genre: "; std::cin >> genre;
            std::cout << "Release Year: "; std::cin >> release_year;
            std::cout << "Trailer: "; std::cin >> trailer;

            this->controller.AddMovie(title, genre, release_year, likes, trailer);
            std::cout << "Movie added sucessfully !\n";
            break;
        }
        case DELETE: {
            std::string title;
            std::cout << "The movie you want to remove (title): "; std::cin >> title;
            try {
                this->controller.DeleteMovie(title);
                std::cout << "Movie deleted sucessfully !\n";
            }
            catch (std::exception& e) {
                std::cout << e.what();
            }

            break;
        }
        case UPDATE: {
            std::string title, new_title, new_genre, new_trailer;
            int new_release_year, new_likes;

            std::cout << "The movie you want to update (title): "; std::cin >> title;
            std::cout << "New title: "; std::cin >> new_title;
            std::cout << "New Genre: "; std::cin >> new_genre;
            std::cout << "New Release Year: "; std::cin >> new_release_year;
            std::cout << "New Trailer: "; std::cin >> new_trailer;
            std::cout << "New Likes: "; std::cin >> new_likes;

            try {
                this->controller.UpdateMovie(title, new_title, new_genre, new_release_year, new_likes, new_trailer);
                std::cout << "Movie deleted sucessfully !\n";
            }
            catch (std::exception& e) {
                std::cout << e.what();
            }

            break;
        }
        case SHOW_ALL: {
            std::cout << "Movies:\n";
            for (int i = 0; i < this->controller.getRepositorySize(); i++) {
                std::cout << i + 1 << ". " << this->controller.getMovie(i);
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