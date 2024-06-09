from menu_options import *


def main():
    complex_numbers_list = []
    complex_number_dictionary = {}

    while True:
        show_menu()

        user_choice = get_user_choice()
        if handle_user_choice(user_choice, complex_numbers_list, complex_number_dictionary):
            break

# Functions to deal with complex numbers -- list representation
def read_complex_number() -> list:
    real_part = int(input("Real part = "))
    imaginary_part = int(input("Imaginary part = "))

    return [real_part, imaginary_part]
def display_complex_numbers_list(complex_numbers_list):
    complex_list_as_string = ""

    for i, complex_number in enumerate(complex_numbers_list):
        complex_list_as_string += f"{complex_number[0]}+{complex_number[1]}i"

        if i < len(complex_numbers_list) - 1:
            complex_list_as_string += ", "

    print(complex_list_as_string)
###################

# Functions to deal with complex numbers -- dict representation
def read_complex_number_dictionary() -> dict:
    real_part = int(input("a = "))
    imaginary_part = int(input("b = "))

    return {"real_part": real_part, "imaginary_part": imaginary_part}
def display_complex_numbers_dictionary(complex_numbers_dictionary):
    comma_counter = 1
    complex_numbers_dictionary_length = len(complex_numbers_dictionary)
    print(complex_numbers_dictionary_length)
    for complex_name, complex_number in complex_numbers_dictionary.items():
        real_part = complex_number['real_part']
        imaginary_part = complex_number['imaginary_part']

        if imaginary_part > 0:
            print(f"{real_part} + {imaginary_part}i", end="")
        else:
            print(f"{real_part} {imaginary_part}i", end="")
        if comma_counter < complex_numbers_dictionary_length:
            print(",", end=" ")
        comma_counter += 1
###################

# Functions that deal with subarray/subsequence properties
# 1+3i, 31i, 33+i, 111, 11-313i
def digits_of_number(number):
    digits_complex_number = 0
    frequency_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index in number:
        if (index < 0):
            index = index * (-1)
        while (index > 0):
            frequency_list[index % 10] = 1
            index //= 10
    for index in range(1, 10):
        if (frequency_list[index] == 1):
            digits_complex_number = digits_complex_number * 10 + index
    return digits_complex_number

def get_longest_subarray_same_base_10_digits(complex_numbers_list):
    current_subarray = []
    current_subarray_length = 0
    max_current_subarray = []
    max_current_subarray_length = 0
    current_digits = 0

    for complex_number in complex_numbers_list:
        complex_number_digits = digits_of_number(complex_number)
        if (current_digits == complex_number_digits):
            current_subarray.append(complex_number)
            current_subarray_length += 1
        else:
            if (current_subarray_length > max_current_subarray_length):
                max_current_subarray_length = current_subarray_length
                max_current_subarray = current_subarray
            current_subarray = []
            current_subarray.append(complex_number)
            current_subarray_length = 1
            current_digits = complex_number_digits
    return max_current_subarray
###################

# UI Menu section
def show_menu():
    for key, value in menu_options.items():
        print(f"{key} - {value}")
def get_user_choice():
    return input("Please enter your choice:\n>> ")
###################

# Handle user choice section
def handle_user_choice(user_choice, complex_numbers_list, complex_numbers_dictionary):
    if user_choice in menu_options:
        if menu_options[user_choice] == MENU_EXIT:
            print("Exiting the application.")
            return True
        elif menu_options[user_choice] == MENU_READ_COMPLEX_NUMBERS:

            print("Please enter how many complex numbers to read: ")
            complex_numbers_list_length = int(input(">> "))

            print("Please enter " + str(complex_numbers_list_length) + " complex numbers: ")
            for _ in range(complex_numbers_list_length):
                complex_numbers_list.append(read_complex_number())
                print("")
            """
            print("Please enter how many complex numbers to read: ")
            complex_numbers_dictionary_length = int(input(">> "))

            print("Please enter " + str(complex_numbers_dictionary_length) + " complex numbers: ")
            for i in range(complex_numbers_dictionary_length):
                new_complex_number = read_complex_number_dictionary()
                complex_numbers_dictionary[f'complex_{i + 1}'] = new_complex_number
                print("")"""
        elif menu_options[user_choice] == MENU_DISPLAY_COMPLEX_NUMBERS:
            display_complex_numbers_list(complex_numbers_list)
            # display_complex_numbers_dictionary(complex_numbers_dictionary)
            print("\n")
        elif menu_options[user_choice] == MENU_LONGEST_SUBARRAY:
            longest_subarray = get_longest_subarray_same_base_10_digits(complex_numbers_list)
            if longest_subarray:
                print(f"Longest subarray with the same base 10 digits: {longest_subarray}")
            else:
                print("No subarray found with the same base 10 digits.")
    else:
        print("Wrong input. Please try again !")
###################

if __name__ == "__main__":
    main()
