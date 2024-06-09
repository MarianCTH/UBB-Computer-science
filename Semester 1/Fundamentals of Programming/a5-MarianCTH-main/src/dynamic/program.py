from menu_options import *

def main():
    complex_numbers_list = []
    while True:
        show_menu()

        user_choice = get_user_choice()
        if handle_user_choice(user_choice, complex_numbers_list):
            break

# Functions to deal with complex numbers -- list representation
def read_complex_number() -> list:
    real_part = int(input("a = "))
    imag_part = int(input("b = "))

    return [real_part, imag_part]
def display_complex_numbers_list(complex_numbers_list):
    complex_number_list_as_string = ""

    for i, complex_number in enumerate(complex_numbers_list):
        complex_number_list_as_string  += f"{complex_number[0]}+{complex_number[1]}i"

        if i < len(complex_numbers_list) - 1:
            complex_number_list_as_string  += ", "

    print(complex_number_list_as_string)
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
def get_real_part_list(complex_numbers_list) -> list:
    real_part_only_list = []
    for complex_numbers in complex_numbers_list:
        real_part_only_list.append(complex_numbers[0])
        
    return real_part_only_list
# The length and elements of a longest increasing subsequence, when considering each number's real part
def longest_increasing_subsequence_list(real_part_list):
    real_part_list_length = len(real_part_list)
    real_part_lengths = [1] * real_part_list_length
    predecessors = [-1] * real_part_list_length

    for i in range(1, real_part_list_length):
        for j in range(0, i):
            if real_part_list[i] > real_part_list[j] and real_part_lengths[i] < real_part_lengths[j] + 1:
                real_part_lengths[i] = real_part_lengths[j] + 1
                predecessors[i] = j

    print(real_part_lengths)
    print(predecessors)
    max_length_index, _= max(enumerate(real_part_lengths), key=lambda x: x[1])

    list_elements = []
    while max_length_index != -1:
        list_elements.insert(0, real_part_list[max_length_index])
        max_length_index = predecessors[max_length_index]

    return len(list_elements), list_elements

###################

# UI Menu section
def show_menu():
    for key, value in menu_options.items():
        print(f"{key} - {value}")
def get_user_choice():
    return input("Please enter your choice:\n>> ")
###################

# Handle user choice section
def handle_user_choice(user_choice, complex_numbers_list):
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
                print("")
            """
        elif menu_options[user_choice] == MENU_DISPLAY_COMPLEX_NUMBERS:
            display_complex_numbers_list(complex_numbers_list)
            # display_complex_numbers_dictionary(complex_numbers_dictionary)
            print("\n")
        elif menu_options[user_choice] == MENU_LONGEST_SUBSEQUENCE:
            longest_increasing_subsequence_length, longest_increasing_subsequence = longest_increasing_subsequence_list([1,3,2,4,10,6,1])#get_real_part_list(complex_numbers_list))
            print(f"Longest increasing subsequence is {longest_increasing_subsequence} with length {longest_increasing_subsequence_length}")
    else:
        print("Wrong input. Please try again !")
###################

if __name__ == "__main__":
    main()
