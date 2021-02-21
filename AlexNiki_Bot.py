import telebot
import pyexcel
from Config import TOKEN

bot = telebot.TeleBot(TOKEN)
bd_array = pyexcel.get_array(file_name="./src/ДР.xls")

# move = input('hello:')
# bd_array = pyexcel.get_array(file_name="./src/ДР.xls")
# for i, row in enumerate(bd_array):
#     for j, element in enumerate(row):
#         if element == move:
#             message = bd_array[i][0] + ' ' + bd_array[i][1] + ' ' + bd_array[i][2] + ' ' + bd_array[i][3].strftime("%d-%m-%Y")
#             print(message)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я предосталяю информацию о днях рождениях!')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text
    chat_id = message.chat.id

    for i, row in enumerate(bd_array):
        for j, element in enumerate(row):
            if element == text:
                message = bd_array[i][0] + ' ' + bd_array[i][1] + ' ' + bd_array[i][2] + ' ' + bd_array[i][3].strftime("%d-%m-%Y")
                bot.send_message(chat_id, message)

bot.polling()
