import telebot
from game_module import handle_game
from calendar_module import handle_calendar

token = '978121031:AAELw5ZrRFwBmk8ewLIFs7f36ZRe81PNvVM'
bot = telebot.TeleBot(token)
states = {}

#stat = {'wins' : 0, 'loss' :0   }

#multiplayer_stats = {}

MAIN = 'main'
GAME = 'game'
CALENDAR = 'calendar'

@bot.message_handler(func=lambda message: True)
def dispatcher (message):
    print (states)
    user_id = message.from_user.id
    state = states.get(user_id, MAIN)
    print('current state', user_id, state)
    if state == MAIN:
        if message.text == '/game':
            states[user_id] = GAME
            handle_game(message, bot, states)

        elif message.text == '/calendar':
            states[user_id] = CALENDAR
            handle_calendar(message, bot, states)
        else:
            bot.send_message(user_id, 'Выберите /game или /calendar')
    elif state == GAME:
            handle_game(message, bot, states)
    elif state == CALENDAR:
        handle_calendar(message, bot, states)

bot.polling()