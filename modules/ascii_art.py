import os


def clear():
    os.system('cls')


def title():
    clear()
    print('\033[35m' + "          _____ _____ _____     ")
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
    print("    |___|_| |___|__,|_| |___|_|   "+'\033[39m')
    print('\033[6m')
    input('press ENTER to start'.center(37) + '\033[0m')


def bye():
    clear()
    print('\033[35;1m'+"   __                      __     ")
    print("  /\\ \\                    /\\ \\    ")
    print("  \\ \\ \\____  __  __     __\\ \\ \\   ")
    print("   \\ \\ '__`\\/\\ \\/\\ \\  /'__`\\ \\ \\  ")
    print("    \\ \\ \\L\\ \\ \\ \\_\\ \\/\\  __/\\ \\_\\ ")
    print("     \\ \\_,__/\\/`____ \\ \\____\\\\/\\_\\")
    print("      \\/___/  `/___/> \\/____/ \\/_/")
    print("                 /\\___/           ")
    print("                 \\/__/            \033[0m"+'\033[0m')


def dices():
    print('\033[34;1m'+"       .-------."+'\033[32m'+"    ______")
    print('\033[34;1m'+"      /   o   /|"+'\033[32m'+"   /\\     \\")
    print('\033[34;1m'+"     /_______/o|"+'\033[32m'+"  /o \\  o  \\")
    print('\033[34;1m'+"     | o     | |"+'\033[32m'+" /   o\\_____\\ ")
    print('\033[34;1m'+"     |   o   |o/"+'\033[32m'+" \\o   /o    /")
    print('\033[34;1m'+"     |     o |/ "+'\033[32m'+"  \\ o/  o  /")
    print('\033[34;1m'+"     '-------'  "+'\033[32m'+"   \\/____o/"+'\033[0m')
