# 15. Generate the largest perfect number smaller than a given natural number n. 
# If such a number does not exist, a message should be displayed. 
# A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3).

def main():
    #introduction
    n = int(input("Please enter a natural number: "))

    #calculating the largest perfect number smaller than n
    lpn = largestPerfectNumber(n)

    #printing the result
    print("Largest perfect number smaller than " + str(n) + " is " + str(lpn))

#sum of all x divisors
def divisorSum(x):
    sum = 0
    for i in range(1, x + 1):
        if(x % i == 0):
            sum += i
    return sum

#finding the largest perfect number by lowering with one everytime the number is not perfect
def largestPerfectNumber(y):
    found = False
    y -= 1
    while (found == False):
        if(divisorSum(y) - y == y):
            found = True
            return y
        else:
            y -= 1
    return None


main()
