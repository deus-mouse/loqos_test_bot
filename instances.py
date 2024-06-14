from random import randint

phrazes = {'start':
               'Привет! Здесь ты можешь найти подборку важной информации для комфортного начала жизни на Кипре!',
           'start_tails': ['Напиши свой вопрос или выбери один из разделов.',
                           'Кликни на нужный раздел или напиши вопрос.',
                           'Выбери одну из кнопок или задай свой вопрос.'],
           }



# g = phrazes.get('start_tails')[randint(0, len(phrazes.get('start_tails')-1))]
g = phrazes.get('start_tails')
r = randint(0, len(phrazes.get('start_tails'))-1)
print(g)
print(r)