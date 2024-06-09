#include "Algorithms.h"

void stringSort(char** string, int size) {
	for (int i = 0; i < size; i++) {
		for (int j = i; j < size; j++) {
			if (strcmp(string[i], string[j]) > 0) {
				char* temp = string[i];
				string[i] = string[j];
				string[j] = temp;
			}
		}
	}
}