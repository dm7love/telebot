import openai
from states import MAIN, OPENAI, states
from config import OPENAI_API_KEY
from openai import RateLimitError

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def handle_chatgpt(message, bot, states):
    user_id = message.from_user.id
    text = message.text.strip()
    #state = states.get(user_id)
    #if state == OPENAI:
     #bot.send_message(user_id, "Вы в разделе ChatGPT задавайте вопросы как обычному чату GPT, если вы хотите покинуть раздел введите /exit")
    if message.text == '/exit':
        states[user_id] = MAIN
        bot.send_message(user_id, "Вы вернулись в главное меню.")

    try:
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Или "gpt-4" если у тебя доступ
        messages=[
            {"role": "system", "content": "Ты дружелюбный помощник."},
            {"role": "user", "content": text}
        ]
    )
        reply = response.choices[0].message.content
        bot.send_message(user_id, reply)
    except RateLimitError:
        bot.send_message(user_id, "Извините, превышен лимит использования OpenAI API. Попробуйте позже или проверьте настройки.")