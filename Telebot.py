import telebot

token = '978121031:AAELw5ZrRFwBmk8ewLIFs7f36ZRe81PNvVM'

bot = telebot.TeleBot(token)

states = {}

#stat = {'wins' : 0, 'loss' :0   }

#multiplayer_stats = {}

MAIN_STATE = 'main'
QASK = 'qask'
QANS = 'qans'

@bot.message_handler(func=lambda message: True)
def dispatcher (message):
    print (states)
    user_id = message.from_user.id
    state = states.get(user_id, MAIN_STATE)
    print('current state', user_id, state)
    if state == MAIN_STATE:
        main_handler(message)
    elif state == QASK:
        qask(message)
    elif state == QANS:
        qans(message)
    #current_user_state = states.get(user_id, 'main')

def main_handler(message):
    if message.text == ('/start'):
        bot.reply_to(message, 'Это бот-игра "Кто хочет стать миллионером"')
        states[message.from_user.id] = QASK
    elif message.text == ('Привет'):
          bot.reply_to(message,'Ну привет!')
    else:
        bot.reply_to(message, 'Я тебя не понял')
def qask(message):
    if message.text == ('Спроси меня вопрос'):
        bot.send_message(message.from_user.id, 'Какую площадь имеет клетка стандартной школьной тетрадки: 0,25; 1,0; 0,5; 1,25')
        states[message.from_user.id] = QANS
    elif message.text == ('/stop'):
        bot.reply_to(message, 'До свидания!')
        states[message.from_user.id] = MAIN_STATE
#    elif message.text == ('Счет'):
#        if message.from_user.id in multiplayer_stats:
#            stats = multiplayer_stats[message.from_user.id]
#        else:
 #           stats = {'wins' : 0, 'loss' :0   }
    else:
        bot.reply_to(message, 'Я тебя не понял')
def qans(message):
    if message.text == ('0,25'):
        bot.reply_to(message, 'Правильно!')
        states[message.from_user.id] = QASK
#        stat ['wins'] +=1
    if message.text == (('1,0') or ('1,25') or ('0,5')):
        bot.reply_to(message, 'Неправильно :(')
        states[message.from_user.id] = QASK
#        stat['loss'] += 1
    else:
        bot.reply_to(message, 'Я тебя не понял')

bot.polling()