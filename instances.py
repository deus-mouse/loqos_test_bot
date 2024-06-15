from telegram import KeyboardButton

phrazes = {'start':
               'Привет! Здесь ты можешь найти подборку важной информации для комфортного начала жизни на Кипре!',
           'start_tails': ['Напиши свой вопрос или выбери один из разделов.',
                           'Кликни на нужный раздел или напиши вопрос.',
                           'Выбери одну из кнопок или задай свой вопрос.'],
           }

buttons = [
    [KeyboardButton("Документы")],
    [KeyboardButton("Создайте свою компанию")],
    [KeyboardButton("Налогообложение")]
]

buttons_main_json = [
    {"title": "Документы", "payload": "/documents"},
    {"title": "Создайте свою компанию", "payload": "/setup_company"},
    {"title": "Налогообложение", "payload": "/taxation"}
]