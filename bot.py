# -*- coding: utf-8 -*-
import time
import telebot
import config
import re

def findWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

bot = telebot.TeleBot(config.token)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    #bot.send_message(message.chat.id, message.text)
#тестинги - хуестинги
    input = message.text
    dic = {
    'ужин': 'хуюжин',
    'ужинать':'хуюжинать',
    'ужинали':'хуюжинали',
    'ужинаем':'хуюжинаем',
    'пользователи':'хуельзователи',
    'биллинга':'хуиллинга',
    'уключина':'хуиключина',
    'случаев':'хуючаев',
    'случай':'хуючий',
    'службами':'хуюжбами',
    'сущности':'хующности',
    }

    for word in dic.keys():
        out = findWord(word)(input)
        if out is not None:
            #out = dic[word]
            bot.send_message(message.chat.id, word + ' - ' + dic[word])
            break

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as er_msg:
        print(er_msg)