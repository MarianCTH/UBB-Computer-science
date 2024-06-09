#include "MoviesWGUI.h"
#include "Model.h"
#include "ui_MoviesWGUI.h"

MoviesWGUI::MoviesWGUI(Controller controller)
    : controller(controller)
{
    ui.setupUi(this);
	this->hideAdminMenu();
	this->hideUserMenu();
	this->hideAddMovieForm();
	this->hideDeleteMovieForm();
	this->hideUpdateMovieForm();
	this->hideSearchMovieForm();
	this->hideDeleteFromWatchListForm();
	ui.undoButton->hide();
	ui.redoButton->hide();
	ui.textCout->hide();
	ui.watchListTable->hide();
	ui.showTableButton->hide();
}

MoviesWGUI::~MoviesWGUI()
{}

void MoviesWGUI::hideMainMenu()
{
	ui.modeMessage->hide();
	ui.adminButton->hide();
	ui.userButton->hide();
}

void MoviesWGUI::showAdminMenu() {
	ui.chooseAction1->show();
	ui.Add->show();
	ui.Delete->show();
	ui.Update->show();
	ui.ShowAll->show();
	ui.undoButton->show();
	ui.redoButton->show();
	ui.Exit->show();
}

void MoviesWGUI::hideAdminMenu() {
	ui.chooseAction1->hide();
	ui.Add->hide();
	ui.Delete->hide();
	ui.Update->hide();
	ui.ShowAll->hide();
	ui.undoButton->hide();
	ui.redoButton->hide();
	ui.Exit->hide();
	ui.MoviesList->hide();
}

void MoviesWGUI::showAddMovieForm() {
	ui.titleLabel->show();
	ui.genreLabel->show();
	ui.yearLabel->show();
	ui.trailerLabel->show();

	ui.titleInput->show();
	ui.genreInput->show();
	ui.yearInput->show();
	ui.trailerInput->show();
	ui.sendAddMovie->show();
}

void MoviesWGUI::hideAddMovieForm() {
	ui.titleLabel->hide();
	ui.genreLabel->hide();
	ui.yearLabel->hide();
	ui.trailerLabel->hide();

	ui.titleInput->hide();
	ui.genreInput->hide();
	ui.yearInput->hide();
	ui.trailerInput->hide();
	ui.sendAddMovie->hide();
}

void MoviesWGUI::showDeleteMovieForm() {
	ui.removeMovieLabel->show();
	ui.movieToRemove->show();
	ui.sendDeleteMovie->show();
}

void MoviesWGUI::hideDeleteMovieForm() {
	ui.removeMovieLabel->hide();
	ui.movieToRemove->hide();
	ui.sendDeleteMovie->hide();
}

void MoviesWGUI::showUpdateMovieForm() {
	ui.movieToUpdate->show();
	ui.sendUpdateMovie->show();
	ui.titleUpdate->show();
	ui.genreUpdate->show();
	ui.yearUpdate->show();
	ui.likesUpdate->show();
	ui.trailerUpdate->show();
}

void MoviesWGUI::hideUpdateMovieForm() {
	ui.movieToUpdate->hide();
	ui.sendUpdateMovie->hide();
	ui.titleUpdate->hide();
	ui.genreUpdate->hide();
	ui.yearUpdate->hide();
	ui.likesUpdate->hide();
	ui.trailerUpdate->hide();
}

void MoviesWGUI::on_adminButton_clicked()
{
	this->hideMainMenu();
	this->showAdminMenu();
}

void MoviesWGUI::on_userButton_clicked()
{
	this->hideMainMenu();
	this->showUserMenu();
}

void MoviesWGUI::on_Exit_clicked() {
	this->close();
}

void MoviesWGUI::on_ShowAll_clicked() {
	this->hideAddMovieForm();
	this->hideDeleteMovieForm();
	this->hideUpdateMovieForm();
	ui.MoviesList->show();
	ui.MoviesList->clear();
	for (int i = 0; i < this->controller.getRepositorySize(); i++) {
		Movie movie = this->controller.getMovie(i);
		ui.MoviesList->addItem((movie.getTitle() + ", " +  
			movie.getGenre() + ", " + 
			std::to_string(movie.getReleaseYear()) + ", " + 
			std::to_string(movie.getLikes()) + ", " +
			movie.getTrailer()).c_str());
	}
}

void MoviesWGUI::on_Add_clicked() {
	ui.MoviesList->hide();
	this->hideDeleteMovieForm();
	this->hideUpdateMovieForm();
	this->showAddMovieForm();
}

void MoviesWGUI::on_sendAddMovie_clicked() {
	std::string title = ui.titleInput->text().toStdString();
	std::string genre = ui.genreInput->text().toStdString();
	int year = ui.yearInput->text().toInt();
	std::string trailer = ui.trailerInput->text().toStdString();
	this->controller.AddMovie(title, genre, year, 0, trailer);
	this->hideAddMovieForm();
}

void MoviesWGUI::on_Delete_clicked() {
	ui.MoviesList->hide();
	this->hideAddMovieForm();
	this->hideUpdateMovieForm();
	this->showDeleteMovieForm();
}

void MoviesWGUI::on_sendDeleteMovie_clicked() {
	std::string title = ui.movieToRemove->text().toStdString();
	this->controller.DeleteMovie(title);
	this->hideDeleteMovieForm();
}

void MoviesWGUI::on_Update_clicked() {
	ui.MoviesList->hide();
	this->hideAddMovieForm();
	this->hideDeleteMovieForm();
	this->showUpdateMovieForm();
}

void MoviesWGUI::on_sendUpdateMovie_clicked() {
	std::string title_to_update = ui.movieToUpdate->text().toStdString();
	std::string title = ui.titleUpdate->text().toStdString();
	std::string genre = ui.genreUpdate->text().toStdString();
	int year = ui.yearUpdate->text().toInt();
	int likes = ui.likesUpdate->text().toInt();
	std::string trailer = ui.trailerUpdate->text().toStdString();
	this->controller.UpdateMovie(title_to_update, title, genre, year, likes, trailer);
	this->hideUpdateMovieForm();
}

void MoviesWGUI::on_undoButton_clicked() {
	this->controller.undo();
}

void MoviesWGUI::on_redoButton_clicked() {
	this->controller.redo();
}