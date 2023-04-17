import json
from os import system
from colorama import init, Fore
init()


def clear():
    system('cls')


def main_menu():
    options = ('Create', 'List', 'Edit', 'Add', 'Modify', 'Exit')
    options_text = (' a character', ' all characters', ' character', ' new class', ' existing class', '')
    padding = ' '*3
    hint = False
    while True:
        clear()
        print(Fore.MAGENTA + 'RPG CHARACTER CREATOR'.center(25))
        print('MAIN MENU'.center(25) + Fore.RESET, end='\n\n')
        for i in range(0, len(options)):
            print(padding+Fore.LIGHTCYAN_EX+options[i]+Fore.RESET+options_text[i])
        if hint:
            print('\n'+Fore.LIGHTBLACK_EX + 'Options: ')
            for i in range(0, len(options)):
                print(f'[{options[i]}]', end='')
            print('\n' + Fore.RESET)
        option = input('>>')
        option = option.casefold()
        if option == options[5].casefold():  # Exit
            break
        elif option == options[0].casefold():  # Create a character
            char_creation_menu()
            hint = False
            continue
        elif option == options[1].casefold():  # List all characters
            char_list_menu()
            hint = False
            continue
        elif option == options[2].casefold():  # Edit character
            clear()
            print('Edit menu soon')
            input('>>')
            hint = False
            continue
        elif option == options[3].casefold():  # Add new class
            clear()
            print('Add class menu soon')
            input('>>')
            hint = False
            continue
        elif option == options[4].casefold():  # Modify existing class
            clear()
            print('Modify class menu soon')
            input('>>')
            hint = False
            continue
        else:
            hint = True
            continue


def char_creation_menu():
    while True:
        clear()
        print(Fore.MAGENTA+'CHARACTER CREATION MENU'+Fore.RESET, end='\n\n')
        for c in classes.keys():
            print(' '*3+Fore.LIGHTCYAN_EX+c+Fore.RESET)
        print('Choose a class or')
        print(Fore.LIGHTCYAN_EX+'Return'+Fore.RESET, 'to main menu')
        option = input('>>')
        if option.casefold() == 'Return'.casefold():
            break


def char_list_menu():
    while True:
        clear()
        print('  Name | Class | Level\n'*5)
        print('Choose a character or')
        print('Return to main menu')
        option = input('>>')
        if option.casefold() == 'Return'.casefold():
            break


with open('modules/classes.json') as f:
    classes = json.load(f)
