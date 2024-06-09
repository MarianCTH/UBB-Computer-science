#include <iostream>
#include "AdminUI.h"
#include "UserUI.h"
#include "Repository.h"
#include "Controller.h"
#include "MagicNumbers.h"
#include "Tests.h"

int getMode() {
	int mode_choice;

	std::cout << "Please choose a mode:\n[1] Administrator\n[2] User\n[3] Exit\n>> ";
	std::cin >> mode_choice;

	return mode_choice;
}

void AddDefaultInputs(Controller& controller) {
	controller.AddMovie("Inception", "Sci-Fi", 2010, 1500, "https://www.youtube.com/watch?v=YoHD9XEInc0");
	controller.AddMovie("The Shawshank Redemption", "Drama", 1994, 2000, "https://www.youtube.com/watch?v=6hB3S9bIaco");
	controller.AddMovie("The Dark Knight", "Action", 2008, 2200, "https://www.youtube.com/watch?v=EXeTwQWrcwY");
	controller.AddMovie("Interstellar", "Sci-Fi", 2014, 1800, "https://www.youtube.com/watch?v=zSWdZVtXT7E");
	controller.AddMovie("Pulp Fiction", "Crime", 1994, 1900, "https://www.youtube.com/watch?v=s7EdQ4FqbhY");
	controller.AddMovie("Forrest Gump", "Drama", 1994, 2100, "https://www.youtube.com/watch?v=bLvqoHBptjg");
	controller.AddMovie("The Matrix", "Sci-Fi", 1999, 1700, "https://www.youtube.com/watch?v=vKQi3bBA1y8");
	controller.AddMovie("The Godfather", "Crime", 1972, 2300, "https://www.youtube.com/watch?v=sY1S34973zA");
	controller.AddMovie("The Lord of the Rings: The Return of the King", "Fantasy", 2003, 2400, "https://www.youtube.com/watch?v=r5X-hFf6Bwo");
	controller.AddMovie("Fight Club", "Drama", 1999, 1600, "https://www.youtube.com/watch?v=SUXWAEX2jlg");
}

void checkMode(int mode) {
	Repository<Movie> repository(51);
	Repository<Movie> watchList(51);

	Controller controller(repository, watchList);
	AddDefaultInputs(controller);

	AdminUI adminUI(controller);
	UserUI userUI(controller);

	if (mode == ADMINISTRATOR_MODE)
		adminUI.Init();
	else if (mode == USER_MODE)
		userUI.Init();
	else if (mode == EXIT)
		exit(1);
	else
		std::cout << "Invalid mode. Please try again !";
}

int main() {
	Tests::StartTests();
	checkMode(getMode());
	_CrtDumpMemoryLeaks;
}