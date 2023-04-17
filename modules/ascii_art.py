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
