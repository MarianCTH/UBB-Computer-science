#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include "stdlib.h"


int isPrime(int);
int checkRelativePrime(int, int);
int *maxSubArray(int[], int, int*);
int sum(int[], int);

void UI() {

	printf("1 - All numbers smaller than n that are relatively prime");
	printf("\n2 - Find the longest contiguous subsequence with the maximum sum");
	printf("\n3 - Exit");
	printf("\n>> ");

	int choice;
	scanf("%d", &choice);

	if (choice == 1) {
		int n;
		printf("Please enter a number: ");
		scanf("%d", &n);
		int* v = malloc(sizeof(int) * n);

		int i = 0, j = n;
		while (j > 0) {
			if (checkRelativePrime(j, n))
				v[i++] = j;
			j--;
		}

		printf("\nAll the numbers smaller than %d that are relatively prime:\n", n);
		for (int f = 0; f < i; f++)
			printf("%d ", v[f]);

		free(v);
	}
	else if (choice == 2) {
		int n;

		printf("Please enter a number:\n>> ");
		scanf("%d", &n);
		
		int* v = malloc(sizeof(int) * n);
		printf("\nPlease enter n numbers:\n");
		for (int i = 0; i < n; i++)
			scanf("%d", &v[i]);

		int size;
		int *maxSA = maxSubArray(v, n, &size);
		printf("Longest contiguous subsequence with the maximum sum: ");
		for (int i = 0; i < size; i++) {
			printf("%d ", maxSA[i]);
		}
		free(v); free(maxSA);
	}
	else if (choice == 3) exit(0);
	else printf("Invalid input !");
}

int main() {
	UI();

	return 0;
}

/*
	Check if 2 numbers are relative primes assuming that n is already prime
*/
int checkRelativePrime(int n, int m) {
	for (int j = 2; j <= m; j++)
		if (m % j == 0 && n % j == 0)
			return 0;

	return 1;
}

/*
	Get the subarray that has the max sum from a given array
	test case:
	13
	5 2 3 4 1 8 15 16 0 5 9 25 6

	5
	2 3 4
	1 8 15 16
	0 5 9 25
	6
*/
int* maxSubArray(int v[], int n, int* size) {
	int current_subarray[101] = { 0 }, 
		*max_subarray = malloc(sizeof(int) * n),
		cindex = 0;

	for (int i = 0; i < n; i++)
		if (i == 0 || v[i] > v[i - 1]) {
			current_subarray[cindex++] = v[i];

			if (sum(current_subarray, cindex) > sum(max_subarray, *size))
				for (int j = 0; j < cindex; j++)
				{
					max_subarray[j] = current_subarray[j];
					*size = cindex;
				}
		}
		else
		{
			cindex = 0;
			current_subarray[cindex++] = v[i];
		}

	return max_subarray;
}

/*
	Calculate the same of an array
*/
int sum(int v[], int n) {
	int s = 0;

	for (int i = 0; i < n; i++)
		s += v[i];

	return s;
}