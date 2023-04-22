import re
import json
from os import system
from time import sleep


def clear():
    system('cls')


def sleep_print(*texts: str, secs: float = 0.1) -> None:
    if not texts:
        return
    if secs < 0:
        return
    sleep(secs)
    for text in texts:
        print(text)


def select_validation(options_tuple, *add_options, stdoption=None):
    option = default_option(stdoption)
    options = [item.casefold() for item in options_tuple]
    if add_options:
        options.extend([item.casefold() for item in add_options])
    if option not in options:
        print('\n' + '\033[30;1m' + 'Options: ')
        for i in range(0, len(options)):
            print(f'[{options[i].title()}]', end='')
        print('\n' + '\033[0m')
        option = default_option(stdoption)
        while option not in options:
            print('\033[31;1m' + 'Invalid option!' + '\033[0m')
            option = default_option(stdoption)
        return option
    else:
        return option


def default_option(stdoption):
    if stdoption:
        stdoption = stdoption.casefold()
        option = input('>>').casefold() or stdoption
        if option.casefold() == stdoption:
            return stdoption
        else:
            return option
    else:
        option = input('>>').casefold()
        return option


def print_wrapped_text(text: str, max_chars_per_line: int, is_paragraph: bool = False) -> None:
    if not text:
        return
    words = text.split()
    current_line = '  ' if is_paragraph else ''
    wrapped_text_lines = []
    for word in words:
        if len(current_line + ' ' + word) <= max_chars_per_line:
            current_line += ' ' + word if current_line else word
        else:
            wrapped_text_lines.append(current_line)
            current_line = word
    wrapped_text_lines.append(current_line)
    for text_line in wrapped_text_lines:
        sleep_print(text_line)


def input_validation(len_min: int = 4, len_max: int = 20):
    user_input = input('>> ').strip()
    user_input = re.sub('\s+', ' ', user_input)   # Remove duplicate spaces
    if not len_min <= len(user_input) <= len_max:
        print(f"Must have between {len_min} and {len_max} characters.")
        return None
    if not re.match("^[a-zA-Z,'\"\s]+$", user_input):
        print("Must contain only letters, spaces, double quotes, one apostrophe and one comma.")
        return None
    if user_input.count('"') > 2:
        print("Must contain no more than 2 double quotes.")
        return None
    elif user_input.count("'") > 1:
        print("Must contain no more than 1 apostrophe.")
        return None
    elif user_input.count(",") > 1:
        print("Must contain no more than 1 comma.")
        return None
    # If all validations passed, return the valid string
    return user_input


def view_sheet(char):
    with open('database/classes.json', 'r') as archive:
        char_class_data = json.load(archive)
    modify = char_class_data[str(char['char class']).casefold()]['modify']
    clear()
    print('Name:'.rjust(10), char["name"])
    print('Gender:'.rjust(10), char["gender"])
    print('Class:'.rjust(10), f'level {char["level"]} {char["char class"]}')
    print('Skill:'.rjust(10), char["skill"])
    for attribute, points in char['attributes'].items():
        if modify[attribute] > 0:
            print(f"{attribute}:".rjust(10), points, '\033[30;1m' + f"(+{modify[attribute]})" + '\033[0m')
        elif modify[attribute] < 0:
            print(f"{attribute}:".rjust(10), points, '\033[30;1m' + f"(-{modify[attribute]})" + '\033[0m')
        else:
            print(f"{attribute}:".rjust(10), points)
    print('')
