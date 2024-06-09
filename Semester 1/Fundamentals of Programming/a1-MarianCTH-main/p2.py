# 10. The palindrome of a number is the number obtained by reversing the order 
# of its digits (e.g. the palindrome of 237 is 732). For a given natural number n, determine its palindrome.

def main():
    #introducing a value
    v = int(input("Please write a value: "))

    #showing the palindrome
    print("The palindrome of the given value is " + str(reverse(v)))


def reverse(n):
    reversed = 0
    while(n):
        reversed = (reversed * 10) + (n % 10)
        n = n // 10
    return reversed

main()
