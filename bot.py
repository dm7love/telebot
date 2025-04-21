import telebot
from game_module import handle_game
from calendar_module import handle_calendar
from states import MAIN, GAME, CALENDAR, QASK, QANS, OPENAI, states
from config import TELEGRAM_TOKEN
from openai_module import handle_chatgpt

bot = telebot.TeleBot(TELEGRAM_TOKEN)

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
        elif message.text == '/chatGPT':
            states[user_id] = OPENAI
            handle_chatgpt(message, bot, states)
        else:
            bot.send_message(user_id, 'Выберите /game или /calendar или /chatGPT')
           #in case of state debug needed use code line below
           #print(f"[DEBUG] user_id: {user_id}, state: {state}, message: {message.text}")
    elif state in (GAME, QASK, QANS):
            handle_game(message, bot, states)
    elif state == CALENDAR:
        handle_calendar(message, bot, states)
    elif state == OPENAI:
        handle_chatgpt(message, bot, states)

bot.polling()