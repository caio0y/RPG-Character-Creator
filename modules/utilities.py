import json
from time import sleep
from os import system
from colorama import init, Fore
init()


def clear():
    system('cls')


def main_menu():
    menu = ({'Create': ' a character', 'List': ' all characters', 'Edit': ' character', 'Add': ' new class',
            'Modify': ' existing class', 'Exit': ''})
    options = tuple(key.casefold() for key in menu.keys())
    padding = ' '*3
    while True:
        clear()
        print(Fore.MAGENTA + 'RPG CHARACTER CREATOR'.center(25))
        print('MAIN MENU'.center(25) + Fore.RESET, end='\n\n')
        for k, v in menu.items():
            sleep(0.1)
            print(padding+Fore.LIGHTCYAN_EX+k+Fore.RESET+v)
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
            input('Erro desconhecido')
            continue


def char_creation_menu():
    options = tuple(item.casefold() for item in classes.keys())
    exit_menu = 'Return'
    padding = ' ' * 3
    while True:
        clear()
        print(Fore.MAGENTA+'CHARACTER CREATION MENU'+Fore.RESET, end='\n\n')
        for o in options:
            sleep(0.1)
            print(padding+Fore.LIGHTCYAN_EX+o.title()+Fore.RESET)
        print('Choose a class or')
        print(Fore.LIGHTCYAN_EX+'Return'+Fore.RESET, 'to main menu')
        option = select_validation(options, True, exit_menu)
        if option == exit_menu.casefold():
            break
        elif option in options:
            print(f'You choose {option.title()}')
            sleep(1)
            continue
        else:
            continue


def char_list_menu():
    options = ['Return']
    while True:
        clear()
        print('  Name | Class | Level\n'*5)
        print('Choose a character or')
        print('Return to main menu')
        option = input('>>')
        if option.casefold() == options[0].casefold():
            break


def select_validation(options_tuple, need_add_options=False, *add_options):
    selected_option = input('>>').casefold()
    options_list = [item.casefold() for item in options_tuple]
    if need_add_options:
        options_list.extend([item.casefold() for item in add_options])
    if selected_option not in options_list:
        print('\n' + Fore.LIGHTBLACK_EX + 'Options: ')
        for i in range(0, len(options_list)):
            print(f'[{options_list[i].title()}]', end='')
        print('\n' + Fore.RESET)
        selected_option = input('>>').casefold()
        while selected_option not in options_list:
            print(Fore.RED+'Invalid option!'+Fore.RESET)
            selected_option = input('>>').casefold()
        return selected_option
    else:
        return selected_option


with open('modules/classes.json') as f:
    classes = json.load(f)
