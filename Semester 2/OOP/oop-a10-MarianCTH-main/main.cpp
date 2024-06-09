#include "MoviesWGUI.h"
#include <QtWidgets/QApplication>
#include "Repository.h"
#include "WatchListRepository.h"
#include "Controller.h"

int main(int argc, char *argv[])
{
    Repository<Movie> repository("movies.txt");
    repository.LoadDataFromFile();
    WatchListRepository watchList("");
    watchList.setFileName("watchlist.csv");
    watchList.setFileType("csv");
    Controller controller(repository, watchList);

    QApplication a(argc, argv);
    MoviesWGUI w(controller);
    w.show();
    return a.exec();
}
