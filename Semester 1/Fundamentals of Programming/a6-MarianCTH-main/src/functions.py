from datetime import datetime
import copy
expenses_modification_history = []

def is_valid_sum(amount):
   if not amount.isnumeric():
       return False
   amount = int(amount)
   return True
def is_valid_category(category):
    default_categories = ["housekeeping", "food", "transport", "clothing", "internet", "others"]
    for category_type in default_categories:
        if category_type == category:
            return True
    return False
def is_valid_day(day):
    day = int(day)
    if day > 30 or day < 1:
        return False
    return True
def is_valid_operator(operator):
    operators = ['<', '>', '=']
    if operator in operators:
        return True
    return False

def add_expense(family_expenses, amount, category):
    expenses_modification_history.append(copy.deepcopy(family_expenses))

    if amount and category:
        if is_valid_sum(amount) and is_valid_category(category):
            current_day = datetime.now().day
            expenses_length = len(family_expenses)
            family_expenses[expenses_length] = {"day": current_day, "amount": amount, "category": category}
            print("Expense added successfully !")
        else:
            print("Invalid amount or category input !")
def insert_expense(family_expenses, day, amount, category):
    expenses_modification_history.append(copy.deepcopy(family_expenses))

    if is_valid_day(day) and is_valid_sum(amount) and is_valid_category(category):
        expenses_length = len(family_expenses)
        family_expenses[expenses_length] = {"day": day, "amount": amount, "category": category}
        print("Expense added successfully !")
    else:
        print("Invalid day, amount or category input !")
def remove_expense(family_expenses, day=None, start_day=None, end_day=None, category=None):
    expenses_modification_history.append(copy.deepcopy(family_expenses))

    keys_to_remove = []

    if day and is_valid_day(day):
        for expense_key, expense_data in family_expenses.items():
            if int(expense_data['day']) == int(day):
                keys_to_remove.append(expense_key)
                print("Day removed succesfully !")
    elif start_day and end_day:
        for expense_key, expense_data in family_expenses.items():
            if int(start_day) <= int(expense_data['day']) <= int(end_day):
                keys_to_remove.append(expense_key)
                print("Removed succesfully !")
    elif category and is_valid_category(category):
        for expense_key, expense_data in family_expenses.items():
            if expense_data['category'] == category:
                keys_to_remove.append(expense_key)
                print("Category removed succesfully !")

    for expense_key in keys_to_remove:
        family_expenses.pop(expense_key, None)
def list_expenses(family_expenses, category=None, operator=None, amount=None):
        if category and operator and amount and operator:
            if is_valid_category(category):
                for expenses in family_expenses:
                    if family_expenses[expenses]['category'] == category and eval(family_expenses[expenses]['amount'] + operator + str(amount)):
                        print(f"Day: {family_expenses[expenses]['day']}, Amount: {family_expenses[expenses]['amount']}, Category: {family_expenses[expenses]['category']}")
            else:
                print("Invalid category, amount or operator !")
        elif category:
            if is_valid_category(category):
                for expenses in family_expenses:
                    if family_expenses[expenses]['category'] == category:
                        print(f"Day: {family_expenses[expenses]['day']}, Amount: {family_expenses[expenses]['amount']}, Category: {family_expenses[expenses]['category']}")
            else:
                print("Invalid category, amount or operator !")
        else:
            for expenses in family_expenses:
                print(f"Day: {family_expenses[expenses]['day']}, Amount: {family_expenses[expenses]['amount']}, Category: {family_expenses[expenses]['category']}")
def filter_expenses(family_expenses, category, operator=None, amount=None):
    expenses_modification_history.append(copy.deepcopy(family_expenses))

    keys_to_remove = []

    if category and operator and amount:
        if is_valid_category(category) and is_valid_operator(operator) and is_valid_sum(amount):
            for expense_key, expense_data in family_expenses.items():
                if not (expense_data['category'] == category and eval(expense_data['amount'] + operator + amount)):
                    keys_to_remove.append(expense_key)
            print("Filter done succesfully !")
        else:
            print("Invalid input !")
    elif category:
        if is_valid_category(category):
            for expense_key, expense_data in family_expenses.items():
                if expense_data['category'] != category:
                    keys_to_remove.append(expense_key)
            print("Filter done succesfully !")
        else:
            print("Invalid category !")

    for expense_key in keys_to_remove:
        family_expenses.pop(expense_key, None)
def undo_operation(family_expenses):
    if len(expenses_modification_history) > 1:
        family_expenses.clear()
        family_expenses.update(expenses_modification_history.pop(-2))
        print("Undo operation successful!")
    else:
        print("Undo not possible. No previous state available.")
