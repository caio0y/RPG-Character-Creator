import json
from datetime import datetime
from random import randint as roll
from modules.ascii_art import dices
from modules.utilities import clear, select_validation, print_wrapped_text, sleep_print, input_validation, view_sheet


def create_char(selected_class):
    with open('database/classes.json', 'r') as f:
        char_classes_data = json.load(f)
        selected_class_data = char_classes_data[selected_class]
    char_name = name()
    char_gender = gender(char_name)
    char_skill = select_skill(selected_class, [skill for skill in selected_class_data['skills']])
    attributes = roll_dices(char_name, selected_class_data['modify'])
    character = {
        'name': char_name,
        'gender': char_gender,
        'char class': selected_class_data['name'],
        'level': 1,
        'skill': char_skill,
        'attributes': attributes,
        'create_date': datetime.now().strftime('%d/%m/%y - %H:%M')
    }
    input(f"\n\033[6mPress ENTER to view the {char_name}'s sheet\033[0m")
    view_sheet(character)
    save_character(char_name.casefold(), character)


def name():
    clear()
    print("What's the name of your character?")
    while True:
        char_name = input_validation()
        if char_name:
            char_name = char_name.title()
            break
    return char_name


def gender(char_name):
    genders = ['Female', 'Male', 'Other']
    while True:
        clear()
        print(f"What's the gender of {char_name}?")
        char_gender = select_validation(genders, stdoption=genders[2])
        print(f'You chose {char_gender}, are you sure?')
        confirm = select_validation(('yes', 'no'), stdoption='yes')
        if confirm == 'yes':
            return char_gender


def select_skill(selected_class, skills):
    clear()
    print(f'Choose a skill of the {selected_class} class:\n')
    for skill in skills:
        print(f"{skill['name']}".center(50))
        print_wrapped_text(skill['description'], 50, True)
        print('')
    char_skill = select_validation([skill['name'] for skill in skills]).title()
    return char_skill


def roll_dices(char_name, modify: dict):
    empty_attributes = ['CHA', 'DEX', 'FOR', 'INT', 'WIS']
    attributes = {}
    clear()
    dices()
    print(f"Now we will roll dices to define\nthe attribute points of {char_name}!")
    while empty_attributes:
        input('\n\033[6mPress ENTER to roll the dices\033[0m')
        clear()
        dice_1 = roll(1, 6)
        dice_2 = roll(1, 6)
        total = dice_1 + dice_2
        messages = [
            'Rolling the first die...',
            'It landed on: ' + str(dice_1),
            'Rolling the second die...',
            'It landed on: ' + str(dice_2),
            'Choose an attribute to assign ' + str(total) + ' points to:'
        ]
        for message in messages:
            sleep_print(message, secs=0.1)
        if len(empty_attributes) > 1:
            for a in empty_attributes:
                print(a, end=' ')
            select_attribute = select_validation(empty_attributes).upper()
            print(f'{total} goes to {select_attribute}')
            attributes.update({select_attribute: total})
            empty_attributes.remove(select_attribute)
        else:
            print(f'{total} goes to {empty_attributes[0]}')
            attributes.update({empty_attributes[0]: total})
            empty_attributes.pop(0)
    for key in modify.keys():
        attributes[key] += modify[key]
    return attributes


def save_character(char_name, character):
    while True:
        print(f"Do you want to save the {char_name.title()}'s sheet?")
        save = select_validation(('yes', 'no'), stdoption='yes')
        if save == 'yes':
            try:
                with open('database/characters.json', 'r+') as f:
                    characters_data = json.load(f)
                    characters_data[char_name] = character
                    f.seek(0)

                    json.dump(characters_data, f, indent=4)
            except FileNotFoundError:
                with open('database/characters.json', 'w') as f:
                    character_data = {char_name: character}
                    json.dump(character_data, f, indent=4)
            break
        elif save == 'no':
            print(f"Are you sure you want to discard the {char_name.title()}'s sheet?")
            save = select_validation(('yes', 'no'), stdoption='no')
            if save == 'yes':
                sleep_print(f'{char_name.title()} discarted...')
                sleep_print('Forever...')
                break
            elif save == 'no':
                continue
