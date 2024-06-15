from telegram import KeyboardButton, InlineKeyboardButton
from random import randint


def get_keyboard_from_json(data):
    transformed_buttons = [[KeyboardButton(button["title"])] for button in data]
    return transformed_buttons


def get_inline_keyboard_from_json(data):
    transformed_buttons = []
    for button in data:
        title = button["title"]
        payload = button["payload"].lstrip("/")
        inline_button = InlineKeyboardButton(title, callback_data=payload)
        transformed_buttons.append([inline_button])
    return transformed_buttons


def get_random_object(data):
    return data[randint(0, len(data)-1)]


def find_values_by_titles(buttons, search_titles):
    found_items = []
    for button in buttons:
        if button.get('title') in search_titles:
            found_items.append(button)
    return found_items


def get_title_by_payload(buttons, search_payload):
    print(f'{buttons=}')
    for button_tuple in buttons:
        button = button_tuple[0]
        if button.callback_data == search_payload:
            return button.text
    return None