#pragma once
#include <iostream>
#include <string>
#include "Controller.h"

#define SEARCH_BY_GENRE 1
#define DELETE_MOVIE_WATCH_LIST 2
#define SEE_WATCH_LIST 3
#define OPEN_THE_FILE 4
#define EXIT 5

class UserUI {
	Controller controller;
public:
	UserUI(Controller);
	void displayMenu();
	void Init();
};