#1.Generate the first prime number larger than a given natural number n.
def main():
    #introduction
    n = int(input("Please enter a number:\n"))

    #showing the result
    result = NextPrimeNumber(n)
    print("\nThe first prime number larger than " + str(n) + " is " + str(result))

def isPrime(x):
    if(x < 2):
        return False
    if(x == 2):
        return True
    if(x % 2 == 0):
        return False
    for i in range(2, int(x**0.5) + 1):
        if(x % i == 0):
            return False
    return True

#the function to find the first prime number larger than a given number
def NextPrimeNumber(number):
    if number < 2:
        return 2
    number += 1
    while not isPrime(number):
        number += 1
    return number


main()
