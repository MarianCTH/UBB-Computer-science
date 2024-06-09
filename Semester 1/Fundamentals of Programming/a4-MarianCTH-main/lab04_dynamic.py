"""
    Dynamic Programming
    1. Determine the longest common subsequence of two given sequences.
    Subsequence elements are not required to occupy consecutive positions.
    For example, if X = "MNPNQMN" and Y = "NQPMNM", the longest common subsequence has length 4, and can be one of "NQMN", "NPMN" or "NPNM".
    Determine and display both the length of the longest common subsequence as well as at least one such subsequence.

      1 2 3 4 5 6 7
    1 M N P N Q M N
    2 N Q P M N M
"""


def findLongestSubsequnce(firstSequence, secondSequence):
    firstSequenceLen = len(firstSequence)
    secondSequenceLen = len(secondSequence)
    frequencyMatrix = [[0] * (secondSequenceLen + 1) for _ in range(firstSequenceLen + 1)]

    for i in range(1, firstSequenceLen + 1):
        for j in range(1, secondSequenceLen + 1):
            if firstSequence[i - 1] == secondSequence[j - 1]:
                frequencyMatrix[i][j] = frequencyMatrix[i - 1][j - 1] + 1
            else:
                frequencyMatrix[i][j] = max(frequencyMatrix[i - 1][j], frequencyMatrix[i][j - 1])
    # frequency matrix = how many unique chars repeat till i & j

    longestSequenceLength = frequencyMatrix[firstSequenceLen][secondSequenceLen]
    longestSequence = [""] * longestSequenceLength

    i = firstSequenceLen
    j = secondSequenceLen
    while i > 0 and j > 0:
        if firstSequence[i - 1] == secondSequence[j - 1]:
            longestSequence[longestSequenceLength - 1] = firstSequence[i - 1]
            i -= 1
            j -= 1
            longestSequenceLength -= 1
        elif frequencyMatrix[i - 1][j] > frequencyMatrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    longestSequenceString = ""
    for ls in longestSequence:
        longestSequenceString += ls

    return frequencyMatrix[firstSequenceLen][secondSequenceLen], longestSequenceString


def main():
    firstSequenceInput = "MNPNQMN"
    secondSequenceInput = "NQPMNM"

    longestSequenceLength, longestSequence = findLongestSubsequnce(firstSequenceInput, secondSequenceInput)

    print(
        "Longest subsequence from " + firstSequenceInput + " and " + secondSequenceInput + " is " + longestSequence + " (Length: " + str(
            longestSequenceLength) + ")")


main()