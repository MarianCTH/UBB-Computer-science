import random
import timeit

MenuOptions = ["Generate a list of n random natural numbers. Generated numbers must be between 0 and 100",
                 "Sort the list using the insert algorithm",
                 "Sort the list using the comb algorithm",
                 "Sort 5 generated lists with the best case",
                 "Sort 5 generated lists with the average case",
                 "Sort 5 generated lists with the worst case",
                 "Exit the program"]

# Display the numbers of a list
def displayList(listToDisplay):
    for i in listToDisplay:
        print(str(i), end = " ")

# Insert Sort
def insertSort(unsortedList, step) -> list[int]:
    SortedList = unsortedList
    stepCount = 0
    for i in range(1, len(SortedList)):
        j = i
        while j > 0 and SortedList[j-1] > SortedList[j]:
            temporarySwapVariable = SortedList[j]
            SortedList[j] = SortedList[j - 1]
            SortedList[j - 1] = temporarySwapVariable
            j -= 1
            stepCount += 1

            if stepCount == int(step):
                print("\nPartially sorted list: ", end = " ")
                displayList(SortedList)
                stepCount = 0

    return SortedList

# getNextGap function
def getNextGap(gap) -> int:
    return int(gap // 1.3)
# Comb Sort
def combSort(unsortedList, step) -> list[int]:
    SortedList = unsortedList
    listSize = len(SortedList)
    gap = listSize
    swapped = True
    stepCount = 0

    while gap > 1 or swapped:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, listSize - gap):
            if SortedList[i] > SortedList[i + gap]:
                temporarySwapVariable = SortedList[i]
                SortedList[i] = SortedList[i + gap]
                SortedList[i + gap] = temporarySwapVariable
                swapped = True
                stepCount += 1
                if stepCount == int(step):
                    print("\nPartially sorted list: ", end = " ")
                    displayList(SortedList)
                    stepCount = 0

    return SortedList
# Displaying the menu options
def displayMenuOptions():
    print("\n\nPlease choose from the following options:")
    index = 1
    for menuOption in MenuOptions:
        print(f"{index} - {menuOption}")
        index += 1
# Generating the random list with the help of random library
def generateRandomList(listLength) -> list[int]:
    generatedList = []
    for i in range(listLength):
        generatedList.append(random.randint(1, 99))
    return generatedList
"""
    Display the timings and the length of a default list using specified sort 
    Supported sorting algorithms:
    - Insert
    - Comb
"""
def displayBestCaseStats(defaultTestingList, sortingAlgorithmName):
    if(sortingAlgorithmName == "Insert"):
        for length in defaultTestingList:
            bestCaseList = list(range(1, length + 1))
            time = timeit.timeit(lambda: insertSort(bestCaseList, 0), number=1)
            print(f"List Length: {length}, Time: {time:.7f} seconds")
    elif(sortingAlgorithmName == "Comb"):
        for length in defaultTestingList:
            bestCaseList = list(range(1, length + 1))
            time = timeit.timeit(lambda: combSort(bestCaseList, 0), number=1)
            print(f"List Length: {length}, Time: {time:.7f} seconds")
def displayAverageCaseStats(defaultTestingList, sortingAlgorithmName):
    if(sortingAlgorithmName == "Insert"):
        for length in defaultTestingList:
            averageCaseList = generateRandomList(length)
            time = timeit.timeit(lambda: insertSort(averageCaseList, 0), number=1)
            print(f"List Length: {length}, Time: {time:.7f} seconds")
    elif(sortingAlgorithmName == "Comb"):
        for length in defaultTestingList:
            averageCaseList = generateRandomList(length)
            time = timeit.timeit(lambda: combSort(averageCaseList, 0), number=1)
            print(f"List Length: {length}, Time: {time:.7f} seconds")
def displayWorstCaseStats(defaultTestingList, sortingAlgorithmName):
    if(sortingAlgorithmName == "Insert"):
        for length in defaultTestingList:
            worstCaseList = list(range(length, 0, -1))
            time = timeit.timeit(lambda: insertSort(worstCaseList, 0), number=1)
            print(f"List Length: {length}, Time: {time:.7f} seconds")
    elif(sortingAlgorithmName == "Comb"):
        for length in defaultTestingList:
            worstCaseList = list(range(length, 0, -1))
            time = timeit.timeit(lambda: combSort(worstCaseList, 0), number=1)
            print(f"List Length: {length}, Time: {time:.7f} seconds")
def main():
    generatedList = []
    defaultTestingList = [500, 1000, 2000, 4000, 8000]

    while(True):
        displayMenuOptions()
        option = input(">> ")

        match option:
            case "1":
                print("\nPlease enter how many numbers you want to generate:")
                listLen = int(input(">> "))

                generatedList = generateRandomList(listLen)

                print("Generated list: ", end=" ")
                displayList(generatedList)
            case "2":
                if len(generatedList) != 0:
                    print("\nPlease enter the step: ")
                    step = input(">> ")
                    sortedListInsert = insertSort(generatedList, step)

                    print("\nSorted list with insert algorithm: ", end=" ")
                    displayList(sortedListInsert)
                else:
                    print("\nThere is no generated list. Please use first function before using 2 or 3.")
            case "3":
                if len(generatedList) != 0:
                    print("\nPlease enter the step: ")
                    step = input(">> ")

                    sortedListComb = combSort(generatedList, step)

                    print("\nSorted list with comb algorithm: ", end=" ")
                    displayList(sortedListComb)
                else:
                    print("There is no generated list. Please use first function before using 2 or 3.")
            case "4":
                print("\nBest case timing for insert sort:")
                displayBestCaseStats(defaultTestingList, "Insert")

                print("\nBest case timing for Comb Sort:")
                displayBestCaseStats(defaultTestingList, "Comb")
            case "5":
                print("\nAverage case timing for insert sort:")
                displayAverageCaseStats(defaultTestingList, "Insert")

                print("\nAverage case timing for Comb Sort:")
                displayAverageCaseStats(defaultTestingList, "Comb")
            case "6":
                print("\nWorst case timing for insert sort:")
                displayWorstCaseStats(defaultTestingList, "Insert")

                print("\nWorst case timing for Comb Sort:")
                displayWorstCaseStats(defaultTestingList, "Comb")
            case "7":
                print("\n\n\nClosing the program...\n\n\n")
                break
            case _:
                print("\nThis is not a valid option ! Please try again...")

main()