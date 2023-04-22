from modules.utilities import clear, sleep_print, select_validation, print_wrapped_text, view_sheet
from modules.character_creator import create_char
from time import sleep
import json


def main_menu():
    menu = ({'Create': ' a character', 'List': ' all characters', 'Edit': ' existing character', 'Add': ' new class',
             'Modify': ' existing class', 'Exit': ''})
    options = tuple(key.casefold() for key in menu.keys())
    padding = ' ' * 3
    while True:
        clear()
        print('\033[35m'+'RPG CHARACTER CREATOR'.center(25))
        print('MAIN MENU'.center(25)+'\033[0m', end='\n\n')
        for k, v in menu.items():
            sleep_print(padding + '\033[36;1m' + k + '\033[0m' + v)
        option = select_validation(options)
        if option == options[5]:  # Exit
            break
        elif option == options[0]:  # Create a character
            char_creation_menu()
            continue
        elif option == options[1]:  # List all characters
            char_list_menu()
            continue
        elif option == options[2]:  # Edit character
            clear()
            print('Edit menu soon')
            input('>>')
            continue
        elif option == options[3]:  # Add new class
            clear()
            print('Add class menu soon')
            input('>>')
            continue
        elif option == options[4]:  # Modify existing class
            clear()
            print('Modify class menu soon')
            input('>>')
            continue
        else:
            continue


def char_creation_menu():
    options = tuple(item.casefold() for item in classes.keys())
    exit_menu = 'Return'
    padding = ' ' * 3
    while True:
        clear()
        print('\033[35m' + 'CREATION MENU' + '\033[0m', end='\n\n')
        for o in options:
            sleep(0.1)
            print(padding + '\033[36;1m' + o.title() + '\033[0m')
        print('\nChoose a class or')
        print('\033[36;1m' + 'Return' + '\033[0m', 'to main menu')
        option = select_validation(options, exit_menu)
        if option == exit_menu.casefold():
            break
        elif option in options:
            confirm = show_class(option.casefold())
            if confirm == 'yes':  # Create char with selected class
                create_char(option)
                continue
            else:  # Return to classes' list
                continue
        else:
            continue


def show_class(choose_class):
    clear()
    class_data = classes[choose_class]
    skills = class_data['skills']
    print('\033[35;1m' + f"{class_data['name']}".upper().center(50) + '\033[0m')
    print_wrapped_text(class_data['description'], 50, True)
    sleep_print('')
    print('Attribute bonus: '.rjust(25), end='')
    for k, v in class_data['modify'].items():
        if v > 0:
            print(f'+{v} {k}', end=' ')
    sleep_print('\n')
    print('Skills'.center(50))
    for skill in skills:
        print('\033[35m' + f'{skill["name"]}'.center(50) + '\033[0m')
        print_wrapped_text(skill['description'], 50, True)
        print('')
    print('Confirm selection?')
    create = select_validation(('yes', 'no'), stdoption='yes')
    return create


def char_list_menu():
    with open('database/characters.json', 'r') as archive:
        characters_data = json.load(archive)
    chars_names = [name for name in characters_data.keys()]
    while True:
        clear()
        for name in chars_names:
            char = characters_data[name]
            print(' '+char['name'].ljust(20), end='')
            print(char['gender'].ljust(6), end=' | ')
            print('Level', (char['level']), char['char class'])
        option = select_validation(chars_names, 'return', stdoption='return')
        if option == 'return':
            break
        else:
            sheet = characters_data[option]
            view_sheet(sheet)
            input('\nReturn to...?')


with open('database/classes.json') as f:
    classes = json.load(f)
