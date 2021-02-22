import telebot
import psycopg2

from Config import TOKEN
from Config import SQLALCHEMY_DATABASE_URI

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я предосталяю информацию о днях рождениях!')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text
    chat_id = message.chat.id

    conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI)
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from birthdays where lastname = %s or firstname = %s or middlename = %s"
    cursor.execute(postgreSQL_select_Query, (text, text, text))
    bd_records = cursor.fetchall()

    for row in bd_records:
        message = row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3].strftime("%d-%m-%Y")
        bot.send_message(message.chat.id, message)
    conn.close()

bot.polling()
