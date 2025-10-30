import telebot
from config import api
from logic import get_class

bot = telebot.TeleBot("8087350032:AAE52k04_Pe-T6ILwlLC8FgiA2ufVvFaok0")

@bot.message_handler(content_types=['photo'])

def get_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    class_name, score = get_class(file_name)
    if class_name == "Кошки" and score > 0.75:
        bot.reply_to(message, "Это кошка - она может ловить мышей")
    elif class_name == "Собаки" and score > 0.75:
        bot.reply_to(message, "Это собака - она может гонять ненужных кошек)")
    else:
        bot.reply_to(message, "я не понял, что на кортинке")        
bot.polling()