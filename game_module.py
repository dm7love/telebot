MAIN = 'main'
QASK = 'qask'
QANS = 'qans'
GAME = 'game'

def handle_game(message, bot, states):
    user_id = message.from_user.id
    state = states.get(user_id)

    if state == GAME:
        bot.send_message(user_id, "Добро пожаловать в игру!\nНапиши: Спроси меня вопрос")
        states[user_id] = QASK
        return

    elif state == QASK:
        if message.text == 'Спроси меня вопрос':
            bot.send_message(user_id, 'Какую площадь имеет клетка тетрадки: 0,25; 1,0; 0,5; 1,25')
            states[user_id] = QANS
        elif message.text == '/stop':
            bot.send_message(user_id, 'Выход из игры.')
            states[user_id] = MAIN
        else:
            bot.send_message(user_id, 'Я тебя не понял')

    elif state == QANS:
        if message.text == '0,25':
            bot.send_message(user_id, 'Правильно!')
        elif message.text in ['1,0', '0,5', '1,25']:
            bot.send_message(user_id, 'Неправильно :(')
        else:
            bot.send_message(user_id, 'Я тебя не понял')
        states[user_id] = QASK