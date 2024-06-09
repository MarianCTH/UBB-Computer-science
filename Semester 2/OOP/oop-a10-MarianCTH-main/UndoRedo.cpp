#include "UndoRedo.h"

void ActionAdd::executeUndo() {
    repo.DeleteMovie(addedMovieIndex);
}

void ActionAdd::executeRedo() {
    repo.AddMovie(addedMovie);
}

void ActionRemove::executeUndo() {
    repo.AddMovie(removedMovie);
}

void ActionRemove::executeRedo() {
    repo.DeleteMovie(removedMovieIndex);
}

void ActionUpdate::executeUndo() {
    repo.UpdateMovie(movieIndex, oldMovie);
}

void ActionUpdate::executeRedo() {
    repo.UpdateMovie(movieIndex, newMovie);
}