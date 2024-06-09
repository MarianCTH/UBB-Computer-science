#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include "stdlib.h"
#include "Medicine.h"
#include "string.h"

Medicine CreateMedicine(char name[], int concentration, int quantity, double price) {
	Medicine m;

	strcpy(m.name, name);
	m.concentration = concentration;
	m.quantity = quantity;
	m.price = price;

	return m;
}

char* getName(Medicine* m) {
	return m->name;
}
int getConcentration(Medicine* m) {
	return m->concentration;
}
int getQuantity(Medicine* m) {
	return m->quantity;
}
double getPrice(Medicine* m) {
	return m->price;
}

void setName(Medicine* m, char new_name[]) {
	strcpy(m->name, new_name);
}
void setQuantity(Medicine* m, int new_quantity){
	m->quantity = new_quantity;
}
void setConcentration(Medicine* m, int new_concentration) {
	m->concentration = new_concentration;
}
void setPrice(Medicine* m, double new_price) {
	m->price = new_price;
}

void toString(Medicine* m) {
	printf("Name: %s, Concentration: %d, Quantity: %d, Price: %.2lf", m->name, m->concentration, m->quantity, m->price);
}