#!/usr/bin/python

from gpiozero import DistanceSensor, LED
from signal import pause
import telebot
import pygame.mixer
from pygame.mixer import Sound # Load the required library

pygame.mixer.init()
ventana_sensor = DistanceSensor(14, 15, max_distance=1,threshold_distance=0.9)
sound = Sound('alerta.wav')

API_TOKEN = "1491889902:AAHHVW6R5-VXuHdyJIzM11_59dZGTp-BNG0"
bot = telebot.TeleBot(API_TOKEN)
chat_id = 0

@bot.message_handler(commands=['help','start'])
def ayuda(message):
    global chat_id
    chat_id  = message.chat.id
    bot.reply_to(message,"""Hola, ya está el sistema de alarmas activado""")

def activaAlarma(sound):
    global chat_id,bot
    try: 
        sound.play()
        print("Detectando alguna proximidad")
        bot.send_message(chat_id, '¡Hay algo cerca de casa!')
    except: 
        print("Da el comando /start o help para que se muestre en el bot el mensaje")
        
def desactivaAlarma(sound):
    global chat_id,bot
    try: 
        sound.stop()
        print("No se percibe nada")
        bot.send_message(chat_id, 'No hay nadie cerca de casa')
    except: 
        print("Da el comando /start o help para que se muestre en el bot el mensaje")

ventana_sensor.when_in_range = lambda:activaAlarma(sound)
ventana_sensor.when_out_of_range = lambda:desactivaAlarma(sound)

bot.polling()