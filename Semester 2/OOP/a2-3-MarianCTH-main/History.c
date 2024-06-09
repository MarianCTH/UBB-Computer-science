#include "Medicine.h"
#include "History.h"
#include "stdlib.h"

History* CreateHistory(int capacity) {
    History* history = (History*)malloc(sizeof(History));

    if (history == NULL)
        return NULL;

    history->changes = (Change*)malloc(sizeof(Change) * capacity);
    if (history->changes == NULL)
        return NULL;

    history->capacity = capacity;
    history->length = 0;
    history->top = -1;

    return history;
}

void DestroyHistory(History* history) {
    free(history->changes);
    free(history);
}

void AddChange(History* history, Change change) {
    if (history->length == history->capacity)
        return;

    history->changes[++history->top] = change;
    history->length++;
}