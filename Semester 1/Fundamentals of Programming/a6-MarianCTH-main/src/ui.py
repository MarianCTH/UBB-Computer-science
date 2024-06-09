#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#

from functions import *
from program_formats import *

ADD_CORRECT_PARAMETERS = 3
INSERT_CORRECT_PARAMETERS = 4
REMOVE_DAY_TO_DAY = 4
REMOVE_DAY_OR_CATEGORY = 2
LIST_ALL_EXPENSES = 1
LIST_EXPENSES_BY_CATEGORY = 2
LIST_EXPENSES_BY_CATEGORY_AND_CONDITION = 4
FILTER_BY_CATEGORY = 2
FILTER_BY_CATEGORY_AND_CONDITION = 4

def display_functionalities():
    print("Program functionalities: ")
    for format_name, format_description in PROGRAM_FORMATS.items():
        print(f"{format_name}:")
        if isinstance(format_description, set):
            for format_item in format_description:
                print(f"  - {format_item}")
        else:
            print(f"  - {format_description}")
def get_user_command() -> str:
    return input("\nPlease enter a command\n>> ")
def handle_user_command(user_input: str, family_expenses):
    user_command_parameters = user_input.split()
    if not user_command_parameters:
        print("Invalid command. Please enter a valid command.")
        return

    user_command = user_command_parameters[0].lower()
    if user_command == 'add':
        if len(user_command_parameters) == ADD_CORRECT_PARAMETERS:
            sum_value = user_command_parameters[1]
            category = user_command_parameters[2]

            add_expense(family_expenses, sum_value, category)
        else:
            print("Invalid 'add' command. Please follow the format: add <sum> <category>")
    elif user_command == 'insert':
        if len(user_command_parameters) == INSERT_CORRECT_PARAMETERS:
            day = user_command_parameters[1]
            sum_value = user_command_parameters[2]
            category = user_command_parameters[3]

            insert_expense(family_expenses, day, sum_value, category)
        else:
            print("Invalid 'insert' command. Please follow the format: insert <day> <sum> <category>")
    elif user_command == 'remove':
        if (len(user_command_parameters) >= REMOVE_DAY_OR_CATEGORY and
            len(user_command_parameters) <= REMOVE_DAY_TO_DAY):
            if 'to' in user_command_parameters:
                start_day = user_command_parameters[1]
                end_day = user_command_parameters[3]
                remove_expense(family_expenses, start_day=start_day, end_day=end_day)
            else:
                day_or_category = user_command_parameters[1]
                if day_or_category.isdigit():
                    remove_expense(family_expenses, day=int(day_or_category))
                else:
                    remove_expense(family_expenses, category=day_or_category)
        else:
            print("Invalid 'remove' command. Please follow the format: remove <day or category> | remove <start day> to <end day>")
    elif user_command == 'list':
        if len(user_command_parameters) == LIST_ALL_EXPENSES:
            list_expenses(family_expenses)
        elif len(user_command_parameters) == LIST_EXPENSES_BY_CATEGORY:
            category = user_command_parameters[1]
            list_expenses(family_expenses, category=category)
        elif (len(user_command_parameters) == LIST_EXPENSES_BY_CATEGORY_AND_CONDITION and
              user_command_parameters[2] in {'<', '=', '>'}):
            category = user_command_parameters[1]
            operator = user_command_parameters[2]
            amount = user_command_parameters[3]
            list_expenses(family_expenses, category=category, operator=operator, amount = amount)
        else:
            print("Invalid 'list' command. Please follow the format: list | list <category> | list <category> [<|=|>] <value>")
    elif user_command == 'filter':
        if len(user_command_parameters) == FILTER_BY_CATEGORY:
            category = user_command_parameters[1]
            filter_expenses(family_expenses, category=category)
        elif len(user_command_parameters) == FILTER_BY_CATEGORY_AND_CONDITION:
            category = user_command_parameters[1]
            operator = user_command_parameters[2]
            amount = user_command_parameters[3]
            filter_expenses(family_expenses, category=category, operator=operator, amount=amount)
        else:
            print("Invalid 'filter' command. Please follow the format: filter <category> | filter <category> [<|=|>] <value>")
    elif user_command == 'undo':
        undo_operation(family_expenses)
    else:
        print("Unknown command. Please enter a valid command.")

def initialise_ui():
    family_expenses = {}
    display_functionalities()
    while True:
        handle_user_command(get_user_command(), family_expenses)
