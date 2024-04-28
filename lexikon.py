
LEXICON_COMMANDS: dict[str, str] = {
    '/help': 'Справка по работе бота',
    '/cancel': 'Закончить игру',
    '/stat': 'Узнать Счёт'}


start_greeding = ('Давайте сыграем в игру "Угадай число" ?\n\n'
                  '\U0001f1f7\U0001f1fa По умолчанию используется русский язык.\n'
                  'Чтобы получить правила игры и список доступных\n'
                  'команд - отправьте команду /help')

positiv_answer = ['да', 'давай', 'сыграем', 'игра', 'yes', 'es', 'нуы',
                  'играть', 'хочу играть', 'OK', 'ok', 'хочу', 'lfdfq',
                  'хорошо', 'ну', 'ладно', 'lf', 'la', 'da', 'jr', '[jxe', 'ja']

negative_answer = ['нет', 'не', 'не хочу', 'не буду', 'no', 'net', 'yen', 'ytn', 'nein', 'nicht', 'ne', 'nie']






language_dict = {'if not start': 'Для начала работы с ботом введите /start',

                 'game rules': ('\U0001f4e2 Правила игры :\n\nЯ загадываю число от 1\uFE0F\u20E3 до 1\uFE0F\u20E30\uFE0F\u20E30\uFE0F\u20E3, '
                                f'а вам нужно его угадать\nУ вас есть 5 попыток '
                                f'попыток\n\nДоступные команды:\n/help - правила '
                                f'игры и список команд\n/cancel - выйти из игры\n'),


                 'start ?': '  :  BOT    \U0001f3c1\n\nНачинаем игру ?    \U0001f920 ',

                 'exit from game': 'Вы вышли из игры. Если захотите сыграть снова - напишите об этом',


                 'user not in game now': 'А мы итак с вами не играем.\nМожет, сыграем разок?',



                 'attempts number is': 'Количество Ваших попыток = ',


                 'had a look at scores ?': 'Посмотрел счёт ? \n А теперь сыграем ?',


                 'number your attempts': 'Количество ваших попыток 5\uFE0F\u20E3 ',


                 'last att': 'Количество оставшихся попыток - ',



                 'taily is guessed': ('Вы загадали Число !\nНачинаем игру ? \U0001f3b0',
                      "You guessed a Number !\nLet's start the Game? \U0001f3b0",
                      'Du hast eine Zahl erraten !\nLasst uns das Spiel beginnen? \U0001f3b0 '),




                 'not digit sent in game': 'Пока мы играем в игру, я могу реагировать только на числа от 1 до 100 и команды /cancel и /stat',

                 'pity': 'Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом \U0001f197 \u2753',


                 'wrong sent data': 'Мы же сейчас с вами играем. \nПрисылайте, пожалуйста, числа от 1 до 100',


                 'wow': 'Ура !!! \U0001f389 ',

                 'user guessed': ' Вы угадали !\U0001f3c6\nМоё число ',

                 'play new game after user wins': '\n\nМожет, сыграем еще?',

                 'less': 'Мое число меньше \u2198\uFE0F',

                 'dont repeat your number': 'Вы же знаете, что я не это число загадал)))',

                 'more': 'Мое число больше \u2197\uFE0F',

                 'unf': '\U0001F61E К сожалению ',

                 'no att lost': ', у нас больше не осталось попыток. Никто не выиграл :(\n\nМое число было ',


                 'again': '\n\nДавайте сыграем ещё ! \U0001F609',


                 'in game false': 'Мы еще не играем. Хотите сыграть?',


                 'mal': ' попыток',

                 'start chat': 'Для начала работы с ботом введите /start',

                 'silly bot': 'Я довольно ограниченный бот, давайте просто сыграем в игру?',

                 'My namber was': 'Моё число было ',


                 'wrong content type': ', Вы хотите сыграть в игру ?',

                 'restart': 'Нельзя запусть бота дважды !)))',

                 'after_user_win':'Вы загадали Число !\nЯ тоже ! \nНачинайте отгадывать !',


                 }

