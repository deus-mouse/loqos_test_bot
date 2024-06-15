from telegram import KeyboardButton
from random import randint


def get_keyboard_from_json(data):
    transformed_buttons = [[KeyboardButton(button["title"])] for button in data]
    return transformed_buttons


def get_random_object(data):
    return data[randint(0, len(data)-1)]