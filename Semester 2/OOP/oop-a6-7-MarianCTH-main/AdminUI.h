#pragma once
#include <iostream>
#include <string>
#include "Controller.h"

#define ADD 1
#define DELETE 2
#define UPDATE 3
#define SHOW_ALL 4
#define EXIT 5

class AdminUI {
	Controller controller;
public:
	AdminUI(Controller);
	void displayMenu();
	void Init();
};