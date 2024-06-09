#pragma once
#include "Medicine.h"
#include "History.h"

typedef struct {
	Medicine *medicine;
	int length;
	int capacity;
} Repository;

Repository* CreateRepository(int);
void Destroy(Repository*);
void resize(Repository*);
void AddMedicine(Repository*, History*, Medicine);
void UpdateMedicine(Repository*, History*, Medicine, int);
void DeleteMedicine(Repository*, History*, int);
void Undo(Repository*, History*);
void Redo(Repository*, History*);