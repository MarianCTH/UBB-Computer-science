#pragma once
#include "Repository.h"
#include "History.h"
void DisplayMenu();
int GetUserChoice();
void HandleUserChoice(int, Repository*, History*);
void UI();