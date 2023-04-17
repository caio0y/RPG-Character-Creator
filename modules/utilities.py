import os
from colorama import init, Style, Fore
init()


def clear():
    os.system('cls')


def title():
    clear()
    print(Fore.MAGENTA + "          _____ _____ _____     ")
    print("         | __  |  _  |   __|    ")
    print("         |    -|   __|  |  |    ")
    print("         |__|__|__|  |_____|    ")
    print("     _                   _           ")
    print(" ___| |_ ___ ___ ___ ___| |_ ___ ___")
    print("|  _|   | .'|  _| .'|  _|  _| -_|  _|")
    print("|___|_|_|__,|_| |__,|___|_| |___|_|  ")
    print("                     _             ")
    print("     ___ ___ ___ ___| |_ ___ ___  ")
    print("    |  _|  _| -_| .'|  _| . |  _| ")
    print("    |___|_| |___|__,|_| |___|_|   "+Fore.RESET)
    print('\033[6m')
    input('press ENTER to start'.center(37) + Style.RESET_ALL)


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
            bye()
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


def bye():
    clear()
    print(Fore.LIGHTMAGENTA_EX+"   __                      __     ")
    print("  /\\ \\                    /\\ \\    ")
    print("  \\ \\ \\____  __  __     __\\ \\ \\   ")
    print("   \\ \\ '__`\\/\\ \\/\\ \\  /'__`\\ \\ \\  ")
    print("    \\ \\ \\L\\ \\ \\ \\_\\ \\/\\  __/\\ \\_\\ ")
    print("     \\ \\_,__/\\/`____ \\ \\____\\\\/\\_\\")
    print("      \\/___/  `/___/> \\/____/ \\/_/")
    print("                 /\\___/           ")
    print("                 \\/__/            \033[0m"+Fore.RESET)


def char_creation_menu():
    while True:
        clear()
        print(Fore.MAGENTA+'CHARACTER CREATION MENU'+Fore.RESET)
        print('Bard')
        print('Cleric')
        print('Rogue')
        print('Warrior')
        print('Wizard')
        print('Choose a class or')
        print('Return to main menu')
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
