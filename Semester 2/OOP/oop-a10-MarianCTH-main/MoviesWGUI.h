#pragma once

#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMessageBox>
#include "Model.h"
#include "ui_MoviesWGUI.h"
#include "Controller.h"
#include <string>

class MoviesWGUI : public QMainWindow
{
    Controller controller;
    bool yes_pressed = false;
    bool no_pressed = false;
    bool exit_search = false;
    MyModel* watchListModel;
    Q_OBJECT
public:
    MoviesWGUI(Controller controller);
    ~MoviesWGUI();

    void hideMainMenu();
    void showAdminMenu();
    void showUserMenu();
    void hideAdminMenu();
    void hideUserMenu();
    void showAddMovieForm();
    void hideAddMovieForm();
    void showDeleteMovieForm();
    void hideDeleteMovieForm();
    void showUpdateMovieForm();
    void hideUpdateMovieForm();
private slots: // FOR ADMIN
    void on_adminButton_clicked();
    void on_userButton_clicked();
    void on_Exit_clicked();
    void on_ShowAll_clicked();
    void on_Add_clicked();
    void on_sendAddMovie_clicked();
    void on_Delete_clicked();
    void on_Update_clicked();
    void on_sendDeleteMovie_clicked();
    void on_sendUpdateMovie_clicked();
    void on_undoButton_clicked();
    void on_redoButton_clicked();
// FOR USER
    void hideSearchMovieForm();
    void showSearchMovieForm();
    void showDeleteFromWatchListForm();
    void hideDeleteFromWatchListForm();
    void on_ExitForUser_clicked();
    void on_searchMovie_clicked();
    void on_deleteFromWatchList_clicked();
    void on_seeWatchList_clicked();
    void on_openWatchList_clicked();
    void on_sendSearchMovies_clicked();
    void on_yesAdd_clicked();
    void on_noAdd_clicked();
    void on_exitSearch_clicked();
    void on_sendDeleteMovie2_clicked();
    void on_showTableButton_clicked();
private:
    Ui::MoviesWGUIClass ui;
};
