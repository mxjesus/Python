#!/usr/bin/python
import settings
import telebot

TOKEN = '1404908081:AAFyzExO0EMpH8hHj6GLTr18jLh5ww5LNFo'
bot = telebot.TeleBot(TOKEN)

def listener(mensajes):
    for m in mensajes:
        chat_id = m.chat.id
        texto = m.text
        print('ID: ' + str(chat_id) + ' - MENSAJE: ' + texto)
        if texto == "/help" or texto == "/start":
            break
        try:
            numero = int(texto)
            if numero >= 0  and numero <= 100:
                atenuacion(numero,m)
            else:
                bot.reply_to(m, """\
                Ingresa un número del 0 al 100\
                """)
        except:
            bot.reply_to(m, """\
            Ingresa un número del 0 al 100\
            """)
            
def atenuacion(numero,m):
    settings.intensidadLeds = numero/100
    
@bot.message_handler(commands=['help','start'])
def ayuda(message):
    bot.reply_to(message, """\
¡Hola! Para atenuar los LEDs, simplemente dé \
un número del 0 al 100, puede ser flotante.\
""")


bot.set_update_listener(listener)

bot.polling()