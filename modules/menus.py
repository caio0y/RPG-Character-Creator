from modules.utilities import clear, sleep_print, select_validation, print_wrapped_text
from modules.character_creator import create_char
from colorama import init, Fore
from time import sleep
import json
init()


def main_menu():
    menu = ({'Create': ' a character', 'List': ' all characters', 'Edit': ' existing character', 'Add': ' new class',
             'Modify': ' existing class', 'Exit': ''})
    options = tuple(key.casefold() for key in menu.keys())
    padding = ' ' * 3
    while True:
        clear()
        print(Fore.MAGENTA + 'RPG CHARACTER CREATOR'.center(25))
        print('MAIN MENU'.center(25) + Fore.RESET, end='\n\n')
        for k, v in menu.items():
            sleep_print(padding + Fore.LIGHTCYAN_EX + k + Fore.RESET + v)
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
        print(Fore.MAGENTA + 'CHARACTER CREATION MENU' + Fore.RESET, end='\n\n')
        for o in options:
            sleep(0.1)
            print(padding + Fore.LIGHTCYAN_EX + o.title() + Fore.RESET)
        print('Choose a class or')
        print(Fore.LIGHTCYAN_EX + 'Return' + Fore.RESET, 'to main menu')
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
    print(Fore.LIGHTMAGENTA_EX + f"{class_data['name']}".upper().center(50) + Fore.RESET)
    print_wrapped_text(class_data['description'], 50, True)
    sleep_print('')
    print('Attribute bonus: '.rjust(25), end='')
    for k, v in class_data['modify'].items():
        if v > 0:
            print(f'+{v} {k}', end=' ')
    sleep_print('\n')
    print('Skills'.center(50))
    for skill in skills:
        print(Fore.MAGENTA + f'{skill["name"]}'.center(50) + Fore.RESET)
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


with open('database/classes.json') as f:
    classes = json.load(f)
