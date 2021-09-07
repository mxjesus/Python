#!/usr/bin/python
import settings
import telebot

#LED
def on(pin):
    settings.ledList[pin] = 1
    return

def off(pin):
    settings.ledList[pin] = 0
    return

#LED
def onall():
    lista = [1,2,3,4,5,6,7,8]
    for pin in lista:
        settings.ledList[pin] = 1
    return

def offall():
    lista = [1,2,3,4,5,6,7,8]
    for pin in lista:
        settings.ledList[pin] = 0
    return

API_TOKEN = '1438902983:AAFVShpVkfuo7iNwMrOQ1Kd_K7DOc-4AP-4'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/help'
@bot.message_handler(commands=['help','start'])
def ayuda(message):
    offall()
    bot.reply_to(message, """\
¡Hola! Para prender cada foco debes de seguir los siguientes comandos
/on para encender todos los LEDs
/off para apagar todos los LEDs
/on# para encender un LED donde # es el número que se le asignó. 
/off# para apagar un LED donde # es el número que se le asignó. 
Hay que mencionar que # va de un rango del 1 a 8 \
""")

@bot.message_handler(commands=['on','On','oN','ON'])
def ledson(message):
    onall()
    bot.reply_to(message, """\
Prendiendo todos los LEDs\
""")

@bot.message_handler(commands=['off','Off','OfF','oFf','OFf','ofF','oFF','OFF'])
def ledsoff(message):
    offall()
    bot.reply_to(message, """\
Apagando todos los LEDs\
""")

@bot.message_handler(commands=['on1','On1','oN1','ON1'])
def ledon1(message):
    on(1)
    bot.reply_to(message, """\
Prendiendo el LED 1\
""")

@bot.message_handler(commands=['on2','On2','oN2','ON2'])
def ledon2(message):
    on(2)
    bot.reply_to(message, """\
Prendiendo el LED 2\
""")

@bot.message_handler(commands=['on3','On3','oN3','ON3'])
def ledson3(message):
    on(3)
    bot.reply_to(message, """\
Prendiendo el LED 3\
""")

@bot.message_handler(commands=['on4','On4','oN4','ON4'])
def ledson4(message):
    on(4)
    bot.reply_to(message, """\
Prendiendo el LED 4\
""")

@bot.message_handler(commands=['on5','On5','oN5','ON5'])
def ledson5(message):
    on(5)
    bot.reply_to(message, """\
Prendiendo el LED 5\
""")

@bot.message_handler(commands=['on6','On6','oN6','ON6'])
def ledson6(message):
    on(6)
    bot.reply_to(message, """\
Prendiendo el LED 6\
""")

@bot.message_handler(commands=['on7','On7','oN7','ON7'])
def ledson7(message):
    on(7)
    bot.reply_to(message, """\
Prendiendo el LED 7\
""")

@bot.message_handler(commands=['on8','On8','oN8','ON8'])
def ledson8(message):
    on(8)
    bot.reply_to(message, """\
Prendiendo el LED 8\
""")

@bot.message_handler(commands=['off1','Off1','OfF1','oFf1','OFf1','ofF1','oFF1','OFF1'])
def ledoff1(message):
    off(1)
    bot.reply_to(message, """\
Apagando el LED 1\
""")

@bot.message_handler(commands=['off2','Off2','OfF2','oFf2','OFf2','ofF2','oFF2','OFF2'])
def ledoff2(message):
    off(2)
    bot.reply_to(message, """\
Apagando el LED 2\
""")

@bot.message_handler(commands=['off3','Off3','OfF3','oFf3','OFf3','ofF3','oFF3','OFF3'])
def ledoff3(message):
    off(3)
    bot.reply_to(message, """\
Apagando el LED 3\
""")

@bot.message_handler(commands=['off4','Off4','OfF4','oFf4','OFf4','ofF4','oFF4','OFF4'])
def ledoff4(message):
    off(4)
    bot.reply_to(message, """\
Apagando el LED 4\
""")

@bot.message_handler(commands=['off5','Off5','OfF5','oFf5','OFf5','ofF5','oFF5','OFF5'])
def ledoff5(message):
    off(5)
    bot.reply_to(message, """\
Apagando el LED 5\
""")

@bot.message_handler(commands=['off6','Off6','OfF6','oFf6','OFf6','ofF6','oFF6','OFF6'])
def ledoff6(message):
    off(6)
    bot.reply_to(message, """\
Apagando el LED 6\
""")

@bot.message_handler(commands=['off7','Off7','OfF7','oFf7','OFf7','ofF7','oFF7','OFF7'])
def ledoff7(message):
    off(7)
    bot.reply_to(message, """\
Apagando el LED 7\
""")

@bot.message_handler(commands=['off8','Off8','OfF8','oFf8','OFf8','ofF8','oFF8','OFF8'])
def ledoff8(message):
    off(8)
    bot.reply_to(message, """\
Apagando el LED 8\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
