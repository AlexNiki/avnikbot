import telebot
import psycopg2
import schedule
import datetime
import time
from multiprocessing.context import Process

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

    if len(bd_records) == 0:
        bot.send_message(message.chat.id, 'Ничего не найдено')
    else:
        for row in bd_records:
            msg = row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3].strftime("%d-%m-%Y")
            bot.send_message(message.chat.id, msg)
    conn.close()


def check_birthday():
    now = datetime.datetime.now()
    conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI)
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from birthdays where birthday = %s"
    cursor.execute(postgreSQL_select_Query, (now.strftime("%Y-%m-%d"),))
    bd_records = cursor.fetchall()

    if len(bd_records) == 0:
        bot.send_message(bot.get_updates(), 'Сегодня дней рождений нет!')
    else:
        for row in bd_records:
            msg = row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3].strftime("%d-%m-%Y")
            bot.send_message(bot.get_updates(), msg)

    conn.close()

schedule.every().day.at("20:22").do(check_birthday)

class ScheduleMessage():
    def try_send_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    def start_process():
        p1 = Process(target=ScheduleMessage.try_send_schedule, args=())
        p1.start()

ScheduleMessage.start_process()
bot.polling()
