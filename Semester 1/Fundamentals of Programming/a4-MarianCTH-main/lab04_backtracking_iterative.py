"""
    Backtracking
    2. Consider a positive number n. Determine all its decompositions as sums of prime numbers.
"""

def main():
    print("Please enter a positive number: ")
    userInputNumber = int(input(">> "))

    print("\nAll decompositions of ", userInputNumber, " as sums of prime numbers:")
    decomposeNumberIntoPrimeSums(userInputNumber)

def isPrimeNumber(givenNumber: int):
    if(givenNumber < 2) : return 0
    if(givenNumber == 2) : return 1
    if(givenNumber % 2 == 0) : return 0
    for i in range(3, int(givenNumber**0.5) + 1):
        if givenNumber % i == 0:
            return 0
    return 1

def printList(listOfSums: list):
    print()
    for i in range(len(listOfSums)):
        print(listOfSums[i], end="")
        if i < len(listOfSums) - 1:
            print(" + ", end="")

def decomposeNumberIntoPrimeSums(userInputNumber):
    currentList = [(0, [], 2)]

    while currentList:
        currentSum, currentDecomposition, currentPrime = currentList.pop()

        if currentSum == userInputNumber:
            printList(currentDecomposition)
            continue

        for i in range(currentPrime, userInputNumber + 1):
            if currentSum + i <= userInputNumber and isPrimeNumber(i):
                newDecomposition = currentDecomposition.copy()
                newDecomposition.append(i)
                currentList.append((currentSum + i, newDecomposition, i))

main()