def handle_calendar(message, bot, states):
    user_id = message.from_user.id
    bot.send_message(user_id, "Здесь будет логика создания событий в Google Calendar (в разработке).")
    states[user_id] = 'main'