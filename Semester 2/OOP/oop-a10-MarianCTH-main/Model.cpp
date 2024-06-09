#include "Model.h"

MyModel::MyModel(QObject* parent)
    : QAbstractTableModel(parent)
{
}

int MyModel::rowCount(const QModelIndex&) const
{
    return tdata.size();
}

int MyModel::columnCount(const QModelIndex&) const
{
    return 5;
}

QVariant MyModel::data(const QModelIndex& index, int role) const
{
    if (role == Qt::DisplayRole) {
        int row = index.row();
        int column = index.column();
        return tdata[row][column];
    }

    return QVariant();
}

void MyModel::setDataInTable(vector<Movie> movies) {
    if (movies.empty())
        return;
    if (!tdata.empty()) {
        beginRemoveRows(QModelIndex(), 0, tdata.size() - 1);
        tdata.clear();
        endRemoveRows();
    }
    int i = 0;
    tdata.resize(movies.size());
    beginInsertRows(QModelIndex(), 0, tdata.size() - 1);
    for (auto& movie : movies) {
        tdata[i].resize(5);
        tdata[i][0] = movie.getTitle().c_str();
        tdata[i][1] = movie.getGenre().c_str();
        tdata[i][2] = std::to_string(movie.getReleaseYear()).c_str();
        tdata[i][3] = std::to_string(movie.getLikes()).c_str();
        tdata[i][4] = movie.getTrailer().c_str();
        ++i;
    }
    endInsertRows();
}