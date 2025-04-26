import random
from states import MAIN, QASK, QANS, states
from charlie import QUESTIONS

user_data = {}  # {user_id: {"score": int, "current_question": dict}}

def handle_game(message, bot, states):
    user_id = message.from_user.id
    state = states.get(user_id)
    text = message.text.strip()

    if text == '/game':
        bot.send_message(user_id, 'Добро пожаловать в игру "Ответь на вопрос"! ✨')
        user_data[user_id] = {"score": 0}
        states[user_id] = QASK
        qask(message, bot, user_id)
        return
    if text == '/stop':
        score = user_data.get(user_id, {}).get("score", 0)
        bot.send_message(user_id, f"Вы завершили игру. Ваш счёт: {score} баллов.")
        states[user_id] = MAIN
        bot.send_message(user_id, "Вы вернулись в главное меню.")
        user_data.pop(user_id, None)
        return

    if state == QASK:
        qask(message, bot, user_id)
    elif state == QANS:
        qans(message, bot, user_id)
    else:
        bot.send_message(user_id, 'Я тебя не понял. Напиши /game чтобы начать.')

def qask(message, bot, user_id):

    previous = user_data[user_id].get("current_question")
    question = random.choice(QUESTIONS)
    while previous and question["question"] == previous["question"]:
        question = random.choice(QUESTIONS)

    user_data[user_id]["current_question"] = question
    states[user_id] = QANS

    options_text = "\n".join(question["options"])
    bot.send_message(user_id, f"{question['question']}\n\n{options_text}")

def qans(message, bot, user_id):
            text = message.text.strip()
            current = user_data[user_id].get("current_question")

            if not current:
                bot.send_message(user_id, 'Вопрос не задан. Напиши: Спроси меня вопрос')
                states[user_id] = QASK
                return

            if text == current["answer"]:
                bot.send_message(user_id, "Правильно! 🎉")
                user_data[user_id]["score"] += 1
            elif text in current["options"]:
                bot.send_message(user_id, f"Неправильно 😢. Правильный ответ: {current['answer']}")
            else:
                bot.send_message(user_id, 'Пожалуйста, выбери один из предложенных вариантов.')

            states[user_id] = QASK
            show_score(bot, user_id)
            qask(message, bot, user_id)

def show_score(bot, user_id):
    score = user_data[user_id]["score"]
    bot.send_message(user_id, f"Счёт: {score} баллов.")