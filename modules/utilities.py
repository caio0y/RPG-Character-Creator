import json
from os import system
from time import sleep
from colorama import init, Fore
init()


def clear():
    system('cls')


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
            sleep(0.1)
            print(padding + Fore.LIGHTCYAN_EX + k + Fore.RESET + v)
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
        option = select_validation(options, True, exit_menu)
        if option == exit_menu.casefold():
            break
        elif option in options:
            confirm = show_class(option.title())
            if confirm == 'Y':
                input('Yes')
                continue
            else:
                input('No')
                continue
        else:
            continue


def char_list_menu():
    options = ['Return']
    while True:
        clear()
        print('  Name | Class | Level\n' * 5)
        print('Choose a character or')
        print('Return to main menu')
        option = input('>>')
        if option.casefold() == options[0].casefold():
            break


def select_validation(options_tuple, need_add_options=False, *add_options):
    option = input('>>').casefold()
    options = [item.casefold() for item in options_tuple]
    if need_add_options:
        options.extend([item.casefold() for item in add_options])
    if option not in options:
        print('\n' + Fore.LIGHTBLACK_EX + 'Options: ')
        for i in range(0, len(options)):
            print(f'[{options[i].title()}]', end='')
        print('\n' + Fore.RESET)
        option = input('>>').casefold()
        while option not in options:
            print(Fore.RED + 'Invalid option!' + Fore.RESET)
            option = input('>>').casefold()
        return option
    else:
        return option


def show_class(choose_class):
    class_data = classes[choose_class]
    skills = class_data['skills']
    print(Fore.LIGHTMAGENTA_EX + class_data['name'] + Fore.RESET)
    print(class_data['description'])
    for k, v in class_data['modify'].items():
        if v > 0:
            print(f'+{v} {k}')
    print('')
    for skill in skills:
        print(skill['name'])
        print(skill['description'])
        print('')
    create = input('Confirm selection? [Y]') or 'Y'
    return create


with open('database/classes.json') as f:
    classes = json.load(f)
