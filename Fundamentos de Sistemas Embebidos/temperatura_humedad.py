#!/usr/bin/python

#temperatura_humedad.py
#Librerias
import RPi.GPIO as GPIO
import Adafruit_DHT
import smtplib
from email.mime.text import MIMEText
import time
import os, sys

#Configuraciones de los pines GPIO de la Raspberry
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT) #Pin que corresponde al led rojo
GPIO.setup(16,GPIO.OUT) #Pin que corresponde al led verde

#Variables Globales
sensor = Adafruit_DHT.DHT11
pin_temperatura = 21 #pin de la raspberry que recibe los datos de temperatura y humedad del sensor
correo_origen = 'temperaturacelsiusrasp@gmail.com' #correo de origen
contraseña = '21tempB4yrrebpsar'
correo_destino = 'tachuyer@gmail.com' # correo de destino
temperatura_umbral = 20.0  #temperatura límite en °C

#Función para el envio de correo electrónico
def Enviar_correo(temperatura):
    
    msg = MIMEText(f"La temperatura esta demasiado alta.la temperatura es de: {temperatura:.2f}°C")
    msg['Subject'] = 'Monitoreo de Temperatura'
    msg['From'] = correo_origen
    msg['To'] = correo_destino
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(correo_origen,contraseña)
    server.sendmail(correo_origen,correo_destino,msg.as_string())
    print("Su Email ha sido enviado.")
    server.quit()


while True: 

    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin_temperatura)
    
    if humedad is not None and temperatura is not None:
        print(f'Temperatura={temperatura:.2f}*C  Humedad={humedad:.2f}%')
        
    else:
        print('Fallo la lectura del sensor.Intentar de nuevo')
        
    #Condicional que me permite controlar cuando la temperatura sobrepase el limite
    if temperatura > temperatura_umbral:
        
        GPIO.output(20,True) # enciende el led rojo como señal de advertencia
        GPIO.output(16,False) # apaga el led verde
        Enviar_correo(temperatura)
        
    else:
        
        GPIO.output(20,False) # led rojo apagado
        GPIO.output(16,True) # mantenga el led verde encendido
        #os.system("sudo python3 /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/lightshowpi/music/sample/ovenrake_deck-the-halls.mp3")
        
    
    time.sleep(0.01)
    
GPIO.cleanup()