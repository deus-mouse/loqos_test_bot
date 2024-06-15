from telegram import KeyboardButton


def get_keyboard_from_json(data):
    transformed_buttons = [[KeyboardButton(button["title"])] for button in data]
    print(f'{transformed_buttons=}')
    return transformed_buttons