#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "UI.h"
#include "MagicNumbers.h"
#include "Repository.h"
#include "History.h"
#include "Algorithms.h"

void DisplayMenu() {
	printf("\n1 - CRUD");
	printf("\n2 - Search");
	printf("\n3 - Medicines in short supply");
	printf("\n4 - Undo");
	printf("\n5 - Redo");
	printf("\n6 - Exit");
}

int GetUserChoice() {
	int n;

	printf("\nPlease enter your choice:\n>> ");
	scanf("%d", &n);

	return n;
}

void HandleUserChoice(int UserChoice, Repository* MedicineRepository, History* ChangeHistory) {
	if (UserChoice == CRUD) {
		printf("\n1 - Add\n2 - Delete\n3 - Update\n>> ");
		int choice2;
		scanf("%d", &choice2);

		if (choice2 == ADD) {
			char name[30];
			int concentration, quantity;
			double price;

			printf("Name =  "); scanf("%s", &name);
			printf("Concentration =  "); scanf("%d", &concentration);
			printf("Quantity =  "); scanf("%d", &quantity);
			printf("Price =  "); scanf("%lf", &price);

			int exists = 0, found_index = 0;
			for(; found_index < MedicineRepository->length; found_index++)
				if (strcmp(name, getName(&MedicineRepository->medicine[found_index])) == 0 && getConcentration(&MedicineRepository->medicine[found_index]) == concentration) {
					exists = 1;
					break;
				}

			if (exists == 0) {
				Medicine NewMedicine = CreateMedicine(name, concentration, quantity, price);
				AddMedicine(MedicineRepository, ChangeHistory, NewMedicine);
				printf("Medicine added succesfully !\n");
			}
			else {
				printf("Medicine already exists. The quantity will be updated !\n");
				setQuantity(&MedicineRepository->medicine[found_index], quantity);
			}
		}
		else if (choice2 == DELETE) {
			char name[30];
			int found_index = 0, exists = 0;
			printf("Name of the medicine to delete: "); scanf("%s", &name);
			for (; found_index < MedicineRepository->length; found_index++)
				if (strcmp(name, getName(&MedicineRepository->medicine[found_index])) == 0) {
					exists = 1;
					break;
				}

			if (exists == 1) {
				DeleteMedicine(MedicineRepository, ChangeHistory, found_index);
			}
			else {
				printf("Medicine not found !");
			}
		}
		else if (choice2 == UPDATE) {
			char new_name[30], name[30];
			int new_concentration, new_quantity, found_index = 0, exists = 0;
			double new_price;

			printf("Name of the medicine to update: "); scanf("%s", &name);
			for (; found_index < MedicineRepository->length; found_index++)
				if (strcmp(name, getName(&MedicineRepository->medicine[found_index])) == 0){
					exists = 1;
					break;
				}

			if (exists == 1) {
				printf("New name =  "); scanf("%s", &new_name);
				printf("New concentration =  "); scanf("%d", &new_concentration);
				printf("New quantity =  "); scanf("%d", &new_quantity);
				printf("New price =  "); scanf("%lf", &new_price);
				Medicine NewMedicine = CreateMedicine(new_name, new_concentration, new_quantity, new_price);
				UpdateMedicine(MedicineRepository, ChangeHistory, NewMedicine, found_index);
			}
			else {
				printf("Medicine not found !");
			}
		}
		else {
			printf("\nInvalid option !");
		}
	}
	else if (UserChoice == Search) {
		char search_key[50];
		int index = 0;

		printf("Please enter search key:\n>> "); scanf("%s", &search_key);
		
		if (MedicineRepository->length > 0) {
			if (strlen(search_key) == 0) {
				for (int i = 0; i < MedicineRepository->length; i++) {
					printf("\n%d. ", index + 1);
					toString(&MedicineRepository->medicine[i]);
					index++;
				}
			}
			else {
				int current_found_names = 0;
				char** found_names = (char**)malloc(sizeof(char*) * MedicineRepository->length);
				for (int i = 0; i < MedicineRepository->length; i++)
					found_names[i] = (char*)malloc(sizeof(char) * 30);

				for (int i = 0; i < MedicineRepository->length; i++) {
					if (strstr(getName(&MedicineRepository->medicine[i]), search_key) != NULL) {
						strcpy(found_names[current_found_names], getName(&MedicineRepository->medicine[i]));
						current_found_names++;
					}
				}
				if (current_found_names > 0) {
					printf("\nMedicines found: ");
					for (int i = 0; i < current_found_names; i++)
						for (int j = 0; j < MedicineRepository->length; j++) {
							if (strcmp(MedicineRepository->medicine[j].name, found_names[i]) == 0) {
								printf("\n%d. ", i + 1);
								toString(&MedicineRepository->medicine[j]);
							}
						}
				}
				else {
					printf("\nNo medicines found !");
				}
				stringSort(found_names, current_found_names);


				for (int i = 0; i < MedicineRepository->length; i++)
					free(found_names[i]);
				free(found_names);
			}
		}
		else printf("The medicine list is empty !\n");

	}
	else if (UserChoice == ShortSupply) {
		int x, index = 0;
		printf("Quantity = "); scanf("%d", &x);

		if (MedicineRepository->length > 0){
			printf("\nMedicines with quantity lower than %d", x);
			for (int i = 0; i < MedicineRepository->length; i++) {
				if (getQuantity(&MedicineRepository->medicine[i]) < x){
					printf("\n%d. ", index + 1);
					toString(&MedicineRepository->medicine[i]);
					index++;
				}
			}
		}
		else printf("The medicine list is empty !\n");
	}
	else if (UserChoice == UNDO) {
		Undo(MedicineRepository, ChangeHistory);
	}
	else if (UserChoice == REDO){
		Redo(MedicineRepository, ChangeHistory);
	}
	else if (UserChoice == Exit) {
		Destroy(MedicineRepository);
		DestroyHistory(ChangeHistory);

		printf("\n\n\nExiting...\n\n\n");
		exit(1);
	}
	else {
		printf("\nInvalid option !");
	}
}

void UI() {
	Repository *MedicineRepository = CreateRepository(101);
	History *ChangeHistory = CreateHistory(101);

	while (1) {
		DisplayMenu();
		HandleUserChoice(GetUserChoice(), MedicineRepository, ChangeHistory);
	}
}