/********************************************************************************
** Form generated from reading UI file 'MoviesWGUI.ui'
**
** Created by: Qt User Interface Compiler version 6.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MOVIESWGUI_H
#define UI_MOVIESWGUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MoviesWGUIClass
{
public:
    QWidget *centralWidget;
    QPushButton *userButton;
    QPushButton *adminButton;
    QLabel *modeMessage;
    QLabel *chooseAction1;
    QPushButton *Add;
    QPushButton *Delete;
    QPushButton *ShowAll;
    QPushButton *Exit;
    QPushButton *Update;
    QListWidget *MoviesList;
    QLabel *titleLabel;
    QLabel *genreLabel;
    QLabel *yearLabel;
    QLabel *trailerLabel;
    QPushButton *sendAddMovie;
    QLineEdit *titleInput;
    QLineEdit *genreInput;
    QLineEdit *yearInput;
    QLineEdit *trailerInput;
    QLineEdit *movieToRemove;
    QLabel *removeMovieLabel;
    QPushButton *sendDeleteMovie;
    QPushButton *sendUpdateMovie;
    QLineEdit *titleUpdate;
    QLineEdit *genreUpdate;
    QLineEdit *yearUpdate;
    QLineEdit *trailerUpdate;
    QLineEdit *likesUpdate;
    QLineEdit *movieToUpdate;
    QPushButton *ExitForUser;
    QPushButton *searchMovie;
    QPushButton *deleteFromWatchList;
    QPushButton *seeWatchList;
    QPushButton *openWatchList;
    QLabel *chooseAction1_2;
    QLineEdit *genreSearch;
    QPushButton *sendSearchMovies;
    QPlainTextEdit *textCout;
    QPushButton *yesAdd;
    QPushButton *noAdd;
    QPushButton *exitSearch;
    QLabel *removeMovieLabel_2;
    QLineEdit *movieToRemove_2;
    QPushButton *sendDeleteMovie2;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MoviesWGUIClass)
    {
        if (MoviesWGUIClass->objectName().isEmpty())
            MoviesWGUIClass->setObjectName("MoviesWGUIClass");
        MoviesWGUIClass->resize(720, 460);
        centralWidget = new QWidget(MoviesWGUIClass);
        centralWidget->setObjectName("centralWidget");
        userButton = new QPushButton(centralWidget);
        userButton->setObjectName("userButton");
        userButton->setGeometry(QRect(310, 160, 80, 24));
        adminButton = new QPushButton(centralWidget);
        adminButton->setObjectName("adminButton");
        adminButton->setGeometry(QRect(310, 120, 80, 24));
        modeMessage = new QLabel(centralWidget);
        modeMessage->setObjectName("modeMessage");
        modeMessage->setGeometry(QRect(290, 90, 131, 21));
        chooseAction1 = new QLabel(centralWidget);
        chooseAction1->setObjectName("chooseAction1");
        chooseAction1->setEnabled(true);
        chooseAction1->setGeometry(QRect(20, 20, 131, 21));
        Add = new QPushButton(centralWidget);
        Add->setObjectName("Add");
        Add->setEnabled(true);
        Add->setGeometry(QRect(20, 50, 80, 24));
        Add->setCheckable(false);
        Delete = new QPushButton(centralWidget);
        Delete->setObjectName("Delete");
        Delete->setEnabled(true);
        Delete->setGeometry(QRect(20, 90, 80, 24));
        ShowAll = new QPushButton(centralWidget);
        ShowAll->setObjectName("ShowAll");
        ShowAll->setEnabled(true);
        ShowAll->setGeometry(QRect(20, 170, 80, 24));
        Exit = new QPushButton(centralWidget);
        Exit->setObjectName("Exit");
        Exit->setEnabled(true);
        Exit->setGeometry(QRect(20, 210, 80, 24));
        Update = new QPushButton(centralWidget);
        Update->setObjectName("Update");
        Update->setEnabled(true);
        Update->setGeometry(QRect(20, 130, 80, 24));
        MoviesList = new QListWidget(centralWidget);
        MoviesList->setObjectName("MoviesList");
        MoviesList->setGeometry(QRect(180, 10, 521, 251));
        titleLabel = new QLabel(centralWidget);
        titleLabel->setObjectName("titleLabel");
        titleLabel->setGeometry(QRect(288, 70, 51, 21));
        genreLabel = new QLabel(centralWidget);
        genreLabel->setObjectName("genreLabel");
        genreLabel->setGeometry(QRect(280, 100, 51, 21));
        yearLabel = new QLabel(centralWidget);
        yearLabel->setObjectName("yearLabel");
        yearLabel->setGeometry(QRect(250, 130, 81, 21));
        trailerLabel = new QLabel(centralWidget);
        trailerLabel->setObjectName("trailerLabel");
        trailerLabel->setGeometry(QRect(280, 160, 51, 21));
        sendAddMovie = new QPushButton(centralWidget);
        sendAddMovie->setObjectName("sendAddMovie");
        sendAddMovie->setGeometry(QRect(340, 190, 80, 24));
        titleInput = new QLineEdit(centralWidget);
        titleInput->setObjectName("titleInput");
        titleInput->setGeometry(QRect(330, 70, 113, 24));
        genreInput = new QLineEdit(centralWidget);
        genreInput->setObjectName("genreInput");
        genreInput->setGeometry(QRect(330, 100, 113, 24));
        yearInput = new QLineEdit(centralWidget);
        yearInput->setObjectName("yearInput");
        yearInput->setGeometry(QRect(330, 130, 113, 24));
        trailerInput = new QLineEdit(centralWidget);
        trailerInput->setObjectName("trailerInput");
        trailerInput->setGeometry(QRect(330, 160, 113, 24));
        movieToRemove = new QLineEdit(centralWidget);
        movieToRemove->setObjectName("movieToRemove");
        movieToRemove->setGeometry(QRect(270, 110, 181, 31));
        removeMovieLabel = new QLabel(centralWidget);
        removeMovieLabel->setObjectName("removeMovieLabel");
        removeMovieLabel->setGeometry(QRect(270, 80, 211, 21));
        removeMovieLabel->setStyleSheet(QString::fromUtf8("font: 14pt \"Segoe UI\";"));
        sendDeleteMovie = new QPushButton(centralWidget);
        sendDeleteMovie->setObjectName("sendDeleteMovie");
        sendDeleteMovie->setGeometry(QRect(310, 150, 101, 31));
        sendUpdateMovie = new QPushButton(centralWidget);
        sendUpdateMovie->setObjectName("sendUpdateMovie");
        sendUpdateMovie->setGeometry(QRect(260, 220, 131, 31));
        titleUpdate = new QLineEdit(centralWidget);
        titleUpdate->setObjectName("titleUpdate");
        titleUpdate->setGeometry(QRect(270, 70, 113, 24));
        genreUpdate = new QLineEdit(centralWidget);
        genreUpdate->setObjectName("genreUpdate");
        genreUpdate->setGeometry(QRect(270, 100, 113, 24));
        yearUpdate = new QLineEdit(centralWidget);
        yearUpdate->setObjectName("yearUpdate");
        yearUpdate->setGeometry(QRect(270, 130, 113, 24));
        trailerUpdate = new QLineEdit(centralWidget);
        trailerUpdate->setObjectName("trailerUpdate");
        trailerUpdate->setGeometry(QRect(270, 190, 113, 24));
        likesUpdate = new QLineEdit(centralWidget);
        likesUpdate->setObjectName("likesUpdate");
        likesUpdate->setGeometry(QRect(270, 160, 113, 24));
        movieToUpdate = new QLineEdit(centralWidget);
        movieToUpdate->setObjectName("movieToUpdate");
        movieToUpdate->setGeometry(QRect(250, 33, 161, 31));
        ExitForUser = new QPushButton(centralWidget);
        ExitForUser->setObjectName("ExitForUser");
        ExitForUser->setEnabled(true);
        ExitForUser->setGeometry(QRect(20, 170, 131, 24));
        searchMovie = new QPushButton(centralWidget);
        searchMovie->setObjectName("searchMovie");
        searchMovie->setEnabled(true);
        searchMovie->setGeometry(QRect(20, 50, 131, 24));
        deleteFromWatchList = new QPushButton(centralWidget);
        deleteFromWatchList->setObjectName("deleteFromWatchList");
        deleteFromWatchList->setEnabled(true);
        deleteFromWatchList->setGeometry(QRect(20, 80, 131, 24));
        seeWatchList = new QPushButton(centralWidget);
        seeWatchList->setObjectName("seeWatchList");
        seeWatchList->setEnabled(true);
        seeWatchList->setGeometry(QRect(20, 110, 131, 24));
        openWatchList = new QPushButton(centralWidget);
        openWatchList->setObjectName("openWatchList");
        openWatchList->setEnabled(true);
        openWatchList->setGeometry(QRect(20, 140, 131, 24));
        chooseAction1_2 = new QLabel(centralWidget);
        chooseAction1_2->setObjectName("chooseAction1_2");
        chooseAction1_2->setEnabled(true);
        chooseAction1_2->setGeometry(QRect(20, 20, 131, 21));
        genreSearch = new QLineEdit(centralWidget);
        genreSearch->setObjectName("genreSearch");
        genreSearch->setGeometry(QRect(300, 90, 131, 31));
        sendSearchMovies = new QPushButton(centralWidget);
        sendSearchMovies->setObjectName("sendSearchMovies");
        sendSearchMovies->setGeometry(QRect(300, 127, 131, 41));
        textCout = new QPlainTextEdit(centralWidget);
        textCout->setObjectName("textCout");
        textCout->setGeometry(QRect(180, 270, 341, 81));
        yesAdd = new QPushButton(centralWidget);
        yesAdd->setObjectName("yesAdd");
        yesAdd->setGeometry(QRect(230, 360, 80, 24));
        noAdd = new QPushButton(centralWidget);
        noAdd->setObjectName("noAdd");
        noAdd->setGeometry(QRect(360, 360, 80, 24));
        exitSearch = new QPushButton(centralWidget);
        exitSearch->setObjectName("exitSearch");
        exitSearch->setGeometry(QRect(490, 360, 80, 24));
        removeMovieLabel_2 = new QLabel(centralWidget);
        removeMovieLabel_2->setObjectName("removeMovieLabel_2");
        removeMovieLabel_2->setGeometry(QRect(220, 100, 321, 21));
        removeMovieLabel_2->setStyleSheet(QString::fromUtf8("font: 14pt \"Segoe UI\";"));
        movieToRemove_2 = new QLineEdit(centralWidget);
        movieToRemove_2->setObjectName("movieToRemove_2");
        movieToRemove_2->setGeometry(QRect(270, 130, 181, 31));
        sendDeleteMovie2 = new QPushButton(centralWidget);
        sendDeleteMovie2->setObjectName("sendDeleteMovie2");
        sendDeleteMovie2->setGeometry(QRect(300, 170, 101, 31));
        MoviesWGUIClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(MoviesWGUIClass);
        statusBar->setObjectName("statusBar");
        MoviesWGUIClass->setStatusBar(statusBar);

        retranslateUi(MoviesWGUIClass);

        Add->setDefault(false);


        QMetaObject::connectSlotsByName(MoviesWGUIClass);
    } // setupUi

    void retranslateUi(QMainWindow *MoviesWGUIClass)
    {
        MoviesWGUIClass->setWindowTitle(QCoreApplication::translate("MoviesWGUIClass", "MoviesWGUI", nullptr));
        userButton->setText(QCoreApplication::translate("MoviesWGUIClass", "User", nullptr));
        adminButton->setText(QCoreApplication::translate("MoviesWGUIClass", "Administrator", nullptr));
        modeMessage->setText(QCoreApplication::translate("MoviesWGUIClass", "Please choose the mode:", nullptr));
        chooseAction1->setText(QCoreApplication::translate("MoviesWGUIClass", "Please choose an action:", nullptr));
        Add->setText(QCoreApplication::translate("MoviesWGUIClass", "Add Movie", nullptr));
        Delete->setText(QCoreApplication::translate("MoviesWGUIClass", "Delete Movie", nullptr));
        ShowAll->setText(QCoreApplication::translate("MoviesWGUIClass", "Show All", nullptr));
        Exit->setText(QCoreApplication::translate("MoviesWGUIClass", "Exit", nullptr));
        Update->setText(QCoreApplication::translate("MoviesWGUIClass", "Update Movie", nullptr));
        titleLabel->setText(QCoreApplication::translate("MoviesWGUIClass", "Title", nullptr));
        genreLabel->setText(QCoreApplication::translate("MoviesWGUIClass", "Genre", nullptr));
        yearLabel->setText(QCoreApplication::translate("MoviesWGUIClass", "Release Year", nullptr));
        trailerLabel->setText(QCoreApplication::translate("MoviesWGUIClass", "Trailer", nullptr));
        sendAddMovie->setText(QCoreApplication::translate("MoviesWGUIClass", "Add Movie", nullptr));
        titleInput->setText(QString());
        genreInput->setText(QString());
        yearInput->setText(QString());
        trailerInput->setText(QString());
        removeMovieLabel->setText(QCoreApplication::translate("MoviesWGUIClass", "Movie to delete(title):", nullptr));
        sendDeleteMovie->setText(QCoreApplication::translate("MoviesWGUIClass", "Delete", nullptr));
        sendUpdateMovie->setText(QCoreApplication::translate("MoviesWGUIClass", "Update", nullptr));
        titleUpdate->setText(QCoreApplication::translate("MoviesWGUIClass", "Title", nullptr));
        genreUpdate->setText(QCoreApplication::translate("MoviesWGUIClass", "Genre", nullptr));
        yearUpdate->setText(QCoreApplication::translate("MoviesWGUIClass", "Release Year", nullptr));
        trailerUpdate->setText(QCoreApplication::translate("MoviesWGUIClass", "Trailer", nullptr));
        likesUpdate->setText(QCoreApplication::translate("MoviesWGUIClass", "Likes", nullptr));
        movieToUpdate->setText(QCoreApplication::translate("MoviesWGUIClass", "Title of the movie to update", nullptr));
        ExitForUser->setText(QCoreApplication::translate("MoviesWGUIClass", "Exit", nullptr));
        searchMovie->setText(QCoreApplication::translate("MoviesWGUIClass", "Search Movie", nullptr));
        deleteFromWatchList->setText(QCoreApplication::translate("MoviesWGUIClass", "Delete from watch list", nullptr));
        seeWatchList->setText(QCoreApplication::translate("MoviesWGUIClass", "See watch list", nullptr));
        openWatchList->setText(QCoreApplication::translate("MoviesWGUIClass", "Open watch list", nullptr));
        chooseAction1_2->setText(QCoreApplication::translate("MoviesWGUIClass", "Please choose an action:", nullptr));
        genreSearch->setText(QCoreApplication::translate("MoviesWGUIClass", "Genre", nullptr));
        sendSearchMovies->setText(QCoreApplication::translate("MoviesWGUIClass", "Search", nullptr));
        yesAdd->setText(QCoreApplication::translate("MoviesWGUIClass", "Yes", nullptr));
        noAdd->setText(QCoreApplication::translate("MoviesWGUIClass", "No", nullptr));
        exitSearch->setText(QCoreApplication::translate("MoviesWGUIClass", "Exit search", nullptr));
        removeMovieLabel_2->setText(QCoreApplication::translate("MoviesWGUIClass", "Movie to delete from watchlist(title):", nullptr));
        sendDeleteMovie2->setText(QCoreApplication::translate("MoviesWGUIClass", "Delete", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MoviesWGUIClass: public Ui_MoviesWGUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MOVIESWGUI_H
