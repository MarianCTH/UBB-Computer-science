#pragma once
#include <QAbstractTableModel>
#include <QBrush>
#include <QDebug>
#include <QFont>
#include <vector>
#include "Movie.h"

using namespace std;

class MyModel : public QAbstractTableModel
{
    vector<vector<QString>> tdata;
    Q_OBJECT
public:
    explicit MyModel(QObject* parent = nullptr);

    int rowCount(const QModelIndex& parent = QModelIndex()) const override;
    int columnCount(const QModelIndex& parent = QModelIndex()) const override;
    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
    void setDataInTable(vector<Movie> movies);
};