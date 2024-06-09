#pragma once

typedef struct {
    Medicine medicine;
    int index;
    char action;
} Change;

typedef struct {
    Change* changes;
    int capacity;
    int length;
    int top;
} History;

History* CreateHistory(int);
void DestroyHistory(History*);
void AddChange(History*, Change);