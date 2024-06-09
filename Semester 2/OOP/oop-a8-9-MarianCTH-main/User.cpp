#include "MoviesWGUI.h"

void MoviesWGUI::showUserMenu() {
	ui.chooseAction1_2->show();
	ui.searchMovie->show();
	ui.deleteFromWatchList->show();
	ui.seeWatchList->show();
	ui.openWatchList->show();
	ui.ExitForUser->show();
}

void MoviesWGUI::hideUserMenu() {
	ui.chooseAction1_2->hide();
	ui.searchMovie->hide();
	ui.deleteFromWatchList->hide();
	ui.seeWatchList->hide();
	ui.openWatchList->hide();
	ui.ExitForUser->hide();
}

void MoviesWGUI::hideSearchMovieForm() {
	ui.genreSearch->hide();
	ui.sendSearchMovies->hide();
    ui.textCout->hide();
    ui.yesAdd->hide();
    ui.noAdd->hide();
    ui.exitSearch->hide();
}

void MoviesWGUI::showSearchMovieForm() {
	ui.genreSearch->show();
	ui.sendSearchMovies->show();
}

void MoviesWGUI::showDeleteFromWatchListForm() {
    ui.removeMovieLabel_2->show();
	ui.movieToRemove_2->show();
	ui.sendDeleteMovie2->show();
}

void MoviesWGUI::hideDeleteFromWatchListForm() {
    ui.removeMovieLabel_2->hide();
    ui.movieToRemove_2->hide();
    ui.sendDeleteMovie2->hide();
}

void MoviesWGUI::on_ExitForUser_clicked() {
	this->close();
}

void MoviesWGUI::on_searchMovie_clicked() {
	this->hideSearchMovieForm();
    hideDeleteFromWatchListForm();
    ui.MoviesList->hide();
    this->showSearchMovieForm();
}

void MoviesWGUI::on_sendSearchMovies_clicked() {
    std::string genre = ui.genreSearch->text().toStdString();
    if (genre == "") {
        std::cout << "Movies:\n";
        for (int i = 0; i < this->controller.getRepositorySize(); i++) {
            ui.textCout->show();
            Movie movie = this->controller.getMovie(i);
            ui.textCout->setPlainText((movie.getTitle() + ", " +
                movie.getGenre() + ", " +
                std::to_string(movie.getReleaseYear()) + ", " +
                std::to_string(movie.getLikes()) + ", " +
                movie.getTrailer()).c_str());
        }
    }
    else {
        int found_movies_size;
        int* found_movies = this->controller.SearchMovies(genre, "genre", found_movies_size);
        if (found_movies[0] == -1) {
            ui.textCout->show();
            ui.textCout->setPlainText(("No movies found with the genre " + genre).c_str());
        }
        else {
            QEventLoop loop;
            connect(ui.yesAdd, &QPushButton::clicked, &loop, &QEventLoop::quit);
            connect(ui.noAdd, &QPushButton::clicked, &loop, &QEventLoop::quit);
            connect(ui.exitSearch, &QPushButton::clicked, &loop, &QEventLoop::quit);
            for (int i = 0; i < found_movies_size; i++) {
                Movie m = this->controller.getMovie(found_movies[i]);
                ui.textCout->show();
                ui.textCout->setPlainText((m.getTitle() + ", " +
                    m.getGenre() + ", " +
                    std::to_string(m.getReleaseYear()) + ", " +
                    std::to_string(m.getLikes()) + ", " +
                    m.getTrailer()).c_str());
                system(("start " + m.getTrailer()).c_str());

                ui.textCout->setPlainText(ui.textCout->toPlainText() + "\nDo you want to add the movie to the watch list?");
                ui.yesAdd->show();
                ui.noAdd->show();
                ui.exitSearch->show();
                loop.exec();

                if (yes_pressed == true) {
                    this->controller.AddMovieToWatchList(m);
                    yes_pressed = 0;
                }
                else if (no_pressed == true)
                {
                    if (i == found_movies_size - 1)
                        i = 0;
                    no_pressed = 0;
                }            
                else if (exit_search == true)
                {
                    delete[] found_movies;
                    exit_search = 0;
                    this->hideSearchMovieForm();
                    break;
                }
            }
        }
    }
}

void MoviesWGUI::on_deleteFromWatchList_clicked() {
	this->hideSearchMovieForm();
    ui.MoviesList->hide();
    showDeleteFromWatchListForm();
}

void MoviesWGUI::on_seeWatchList_clicked() {
	this->hideSearchMovieForm();
    hideDeleteFromWatchListForm();
    ui.MoviesList->show();
    ui.MoviesList->clear();

    for (int i = 0; i < this->controller.getWatchListSize(); i++) {
        Movie movie = this->controller.getMovieFromWatchList(i);
        ui.MoviesList->addItem((movie.getTitle() + ", " +
            movie.getGenre() + ", " +
			std::to_string(movie.getReleaseYear()) + ", " +
			std::to_string(movie.getLikes()) + ", " +
			movie.getTrailer()).c_str());
    }
}

void MoviesWGUI::on_openWatchList_clicked() {
	this->hideSearchMovieForm();
    hideDeleteFromWatchListForm();
    ui.MoviesList->hide();
    if (this->controller.getFileTypeFromRepo() == "csv") {
        std::string command = "notepad " + this->controller.getFileNameFromRepo();
        system(command.c_str());
    }
    else if (this->controller.getFileTypeFromRepo() == "html") {
        std::string command = "start " + this->controller.getFileNameFromRepo();
        system(command.c_str());
    }
}

void MoviesWGUI::on_yesAdd_clicked() {
    this->yes_pressed = true;
}

void MoviesWGUI::on_noAdd_clicked() {
    this->no_pressed = true;
}

void MoviesWGUI::on_exitSearch_clicked() {
    this->exit_search = true;
}

void MoviesWGUI::on_sendDeleteMovie2_clicked() {
    try {
        std::string title = ui.movieToRemove_2->text().toStdString();
        this->controller.DeleteMovieFromWatchList(title, 0);
        this->hideDeleteFromWatchListForm();
    }
    catch (std::exception& e) {
        QMessageBox::critical(this, "Error", e.what());
    }
    this->hideDeleteMovieForm();
}
