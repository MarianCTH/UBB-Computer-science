#pragma once

typedef struct {
	char name[30];
	int concentration;
	int quantity;
	double price;
} Medicine;

Medicine CreateMedicine(char[], int, int, double);
char* getName(Medicine*);
int getConcentration(Medicine*);
int getQuantity(Medicine*);
double getPrice(Medicine*);

void setName(Medicine*, char[]);
void setQuantity(Medicine*, int);
void setConcentration(Medicine*, int);
void setPrice(Medicine*, double);

void toString(Medicine*);