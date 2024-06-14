from telegram import KeyboardButton

phrazes = {'start':
               'Привет! Здесь ты можешь найти подборку важной информации для комфортного начала жизни на Кипре!',
           'start_tails': ['Напиши свой вопрос или выбери один из разделов.',
                           'Кликни на нужный раздел или напиши вопрос.',
                           'Выбери одну из кнопок или задай свой вопрос.'],
           }

buttons = [
    [KeyboardButton("Документы")],
    [KeyboardButton("Set up your company")],
    [KeyboardButton("Taxation")]
]