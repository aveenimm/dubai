import telebot

# Твой токен от BotFather
TOKEN = "8383518621:AAF1MnJWK-Q3tWK0jmnfeci2Q89gNO3wggQ"
bot = telebot.TeleBot(TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой бот 🤖")

# Ответ на любое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Выберите, пожалуйста, команду")

# Запуск бота
bot.polling(none_stop=True)
