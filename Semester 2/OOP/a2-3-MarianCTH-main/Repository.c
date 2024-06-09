#include "Repository.h"
#include "History.h"
#include "stdlib.h"

Repository* CreateRepository(int capacity) {
	Repository* repo = (Repository*)malloc(sizeof(Repository));

	if (repo == NULL)
		return NULL;
	
	repo->capacity = capacity;
	repo->length = 0;

	repo->medicine = (Medicine*)malloc(sizeof(Medicine) * capacity);
	if (repo->medicine == NULL)
		return NULL;

	return repo;
}

void Destroy(Repository* repo) {
	if (repo == NULL)
		return;

	free(repo->medicine);
	repo->medicine = NULL;

	free(repo);
}

void resize(Repository* repo) {
	if (repo->medicine = NULL)
		return;

	repo->capacity++;
	repo->medicine = (Medicine*)realloc(repo->medicine, sizeof(Medicine) * repo->capacity);
}

void AddMedicine(Repository* repo, History* history, Medicine m) {
	if (repo == NULL)
		return;
	if (repo->medicine == NULL)
		return;

	if (repo->length == repo->capacity)
		resize(repo);
		repo->medicine[repo->length] = m;
		repo->length++;

	Change change;
	change.medicine = m;
	change.index = repo->length - 1;
	change.action = 'A';
	AddChange(history, change);
}

void UpdateMedicine(Repository *repo, History* history, Medicine m, int index) {
	if (repo == NULL)
		return;
	if (repo->medicine == NULL)
		return;

	setName(&repo->medicine[index], m.name);
	setConcentration(&repo->medicine[index], m.concentration);
	setQuantity(&repo->medicine[index], m.quantity);
	setPrice(&repo->medicine[index], m.price);

	Change change;
	change.medicine = m;
	change.index = index;
	change.action = 'U';
	AddChange(history, change);
}

void DeleteMedicine(Repository* repo, History* history, int index) {
	if (repo == NULL || repo->medicine == NULL || index < 0 || index >= repo->length)
		return;

	for (int i = index; i < repo->length - 1; i++) {
		repo->medicine[i] = repo->medicine[i + 1];
	}

	repo->length--;

	Change change;
	change.medicine = repo->medicine[index];
	change.index = index;
	change.action = 'D';
	AddChange(history, change);
}

void Undo(Repository* repo, History* history) {
	if (history->top == -1)
		return;
	Change lastChange = history->changes[history->top--];
	switch (lastChange.action) {
	case 'A':
		repo->length--;
		break;
	case 'U':
		UpdateMedicine(repo, history, lastChange.medicine, lastChange.index);
		break;
	case 'D':
		AddMedicine(repo, history, lastChange.medicine);
		break;
	}
}

void Redo(Repository* repo, History* history) {
	if (history->top == history->length - 1)
		return;
	Change nextChange = history->changes[++history->top];
	switch (nextChange.action) {
	case 'A':
		AddMedicine(repo, history, nextChange.medicine);
		break;
	case 'U':
		UpdateMedicine(repo, history, nextChange.medicine, nextChange.index);
		break;
	case 'D':
		repo->length--;
		break;
	}
}