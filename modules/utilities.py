import logging
from os import system
from time import sleep
from colorama import init, Fore

init()
logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def clear():
    system('cls')


def sleep_print(*texts: str, secs: float = 0.1) -> None:
    if not texts:
        logging.error('Empty string variable in sleep_print function')
        return
    if secs < 0:
        logging.error('secs argument is less than zero')
        return
    sleep(secs)
    for text in texts:
        print(text)


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


def print_wrapped_text(text: str, max_chars_per_line: int, is_paragraph: bool = False) -> None:
    if not text:
        logging.error('Empty string variable in print_wrapped_text function')
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
